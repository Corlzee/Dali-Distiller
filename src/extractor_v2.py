#!/usr/bin/env python3
"""
Dali-Distiller V2: Enhanced SurrealDB Documentation Syntax Extractor

Like Salvador Dalí extracting impossible visions from reality,
this extracts BNF-like syntax patterns, function signatures, and operators
from SurrealDB .mdx documentation files.

"The persistence of documentation in the soft watches of extraction."
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
import yaml

class SurrealQLSyntaxExtractorV2:
    def __init__(self, docs_path: str):
        """Initialize extractor with path to docs.surrealdb.com repo"""
        self.docs_path = Path(docs_path)
        self.surrealql_path = self.docs_path / "src/content/doc-surrealql"
        self.extracted_syntax = {}
        self.extracted_functions = {}
        self.extracted_operators = {}
        self.metadata = {}
        
    def find_mdx_files(self) -> List[Path]:
        """Find all .mdx files in the doc-surrealql directory"""
        mdx_files = []
        for root, dirs, files in os.walk(self.surrealql_path):
            for file in files:
                if file.endswith('.mdx'):
                    mdx_files.append(Path(root) / file)
        return mdx_files
    
    def extract_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Extract YAML frontmatter from MDX file"""
        if not content.startswith('---'):
            return {}, content
            
        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}, content
            
        try:
            frontmatter = yaml.safe_load(parts[1])
            remaining_content = parts[2]
            return frontmatter, remaining_content
        except yaml.YAMLError:
            return {}, content
    
    def extract_syntax_blocks(self, content: str) -> List[str]:
        """Extract code blocks marked with 'syntax title="SurrealQL Syntax"' or just 'syntax'"""
        # Try both patterns
        patterns = [
            r'```surql title="SurrealQL Syntax"\n(.*?)\n```',
            r'```syntax title="SurrealQL Syntax"\n(.*?)\n```',
            r'```syntax\n(.*?)\n```'
        ]
        
        all_matches = []
        for pattern in patterns:
            matches = re.findall(pattern, content, re.DOTALL)
            all_matches.extend([match.strip() for match in matches])
        
        return all_matches
    
    def extract_api_definition_blocks(self, content: str) -> List[Dict]:
        """Extract API DEFINITION blocks for functions"""
        pattern = r'```surql title="API DEFINITION"\n(.*?)\n```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        signatures = []
        for match in matches:
            sig = self.parse_function_signature(match.strip())
            if sig:
                signatures.append(sig)
        return signatures
    
    def parse_function_signature(self, signature: str) -> Optional[Dict]:
        """Parse a function signature like 'array::add(array, value) -> array'"""
        # Match pattern: namespace::function(params) -> return_type
        pattern = r'^([a-z_]+)::([a-z_]+)\((.*?)\)(?:\s*->\s*(.+))?$'
        match = re.match(pattern, signature.strip())
        
        if not match:
            return None
            
        namespace, function_name, params_str, return_type = match.groups()
        
        # Parse parameters
        parameters = []
        if params_str:
            # Split by comma but handle nested types
            param_parts = self._split_params(params_str)
            for param in param_parts:
                param = param.strip()
                if param:
                    # Check if parameter has a name or just type
                    if ':' in param:
                        name, ptype = param.split(':', 1)
                        parameters.append({'name': name.strip(), 'type': ptype.strip()})
                    else:
                        # Just type, no name
                        parameters.append({'type': param})
        
        return {
            'raw': signature,
            'namespace': namespace,
            'function': function_name,
            'parameters': parameters,
            'return_type': return_type.strip() if return_type else None
        }
    
    def _split_params(self, params_str: str) -> List[str]:
        """Split parameters by comma, handling nested types"""
        params = []
        current = ""
        depth = 0
        
        for char in params_str:
            if char == ',' and depth == 0:
                params.append(current.strip())
                current = ""
            else:
                if char in '([{<':
                    depth += 1
                elif char in ')]}>':
                    depth -= 1
                current += char
        
        if current:
            params.append(current.strip())
        
        return params
    
    def extract_operators_from_mdx(self, operators_file: Path) -> Dict:
        """Extract operators from operators.mdx file"""
        if not operators_file.exists():
            return {}
            
        with open(operators_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        operators = {
            'logical': [],
            'comparison': [],
            'mathematical': [],
            'graph': [],
            'set': [],
            'fuzzy': [],
            'null_handling': [],
            'other': []
        }
        
        # Extract operators using markdown headers with {#id} format
        # Pattern: ## `operator` or `ALT` {#id}
        pattern = r'^##\s*`([^`]+)`(?:\s*or\s*`([^`]+)`)?.*?\{#(\w+)\}$'
        
        lines = content.split('\n')
        for i, line in enumerate(lines):
            match = re.match(pattern, line)
            if match:
                operator = match.group(1)
                alternative = match.group(2)
                op_id = match.group(3)
                
                # Get description from next paragraph
                description = ""
                for j in range(i+1, min(i+10, len(lines))):
                    if lines[j].strip() and not lines[j].startswith('#'):
                        description = lines[j].strip()
                        break
                
                # Clean up description
                description = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', description)  # Remove markdown links
                
                category = self._categorize_operator(operator)
                
                operator_info = {
                    'symbol': operator,
                    'description': description,
                    'id': op_id
                }
                
                if alternative:
                    operator_info['alternative'] = alternative
                
                operators[category].append(operator_info)
        
        return operators
    
    def _categorize_operator(self, operator: str) -> str:
        """Categorize operator based on its symbol"""
        if operator in ['&&', '||', '!', '!!', 'AND', 'OR', 'NOT']:
            return 'logical'
        elif operator in ['=', '!=', '==', '?=', '*=', 'IS', 'IS NOT']:
            return 'comparison'
        elif operator in ['+', '-', '*', '/', '%', '**', '×', '÷']:
            return 'mathematical'
        elif operator in ['->', '<->', '<-']:
            return 'graph'
        elif operator in ['∋', '∌', '∈', '∉', '⊆', '⊇', '⊃', '⊅', 'CONTAINS', 'CONTAINSNOT', 
                         'CONTAINSALL', 'CONTAINSANY', 'CONTAINSNONE', 'INSIDE', 'NOTINSIDE', 
                         'IN', 'NOT IN', 'ALLINSIDE']:
            return 'set'
        elif operator in ['~', '!~', '?~', '*~']:
            return 'fuzzy'
        elif operator in ['??', '?:']:
            return 'null_handling'
        elif operator in ['<', '<=', '>', '>=']:
            return 'comparison'
        elif operator in ['OUTSIDE', 'INTERSECTS']:
            return 'graph'
        elif operator in ['@@', '@[', '@]']:
            return 'other'
        else:
            return 'other'
    
    def process_statement_file(self, file_path: Path) -> Dict:
        """Process a single MDX file for statement syntax"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter, remaining_content = self.extract_frontmatter(content)
            syntax_blocks = self.extract_syntax_blocks(remaining_content)
            
            if not syntax_blocks:
                return None
            
            # Extract statement name from path
            statement_name = file_path.stem.lower()
            if statement_name == 'index':
                statement_name = file_path.parent.name.lower()
            
            return {
                'name': statement_name,
                'syntax': syntax_blocks,
                'frontmatter': frontmatter,
                'file_path': str(file_path.relative_to(self.docs_path))
            }
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
    
    def process_function_file(self, file_path: Path) -> Dict:
        """Process a single MDX file for function signatures"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter, remaining_content = self.extract_frontmatter(content)
            api_blocks = self.extract_api_definition_blocks(remaining_content)
            
            if not api_blocks:
                return None
            
            # Extract namespace from path
            namespace = file_path.stem.lower()
            
            return {
                'namespace': namespace,
                'functions': api_blocks,
                'frontmatter': frontmatter,
                'file_path': str(file_path.relative_to(self.docs_path))
            }
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
    
    def extract_all(self):
        """Extract all syntax patterns, functions, and operators"""
        print("🎨 Starting Dalí-Distiller V2 extraction...")
        
        # Extract statements
        print("\n📄 Extracting statement syntax...")
        statements_path = self.surrealql_path / "statements"
        if statements_path.exists():
            # Process direct .mdx files in statements directory
            for mdx_file in statements_path.glob("*.mdx"):
                if mdx_file.stem not in ['index', '_category_']:
                    result = self.process_statement_file(mdx_file)
                    if result:
                        self.extracted_syntax[result['name']] = result
                        print(f"  ✓ Extracted: {result['name']}")
            
            # Also process subdirectories like define/
            for subdir in statements_path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith('_'):
                    for mdx_file in subdir.glob("*.mdx"):
                        if mdx_file.stem not in ['index', '_category_']:
                            result = self.process_statement_file(mdx_file)
                            if result:
                                # Use directory/filename as key for nested statements
                                key = f"{subdir.name}/{result['name']}"
                                self.extracted_syntax[key] = result
                                print(f"  ✓ Extracted: {key}")
        
        # Extract functions
        print("\n🔧 Extracting function signatures...")
        functions_path = self.surrealql_path / "functions" / "database"
        if functions_path.exists():
            for mdx_file in functions_path.glob("*.mdx"):
                if mdx_file.stem not in ['index', '_category_']:
                    result = self.process_function_file(mdx_file)
                    if result:
                        self.extracted_functions[result['namespace']] = result
                        total_funcs = len(result['functions'])
                        print(f"  ✓ Extracted: {result['namespace']} ({total_funcs} functions)")
        
        # Extract operators
        print("\n⚡ Extracting operators...")
        operators_file = self.surrealql_path / "operators.mdx"
        if operators_file.exists():
            self.extracted_operators = self.extract_operators_from_mdx(operators_file)
            total_ops = sum(len(ops) for ops in self.extracted_operators.values())
            print(f"  ✓ Extracted: {total_ops} operators")
        
        # Calculate metadata
        self.metadata = {
            'version': self._get_surrealdb_version(),
            'extraction_date': str(Path.cwd()),
            'stats': {
                'statements': len(self.extracted_syntax),
                'functions': {
                    'namespaces': len(self.extracted_functions),
                    'total': sum(len(ns['functions']) for ns in self.extracted_functions.values())
                },
                'operators': {
                    'categories': len([cat for cat, ops in self.extracted_operators.items() if ops]),
                    'total': sum(len(ops) for ops in self.extracted_operators.values())
                }
            }
        }
        
        print(f"\n✨ Extraction complete!")
        print(f"   Statements: {self.metadata['stats']['statements']}")
        print(f"   Functions: {self.metadata['stats']['functions']['total']} across {self.metadata['stats']['functions']['namespaces']} namespaces")
        print(f"   Operators: {self.metadata['stats']['operators']['total']} across {self.metadata['stats']['operators']['categories']} categories")
    
    def _get_surrealdb_version(self) -> str:
        """Try to extract SurrealDB version from documentation"""
        # Look for version in configuration or fallback
        version_file = self.docs_path / "src/content/doc-surrealdb/introduction/releases.mdx"
        if version_file.exists():
            try:
                with open(version_file, 'r') as f:
                    content = f.read()
                    # Look for latest version pattern
                    match = re.search(r'## Version v?(\d+\.\d+\.\d+)', content)
                    if match:
                        return match.group(1)
            except:
                pass
        return "2.3.7"  # Default fallback
    
    def save_raw_extraction(self, output_dir: Path):
        """Save raw extraction results"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        raw_data = {
            'metadata': self.metadata,
            'statements': self.extracted_syntax,
            'functions': self.extracted_functions,
            'operators': self.extracted_operators
        }
        
        with open(output_dir / 'raw_extraction_v2.json', 'w') as f:
            json.dump(raw_data, f, indent=2)
        
        print(f"\n💾 Saved raw extraction to {output_dir / 'raw_extraction_v2.json'}")


def main():
    """Main extraction process"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract SurrealQL syntax, functions, and operators')
    parser.add_argument('--docs-path', type=str, 
                      default='/home/konverts/projects/documentation/docs.surrealdb.com',
                      help='Path to docs.surrealdb.com repository')
    parser.add_argument('--output-dir', type=str,
                      default='/home/konverts/projects/surrealAIdoc/output',
                      help='Output directory for extraction results')
    
    args = parser.parse_args()
    
    extractor = SurrealQLSyntaxExtractorV2(args.docs_path)
    extractor.extract_all()
    extractor.save_raw_extraction(Path(args.output_dir))


if __name__ == "__main__":
    main()
