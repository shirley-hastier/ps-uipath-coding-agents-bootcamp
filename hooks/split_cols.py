"""
MkDocs hook -- two-column split shorthand.

Syntax (each delimiter on its own line):

    [[[
    left column content
    |30|
    right column content
    ]]]

The number is the left-column width percentage.
Supported values: 30 (30/70), 50 (50/50), 70 (70/30).

Expands to:

    <div class="img-cols img-cols-{N}" markdown>
      <div markdown>
    left column content
      </div>
      <div markdown>
    right column content
      </div>
    </div>
"""
import re

_SPLIT_PATTERN = re.compile(
    r"\[\[\[\n(.*?)\n\|(\d+)\|\n(.*?)\n\]\]\]",
    re.DOTALL,
)


def on_page_markdown(markdown, **kwargs):
    def _expand(match):
        left_col = match.group(1).strip()
        ratio = match.group(2)
        right_col = match.group(3).strip()
        return (
            f'<div class="img-cols img-cols-{ratio}" markdown>\n'
            f"  <div markdown>\n{left_col}\n  </div>\n"
            f"  <div markdown>\n{right_col}\n  </div>\n"
            f"</div>"
        )

    return _SPLIT_PATTERN.sub(_expand, markdown)
