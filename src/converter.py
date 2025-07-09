#!/usr/bin/env python3
"""
Dali-Distiller: BNF to YAML Schema Converter

Like melting clocks transforming reality, this converts extracted BNF-like 
syntax patterns into AI-optimized YAML schema. Documentation flows into 
liquid perfection through surreal transformation.

"In the metamorphosis of manuals, chaos becomes art."
"""

import json
import yaml
import re
from typing import Dict, List, Any, Optional
from pathlib import Path

class BNFToYAMLConverter:
    def __init__(self, raw_extraction_path: str):
        """Initialize converter with raw extraction data"""
        with open(raw_extraction_path, 'r') as f:
            self.raw_data = json.load(f)
        
        self.schema = {
            'surrealql': {
                'version': '2.3.6',  # Current SurrealDB version
                'docs': 'https://surrealdb.com/docs/surrealql',
                'statements': {},
                'functions': {},
                'types': {
                    'primitives': ['str', 'int', 'float', 'bool', 'datetime', 'duration'],
                    'complex': ['array', 'object', 'record', 'geometry', 'uuid']
                }
            }
        }
        
        # Common options that appear across statements
        self.common_opts = {
            'overwrite': {'type': 'bool', 'syntax': 'OVERWRITE'},
            'if_not_exists': {'type': 'bool', 'syntax': 'IF NOT EXISTS'},
            'if_exists': {'type': 'bool', 'syntax': 'IF EXISTS'}
        }
        
    def parse_bnf_line(self, line: str) -> Dict[str, Any]:
        """Parse a single BNF line into structured data"""
        line = line.strip()
        if not line:
            return {}
            
        # Handle different BNF patterns
        result = {}
        
        # Optional blocks: [ ... ]
        optional_pattern = r'\[\s*([^[\]]+)\s*\]'
        optional_matches = re.findall(optional_pattern, line)
        
        for match in optional_matches:
            # Check for choices within optional blocks
            if '|' in match:
                choices = [choice.strip() for choice in match.split('|')]
                # Filter out empty strings and handle special cases
                choices = [c for c in choices if c and not c.startswith('@')]
                if choices:
                    result['optional_choices'] = choices
            else:
                # Single optional item
                if not match.startswith('@'):
                    result['optional'] = match.strip()
        
        # Variables: @name, @expression, etc.
        var_pattern = r'@(\w+)'
        variables = re.findall(var_pattern, line)
        if variables:
            result['variables'] = variables
            
        # Required keywords (uppercase words not in brackets)
        keyword_pattern = r'\b[A-Z]{2,}\b'
        keywords = re.findall(keyword_pattern, line)
        # Filter out keywords that are part of optional blocks
        filtered_keywords = []
        for keyword in keywords:
            if not any(keyword in opt for opt in optional_matches):
                filtered_keywords.append(keyword)
        if filtered_keywords:
            result['keywords'] = filtered_keywords
            
        return result
    
    def convert_statement_syntax(self, syntax_block: str) -> Dict[str, Any]:
        """Convert a statement syntax block to YAML structure"""
        lines = syntax_block.split('\n')
        statement_structure = {
            'syntax': syntax_block,  # Keep original for reference
            'components': {}
        }
        
        # Parse each line
        parsed_lines = []
        for line in lines:
            parsed = self.parse_bnf_line(line)
            if parsed:
                parsed_lines.append(parsed)
        
        # Extract common patterns
        all_variables = set()
        all_keywords = set()
        optional_components = []
        
        for parsed in parsed_lines:
            if 'variables' in parsed:
                all_variables.update(parsed['variables'])
            if 'keywords' in parsed:
                all_keywords.update(parsed['keywords'])
            if 'optional_choices' in parsed:
                optional_components.append(parsed['optional_choices'])
            if 'optional' in parsed:
                optional_components.append([parsed['optional']])
        
        # Build simplified structure
        if all_variables:
            statement_structure['variables'] = sorted(list(all_variables))
        if all_keywords:
            statement_structure['keywords'] = sorted(list(all_keywords))
        if optional_components:
            statement_structure['optional'] = optional_components
            
        return statement_structure
    
    def process_statements(self):
        """Process all statement syntax blocks"""
        for hierarchy, data in self.raw_data.items():
            if not hierarchy.startswith('statements.'):
                continue
                
            # Build nested structure
            path_parts = hierarchy.split('.')
            current = self.schema['surrealql']['statements']
            
            # Navigate/create nested structure
            for part in path_parts[1:-1]:  # Skip 'statements' and last part
                if part not in current:
                    current[part] = {}
                current = current[part]
            
            # Process syntax blocks for this statement
            statement_name = path_parts[-1]
            if len(data['syntax_blocks']) == 1:
                # Single syntax block
                current[statement_name] = self.convert_statement_syntax(data['syntax_blocks'][0])
            else:
                # Multiple syntax blocks
                current[statement_name] = {
                    'variants': [
                        self.convert_statement_syntax(block) 
                        for block in data['syntax_blocks']
                    ]
                }
            
            # Add metadata
            current[statement_name]['metadata'] = {
                'title': data.get('title', ''),
                'description': data.get('description', ''),
                'sidebar_label': data.get('sidebar_label', '')
            }
    
    def estimate_token_count(self, obj: Any, indent: int = 0) -> int:
        """Estimate token count for YAML structure"""
        if isinstance(obj, dict):
            count = 0
            for key, value in obj.items():
                count += len(str(key).split()) + 1  # key + colon
                count += self.estimate_token_count(value, indent + 1)
            return count
        elif isinstance(obj, list):
            count = 0
            for item in obj:
                count += self.estimate_token_count(item, indent + 1)
            return count
        else:
            return len(str(obj).split())
    
    def create_compact_schema(self) -> Dict[str, Any]:
        """Create a token-optimized compact schema"""
        compact = {
            'surrealql': {
                'v': '2.3.6',
                'docs': 'https://surrealdb.com/docs/surrealql',
                'stmts': {},
                'types': ['str', 'int', 'float', 'bool', 'datetime', 'array', 'object', 'record']
            }
        }
        
        # Compact statement representation
        for category, statements in self.schema['surrealql']['statements'].items():
            compact['surrealql']['stmts'][category] = {}
            for stmt_name, stmt_data in statements.items():
                # Minimal representation focusing on variables and key patterns
                compact_stmt = {}
                
                if 'variables' in stmt_data:
                    compact_stmt['vars'] = stmt_data['variables']
                
                if 'keywords' in stmt_data:
                    # Only include non-obvious keywords
                    filtered_keywords = [k for k in stmt_data['keywords'] 
                                       if k not in ['SELECT', 'FROM', 'WHERE', 'DEFINE']]
                    if filtered_keywords:
                        compact_stmt['keys'] = filtered_keywords
                
                if 'optional' in stmt_data:
                    compact_stmt['opts'] = stmt_data['optional']
                
                compact['surrealql']['stmts'][category][stmt_name] = compact_stmt
        
        return compact
    
    def generate_schemas(self, output_dir: str):
        """Generate both full and compact schemas"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Process all statements
        self.process_statements()
        
        # Generate full schema
        full_schema_path = output_path / 'surrealql_schema_full.yml'
        with open(full_schema_path, 'w') as f:
            yaml.dump(self.schema, f, default_flow_style=False, sort_keys=False, indent=2)
        
        # Generate compact schema
        compact_schema = self.create_compact_schema()
        compact_schema_path = output_path / 'surrealql_schema_compact.yml'
        with open(compact_schema_path, 'w') as f:
            yaml.dump(compact_schema, f, default_flow_style=False, sort_keys=False, indent=2)
        
        # Calculate token estimates
        full_tokens = self.estimate_token_count(self.schema)
        compact_tokens = self.estimate_token_count(compact_schema)
        
        # Generate report
        report = {
            'extraction_stats': {
                'total_files': len(self.raw_data),
                'syntax_blocks': sum(len(data['syntax_blocks']) for data in self.raw_data.values()),
                'statements_processed': len([k for k in self.raw_data.keys() if k.startswith('statements.')])
            },
            'schema_stats': {
                'full_schema_tokens': full_tokens,
                'compact_schema_tokens': compact_tokens,
                'token_reduction': f"{((full_tokens - compact_tokens) / full_tokens * 100):.1f}%"
            },
            'files_generated': [
                str(full_schema_path),
                str(compact_schema_path)
            ]
        }
        
        report_path = output_path / 'conversion_report.json'
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"Schema generation complete!")
        print(f"Full schema: {full_tokens} estimated tokens")
        print(f"Compact schema: {compact_tokens} estimated tokens")
        print(f"Token reduction: {report['schema_stats']['token_reduction']}")
        
        return report


if __name__ == "__main__":
    # Example usage
    raw_extraction_path = "/home/konverts/projects/surrealAIdoc/output/raw_extraction.json"
    output_dir = "/home/konverts/projects/surrealAIdoc/output"
    
    converter = BNFToYAMLConverter(raw_extraction_path)
    
    print("Starting BNF to YAML conversion...")
    report = converter.generate_schemas(output_dir)
    
    print(f"\nConversion complete! Files saved to {output_dir}")
