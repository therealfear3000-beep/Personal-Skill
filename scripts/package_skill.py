#!/usr/bin/env python3

from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PACKAGE_NAME = "hr-case-competition-strategist"
STAGE = DIST / PACKAGE_NAME
ZIP_PATH = DIST / f"{PACKAGE_NAME}.zip"

INCLUDE = [
    "SKILL.md",
    "README.md",
    "references",
    "scripts/score_options.py",
    "examples",
]

def copy_item(source: Path, destination: Path):
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

def main():
    if DIST.exists():
        shutil.rmtree(DIST)

    STAGE.mkdir(parents=True)

    for rel in INCLUDE:
        src = ROOT / rel
        if not src.exists():
            raise FileNotFoundError(f"Missing package input: {rel}")
        copy_item(src, STAGE / rel)

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in STAGE.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(DIST))

    print(f"Created: {ZIP_PATH}")
    print("Upload this ZIP to an Agent Skills-compatible client.")

if __name__ == "__main__":
    main()
