#!/usr/bin/env python3
"""
Convert notebooks in notebooks_src/ to docs/notebooks/*.html and write docs/notebooks/manifest.json.

This runs on the GitHub Actions runner when you push.
"""
import os
import sys
import json
import subprocess
import nbformat

ROOT = os.getcwd()
SRC_DIR = os.path.join(ROOT, "notebooks_src")
OUT_DIR = os.path.join(ROOT, "docs", "notebooks")

os.makedirs(OUT_DIR, exist_ok=True)

def export_notebook(nb_path, out_dir):
    fname = os.path.splitext(os.path.basename(nb_path))[0] + ".html"
    # nbconvert: output file name should not contain path when used with --output-dir
    cmd = ["jupyter", "nbconvert", "--to", "html", "--output", fname, "--output-dir", out_dir, nb_path]
    print("Running:", " ".join(cmd))
    subprocess.check_call(cmd)

def snippet_description(nb_path):
    try:
        nb = nbformat.read(nb_path, as_version=4)
        for cell in nb.cells:
            if cell.cell_type == "markdown" and cell.source.strip():
                txt = cell.source.strip().splitlines()
                return (txt[0][:200] + ("…" if len(txt[0]) > 200 else ""))
    except Exception:
        pass
    return ""

def main():
    entries = []
    if not os.path.isdir(SRC_DIR):
        print("No notebooks_src/ directory found. Nothing to export.")
    else:
        for fname in sorted(os.listdir(SRC_DIR)):
            if not fname.lower().endswith(".ipynb"):
                continue
            src = os.path.join(SRC_DIR, fname)
            try:
                export_notebook(src, OUT_DIR)
                out_filename = os.path.splitext(fname)[0] + ".html"
                title = os.path.splitext(fname)[0]
                desc = snippet_description(src)
                entries.append({
                    "filename": out_filename,
                    "title": title,
                    "description": desc
                })
                print("Exported:", src)
            except subprocess.CalledProcessError as e:
                print("Failed to export:", src, e, file=sys.stderr)
    manifest_path = os.path.join(OUT_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    print("Wrote manifest:", manifest_path)

if __name__ == "__main__":
    main()
