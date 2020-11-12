import itertools
from typing import Any, Mapping, Optional, Sequence, Tuple

from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdformat.renderer import LOGGER, MDRenderer


def update_mdit(_mdit: MarkdownIt) -> None:
    pass


def render_token(
    renderer: MDRenderer,
    tokens: Sequence[Token],
    index: int,
    options: Mapping[str, Any],
    env: dict,
) -> Optional[Tuple[str, int]]:
    first_pass = "mdformat-gfm" not in env
    if first_pass:
        env["mdformat-gfm"] = {}
    return None
