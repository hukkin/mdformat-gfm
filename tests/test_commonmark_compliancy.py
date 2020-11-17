import json
from pathlib import Path

import mdformat
from mdformat._util import is_md_equal
import pytest

SPECTESTS_PATH = Path(__file__).parent / "data" / "commonmark_spec_v0.29.json"
SPECTESTS_CASES = tuple(
    {"name": str(entry["example"]), "md": entry["markdown"]}
    for entry in json.loads(SPECTESTS_PATH.read_text(encoding="utf-8"))
)


@pytest.mark.parametrize(
    "entry", SPECTESTS_CASES, ids=[c["name"] for c in SPECTESTS_CASES]
)
def test_commonmark_spec(entry):
    """Test mdformat-gfm against the Commonmark spec.

    Test that:
    1. Markdown AST is the same before and after 1 pass of formatting
    2. Markdown after 1st pass and 2nd pass of formatting are equal
    """
    md_original = entry["md"]
    md_new = mdformat.text(md_original, extensions={"gfm"})
    md_2nd_pass = mdformat.text(md_new, extensions={"gfm"})
    assert is_md_equal(md_original, md_new, options={}, extensions={"gfm"})
    assert md_new == md_2nd_pass
