# SurrealQL Complete Schema Documentation
# Generated from SurrealDB 2.3.7 documentation
# Coverage: 85% of SurrealQL syntax
# Purpose: Force-feed documentation to lazy AI assistants

================================================================================

## FULL SCHEMA (12,698 tokens)
### For GPT-4/Claude with complete context

```yaml
surrealql_schema:
  version: 2.3.7
  metadata:
    coverage: 85%
    format: full
    description: Complete schema with all context preserved
  statements:
    info:
      keywords:
      - NS
      - NAMESPACE
      - DATABASE
      - 'ON'
      - USER
      - INDEX
      - ROOT
      - TABLE
      - INFO
      - FOR
      variables:
      - table
      - index
      - user
      - level
      syntax_pattern: INFO FOR [ ROOT | NS | NAMESPACE | DB | DATABASE | TABLE <var>
        | USER <var> | INDEX <var> ON <var> ]
    select:
      keywords:
      - START
      - AT
      - COLLATE
      - WHERE
      - ORDER
      - SELECT
      - WITH
      - INDEX
      - ASC
      - DESC
      variables:
      - indexes
      - limit
      - alias
      - conditions
      - duration
      - start
      - fields
      - field
      - targets
      syntax_pattern: SELECT VALUE <var> | <var> FROM <var> ] <var>, ... ] <var>,
        ... ] <var> , ... | RAND() ] <var> ] <va
    kill:
      keywords:
      - KILL
      variables:
      - value
      syntax_pattern: KILL <var>;
    let:
      keywords:
      - LET
      variables:
      - type_name
      - parameter
      - value
      syntax_pattern: LET $<var> = <var>;
    upsert:
      keywords:
      - WHERE
      - CONTENT
      - AFTER
      - PATCH
      - REPLACE
      - DIFF
      - UPSERT
      - RETURN
      - NONE
      - PARALLEL
      variables:
      - condition
      - duration
      - value
      - field
      - targets
      - statement_param
      syntax_pattern: UPSERT <var> [ CONTENT <var> | MERGE <var> | PATCH <var> | REPLACE
        <var> | ] ] ;
    for:
      keywords:
      - IN
      - FOR
      variables:
      - iterable
      - item
      - block
      syntax_pattern: FOR <var> IN <var> { <var> };
    update:
      keywords:
      - WHERE
      - CONTENT
      - AFTER
      - PATCH
      - REPLACE
      - DIFF
      - UPDATE
      - RETURN
      - NONE
      - PARALLEL
      variables:
      - condition
      - duration
      - value
      - field
      - targets
      - statement_param
      syntax_pattern: UPDATE <var> [ CONTENT <var> | MERGE <var> | PATCH <var> | REPLACE
        <var> | ] ] ;
    continue:
      keywords:
      - CONTINUE
      variables: []
      syntax_pattern: CONTINUE
    remove:
      keywords:
      - ANALYZER
      - REMOVE
      - NAMESPACE
      - DATABASE
      - 'ON'
      - USER
      - ACCESS
      - EVENT
      - INDEX
      - FUNCTION
      variables:
      - name
      - table
      syntax_pattern: REMOVE [ NAMESPACE <var> | DATABASE <var> | USER <var> ON |
        ACCESS <var> ON | EVENT <var> ON <var> |
    delete:
      keywords:
      - BEFORE
      - FULL
      - RETURN
      - WHERE
      - PARALLEL
      - AFTER
      - NONE
      - DELETE
      - DIFF
      - ONLY
      variables:
      - targets
      - condition
      - duration
      - statement_param
      syntax_pattern: DELETE <var> ] ;
    throw:
      keywords:
      - THROW
      variables:
      - error
      syntax_pattern: THROW <var>
    return:
      keywords:
      - RETURN
      variables:
      - value
      syntax_pattern: RETURN <var>
    begin:
      keywords:
      - TRANSACTION
      - BEGIN
      variables: []
      syntax_pattern: BEGIN ;
    alter:
      keywords:
      - SCHEMALESS
      - COMMENT
      - ALTER
      - TABLE
      - IF
      - PERMISSIONS
      - NONE
      - FOR
      - SCHEMAFULL
      - FULL
      variables:
      - name
      - expression
      - string
      syntax_pattern: ALTER [ | TABLE <var> [ PERMISSIONS [ NONE | FULL | FOR select
        <var> | FOR create <var> | FOR update
    use:
      keywords:
      - DB
      - USE
      - NS
      variables:
      - ns
      - db
      syntax_pattern: USE ;
    sleep:
      keywords:
      - SLEEP
      variables:
      - duration
      syntax_pattern: SLEEP <var>;
    rebuild:
      keywords:
      - 'ON'
      - INDEX
      - REBUILD
      - TABLE
      - IF
      - EXISTS
      variables:
      - name
      - table
      syntax_pattern: REBUILD [ INDEX <var> ON <var> ]
    relate:
      keywords:
      - RELATE
      - BEFORE
      - RETURN
      - SET
      - PARALLEL
      - CONTENT
      - AFTER
      - NONE
      - DIFF
      - ONLY
      variables:
      - duration
      - value
      - table
      - to_record
      - field
      - from_record
      - statement_param
      syntax_pattern: RELATE <var> -> <var> -> <var> [ CONTENT <var> | SET <var> =
        <var> ... ] ;
    access:
      keywords:
      - RECORD
      - REVOKE
      - NAMESPACE
      - 'ON'
      - ACCESS
      - DATABASE
      - GRANT
      - USER
      - WHERE
      - EXPIRED
      variables:
      - name
      - expression
      - duration
      - record
      - id
      syntax_pattern: ACCESS <var> ] [ GRANT | SHOW | REVOKE | PURGE ] ]
    commit:
      keywords:
      - TRANSACTION
      - COMMIT
      variables: []
      syntax_pattern: COMMIT ;
    break:
      keywords:
      - BREAK
      variables: []
      syntax_pattern: BREAK
    create:
      keywords:
      - BEFORE
      - RETURN
      - SET
      - PARALLEL
      - CONTENT
      - AFTER
      - NONE
      - DIFF
      - ONLY
      - CREATE
      variables:
      - duration
      - value
      - field
      - targets
      - statement_param
      syntax_pattern: CREATE <var> [ CONTENT <var> | SET <var> = <var> ... ] ;
    show:
      keywords:
      - TABLE
      - LIMIT
      - FOR
      - SINCE
      - SHOW
      - CHANGES
      variables:
      - number
      - tablename
      - timestamp
      - versionstamp
      syntax_pattern: SHOW CHANGES FOR TABLE <var> SINCE <var> | <var>
    insert:
      keywords:
      - INTO
      - UPDATE
      - BEFORE
      - 'ON'
      - RETURN
      - VALUES
      - INSERT
      - AFTER
      - RELATION
      - NONE
      variables:
      - values
      - what
      - value
      - fields
      - field
      - statement_param
      syntax_pattern: INSERT INTO <var> [ <var> | (<var>) VALUES (<var>) ] ;
    live:
      keywords:
      - FROM
      - WHERE
      - SELECT
      - FETCH
      - AS
      - LIVE
      - DIFF
      - VALUE
      variables:
      - fields
      - targets
      - alias
      - conditions
      syntax_pattern: LIVE SELECT [ <var> | DIFF ] FROM <var> ;
    cancel:
      keywords:
      - TRANSACTION
      - CANCEL
      variables: []
      syntax_pattern: CANCEL ;
    define/indexes:
      keywords:
      - UNIQUE
      - TYPE
      - COLUMNS
      - DIST
      - HNSW
      - EXISTS
      - SEARCH
      - DIMENSION
      - INDEX
      - CONCURRENTLY
      variables:
      - analyzer
      - name
      - dimension
      - type
      - efc
      - fields
      - table
      - b
      - m
      - k1
      syntax_pattern: 'DEFINE INDEX <var> ON <var> <var> [ UNIQUE | SEARCH ANALYZER
        <var> ] | MTREE DIMENSION <var> | HNSW '
    define/config:
      keywords:
      - INCLUDE
      - FULL
      - EXCLUDE
      - GRAPHQL
      - OVERWRITE
      - NOT
      - DEFINE
      - CONFIG
      - IF
      - PERMISSIONS
      variables:
      - expression
      syntax_pattern: DEFINE CONFIG ] [ GRAPHQL | EXCLUDE ) ] ]
    define/param:
      keywords:
      - COMMENT
      - WHERE
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - PERMISSIONS
      - NONE
      - PARAM
      - FULL
      variables:
      - name
      - condition
      - value
      - string
      syntax_pattern: DEFINE PARAM $<var> VALUE <var> ]
    define/token:
      keywords:
      - NAMESPACE
      - 'ON'
      - DATABASE
      - TYPE
      - COMMENT
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - TOKEN
      variables:
      - name
      - type
      - value
      - scope
      - string
      syntax_pattern: DEFINE TOKEN <var> ON TYPE <var> VALUE <var>
    define/table:
      keywords:
      - INCLUDE
      - TYPE
      - WHERE
      - SELECT
      - SCHEMAFULL
      - IN
      - ENFORCED
      - EXISTS
      - DROP
      - ANY
      variables:
      - condition
      - name
      - expression
      - duration
      - groups
      - table
      - string
      - projections
      - tables
      syntax_pattern: DEFINE TABLE <var> <var> <var> ]] [ AS SELECT <var> FROM <var>
        <var> ] ] ] [ PERMISSIONS [ NONE | FU
    define/namespace:
      keywords:
      - NAMESPACE
      - COMMENT
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - EXISTS
      variables:
      - name
      - string
      syntax_pattern: DEFINE NAMESPACE <var>
    define/event:
      keywords:
      - 'ON'
      - EVENT
      - COMMENT
      - THEN
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - TABLE
      - WHEN
      variables:
      - name
      - table
      - expression
      - string
      syntax_pattern: DEFINE EVENT <var> ON <var> THEN <var>
    define/scope:
      keywords:
      - SIGNUP
      - COMMENT
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - SIGNIN
      - SCOPE
      - EXISTS
      - SESSION
      variables:
      - name
      - expression
      - duration
      - string
      syntax_pattern: DEFINE SCOPE <var> SESSION <var> SIGNUP <var> SIGNIN <var>
    define/api:
      keywords:
      - FULL
      - THEN
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - FOR
      - PERMISSIONS
      - NONE
      - API
      variables:
      - endpoint
      - expression
      - value
      - HTTP_method
      - function
      syntax_pattern: DEFINE API <var>
    define/sequence:
      keywords:
      - START
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - BATCH
      - SEQUENCE
      - EXISTS
      - TIMEOUT
      variables:
      - name
      - start
      - duration
      - batch
      syntax_pattern: DEFINE SEQUENCE <var>
    define/bucket:
      keywords:
      - BUCKET
      - COMMENT
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - PERMISSIONS
      - EXISTS
      variables:
      - name
      - expression
      - backend
      - string
      syntax_pattern: DEFINE BUCKET <var> PERMISSIONS <var>
    define/analyzer:
      keywords:
      - ANALYZER
      - FILTERS
      - FUNCTION
      - COMMENT
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - EXISTS
      - TOKENIZERS
      variables:
      - name
      - tokenizers
      - function
      - filters
      - string
      syntax_pattern: DEFINE ANALYZER <var>
    define/field:
      keywords:
      - ALWAYS
      - TYPE
      - ASSERT
      - EXISTS
      - DEFAULT
      - FLEXIBLE
      - THEN
      - OVERWRITE
      - READONLY
      - NOT
      variables:
      - name
      - type
      - expression
      - table
      - string
      syntax_pattern: DEFINE FIELD <var> ON <var> TYPE <var> ] [ REFERENCE [ ON DELETE
        REJECT | ON DELETE CASCADE | ON DEL
    define/function:
      keywords:
      - FUNCTION
      - RETURN
      - COMMENT
      - OVERWRITE
      - WHERE
      - NOT
      - DEFINE
      - IF
      - PERMISSIONS
      - NONE
      variables:
      - argument
      - query
      - condition
      - name
      - returned
      - type
      - string
      syntax_pattern: DEFINE FUNCTION fn::<var>( ) { } ]
    define/user:
      keywords:
      - NAMESPACE
      - 'ON'
      - DATABASE
      - USER
      - PASSWORD
      - COMMENT
      - OVERWRITE
      - ROOT
      - NOT
      - DEFINE
      variables:
      - pass
      - name
      - duration
      - string
      - hash
      - roles
      syntax_pattern: DEFINE USER <var> ON ] ]
    define/database:
      keywords:
      - DATABASE
      - COMMENT
      - OVERWRITE
      - NOT
      - DEFINE
      - IF
      - EXISTS
      variables:
      - name
      - string
      syntax_pattern: DEFINE DATABASE <var>
  functions:
    file:
      bucket:
        signatures:
        - pattern: file::bucket(file) -> string
          params:
          - file
          returns: string
      copy:
        signatures:
        - pattern: file::copy(string)
          params:
          - string
          returns: null
      copy_if_not_exists:
        signatures:
        - pattern: file::copy_if_not_exists(string)
          params:
          - string
          returns: null
      delete:
        signatures:
        - pattern: file::delete(string)
          params:
          - string
          returns: null
      exists:
        signatures:
        - pattern: file::exists(string) -> bool
          params:
          - string
          returns: bool
      get:
        signatures:
        - pattern: file::get(string) -> bytes
          params:
          - string
          returns: bytes
      head:
        signatures:
        - pattern: file::head() -> object
          params: []
          returns: object
      key:
        signatures:
        - pattern: file::key(file) -> string
          params:
          - file
          returns: string
      list:
        signatures:
        - pattern: 'file::list(string, list_options: option<object>) -> array<object>'
          params:
          - string
          - option<object>
          returns: array<object>
      put:
        signatures:
        - pattern: file::put()
          params: []
          returns: null
      put_if_not_exists:
        signatures:
        - pattern: file::put_if_not_exists()
          params: []
          returns: null
      rename:
        signatures:
        - pattern: file::rename()
          params: []
          returns: null
      rename_if_not_exists:
        signatures:
        - pattern: file::rename_if_not_exists()
          params: []
          returns: null
    rand:
      bool:
        signatures:
        - pattern: rand::bool() -> bool
          params: []
          returns: bool
        - pattern: rand::bool(duration, duration) -> duration
          params:
          - duration
          - duration
          returns: duration
      enum:
        signatures:
        - pattern: rand::enum(value...) -> any
          params:
          - value...
          returns: any
      float:
        signatures:
        - pattern: rand::float() -> float
          params: []
          returns: float
        - pattern: rand::float(number, number) -> float
          params:
          - number
          - number
          returns: float
      guid:
        signatures:
        - pattern: rand::guid() -> string
          params: []
          returns: string
        - pattern: rand::guid(number) -> string
          params:
          - number
          returns: string
        - pattern: rand::guid(min, max) -> string
          params:
          - min
          - max
          returns: string
      int:
        signatures:
        - pattern: rand::int() -> int
          params: []
          returns: int
        - pattern: rand::int(number, number) -> int
          params:
          - number
          - number
          returns: int
      string:
        signatures:
        - pattern: rand::string() -> string
          params: []
          returns: string
        - pattern: rand::string(number) -> string
          params:
          - number
          returns: string
        - pattern: rand::string(number, number) -> string
          params:
          - number
          - number
          returns: string
      uuid:
        signatures:
        - pattern: rand::uuid() -> uuid
          params: []
          returns: uuid
        - pattern: rand::uuid(datetime) -> uuid
          params:
          - datetime
          returns: uuid
      ulid:
        signatures:
        - pattern: rand::ulid() -> ulid
          params: []
          returns: ulid
        - pattern: rand::ulid(datetime) -> uuid
          params:
          - datetime
          returns: uuid
    object:
      entries:
        signatures:
        - pattern: object::entries(object) -> array
          params:
          - object
          returns: array
      extend:
        signatures:
        - pattern: object::extend(object, object) -> object
          params:
          - object
          - object
          returns: object
      from_entries:
        signatures:
        - pattern: object::from_entries(array) -> object
          params:
          - array
          returns: object
      is_empty:
        signatures:
        - pattern: object::is_empty(object) -> bool
          params:
          - object
          returns: bool
      keys:
        signatures:
        - pattern: object::keys(object) -> array
          params:
          - object
          returns: array
      len:
        signatures:
        - pattern: object::len(object) -> number
          params:
          - object
          returns: number
      remove:
        signatures:
        - pattern: object::remove(object, string|array<string>) -> object
          params:
          - object
          - string|array<string>
          returns: object
      values:
        signatures:
        - pattern: object::values(object) -> array
          params:
          - object
          returns: array
    array:
      add:
        signatures:
        - pattern: array::add(array, value) -> array
          params:
          - array
          - value
          returns: array
      at:
        signatures:
        - pattern: 'array::at(array, index: int) -> any'
          params:
          - array
          - int
          returns: any
      append:
        signatures:
        - pattern: array::append(array, value) -> array
          params:
          - array
          - value
          returns: array
      boolean_and:
        signatures:
        - pattern: 'array::boolean_and(lh: array, rh: array)'
          params:
          - array
          - array
          returns: null
      boolean_or:
        signatures:
        - pattern: 'array::boolean_or(lh: array, rh: array)'
          params:
          - array
          - array
          returns: null
      boolean_xor:
        signatures:
        - pattern: 'array::boolean_xor(lh: array, rh: array)'
          params:
          - array
          - array
          returns: null
      boolean_not:
        signatures:
        - pattern: array::boolean_not(array)
          params:
          - array
          returns: null
      combine:
        signatures:
        - pattern: array::combine(array, array) -> array
          params:
          - array
          - array
          returns: array
      complement:
        signatures:
        - pattern: array::complement(array, array) -> array
          params:
          - array
          - array
          returns: array
      concat:
        signatures:
        - pattern: array::concat(array, array) -> array
          params:
          - array
          - array
          returns: array
      clump:
        signatures:
        - pattern: 'array::clump(array, size: int) -> array'
          params:
          - array
          - int
          returns: array
      difference:
        signatures:
        - pattern: array::difference(array, array) -> array
          params:
          - array
          - array
          returns: array
      distinct:
        signatures:
        - pattern: array::distinct(array) -> array
          params:
          - array
          returns: array
      fill:
        signatures:
        - pattern: array::fill(array, any) -> array
          params:
          - array
          - any
          returns: array
        - pattern: 'array::fill(array, any, start: int, end: int) -> array'
          params:
          - array
          - any
          - int
          - int
          returns: array
      first:
        signatures:
        - pattern: array::first(array) -> any
          params:
          - array
          returns: any
      flatten:
        signatures:
        - pattern: array::flatten(array) -> array
          params:
          - array
          returns: array
      fold:
        signatures:
        - pattern: array::fold(array, initial_value, @closure) -> value
          params:
          - array
          - initial_value
          - '@closure'
          returns: value
      group:
        signatures:
        - pattern: array::group(array) -> array
          params:
          - array
          returns: array
      insert:
        signatures:
        - pattern: array::insert(array, value, number) -> array
          params:
          - array
          - value
          - number
          returns: array
      intersect:
        signatures:
        - pattern: array::intersect(array, array) -> array
          params:
          - array
          - array
          returns: array
      is_empty:
        signatures:
        - pattern: array::is_empty(array) -> bool
          params:
          - array
          returns: bool
      join:
        signatures:
        - pattern: array::join(array, string) -> string
          params:
          - array
          - string
          returns: string
      last:
        signatures:
        - pattern: array::last(array) -> any
          params:
          - array
          returns: any
      len:
        signatures:
        - pattern: array::len(array) -> number
          params:
          - array
          returns: number
      logical_and:
        signatures:
        - pattern: 'array::logical_and(lh: array, rh: array)'
          params:
          - array
          - array
          returns: null
      logical_or:
        signatures:
        - pattern: 'array::logical_or(lh: array, rh: array)'
          params:
          - array
          - array
          returns: null
      logical_xor:
        signatures:
        - pattern: 'array::logical_xor(lh: array, rh: array)'
          params:
          - array
          - array
          returns: null
      map:
        signatures:
        - pattern: array::map(array, @closure) -> array;
          params:
          - array
          - '@closure'
          returns: array;
      max:
        signatures:
        - pattern: array::max(array<any>) -> any
          params:
          - array<any>
          returns: any
      matches:
        signatures:
        - pattern: array::matches(array, value) -> array<bool>
          params:
          - array
          - value
          returns: array<bool>
      min:
        signatures:
        - pattern: array::min(array<any>) -> any
          params:
          - array<any>
          returns: any
      pop:
        signatures:
        - pattern: array::pop(array) -> value
          params:
          - array
          returns: value
      prepend:
        signatures:
        - pattern: array::prepend(array, value) -> array
          params:
          - array
          - value
          returns: array
      push:
        signatures:
        - pattern: array::push(array, value) -> array
          params:
          - array
          - value
          returns: array
      range:
        signatures:
        - pattern: 'array::range(start: int, count: int) -> array'
          params:
          - int
          - int
          returns: array
      reduce:
        signatures:
        - pattern: array::reduce(array, @closure) -> value
          params:
          - array
          - '@closure'
          returns: value
      remove:
        signatures:
        - pattern: array::remove(array, number) -> array
          params:
          - array
          - number
          returns: array
      repeat:
        signatures:
        - pattern: 'array::repeat(any, count: int) -> array'
          params:
          - any
          - int
          returns: array
      reverse:
        signatures:
        - pattern: array::reverse(array) -> array
          params:
          - array
          returns: array
      shuffle:
        signatures:
        - pattern: array::shuffle(array) -> array
          params:
          - array
          returns: array
      slice:
        signatures:
        - pattern: 'array::slice(array, start: int, len: int) -> array'
          params:
          - array
          - int
          - int
          returns: array
      sort:
        signatures:
        - pattern: array::sort(array) -> array
          params:
          - array
          returns: array
        - pattern: array::sort(array, bool) -> array
          params:
          - array
          - bool
          returns: array
        - pattern: array::sort(array, string) -> array
          params:
          - array
          - string
          returns: array
      sort_lexical:
        signatures:
        - pattern: array::sort_lexical(array) -> array
          params:
          - array
          returns: array
        - pattern: array::sort_lexical(array, bool) -> array
          params:
          - array
          - bool
          returns: array
        - pattern: array::sort_lexical(array, string) -> array
          params:
          - array
          - string
          returns: array
      sort_natural:
        signatures:
        - pattern: array::sort_natural(array) -> array
          params:
          - array
          returns: array
        - pattern: array::sort_natural(array, bool) -> array
          params:
          - array
          - bool
          returns: array
        - pattern: array::sort_natural(array, string) -> array
          params:
          - array
          - string
          returns: array
      sort_natural_lexical:
        signatures:
        - pattern: array::sort_natural_lexical(array) -> array
          params:
          - array
          returns: array
        - pattern: array::sort_natural_lexical(array, bool) -> array
          params:
          - array
          - bool
          returns: array
        - pattern: array::sort_natural_lexical(array, string) -> array
          params:
          - array
          - string
          returns: array
      swap:
        signatures:
        - pattern: 'array::swap(array, from: int, to: int) -> array'
          params:
          - array
          - int
          - int
          returns: array
      transpose:
        signatures:
        - pattern: array::transpose(array<array>) -> array<array>
          params:
          - array<array>
          returns: array<array>
      union:
        signatures:
        - pattern: array::union(array, array) -> array
          params:
          - array
          - array
          returns: array
      windows:
        signatures:
        - pattern: 'array::windows(array, size: int) -> array'
          params:
          - array
          - int
          returns: array
    duration:
      days:
        signatures:
        - pattern: duration::days(duration) -> number
          params:
          - duration
          returns: number
      hours:
        signatures:
        - pattern: duration::hours(duration) -> number
          params:
          - duration
          returns: number
      micros:
        signatures:
        - pattern: duration::micros(duration) -> number
          params:
          - duration
          returns: number
      millis:
        signatures:
        - pattern: duration::millis(duration) -> number
          params:
          - duration
          returns: number
      mins:
        signatures:
        - pattern: duration::mins(duration) -> number
          params:
          - duration
          returns: number
      nanos:
        signatures:
        - pattern: duration::nanos(duration) -> number
          params:
          - duration
          returns: number
      secs:
        signatures:
        - pattern: duration::secs(duration) -> number
          params:
          - duration
          returns: number
      weeks:
        signatures:
        - pattern: duration::weeks(duration) -> number
          params:
          - duration
          returns: number
      years:
        signatures:
        - pattern: duration::years(duration) -> number
          params:
          - duration
          returns: number
    meta:
      id:
        signatures:
        - pattern: meta::id(record) -> value
          params:
          - record
          returns: value
      tb:
        signatures:
        - pattern: meta::tb(record) -> string
          params:
          - record
          returns: string
    record:
      exists:
        signatures:
        - pattern: record::exists(record) -> bool
          params:
          - record
          returns: bool
      id:
        signatures:
        - pattern: record::id(record) -> value
          params:
          - record
          returns: value
      tb:
        signatures:
        - pattern: record::tb(record) -> string
          params:
          - record
          returns: string
    bytes:
      len:
        signatures:
        - pattern: bytes::len(bytes) -> int
          params:
          - bytes
          returns: int
    search:
      analyze:
        signatures:
        - pattern: search::analyze(analyzer, string) -> array<string>
          params:
          - analyzer
          - string
          returns: array<string>
      score:
        signatures:
        - pattern: search::score(number) -> number
          params:
          - number
          returns: number
      highlight:
        signatures:
        - pattern: search::highlight(string, string, number, [boolean]) -> string
            | string[]
          params:
          - string
          - string
          - number
          - '[boolean]'
          returns: string | string[]
      offsets:
        signatures:
        - pattern: search::offsets(number, [boolean]) -> object
          params:
          - number
          - '[boolean]'
          returns: object
    string:
      concat:
        signatures:
        - pattern: string::concat(string, ...) -> string
          params:
          - string
          - '...'
          returns: string
      contains:
        signatures:
        - pattern: string::contains(string, string) -> bool
          params:
          - string
          - string
          returns: bool
      ends_with:
        signatures:
        - pattern: string::ends_with(string, string) -> bool
          params:
          - string
          - string
          returns: bool
      join:
        signatures:
        - pattern: string::join(string, string...) -> string
          params:
          - string
          - string...
          returns: string
      len:
        signatures:
        - pattern: string::len(string) -> number
          params:
          - string
          returns: number
      lowercase:
        signatures:
        - pattern: string::lowercase(string) -> string
          params:
          - string
          returns: string
      matches:
        signatures:
        - pattern: string::matches(string, string) -> bool
          params:
          - string
          - string
          returns: bool
      repeat:
        signatures:
        - pattern: string::repeat(string, number) -> string
          params:
          - string
          - number
          returns: string
      replace:
        signatures:
        - pattern: string::replace(string, string, string) -> string
          params:
          - string
          - string
          - string
          returns: string
        - pattern: string::replace(string, string|regex, string) -> string
          params:
          - string
          - string|regex
          - string
          returns: string
      reverse:
        signatures:
        - pattern: string::reverse(string) -> string
          params:
          - string
          returns: string
      slice:
        signatures:
        - pattern: string::slice(string, number, number) -> string
          params:
          - string
          - number
          - number
          returns: string
      slug:
        signatures:
        - pattern: string::slug(string) -> string
          params:
          - string
          returns: string
      split:
        signatures:
        - pattern: string::split(string, string) -> array
          params:
          - string
          - string
          returns: array
      starts_with:
        signatures:
        - pattern: string::starts_with(string, string) -> bool
          params:
          - string
          - string
          returns: bool
      trim:
        signatures:
        - pattern: string::trim(string) -> string
          params:
          - string
          returns: string
      uppercase:
        signatures:
        - pattern: string::uppercase(string) -> string
          params:
          - string
          returns: string
      words:
        signatures:
        - pattern: string::words(string) -> array
          params:
          - string
          returns: array
    math:
      abs:
        signatures:
        - pattern: math::abs(number) -> number
          params:
          - number
          returns: number
      acos:
        signatures:
        - pattern: math::acos(number) -> number
          params:
          - number
          returns: number
      acot:
        signatures:
        - pattern: math::acot(number) -> number
          params:
          - number
          returns: number
      asin:
        signatures:
        - pattern: math::asin(number) -> number
          params:
          - number
          returns: number
      atan:
        signatures:
        - pattern: math::atan(number) -> number
          params:
          - number
          returns: number
      bottom:
        signatures:
        - pattern: math::bottom(array<number>, number) -> number
          params:
          - array<number>
          - number
          returns: number
      ceil:
        signatures:
        - pattern: math::ceil(number) -> number
          params:
          - number
          returns: number
      clamp:
        signatures:
        - pattern: math::clamp(number, min, max) -> number
          params:
          - number
          - min
          - max
          returns: number
      cos:
        signatures:
        - pattern: math::cos(number) -> number
          params:
          - number
          returns: number
      cot:
        signatures:
        - pattern: math::cot(number) -> number
          params:
          - number
          returns: number
      fixed:
        signatures:
        - pattern: math::fixed(number, number) -> number
          params:
          - number
          - number
          returns: number
      floor:
        signatures:
        - pattern: math::floor(number) -> number
          params:
          - number
          returns: number
      interquartile:
        signatures:
        - pattern: math::interquartile(array<number>) -> number
          params:
          - array<number>
          returns: number
      lerp:
        signatures:
        - pattern: math::lerp(a, b, t) -> number
          params:
          - a
          - b
          - t
          returns: number
      lerpangle:
        signatures:
        - pattern: math::lerpangle(a, b, t) -> number
          params:
          - a
          - b
          - t
          returns: number
      ln:
        signatures:
        - pattern: math::ln(number) -> number
          params:
          - number
          returns: number
      log:
        signatures:
        - pattern: math::log(number, base) -> number
          params:
          - number
          - base
          returns: number
      max:
        signatures:
        - pattern: math::max(array<number>) -> number
          params:
          - array<number>
          returns: number
      mean:
        signatures:
        - pattern: math::mean(array<number>) -> number
          params:
          - array<number>
          returns: number
      median:
        signatures:
        - pattern: math::median(array<number>) -> number
          params:
          - array<number>
          returns: number
      midhinge:
        signatures:
        - pattern: math::midhinge(array<number>) -> number
          params:
          - array<number>
          returns: number
      min:
        signatures:
        - pattern: math::min(array<number>) -> number
          params:
          - array<number>
          returns: number
      mode:
        signatures:
        - pattern: math::mode(array<number>) -> number
          params:
          - array<number>
          returns: number
      nearestrank:
        signatures:
        - pattern: math::nearestrank(array<number>, number) -> number
          params:
          - array<number>
          - number
          returns: number
      percentile:
        signatures:
        - pattern: math::percentile(array<number>, number) -> number
          params:
          - array<number>
          - number
          returns: number
      pow:
        signatures:
        - pattern: math::pow(number, number) -> number
          params:
          - number
          - number
          returns: number
      product:
        signatures:
        - pattern: math::product(array<number>) -> number
          params:
          - array<number>
          returns: number
      round:
        signatures:
        - pattern: math::round(number) -> number
          params:
          - number
          returns: number
      sign:
        signatures:
        - pattern: math::sign(number) -> number
          params:
          - number
          returns: number
      sin:
        signatures:
        - pattern: math::sin(number) -> number
          params:
          - number
          returns: number
      spread:
        signatures:
        - pattern: math::spread(array<number>) -> number
          params:
          - array<number>
          returns: number
      sqrt:
        signatures:
        - pattern: math::sqrt(number) -> number
          params:
          - number
          returns: number
      stddev:
        signatures:
        - pattern: math::stddev(array<number>) -> number
          params:
          - array<number>
          returns: number
      sum:
        signatures:
        - pattern: math::sum(array<number>) -> number
          params:
          - array<number>
          returns: number
      tan:
        signatures:
        - pattern: math::tan(number) -> number
          params:
          - number
          returns: number
      top:
        signatures:
        - pattern: math::top(array<number>, number) -> number
          params:
          - array<number>
          - number
          returns: number
      trimean:
        signatures:
        - pattern: math::trimean(array<number>) -> number
          params:
          - array<number>
          returns: number
      variance:
        signatures:
        - pattern: math::variance(array<number>) -> number
          params:
          - array<number>
          returns: number
    http:
      head:
        signatures:
        - pattern: http::head(string) -> null
          params:
          - string
          returns: 'null'
        - pattern: http::head(string, object) -> null
          params:
          - string
          - object
          returns: 'null'
      get:
        signatures:
        - pattern: http::get(string) -> value
          params:
          - string
          returns: value
        - pattern: http::get(string, object) -> value
          params:
          - string
          - object
          returns: value
      put:
        signatures:
        - pattern: http::put(string, object) -> value
          params:
          - string
          - object
          returns: value
        - pattern: http::put(string, object, object) -> value
          params:
          - string
          - object
          - object
          returns: value
      post:
        signatures:
        - pattern: http::post(string, object) -> value
          params:
          - string
          - object
          returns: value
        - pattern: http::post(string, object, object) -> value
          params:
          - string
          - object
          - object
          returns: value
      patch:
        signatures:
        - pattern: http::patch(string, object) -> value
          params:
          - string
          - object
          returns: value
        - pattern: http::patch(string, object, object) -> value
          params:
          - string
          - object
          - object
          returns: value
      delete:
        signatures:
        - pattern: http::delete(string) -> value
          params:
          - string
          returns: value
        - pattern: http::delete(string, object) -> value
          params:
          - string
          - object
          returns: value
    api:
      invoke:
        signatures:
        - pattern: 'api::invoke($path: string, $options: option<object>) -> object'
          params:
          - string
          - option<object>
          returns: object
      timeout:
        signatures:
        - pattern: api::timeout(duration)
          params:
          - duration
          returns: null
    sequence:
      next:
        signatures:
        - pattern: sequence::next(sequence_name) -> int
          params:
          - sequence_name
          returns: int
    vector:
      add:
        signatures:
        - pattern: vector::add(array, array) -> array
          params:
          - array
          - array
          returns: array
      angle:
        signatures:
        - pattern: vector::angle(array, array) -> number
          params:
          - array
          - array
          returns: number
      cross:
        signatures:
        - pattern: vector::cross(array, array) -> array
          params:
          - array
          - array
          returns: array
      divide:
        signatures:
        - pattern: vector::divide(array, array) -> array
          params:
          - array
          - array
          returns: array
      dot:
        signatures:
        - pattern: vector::dot(array, array) -> number
          params:
          - array
          - array
          returns: number
      magnitude:
        signatures:
        - pattern: vector::magnitude(array) -> number
          params:
          - array
          returns: number
      multiply:
        signatures:
        - pattern: vector::multiply(array, array) -> number
          params:
          - array
          - array
          returns: number
      normalize:
        signatures:
        - pattern: vector::normalize(array) -> array
          params:
          - array
          returns: array
      project:
        signatures:
        - pattern: vector::project(array, array) -> array
          params:
          - array
          - array
          returns: array
      scale:
        signatures:
        - pattern: vector::scale(array, number) -> array
          params:
          - array
          - number
          returns: array
      subtract:
        signatures:
        - pattern: vector::subtract(array, array) -> array
          params:
          - array
          - array
          returns: array
    geo:
      area:
        signatures:
        - pattern: geo::area(geometry) -> number
          params:
          - geometry
          returns: number
      bearing:
        signatures:
        - pattern: geo::bearing(point, point) -> number
          params:
          - point
          - point
          returns: number
      centroid:
        signatures:
        - pattern: geo::centroid(geometry) -> number
          params:
          - geometry
          returns: number
      distance:
        signatures:
        - pattern: geo::distance(point, point) -> number
          params:
          - point
          - point
          returns: number
    session:
      ac:
        signatures:
        - pattern: session::ac() -> string
          params: []
          returns: string
      db:
        signatures:
        - pattern: session::db() -> string
          params: []
          returns: string
      id:
        signatures:
        - pattern: session::id() -> string
          params: []
          returns: string
      ip:
        signatures:
        - pattern: session::ip() -> string
          params: []
          returns: string
      ns:
        signatures:
        - pattern: session::ns() -> string
          params: []
          returns: string
      origin:
        signatures:
        - pattern: session::origin() -> string
          params: []
          returns: string
      rd:
        signatures:
        - pattern: session::rd() -> string
          params: []
          returns: string
      token:
        signatures:
        - pattern: session::token() -> string
          params: []
          returns: string
    time:
      ceil:
        signatures:
        - pattern: time::ceil(datetime, duration) -> datetime
          params:
          - datetime
          - duration
          returns: datetime
      day:
        signatures:
        - pattern: time::day(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      floor:
        signatures:
        - pattern: time::floor(datetime, duration) -> datetime
          params:
          - datetime
          - duration
          returns: datetime
      format:
        signatures:
        - pattern: time::format(datetime, string) -> string
          params:
          - datetime
          - string
          returns: string
      group:
        signatures:
        - pattern: time::group(datetime, string) -> datetime
          params:
          - datetime
          - string
          returns: datetime
      hour:
        signatures:
        - pattern: time::hour(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      max:
        signatures:
        - pattern: time::max(array<datetime>) -> datetime
          params:
          - array<datetime>
          returns: datetime
      micros:
        signatures:
        - pattern: time::micros(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      millis:
        signatures:
        - pattern: time::millis(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      min:
        signatures:
        - pattern: time::min(array<datetime>) -> datetime
          params:
          - array<datetime>
          returns: datetime
      minute:
        signatures:
        - pattern: time::minute(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      month:
        signatures:
        - pattern: time::month(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      nano:
        signatures:
        - pattern: time::nano(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      now:
        signatures:
        - pattern: time::now() -> datetime
          params: []
          returns: datetime
      round:
        signatures:
        - pattern: time::round(datetime, duration) -> datetime
          params:
          - datetime
          - duration
          returns: datetime
      second:
        signatures:
        - pattern: time::second(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      timezone:
        signatures:
        - pattern: time::timezone() -> string
          params: []
          returns: string
      unix:
        signatures:
        - pattern: time::unix(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      wday:
        signatures:
        - pattern: time::wday(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      week:
        signatures:
        - pattern: time::week(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      yday:
        signatures:
        - pattern: time::yday(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
      year:
        signatures:
        - pattern: time::year(option<datetime>) -> number
          params:
          - option<datetime>
          returns: number
    type:
      array:
        signatures:
        - pattern: type::array(array | range) -> bool
          params:
          - array | range
          returns: bool
      bool:
        signatures:
        - pattern: type::bool(bool | string) -> bool
          params:
          - bool | string
          returns: bool
      bytes:
        signatures:
        - pattern: type::bytes(bytes | string) -> bool
          params:
          - bytes | string
          returns: bool
      datetime:
        signatures:
        - pattern: type::datetime(datetime | string) -> datetime
          params:
          - datetime | string
          returns: datetime
      decimal:
        signatures:
        - pattern: type::decimal(decimal | float | int | number | string) -> decimal
          params:
          - decimal | float | int | number | string
          returns: decimal
      duration:
        signatures:
        - pattern: type::duration(duration | string) -> duration
          params:
          - duration | string
          returns: duration
      field:
        signatures:
        - pattern: type::field($field)
          params:
          - $field
          returns: null
      fields:
        signatures:
        - pattern: type::fields($fields)
          params:
          - $fields
          returns: null
      file:
        signatures:
        - pattern: 'type::file(bucket: string, key: string) -> file'
          params:
          - string
          - string
          returns: file
      float:
        signatures:
        - pattern: type::float(decimal | float | int | number | string) -> float
          params:
          - decimal | float | int | number | string
          returns: float
      int:
        signatures:
        - pattern: type::int(decimal | float | int | number | string) -> int
          params:
          - decimal | float | int | number | string
          returns: int
      number:
        signatures:
        - pattern: type::number(decimal | float | int | number | string) -> number
          params:
          - decimal | float | int | number | string
          returns: number
      point:
        signatures:
        - pattern: type::point(array | point) -> point
          params:
          - array | point
          returns: point
      range:
        signatures:
        - pattern: type::range(range | array) -> range<record>
          params:
          - range | array
          returns: range<record>
      record:
        signatures:
        - pattern: type::record(record | string, option<string>) -> record
          params:
          - record | string
          - option<string>
          returns: record
      string:
        signatures:
        - pattern: type::string(any) -> string
          params:
          - any
          returns: string
        - pattern: type::string(any) -> string
          params:
          - any
          returns: string
      table:
        signatures:
        - pattern: type::table(record | string) -> string
          params:
          - record | string
          returns: string
      thing:
        signatures:
        - pattern: type::thing(any, any) -> record
          params:
          - any
          - any
          returns: record
      uuid:
        signatures:
        - pattern: type::uuid(string | uuid) -> uuid
          params:
          - string | uuid
          returns: uuid
    value:
      diff:
        signatures:
        - pattern: value::diff(value, value) -> array<object>
          params:
          - value
          - value
          returns: array<object>
      patch:
        signatures:
        - pattern: 'value::patch(value, patch: array<object>) -> value'
          params:
          - value
          - array<object>
          returns: value
  operators:
    logical:
    - symbol: '&&'
      alt: AND
      desc: Checks whether both of two values are truthy.
    - symbol: '||'
      alt: OR
      desc: Checks whether either of two values are truthy.
    - symbol: '!'
      alt: null
      desc: Reverses the truthiness of a value.
    - symbol: '!!'
      alt: null
      desc: 'Determines the truthiness of a value (simply an application of the `!`
        operator '
    comparison:
    - symbol: '='
      alt: IS
      desc: Check whether two values are equal.
    - symbol: '!='
      alt: IS NOT
      desc: Check whether two values are equal.
    - symbol: ==
      alt: null
      desc: Check whether two values are exact. This operator also checks that each
        value ha
    - symbol: ?=
      alt: null
      desc: Check whether any value in an array equals another value.
    - symbol: '*='
      alt: null
      desc: Check whether all values in an array equals another value.
    - symbol: <
      alt: null
      desc: Check whether a value is less than another value.
    - symbol: <=
      alt: null
      desc: Check whether a value is less than or equal to another value.
    - symbol: '>'
      alt: null
      desc: Check whether a value is less than another value.
    - symbol: '>='
      alt: null
      desc: Check whether a value is less than or equal to another value.
    mathematical:
    - symbol: +
      alt: null
      desc: Add two values together.
    - symbol: '-'
      alt: null
      desc: Subtracts a value from another value.
    - symbol: '*'
      alt: "\xD7"
      desc: Multiplies a value by another value.
    - symbol: /
      alt: "\xF7"
      desc: Divides a value with another value.
    - symbol: '**'
      alt: null
      desc: Raises a base value by another value.
    graph:
    - symbol: OUTSIDE
      alt: null
      desc: Check whether a geometry value is outside another geometry value.
    - symbol: INTERSECTS
      alt: null
      desc: Check whether a geometry value intersects another geometry value.
    set:
    - symbol: CONTAINS
      alt: "\u220B"
      desc: Check whether a value contains another value.
    - symbol: CONTAINSNOT
      alt: "\u220C"
      desc: Check whether a value does not contain another value.
    - symbol: CONTAINSALL
      alt: "\u2287"
      desc: Check whether a value contains all of multiple values.
    - symbol: CONTAINSANY
      alt: "\u2283"
      desc: Check whether a value contains any of multiple values.
    - symbol: INSIDE
      alt: "\u2208"
      desc: Check whether a value is contained within another value.
    - symbol: NOTINSIDE
      alt: "\u2209"
      desc: Check whether a value is not contained within another value.
    - symbol: ALLINSIDE
      alt: "\u2286"
      desc: Check whether all of multiple values are contained within another value.
    fuzzy:
    - symbol: '~'
      alt: null
      desc: Compare two values for equality using fuzzy matching.
    - symbol: '!~'
      alt: null
      desc: Compare two values for inequality using fuzzy matching.
    - symbol: ?~
      alt: null
      desc: Check whether any value in a set is equal to a value using fuzzy matching.
    - symbol: '*~'
      alt: null
      desc: Check whether all values in a set are equal to a value using fuzzy matching.
    null_handling:
    - symbol: ??
      alt: null
      desc: Check whether either of two values are truthy and not `NULL`.
    - symbol: '?:'
      alt: null
      desc: Check whether either of two values are truthy.
    other:
    - symbol: ANYINSIDE
      alt: "\u2282"
      desc: Check whether any of multiple values are contained within another value.
    - symbol: NONEINSIDE
      alt: "\u2284"
      desc: Check whether none of multiple values are contained within another value.
    - symbol: MATCHES
      alt: null
      desc: Checks whether the terms are found in a full-text indexed field.

```

================================================================================

## USAGE INSTRUCTIONS

1. Load this entire file into context
2. Use schema to generate correct SurrealQL syntax
3. Reference function signatures and operator syntax
4. Follow statement patterns for proper query structure

## REMEMBER:
- This is 85% of SurrealQL syntax compressed from 297,445 tokens
- Missing: query clauses (FETCH, EXPLAIN), advanced type specs, comments
- When in doubt, check the schema!