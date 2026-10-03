"""Structural checks for rubric.yaml.

Usage: python rubric/validate.py [path/to/rubric.yaml]
Exits non-zero and lists every problem found.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import yaml

DEFAULT_PATH = Path(__file__).with_name("rubric.yaml")
SOURCE_REF = re.compile(r"^(S[0-5](:Q\d+(-\d+)?)?|added)$")
NUMERIC_KEYS = {"metric", "direction", "thresholds"}


def _close(x: float, target: float = 1.0) -> bool:
    return math.isclose(x, target, abs_tol=1e-9)


def _check_sources(where: str, refs: list, errors: list[str]) -> None:
    if not refs:
        errors.append(f"{where}: no sources")
    for ref in refs or []:
        if not SOURCE_REF.match(str(ref)):
            errors.append(f"{where}: bad source ref {ref!r}")


def _check_criterion(c: dict, errors: list[str]) -> None:
    cid = c.get("id", "?")
    ctype = c.get("type")
    _check_sources(cid, c.get("sources"), errors)

    if ctype == "numeric":
        missing = NUMERIC_KEYS - c.keys()
        if missing:
            errors.append(f"{cid}: numeric criterion missing {sorted(missing)}")
            return
        good, red = c["thresholds"]["good"], c["thresholds"]["red"]
        direction = c["direction"]
        if direction == "higher_better" and not good > red:
            errors.append(f"{cid}: higher_better requires good > red ({good} vs {red})")
        elif direction == "lower_better" and not good < red:
            errors.append(f"{cid}: lower_better requires good < red ({good} vs {red})")
        elif direction not in ("higher_better", "lower_better"):
            errors.append(f"{cid}: unknown direction {direction!r}")
    elif ctype == "categorical":
        levels = c.get("levels") or {}
        if not levels:
            errors.append(f"{cid}: categorical criterion has no levels")
        if any(not 0.0 <= v <= 1.0 for v in levels.values()):
            errors.append(f"{cid}: level scores must be in [0, 1]")
        if levels and max(levels.values()) != 1.0:
            errors.append(f"{cid}: best level should score 1.0")
    else:
        errors.append(f"{cid}: unknown type {ctype!r}")


def validate(rubric: dict) -> list[str]:
    errors: list[str] = []
    dims = rubric.get("dimensions") or []

    dim_weight = sum(d["weight"] for d in dims)
    if not _close(dim_weight):
        errors.append(f"dimension weights sum to {dim_weight}, expected 1")

    seen: set[str] = set()
    for d in dims:
        crits = d.get("criteria") or []
        crit_weight = sum(c["weight"] for c in crits)
        if not _close(crit_weight):
            errors.append(f"{d['id']}: criterion weights sum to {crit_weight}, expected 1")
        for c in crits:
            if c["id"] in seen:
                errors.append(f"duplicate criterion id {c['id']}")
            seen.add(c["id"])
            _check_criterion(c, errors)

    for g in rubric.get("gates") or []:
        if g["id"] in seen:
            errors.append(f"duplicate id {g['id']}")
        seen.add(g["id"])
        _check_sources(g["id"], g.get("sources"), errors)

    return errors


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else DEFAULT_PATH
    errors = validate(yaml.safe_load(path.read_text()))
    for e in errors:
        print(f"ERROR: {e}")
    if not errors:
        print(f"OK: {path}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
