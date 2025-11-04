"""
Language guardrails for AI-generated content.

Provides a simple mechanism for detecting banned terms in AI output.
If any banned term is present, the content should be discarded and the
report marked as errored.
"""

import re


BANNED_TERMS = [
    r"cura",
    r"detox",
    r"milagroso",
    r"garantid[oa]",
    r"emagreça rápido",
    r"milagre",
    r"corpo inflamado",
    r"anti[ -]?inflamat[óo]rio",
]


def contains_banned_language(text: str) -> bool:
    """Check if a string contains any banned terms.

    Parameters
    ----------
    text : str
        Text to scan for banned terms.

    Returns
    -------
    bool
        True if any banned term is found, otherwise False.
    """
    lowered = text.lower()
    for pattern in BANNED_TERMS:
        if re.search(pattern, lowered):
            return True
    return False