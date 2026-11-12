#!/usr/bin/env python3
"""
Post-render script for Quarto.
Quarto rewrites root-relative script paths (e.g. src="/chivatin/...") to
document-relative paths (e.g. src="./chivatin/..."), which breaks analytics
when the book is hosted under a subfolder (/conferencias_vol_i/).
This script restores the root-relative path in all generated HTML files.
"""
import os
from pathlib import Path

project_dir = Path(__file__).resolve().parent
output_dir_name = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_book")
output_dir = project_dir / output_dir_name

if output_dir.exists():
    for html_file in output_dir.glob("**/*.html"):
        content = html_file.read_text(encoding="utf-8")
        if 'src="./chivatin/' in content:
            updated = content.replace('src="./chivatin/', 'src="/chivatin/')
            html_file.write_text(updated, encoding="utf-8")
            print(f"Fixed analytics path in {html_file.name}")
