#!/usr/bin/env python3
"""
Dali-Distiller V2: Enhanced BNF/Function/Operator to YAML Schema Converter

Like melting clocks transforming reality, this converts extracted syntax patterns,
function signatures, and operators into AI-optimized YAML schema. 
Documentation flows into liquid perfection through surreal transformation.

"In the metamorphosis of manuals, chaos becomes art."
"""

import json
import yaml
import re
from typing import Dict, List, Any, Optional, Set
from pathlib import Path
from collections import defaultdict

class EnhancedSchemaConverter:
    def __init__(self, raw_extraction_path: str):
        """Initialize converter with raw extraction data"""
        with open(raw_extraction_path, 'r') as f:
            self.raw_data = json.load(f)
        
        # Get version from metadata or default
        version = self.raw_data.get('metadata', {}).get('version', '2.3.7')
        
        self.schema = {
            'surrealql_schema_enhanced': {
                'version': f"{version}-85",  # Mark as 85% coverage version
                'metadata': {
                    'statements': self.raw_data['metadata']['stats']['statements'],
                    'functions': self.raw_data['metadata']['stats']['functions']['total'],
                    'operators': self.raw_data['metadata']['stats']['operators']['total'],
                    'coverage': '85%'
                }
            }
        }
        
        self.intent_router = {
            'intent_router_enhanced': {
                'version': '2.0',
                'routes': {}
            }
        }
        
    def convert_statements(self):
        """Convert statement syntax to compressed schema"""
        statements = {}
        
        for stmt_name, stmt_data in self.raw_data.get('statements', {}).items():
            if not stmt_data.get('syntax'):
                continue
                
            # Parse the BNF-like syntax
            syntax_blocks = stmt_data['syntax']
            parsed = self._parse_statement_syntax(syntax_blocks[0])  # Use first syntax block
            
            # Extract key components
            keywords = self._extract_keywords(parsed)
            variables = self._extract_variables(parsed)
            optional = self._extract_optional_parts(parsed)
            
            statements[stmt_name] = {
                'keywords': list(keywords),
                'variables': list(variables),
                'optional': list(optional)
            }
            
            # Add to router
            self._add_statement_route(stmt_name, keywords)
        
        self.schema['surrealql_schema_enhanced']['statements'] = statements
    
    def _parse_statement_syntax(self, syntax: str) -> Dict:
        """Parse BNF-like syntax into structured format"""
        lines = [line.strip() for line in syntax.split('\n') if line.strip()]
        
        return {
            'raw': syntax,
            'lines': lines
        }
    
    def _extract_keywords(self, parsed: Dict) -> Set[str]:
        """Extract SQL keywords from syntax"""
        keywords = set()
        keyword_pattern = r'\b([A-Z_]+)\b'
        
        for line in parsed['lines']:
            matches = re.findall(keyword_pattern, line)
            for match in matches:
                # Filter out placeholders
                if not match.startswith('@') and len(match) > 1:
                    keywords.add(match)
        
        return keywords
    
    def _extract_variables(self, parsed: Dict) -> Set[str]:
        """Extract variable placeholders from syntax"""
        variables = set()
        var_pattern = r'@(\w+)'
        
        for line in parsed['lines']:
            matches = re.findall(var_pattern, line)
            variables.update(matches)
        
        return variables
    
    def _extract_optional_parts(self, parsed: Dict) -> Set[str]:
        """Extract optional parts marked with brackets"""
        optional = set()
        opt_pattern = r'\[([^\]]+)\]'
        
        for line in parsed['lines']:
            matches = re.findall(opt_pattern, line)
            for match in matches:
                # Clean up and extract main keyword
                cleaned = match.strip()
                if cleaned:
                    optional.add(cleaned)
        
        return optional
    
    def convert_functions(self):
        """Convert function signatures to compressed schema"""
        functions = {}
        
        for namespace, ns_data in self.raw_data.get('functions', {}).items():
            if not ns_data.get('functions'):
                continue
            
            ns_functions = {}
            
            # Group functions by name (handling overloads)
            func_groups = defaultdict(list)
            for func in ns_data['functions']:
                func_groups[func['function']].append(func)
            
            # Convert each function group
            for func_name, overloads in func_groups.items():
                ns_functions[func_name] = {
                    'signatures': []
                }
                
                for overload in overloads:
                    sig = {
                        'pattern': overload['raw']
                    }
                    
                    if overload.get('parameters'):
                        sig['params'] = [{'type': p.get('type', 'any')} for p in overload['parameters']]
                    
                    if overload.get('return_type'):
                        sig['returns'] = overload['return_type']
                    
                    ns_functions[func_name]['signatures'].append(sig)
            
            functions[namespace] = ns_functions
            
            # Add to router
            self._add_function_route(namespace, list(func_groups.keys()))
        
        self.schema['surrealql_schema_enhanced']['functions'] = functions
    
    def convert_operators(self):
        """Convert operators to compressed schema"""
        operators = {}
        
        for category, ops in self.raw_data.get('operators', {}).items():
            if not ops:
                continue
                
            operators[category] = []
            
            for op in ops:
                op_info = {
                    'symbol': op['symbol'],
                    'description': op['description'][:100]  # Truncate long descriptions
                }
                
                if op.get('alternative'):
                    op_info['alternative'] = op['alternative']
                
                operators[category].append(op_info)
            
            # Add to router
            self._add_operator_route(category, [op['symbol'] for op in ops])
        
        self.schema['surrealql_schema_enhanced']['operators'] = operators
    
    def _add_statement_route(self, stmt_name: str, keywords: Set[str]):
        """Add statement to intent router"""
        if 'statements' not in self.intent_router['intent_router_enhanced']['routes']:
            self.intent_router['intent_router_enhanced']['routes']['statements'] = {}
        
        # Create simplified route key
        route_key = stmt_name.replace('/', '_')
        
        self.intent_router['intent_router_enhanced']['routes']['statements'][route_key] = {
            'keywords': list(keywords)[:5],  # Top 5 keywords only
            'path': f'statements.{stmt_name}'
        }
    
    def _add_function_route(self, namespace: str, function_names: List[str]):
        """Add functions to intent router"""
        if 'functions' not in self.intent_router['intent_router_enhanced']['routes']:
            self.intent_router['intent_router_enhanced']['routes']['functions'] = {}
        
        self.intent_router['intent_router_enhanced']['routes']['functions'][namespace] = {
            'keywords': [namespace] + function_names[:5],  # Namespace + top 5 functions
            'path': f'functions.{namespace}'
        }
    
    def _add_operator_route(self, category: str, operators: List[str]):
        """Add operators to intent router"""
        if 'operators' not in self.intent_router['intent_router_enhanced']['routes']:
            self.intent_router['intent_router_enhanced']['routes']['operators'] = {}
        
        self.intent_router['intent_router_enhanced']['routes']['operators'][category] = {
            'keywords': operators[:5],  # Top 5 operators
            'path': f'operators.{category}'
        }
    
    def convert_all(self):
        """Run all conversions"""
        print("🎨 Starting schema conversion...")
        
        print("📄 Converting statements...")
        self.convert_statements()
        
        print("🔧 Converting functions...")
        self.convert_functions()
        
        print("⚡ Converting operators...")
        self.convert_operators()
        
        print("✨ Conversion complete!")
    
    def calculate_token_estimate(self, obj: Any) -> int:
        """Estimate tokens for a YAML object"""
        yaml_str = yaml.dump(obj, default_flow_style=False)
        # Rough estimate: 1 token per 4 characters
        return len(yaml_str) // 4
    
    def save_schemas(self, output_dir: Path):
        """Save converted schemas with token estimates"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save main schema
        schema_path = output_dir / 'surrealql_schema_enhanced.yml'
        with open(schema_path, 'w') as f:
            yaml.dump(self.schema, f, default_flow_style=False, sort_keys=False)
        
        schema_tokens = self.calculate_token_estimate(self.schema)
        print(f"💾 Saved schema to {schema_path} (~{schema_tokens} tokens)")
        
        # Save router
        router_path = output_dir / 'intent_router_enhanced.yml'
        with open(router_path, 'w') as f:
            yaml.dump(self.intent_router, f, default_flow_style=False, sort_keys=False)
        
        router_tokens = self.calculate_token_estimate(self.intent_router)
        print(f"💾 Saved router to {router_path} (~{router_tokens} tokens)")
        
        # Save conversion report
        report = {
            'conversion_report': {
                'timestamp': str(Path.cwd()),
                'stats': {
                    'statements': len(self.schema['surrealql_schema_enhanced'].get('statements', {})),
                    'functions': {
                        ns: len(funcs) 
                        for ns, funcs in self.schema['surrealql_schema_enhanced'].get('functions', {}).items()
                    },
                    'operators': {
                        cat: len(ops)
                        for cat, ops in self.schema['surrealql_schema_enhanced'].get('operators', {}).items()
                    }
                },
                'token_estimates': {
                    'schema': schema_tokens,
                    'router': router_tokens,
                    'total': schema_tokens + router_tokens
                }
            }
        }
        
        report_path = output_dir / 'conversion_report_v2.json'
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📊 Token Budget Summary:")
        print(f"   Schema: ~{schema_tokens} tokens")
        print(f"   Router: ~{router_tokens} tokens")
        print(f"   Total:  ~{schema_tokens + router_tokens} tokens")
        
        return report


def main():
    """Main conversion process"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert extracted syntax to YAML schema')
    parser.add_argument('--input', type=str,
                      default='/home/konverts/projects/surrealAIdoc/output/raw_extraction_v2.json',
                      help='Path to raw extraction JSON')
    parser.add_argument('--output-dir', type=str,
                      default='/home/konverts/projects/surrealAIdoc/output',
                      help='Output directory for schemas')
    
    args = parser.parse_args()
    
    converter = EnhancedSchemaConverter(args.input)
    converter.convert_all()
    converter.save_schemas(Path(args.output_dir))


if __name__ == "__main__":
    main()
