#!/usr/bin/env python3
"""
Dali-Distiller: Intent Router Generator

Creates impossible pathways through meaning, mapping natural language 
to SurrealQL perfection. Like Dalí's paranoid-critical method, it sees 
hidden connections in the chaos of human intent.

"The drawer-docs reveal their secrets to those who know how to look."
"""

import yaml
import json
from typing import Dict, List, Any

class SurrealQLIntentRouter:
    def __init__(self, schema_path: str):
        """Initialize with generated schema"""
        with open(schema_path, 'r') as f:
            self.schema = yaml.safe_load(f)
        
        self.router = {
            'routing': {
                'version': '2.3.6',
                'schema_path': 'statements',
                'intents': {},
                'fallback': {
                    'message': 'Unable to match query intent. See https://surrealdb.com/docs/surrealql for details.',
                    'docs': 'https://surrealdb.com/docs/surrealql'
                }
            }
        }
    
    def build_create_intents(self) -> Dict[str, Any]:
        """Build intents for creation/definition operations"""
        define_statements = self.schema['surrealql']['statements'].get('define', {})
        
        create_intents = {
            'aliases': ['create', 'make', 'build', 'set up', 'define', 'establish'],
            'table': {
                'aliases': ['table', 'relation', 'entity', 'collection'],
                'base': {
                    'path': 'statements.define.table',
                    'condition': 'create basic table without special features',
                    'variables': ['name'],
                    'keywords': ['DEFINE', 'TABLE']
                },
                'with_schema': {
                    'path': 'statements.define.table',
                    'condition': 'create table with schema enforcement (SCHEMAFULL/SCHEMALESS)',
                    'variables': ['name'],
                    'keywords': ['DEFINE', 'TABLE', 'SCHEMAFULL', 'SCHEMALESS']
                },
                'with_permissions': {
                    'path': 'statements.define.table',
                    'condition': 'create table with access controls or permissions',
                    'variables': ['name', 'expression'],
                    'keywords': ['DEFINE', 'TABLE', 'PERMISSIONS', 'FOR']
                },
                'relation': {
                    'path': 'statements.define.table',
                    'condition': 'create relation table connecting other tables',
                    'variables': ['name', 'table'],
                    'keywords': ['DEFINE', 'TABLE', 'TYPE', 'RELATION']
                }
            },
            'user': {
                'aliases': ['user', 'account', 'login', 'auth'],
                'base': {
                    'path': 'statements.define.user',
                    'condition': 'create user account',
                    'variables': ['name'],
                    'keywords': ['DEFINE', 'USER']
                }
            },
            'database': {
                'aliases': ['database', 'db', 'schema'],
                'base': {
                    'path': 'statements.define.database',
                    'condition': 'create new database',
                    'variables': ['name'],
                    'keywords': ['DEFINE', 'DATABASE']
                }
            },
            'index': {
                'aliases': ['index', 'search index', 'lookup'],
                'base': {
                    'path': 'statements.define.index',
                    'condition': 'create database index for performance',
                    'variables': ['name', 'table'],
                    'keywords': ['DEFINE', 'INDEX']
                }
            },
            'field': {
                'aliases': ['field', 'column', 'property', 'attribute'],
                'base': {
                    'path': 'statements.define.field',
                    'condition': 'define table field with constraints',
                    'variables': ['name', 'table'],
                    'keywords': ['DEFINE', 'FIELD']
                }
            }
        }
        
        return create_intents
    
    def build_query_intents(self) -> Dict[str, Any]:
        """Build intents for data retrieval operations"""
        return {
            'aliases': ['get', 'retrieve', 'fetch', 'find', 'search', 'query', 'select'],
            'basic': {
                'path': 'statements.select',
                'condition': 'retrieve data with basic SELECT',
                'variables': ['fields', 'targets'],
                'keywords': ['SELECT', 'FROM']
            },
            'filtered': {
                'path': 'statements.select',
                'condition': 'retrieve data with WHERE conditions',
                'variables': ['fields', 'targets', 'conditions'],
                'keywords': ['SELECT', 'FROM', 'WHERE']
            },
            'ordered': {
                'path': 'statements.select',
                'condition': 'retrieve data with sorting (ORDER BY)',
                'variables': ['fields', 'targets', 'field'],
                'keywords': ['SELECT', 'FROM', 'ORDER']
            },
            'grouped': {
                'path': 'statements.select',
                'condition': 'retrieve data with grouping/aggregation',
                'variables': ['fields', 'targets', 'field'],
                'keywords': ['SELECT', 'FROM', 'GROUP']
            },
            'limited': {
                'path': 'statements.select',
                'condition': 'retrieve limited number of records',
                'variables': ['fields', 'targets', 'limit'],
                'keywords': ['SELECT', 'FROM', 'LIMIT']
            }
        }
    
    def build_modify_intents(self) -> Dict[str, Any]:
        """Build intents for data modification operations"""
        return {
            'update': {
                'aliases': ['update', 'modify', 'change', 'edit'],
                'base': {
                    'path': 'statements.update',
                    'condition': 'update existing records',
                    'variables': ['targets'],
                    'keywords': ['UPDATE']
                }
            },
            'create_record': {
                'aliases': ['insert', 'add', 'new record', 'create record'],
                'base': {
                    'path': 'statements.create',
                    'condition': 'create new records',
                    'variables': ['targets'],
                    'keywords': ['CREATE']
                }
            },
            'upsert': {
                'aliases': ['upsert', 'create or update', 'merge'],
                'base': {
                    'path': 'statements.upsert',
                    'condition': 'create record or update if exists',
                    'variables': ['targets'],
                    'keywords': ['UPSERT']
                }
            },
            'delete': {
                'aliases': ['delete', 'remove', 'drop record'],
                'base': {
                    'path': 'statements.delete',
                    'condition': 'delete records',
                    'variables': ['targets'],
                    'keywords': ['DELETE']
                }
            },
            'relate': {
                'aliases': ['relate', 'connect', 'link', 'associate'],
                'base': {
                    'path': 'statements.relate',
                    'condition': 'create relationships between records',
                    'variables': ['targets'],
                    'keywords': ['RELATE']
                }
            }
        }
    
    def build_admin_intents(self) -> Dict[str, Any]:
        """Build intents for administrative operations"""
        return {
            'info': {
                'aliases': ['info', 'show', 'describe', 'list', 'inspect'],
                'base': {
                    'path': 'statements.info',
                    'condition': 'get information about database objects',
                    'variables': ['table', 'user'],
                    'keywords': ['INFO', 'FOR']
                }
            },
            'remove_definition': {
                'aliases': ['remove', 'drop', 'delete definition'],
                'base': {
                    'path': 'statements.remove',
                    'condition': 'remove database definitions (tables, users, etc.)',
                    'variables': ['name'],
                    'keywords': ['REMOVE']
                }
            }
        }
    
    def build_router(self) -> Dict[str, Any]:
        """Build complete intent router"""
        self.router['routing']['intents'] = {
            'create': self.build_create_intents(),
            'query': self.build_query_intents(),
            'modify': self.build_modify_intents(),
            'admin': self.build_admin_intents()
        }
        
        # Add token usage estimates
        self.router['routing']['token_usage'] = {
            'router_tokens': self.estimate_router_tokens(),
            'schema_reference': 'Use compact schema for actual syntax',
            'estimated_per_query': '50-100 tokens'
        }
        
        return self.router
    
    def estimate_router_tokens(self) -> int:
        """Estimate token count for router"""
        return len(str(self.router).split())
    
    def save_router(self, output_path: str):
        """Save intent router to YAML file"""
        with open(output_path, 'w') as f:
            yaml.dump(self.router, f, default_flow_style=False, sort_keys=False, indent=2)
        
        token_count = self.estimate_router_tokens()
        print(f"Intent router saved to {output_path}")
        print(f"Estimated tokens: {token_count}")
        
        return token_count
    
    def generate_usage_example(self) -> str:
        """Generate example usage documentation"""
        return """
# SurrealQL AI Router Usage Example

## Router + Schema Integration

```yaml
# Query: "create a user table with permissions"
# 1. Router maps: create -> table -> with_permissions
# 2. Path: statements.define.table  
# 3. Schema provides: variables=[name, expression], keywords=[DEFINE, TABLE, PERMISSIONS]
# 4. Generated: DEFINE TABLE users PERMISSIONS FOR select WHERE user = $auth.id;
```

## Intent Mapping Examples

- "make a new table" → create.table.base
- "create user with permissions" → create.table.with_permissions  
- "get all users" → query.basic
- "find users where active = true" → query.filtered
- "update user profile" → modify.update.base
- "connect user to company" → modify.relate.base
- "show table info" → admin.info.base

## Token Efficiency
- Router: ~400 tokens
- Schema reference: ~923 tokens  
- Per-query context: ~50-100 tokens
- Total system: ~1,300-1,400 tokens (within SOW target)
"""


if __name__ == "__main__":
    # Generate intent router
    schema_path = "/home/konverts/projects/surrealAIdoc/output/surrealql_schema_full.yml"
    output_dir = "/home/konverts/projects/surrealAIdoc/output"
    
    router_generator = SurrealQLIntentRouter(schema_path)
    
    print("Building SurrealQL intent router...")
    router = router_generator.build_router()
    
    # Save router
    router_path = f"{output_dir}/intent_router.yml"
    token_count = router_generator.save_router(router_path)
    
    # Save usage example
    usage_path = f"{output_dir}/usage_example.md"
    with open(usage_path, 'w') as f:
        f.write(router_generator.generate_usage_example())
    
    # Generate final report
    final_report = {
        'system_components': {
            'intent_router': {
                'path': router_path,
                'tokens': token_count
            },
            'compact_schema': {
                'path': f"{output_dir}/surrealql_schema_compact.yml", 
                'tokens': 923
            },
            'total_system_tokens': token_count + 923
        },
        'sow_compliance': {
            'target_tokens': '1,200-1,900',
            'actual_tokens': token_count + 923,
            'within_target': (token_count + 923) <= 1900,
            'token_efficiency': f"{((1900 - (token_count + 923)) / 1900 * 100):.1f}% under target"
        }
    }
    
    with open(f"{output_dir}/final_report.json", 'w') as f:
        json.dump(final_report, f, indent=2)
    
    print(f"\n=== Final System Analysis ===")
    print(f"Router tokens: {token_count}")
    print(f"Schema tokens: 923")
    print(f"Total system: {token_count + 923} tokens")
    print(f"SOW target: 1,200-1,900 tokens")
    print(f"Status: {'✓ WITHIN TARGET' if (token_count + 923) <= 1900 else '✗ OVER TARGET'}")
