#!/usr/bin/env python3
"""
Post-render script for Quarto.
1. Quarto rewrites root-relative script paths (e.g. src="/chivatin/...") to
   document-relative paths (e.g. src="./chivatin/..."), which breaks analytics
   when the book is hosted under a subfolder (/en/conferencias_vol_i/).
   This script restores the root-relative path in all generated HTML files.
2. Quarto rewrites root-relative navigation links (e.g. href="/conferencias_vol_i/")
   to document-relative paths (e.g. href="./conferencias_vol_i/"), which breaks
   cross-book language switching. This script ensures the link to the Spanish version
   always points to /conferencias_vol_i/.
"""
import os
import re
from pathlib import Path

project_dir = Path(__file__).resolve().parent
output_dir_name = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_book")
output_dir = project_dir / output_dir_name

if output_dir.exists():
    for html_file in output_dir.glob("**/*.html"):
        content = html_file.read_text(encoding="utf-8")
        modified = False

        # 1. Restore root-relative analytics path
        if 'src="./chivatin/' in content:
            content = content.replace('src="./chivatin/', 'src="/chivatin/')
            modified = True

        # 2. Restore root-relative language switcher link to Spanish book (/conferencias_vol_i/)
        new_content = re.sub(
            r'(<a\b[^>]*\bhref=")[^"]*("(?:\s+[^>]*)?>[\s\S]*?Español[\s\S]*?</a>)',
            r'\1/conferencias_vol_i/\2',
            content
        )
        if new_content != content:
            content = new_content
            modified = True

        # Fallback replacement for any remaining doubled/mangled conferencias_vol_i paths
        new_content = re.sub(
            r'href="(?:\./|\.\./|https?://[^/]+/en/conferencias_vol_i/|/en/conferencias_vol_i/)conferencias_vol_i/?"',
            'href="/conferencias_vol_i/"',
            content
        )
        if new_content != content:
            content = new_content
            modified = True

        if modified:
            html_file.write_text(content, encoding="utf-8")
            print(f"Fixed paths in {html_file.name}")
