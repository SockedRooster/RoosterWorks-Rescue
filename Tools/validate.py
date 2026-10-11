#!/usr/bin/env python3
"""Offline checks for RoosterWorks Rescue v1.0.0, Agency v2.27 / Interstellar v1.3."""
from pathlib import Path
from hashlib import sha256
import re

ROOT = Path(__file__).resolve().parents[1]
GD = ROOT / "GameData"
EXPECTED = {"AgencyStationRescue": (8, 8), "InterstellarExpansionCampaign": (11, 4)}
for group, (contracts, craft_count) in EXPECTED.items():
    folder = GD / group
    assert folder.is_dir(), f"Missing folder: {folder}"
    craft = list((folder / "Craft").glob("*.craft"))
    assert len(craft) == craft_count, f"{group}: expected {craft_count} craft, got {len(craft)}"
    names = []
    for cfg in folder.glob("*.cfg"):
        content = cfg.read_text(encoding="utf-8-sig")
        names.extend(re.findall(
            r"^\s*CONTRACT_TYPE(?:\:NEEDS\[[^\]]*\])?\s*\{\s*name\s*=\s*([^\r\n]+)", content, re.M
        ))
        for path in re.findall(r"craftURL\s*=\s*(\S+)", content):
            assert (GD / path).is_file(), f"Missing referenced craft: {path}"
        assert content.count("{") == content.count("}"), f"Bad brace count in {cfg}"
    assert len(names) == contracts and len(names) == len(set(names)), f"{group}: invalid contract names/count"
    print(f"PASS {group}: {contracts} contracts and {craft_count} craft")
manifest = ROOT / "CHECKSUMS-SHA256.txt"
listed = {}
for line in manifest.read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    digest, relative_path = line.split("  ", 1)
    f = ROOT / relative_path
    assert f.is_file(), f"Missing manifest file: {relative_path}"
    assert sha256(f.read_bytes()).hexdigest() == digest, f"Hash mismatch: {relative_path}"
    listed[relative_path] = digest
actual = {f.relative_to(ROOT).as_posix() for f in GD.rglob("*") if f.is_file()}
assert actual == set(listed), f"Missing/excess GameData files: {actual.symmetric_difference(listed)}"
assert len(actual) == 20
print("PASS 20 GameData files, 19 contracts, 12 craft, SHA-256 hashes")
print("NOTE: Offline checks do not test KSP runtime/spawns.")
