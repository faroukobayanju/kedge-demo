"""Tiny release helper: sort and pick version strings, including odd legacy tags."""
from packaging.version import Version, parse

# Compatibility shim for packaging >= 24.0 which removed LegacyVersion
try:
    from packaging.version import LegacyVersion
except ImportError:
    # packaging >= 24.0 removed LegacyVersion; use a dummy class that never matches
    class LegacyVersion:  # type: ignore
        pass


def is_legacy(tag: str) -> bool:
    try:
        return isinstance(parse(tag), LegacyVersion)
    except Exception:
        # In packaging >= 24.0, invalid versions raise InvalidVersion.
        # These are treated as legacy tags.
        return True


def latest(tags: list[str]) -> str:
    """Newest proper release; legacy tags (like 'nightly') never win."""
    proper = [t for t in tags if not is_legacy(t)]
    return max(proper, key=Version)


def sort_tags(tags: list[str]) -> list[str]:
    """Proper versions ascending, then legacy tags alphabetically."""
    proper = sorted((t for t in tags if not is_legacy(t)), key=Version)
    return proper + sorted(t for t in tags if is_legacy(t))
