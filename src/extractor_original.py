#!/usr/bin/env python3
"""
Dali-Distiller: SurrealDB Documentation Syntax Extractor

Like Salvador Dalí extracting impossible visions from reality,
this extracts BNF-like syntax patterns from SurrealDB .mdx documentation files.
Focuses on code blocks with 'syntax title="SurrealQL Syntax"' markers.

"The persistence of documentation in the soft watches of extraction."
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import yaml

class SurrealQLSyntaxExtractor:
    def __init__(self, docs_path: str):
        """Initialize extractor with path to docs.surrealdb.com repo"""
        self.docs_path = Path(docs_path)
        self.surrealql_path = self.docs_path / "src/content/doc-surrealql"
        self.extracted_syntax = {}
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
        """Extract syntax blocks marked with 'syntax title=\"SurrealQL Syntax\"'"""
        # Pattern to match syntax blocks
        pattern = r'```syntax title="SurrealQL Syntax"\n(.*?)\n```'
        matches = re.findall(pattern, content, re.DOTALL)
        return [match.strip() for match in matches]
    
    def extract_example_blocks(self, content: str) -> List[str]:
        """Extract example code blocks (surql, sql)"""
        # Pattern to match example blocks
        pattern = r'```(?:surql|sql)\n(.*?)\n```'
        matches = re.findall(pattern, content, re.DOTALL)
        return [match.strip() for match in matches]
    
    def get_doc_hierarchy(self, file_path: Path) -> str:
        """Convert file path to hierarchical doc path"""
        relative_path = file_path.relative_to(self.surrealql_path)
        # Remove .mdx extension and convert to dot notation
        hierarchy = str(relative_path.with_suffix('')).replace('/', '.')
        return hierarchy
    
    def process_file(self, file_path: Path) -> Optional[Dict]:
        """Process a single .mdx file and extract syntax information"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter, main_content = self.extract_frontmatter(content)
            syntax_blocks = self.extract_syntax_blocks(main_content)
            example_blocks = self.extract_example_blocks(main_content)
            
            if not syntax_blocks:
                return None  # Skip files without syntax blocks
            
            hierarchy = self.get_doc_hierarchy(file_path)
            
            return {
                'file_path': str(file_path),
                'hierarchy': hierarchy,
                'frontmatter': frontmatter,
                'syntax_blocks': syntax_blocks,
                'example_blocks': example_blocks,
                'title': frontmatter.get('title', ''),
                'description': frontmatter.get('description', ''),
                'sidebar_label': frontmatter.get('sidebar_label', '')
            }
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
    
    def extract_all_syntax(self) -> Dict:
        """Extract syntax from all .mdx files"""
        mdx_files = self.find_mdx_files()
        print(f"Found {len(mdx_files)} .mdx files")
        
        extracted_data = {}
        syntax_count = 0
        
        for file_path in mdx_files:
            file_data = self.process_file(file_path)
            if file_data:
                extracted_data[file_data['hierarchy']] = file_data
                syntax_count += len(file_data['syntax_blocks'])
                print(f"✓ {file_data['hierarchy']}: {len(file_data['syntax_blocks'])} syntax blocks")
        
        print(f"\nExtracted {syntax_count} syntax blocks from {len(extracted_data)} files")
        
        self.extracted_syntax = extracted_data
        return extracted_data
    
    def save_raw_extraction(self, output_path: str):
        """Save raw extracted data to JSON file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.extracted_syntax, f, indent=2, ensure_ascii=False)
        print(f"Raw extraction saved to {output_path}")
    
    def get_statistics(self) -> Dict:
        """Get extraction statistics"""
        total_files = len(self.extracted_syntax)
        total_syntax_blocks = sum(len(data['syntax_blocks']) for data in self.extracted_syntax.values())
        total_examples = sum(len(data['example_blocks']) for data in self.extracted_syntax.values())
        
        # Count by category
        categories = {}
        for hierarchy, data in self.extracted_syntax.items():
            category = hierarchy.split('.')[0]
            if category not in categories:
                categories[category] = {'files': 0, 'syntax_blocks': 0}
            categories[category]['files'] += 1
            categories[category]['syntax_blocks'] += len(data['syntax_blocks'])
        
        return {
            'total_files': total_files,
            'total_syntax_blocks': total_syntax_blocks,
            'total_examples': total_examples,
            'categories': categories
        }


if __name__ == "__main__":
    # Example usage
    docs_path = "/home/konverts/projects/documentation/docs.surrealdb.com"
    output_dir = "/home/konverts/projects/surrealAIdoc/output"
    
    extractor = SurrealQLSyntaxExtractor(docs_path)
    
    print("Starting SurrealQL syntax extraction...")
    extracted_data = extractor.extract_all_syntax()
    
    # Save raw extraction
    os.makedirs(output_dir, exist_ok=True)
    extractor.save_raw_extraction(f"{output_dir}/raw_extraction.json")
    
    # Print statistics
    stats = extractor.get_statistics()
    print(f"\n=== Extraction Statistics ===")
    print(f"Total files processed: {stats['total_files']}")
    print(f"Total syntax blocks: {stats['total_syntax_blocks']}")
    print(f"Total examples: {stats['total_examples']}")
    print(f"\nBy category:")
    for category, data in stats['categories'].items():
        print(f"  {category}: {data['files']} files, {data['syntax_blocks']} syntax blocks")
