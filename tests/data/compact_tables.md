simple
.
a | bb
| - | -
1 | 2
.
| a | bb |
| -- | -- |
| 1 | 2 |
.

empty headers
.
|  | |
|- | -
|1 | 2
.
|  |  |
| -- | -- |
| 1 | 2 |
.

no body
.
|  | |
|- | -
.
|  |  |
| -- | -- |
.

alignment
.
a | b | c
:- | -: | :-:
1 | 2 | 3
xxxxxx | yyyyyy | zzzzzz
.
| a | b | c |
| :- | -: | :-: |
| 1 | 2 | 3 |
| xxxxxx | yyyyyy | zzzzzz |
.

nested syntax
.
*a* | [b](link)
| - | -
`c` | [d](link)
.
| *a* | [b](link) |
| -- | -- |
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

paragraph before/after
.
x
a | bb
-- | -
1 | 2
y
.
x

| a | bb |
| -- | -- |
| 1 | 2 |
| y |  |
.

Nested tables in blockquotes:
.
> a|b
> ---|---
> bar|baz
.
> | a | b |
> | -- | -- |
> | bar | baz |
.

references
.
| [![a][b]][c] |
| - |
| [![a][b]][c] |

[b]: link1
[c]: link2
.
| [![a][b]][c] |
| -- |
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

Expanded Unicode (https://github.com/hukkin/mdformat-tables/issues/16)
.
| 模型 | 时间        |
|-------|------|
| BBFN   | 2021-07     |
.
| 模型 | 时间 |
| -- | -- |
| BBFN | 2021-07 |
.
