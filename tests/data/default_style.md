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
