"""A replacement for the "text" inline rule in markdown-it.

The default "text" rule will skip until the next character in
`_TerminatorChars` is found. This extends the set of termination points
to those that can potentially be the beginning of a GFM autolink. The
GFM autolink plugin also works with "text" inline rule disabled, but
this should (at least partially) bring back the performance boost that
"text" inline rule provides.
"""

import re

from markdown_it.rules_inline import StateInline

GFM_WHITESPACE = frozenset(" \t\n\v\f\r")
BEFORE_AUTOLINK_CHARS = GFM_WHITESPACE | {"*", "_", "~", "("}

# The default set of terminator characters
_TerminatorChars = {
    "\n",
    "!",
    "#",
    "$",
    "%",
    "&",
    "*",
    "+",
    "-",
    ":",
    "<",
    "=",
    ">",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "}",
    "~",
}

_default_terminator = "[" + re.escape("".join(_TerminatorChars)) + "]"
_gfm_autolink_terminator = (
    r"(?:" r"www\." "|" "http" "|" "mailto:" "|" "xmpp:" "|" r"[a-zA-Z0-9._+-]+@" r")"
)
_before_autolink = "[" + re.escape("".join(BEFORE_AUTOLINK_CHARS)) + "]"

_RE_TERMINATOR_FIRST_CHAR = re.compile(
    _default_terminator + "|" + _gfm_autolink_terminator
)
_RE_TERMINATOR_NON_FIRST_CHAR = re.compile(
    r"(?s:.)"  # match any character (also newline)
    + _default_terminator
    + "|"
    + _before_autolink
    + _gfm_autolink_terminator
)


def text_rule(state: StateInline, silent: bool) -> bool:
    pos = state.pos

    if not pos:
        if _RE_TERMINATOR_FIRST_CHAR.match(state.src):
            return False
        pos += 1

    terminator_match = _RE_TERMINATOR_NON_FIRST_CHAR.search(state.src, pos - 1)
    if terminator_match:
        pos = terminator_match.start() + 1
    else:
        pos = state.posMax

    if pos == state.pos:
        return False

    if not silent:
        state.pending += state.src[state.pos : pos]

    state.pos = pos

    return True
