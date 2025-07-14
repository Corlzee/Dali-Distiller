#!/usr/bin/env python3
"""
Dali-Distiller Final: Dual-Output Schema Converter

Produces both full-context (14k) and ultra-compressed (2k) versions.
The full version preserves all context for maximum accuracy.
The compressed version is for smaller LLMs with token constraints.

"The persistence of memory offers both clarity and essence."
"""

import json
import yaml
import re
import argparse
from typing import Dict, List, Any, Optional, Set
from pathlib import Path
from collections import defaultdict

class DualSchemaConverter:
    def __init__(self, raw_extraction_path: str):
        """Initialize converter with raw extraction data"""
        with open(raw_extraction_path, 'r') as f:
            self.raw_data = json.load(f)
        
        # Get version from metadata
        self.version = self.raw_data.get('metadata', {}).get('version', '2.3.7')
        
        # Initialize both schema formats
        self.full_schema = None
        self.compressed_schema = None
        
        # Type map for compression
        self.type_map = {
            'array': 'a', 'string': 's', 'number': 'n', 'bool': 'b',
            'object': 'o', 'any': '*', 'duration': 'd', 'datetime': 't',
            'record': 'r', 'geometry': 'g', 'uuid': 'u', 'int': 'i',
            'float': 'f', 'value': 'v', 'null': '0', 'bytes': 'y'
        }
    
    def create_full_schema(self):
        """Create full-context schema (14k tokens) with complete information"""
        self.full_schema = {
            'surrealql_schema': {
                'version': f"{self.version}",
                'metadata': {
                    'coverage': '85%',
                    'format': 'full',
                    'description': 'Complete schema with all context preserved'
                },
                'statements': {},
                'functions': {},
                'operators': {}
            }
        }
        
        # Convert statements with full context
        for stmt_name, stmt_data in self.raw_data.get('statements', {}).items():
            if not stmt_data.get('syntax'):
                continue
            
            syntax_blocks = stmt_data['syntax']
            parsed = self._parse_statement_syntax(syntax_blocks[0])
            
            self.full_schema['surrealql_schema']['statements'][stmt_name] = {
                'keywords': list(self._extract_keywords(parsed))[:10],  # Top 10 keywords
                'variables': list(self._extract_variables(parsed))[:10],
                'syntax_pattern': self._extract_pattern(syntax_blocks[0])
            }
        
        # Convert functions with full signatures
        for namespace, ns_data in self.raw_data.get('functions', {}).items():
            if not ns_data.get('functions'):
                continue
            
            ns_functions = {}
            func_groups = defaultdict(list)
            
            for func in ns_data['functions']:
                func_groups[func['function']].append(func)
            
            for func_name, overloads in func_groups.items():
                ns_functions[func_name] = {
                    'signatures': [
                        {
                            'pattern': sig['raw'],
                            'params': [p.get('type', 'any') for p in sig.get('parameters', [])],
                            'returns': sig.get('return_type', 'any')
                        }
                        for sig in overloads
                    ]
                }
            
            self.full_schema['surrealql_schema']['functions'][namespace] = ns_functions
        
        # Convert operators with descriptions
        for category, ops in self.raw_data.get('operators', {}).items():
            if not ops:
                continue
            
            self.full_schema['surrealql_schema']['operators'][category] = [
                {
                    'symbol': op['symbol'],
                    'alt': op.get('alternative'),
                    'desc': op['description'][:80]  # Truncate very long descriptions
                }
                for op in ops
            ]
    
    def create_compressed_schema(self):
        """Create ultra-compressed schema (2k tokens) for smaller LLMs"""
        self.compressed_schema = {
            'surrealql': {
                'v': self.version,
                'stmts': {},
                'funcs': {},
                'ops': {}
            }
        }
        
        # Compressed statements
        for stmt_name, stmt_data in self.raw_data.get('statements', {}).items():
            if not stmt_data.get('syntax'):
                continue
            
            key = self._abbreviate_statement(stmt_name)
            syntax = stmt_data['syntax'][0]
            keywords = []
            
            for line in syntax.split('\n')[:3]:
                words = re.findall(r'\b([A-Z]{2,})\b', line)
                keywords.extend(w for w in words if not w.startswith('@'))
            
            self.compressed_schema['surrealql']['stmts'][key] = {'k': keywords[:3]}
        
        # Compressed functions
        for namespace, ns_data in self.raw_data.get('functions', {}).items():
            if ns_data.get('functions'):
                ns_key = namespace[:3] if len(namespace) > 3 else namespace
                compressed_funcs = {}
                
                func_groups = defaultdict(list)
                for func in ns_data['functions']:
                    func_groups[func['function']].append(func)
                
                for func_name, overloads in func_groups.items():
                    if len(overloads) == 1:
                        compressed_funcs[func_name] = self._compress_signature(overloads[0])
                    else:
                        compressed_funcs[func_name] = [
                            self._compress_signature(sig) for sig in overloads
                        ]
                
                self.compressed_schema['surrealql']['funcs'][ns_key] = compressed_funcs
        
        # Compressed operators
        for category, ops in self.raw_data.get('operators', {}).items():
            if ops:
                cat_ops = []
                for op in ops:
                    if op.get('alternative'):
                        cat_ops.append(f"{op['symbol']}|{op['alternative']}")
                    else:
                        cat_ops.append(op['symbol'])
                
                self.compressed_schema['surrealql']['ops'][category[:3]] = cat_ops
    
    def _parse_statement_syntax(self, syntax: str) -> Dict:
        """Parse BNF-like syntax into structured format"""
        return {
            'raw': syntax,
            'lines': [line.strip() for line in syntax.split('\n') if line.strip()]
        }
    
    def _extract_keywords(self, parsed: Dict) -> Set[str]:
        """Extract SQL keywords from syntax"""
        keywords = set()
        keyword_pattern = r'\b([A-Z_]+)\b'
        
        for line in parsed['lines']:
            matches = re.findall(keyword_pattern, line)
            keywords.update(m for m in matches if not m.startswith('@') and len(m) > 1)
        
        return keywords
    
    def _extract_variables(self, parsed: Dict) -> Set[str]:
        """Extract variable placeholders from syntax"""
        variables = set()
        var_pattern = r'@(\w+)'
        
        for line in parsed['lines']:
            matches = re.findall(var_pattern, line)
            variables.update(matches)
        
        return variables
    
    def _extract_pattern(self, syntax: str) -> str:
        """Extract simplified pattern from syntax"""
        # Remove optional parts and clean up
        pattern = re.sub(r'\[.*?\]', '', syntax)
        pattern = re.sub(r'@\w+', '<var>', pattern)
        pattern = ' '.join(pattern.split())[:100]  # First 100 chars
        return pattern
    
    def _compress_signature(self, sig: Dict) -> str:
        """Compress a function signature to minimal string"""
        parts = []
        
        if sig.get('parameters'):
            param_types = [self._compress_type(p.get('type', '*')) for p in sig['parameters']]
            parts.append(''.join(param_types))
        else:
            parts.append('')
        
        if sig.get('return_type'):
            parts.append(self._compress_type(sig['return_type']))
        else:
            parts.append('*')
        
        return '>'.join(parts)
    
    def _compress_type(self, type_str: str) -> str:
        """Compress type string to single character"""
        if not type_str:
            return '*'
        
        type_lower = type_str.lower()
        
        if type_lower.startswith('array<'):
            inner = re.search(r'array<(.+)>', type_lower)
            if inner:
                return 'a' + self._compress_type(inner.group(1))
        
        if type_lower.startswith('option<'):
            inner = re.search(r'option<(.+)>', type_lower)
            if inner:
                return '?' + self._compress_type(inner.group(1))
        
        return self.type_map.get(type_lower, '*')
    
    def _abbreviate_statement(self, stmt_name: str) -> str:
        """Abbreviate statement names"""
        abbreviations = {
            'select': 'sel', 'insert': 'ins', 'update': 'upd', 'delete': 'del',
            'create': 'cre', 'alter': 'alt', 'define': 'def', 'remove': 'rem'
        }
        
        if '/' in stmt_name:
            parts = stmt_name.split('/')
            return '/'.join(abbreviations.get(p, p[:3]) for p in parts)
        
        return abbreviations.get(stmt_name, stmt_name[:3])
    
    def create_monolith(self, output_dir: Path, format: str = 'both'):
        """Create a monolithic file containing everything for force-feeding to lazy AIs"""
        
        # Ensure schemas are created
        if not self.full_schema:
            self.create_full_schema()
        if not self.compressed_schema:
            self.create_compressed_schema()
        
        import tiktoken
        enc = tiktoken.encoding_for_model('gpt-4')
        
        monolith_content = []
        
        # Header
        monolith_content.append("# SurrealQL Complete Schema Documentation")
        monolith_content.append(f"# Generated from SurrealDB {self.version} documentation")
        monolith_content.append("# Coverage: 85% of SurrealQL syntax")
        monolith_content.append("# Purpose: Force-feed documentation to lazy AI assistants")
        monolith_content.append("\n" + "="*80 + "\n")
        
        # Add compressed version if requested
        if format in ['compressed', 'both']:
            monolith_content.append("## COMPRESSED SCHEMA (2,185 tokens)")
            monolith_content.append("### For smaller LLMs or token-constrained environments\n")
            monolith_content.append("```yaml")
            monolith_content.append(yaml.dump(self.compressed_schema, default_flow_style=True, width=200))
            monolith_content.append("```")
            monolith_content.append("\n### Type Abbreviations:")
            monolith_content.append("```")
            monolith_content.append("a=array s=string n=number b=bool o=object r=record")
            monolith_content.append("i=int f=float d=duration t=datetime g=geometry u=uuid")
            monolith_content.append("v=value y=bytes *=any 0=null ?=option<>")
            monolith_content.append("```")
            monolith_content.append("\n" + "="*80 + "\n")
        
        # Add full version if requested
        if format in ['full', 'both']:
            monolith_content.append("## FULL SCHEMA (12,698 tokens)")
            monolith_content.append("### For GPT-4/Claude with complete context\n")
            monolith_content.append("```yaml")
            monolith_content.append(yaml.dump(self.full_schema, default_flow_style=False, sort_keys=False))
            monolith_content.append("```")
            monolith_content.append("\n" + "="*80 + "\n")
        
        # Add usage instructions
        monolith_content.append("## USAGE INSTRUCTIONS\n")
        monolith_content.append("1. Load this entire file into context")
        monolith_content.append("2. Use schema to generate correct SurrealQL syntax")
        monolith_content.append("3. Reference function signatures and operator syntax")
        monolith_content.append("4. Follow statement patterns for proper query structure")
        monolith_content.append("\n## REMEMBER:")
        monolith_content.append("- This is 85% of SurrealQL syntax compressed from 297,445 tokens")
        monolith_content.append("- Missing: query clauses (FETCH, EXPLAIN), advanced type specs, comments")
        monolith_content.append("- When in doubt, check the schema!")
        
        # Write monolith file
        filename = f"SURREALQL_MONOLITH_{format.upper()}.md"
        monolith_path = output_dir / filename
        
        full_content = '\n'.join(monolith_content)
        with open(monolith_path, 'w') as f:
            f.write(full_content)
        
        # Calculate tokens
        tokens = len(enc.encode(full_content))
        
        print(f"\n🗿 Monolith created: {monolith_path}")
        print(f"   Format: {format}")
        print(f"   Size: {len(full_content):,} chars / {tokens:,} tokens")
        print(f"   Purpose: Force-feed to lazy AI when needed")
        
        return monolith_path, tokens
    
    def save_schemas(self, output_dir: Path, format: str = 'both'):
        """Save schemas based on format selection"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        import tiktoken
        enc = tiktoken.encoding_for_model('gpt-4')
        
        saved_files = []
        
        # Save full schema if requested
        if format in ['full', 'both']:
            if not self.full_schema:
                self.create_full_schema()
            
            full_path = output_dir / 'surrealql_full.yml'
            with open(full_path, 'w') as f:
                yaml.dump(self.full_schema, f, default_flow_style=False, sort_keys=False)
            
            # Calculate tokens
            with open(full_path, 'r') as f:
                content = f.read()
                tokens = len(enc.encode(content))
            
            print(f"💾 Full schema saved: {full_path}")
            print(f"   Size: {len(content):,} chars / {tokens:,} tokens")
            saved_files.append(('full', tokens))
        
        # Save compressed schema if requested
        if format in ['compressed', 'both']:
            if not self.compressed_schema:
                self.create_compressed_schema()
            
            comp_path = output_dir / 'surrealql_compressed.yml'
            with open(comp_path, 'w') as f:
                yaml.dump(self.compressed_schema, f, default_flow_style=True, width=200)
            
            # Calculate tokens
            with open(comp_path, 'r') as f:
                content = f.read()
                tokens = len(enc.encode(content))
            
            print(f"💾 Compressed schema saved: {comp_path}")
            print(f"   Size: {len(content):,} chars / {tokens:,} tokens")
            saved_files.append(('compressed', tokens))
        
        # Create comparison report
        if format == 'both':
            report = {
                'schema_comparison': {
                    'source_stats': self.raw_data['metadata']['stats'],
                    'outputs': {
                        name: {
                            'tokens': tokens,
                            'target_use': 'GPT-4/Claude' if name == 'full' else 'Smaller LLMs'
                        }
                        for name, tokens in saved_files
                    }
                }
            }
            
            report_path = output_dir / 'schema_comparison.json'
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            print(f"\n📊 Comparison saved: {report_path}")
        
        # Create monolith if requested
        if format in ['full', 'compressed', 'both']:
            self.create_monolith(output_dir, format)


def main():
    """Main conversion process with format selection"""
    parser = argparse.ArgumentParser(
        description='Convert SurrealQL extraction to schema formats'
    )
    parser.add_argument(
        '--input', 
        type=str,
        default='/home/konverts/projects/surrealAIdoc/output/raw_extraction_v2.json',
        help='Path to raw extraction JSON'
    )
    parser.add_argument(
        '--output-dir', 
        type=str,
        default='/home/konverts/projects/surrealAIdoc/output',
        help='Output directory'
    )
    parser.add_argument(
        '--format',
        type=str,
        choices=['full', 'compressed', 'both'],
        default='both',
        help='Output format: full (14k), compressed (2k), or both'
    )
    
    args = parser.parse_args()
    
    print(f"🎨 Dali-Distiller Final: Creating {args.format} schema(s)...")
    
    converter = DualSchemaConverter(args.input)
    converter.save_schemas(Path(args.output_dir), args.format)
    
    print("\n✨ Conversion complete!")


if __name__ == "__main__":
    main()
