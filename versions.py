"""Tiny release helper: sort and pick version strings, including odd legacy tags."""
from packaging.version import Version, parse


def is_legacy(tag: str) -> bool:
    return isinstance(parse(tag), LegacyVersion)


def latest(tags: list[str]) -> str:
    """Newest proper release; legacy tags (like 'nightly') never win."""
    proper = [t for t in tags if not is_legacy(t)]
    return max(proper, key=Version)


def sort_tags(tags: list[str]) -> list[str]:
    """Proper versions ascending, then legacy tags alphabetically."""
    proper = sorted((t for t in tags if not is_legacy(t)), key=Version)
    return proper + sorted(t for t in tags if is_legacy(t))
