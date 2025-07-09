
# Dali-Distiller Usage Example

*"Like Dalí's melting clocks, watch documentation flow into perfect queries..."* 🎨

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
