Table
.
a | b | c
:- | -: | :-:
1 | 2 | 3
xxxxxx | yyyyyy | zzzzzz
.
| a      |      b |   c    |
| :----- | -----: | :----: |
| 1      |      2 |   3    |
| xxxxxx | yyyyyy | zzzzzz |
.

Simple strikethrough
.
~~Hi~~ Hello, world!
.
~~Hi~~ Hello, world!
.

Escaped strikethrough
.
~~Hi~\~ Hello, world!
.
\~~Hi\~~ Hello, world!
.

Nested tasklists
.
- [x] foo
  - [ ] bar
  - [x] baz
- [ ] bim
.
- [x] foo
  - [ ] bar
  - [x] baz
- [ ] bim
.

Mix tasks and other items
.
1. [x] task done
2. not a task
3. [ ] task not done
4. not a task
.
1. [x] task done
1. not a task
1. [ ] task not done
1. not a task
.

Reduce tasklist whitespace
.
-   [x]    reduce spaces
.
- [x] reduce spaces
.

Autolink with a backslash
.
http://www.python.org/autolink\extension
.
http://www.python.org/autolink\extension
.

Autolink with percentage encoded space
.
https://mytest.com/files/word%20document.docx
.
https://mytest.com/files/word%20document.docx
.

Autolink with port
.
test.com:443
.
test.com:443
.

Tasklist escape
.
- [x] foo
- \[ ] bim 
.
- [x] foo
- \[ \] bim
.

empty table headers
.
|  | |
|- | -
|1 | 2
.
|     |     |
| --- | --- |
| 1   | 2   |
.

no table body
.
|  | |
|- | -
.
|     |     |
| --- | --- |
.

table alignment
.
a | b | c
:- | -: | :-:
1 | 2 | 3
xxxxxx | yyyyyy | zzzzzz
.
| a      |      b |   c    |
| :----- | -----: | :----: |
| 1      |      2 |   3    |
| xxxxxx | yyyyyy | zzzzzz |
.

nested table syntax
.
*a* | [b](link)
| - | -
`c` | [d](link)
.
| *a* | [b](link) |
| --- | --------- |
| `c` | [d](link) |
.

A list takes precedence in case of ambiguity
.
a | b
- | -
1 | 2
.
a | b

- | \-
  1 | 2
.

paragraph before/after table
.
x
a | bb
-- | -
1 | 2
y
.
x

| a   | bb  |
| --- | --- |
| 1   | 2   |
| y   |     |
.

Nested tables in blockquotes:
.
> a|b
> ---|---
> bar|baz
.
> | a   | b   |
> | --- | --- |
> | bar | baz |
.

references in table
.
| [![a][b]][c] |
| - |
| [![a][b]][c] |

[b]: link1
[c]: link2
.
| [![a][b]][c] |
| ------------ |
| [![a][b]][c] |

[b]: link1
[c]: link2
.

Escaped table 1
.
| a |
\| - |
.
| a |
| \- |
.

Escaped table 2
.
a
-\:
.
a
\-:
.

Escaped table 3
.
a
:\-
.
a
:\-
.

Expanded Unicode in table (https://github.com/hukkin/mdformat-tables/issues/16)
.
| 模型 | 时间        |
|-------|------|
| BBFN   | 2021-07     |
.
| 模型 | 时间    |
| ---- | ------- |
| BBFN | 2021-07 |
.
