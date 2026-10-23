#!/usr/bin/env python3
"""Publish built APKs to this repository's GitHub Releases.

Two kinds of release are maintained:

1. ``latest`` (pre-release, never marked "Latest")
   Holds every current APK plus ``manifest.json``. The incremental update
   check (scripts/check_app_updates.py) reads this to decide what to rebuild.

2. One release per app build, tagged ``<app>-<arch>-v<version>``
   Holds just that APK. These are what Obtainium tracks: each app gets a
   title prefix ``<app> <arch> v`` that Obtainium can filter on, and the
   tag carries the version. Only the newest ``--keep`` per app/arch are kept.

Requires the ``gh`` CLI with GH_TOKEN / GITHUB_TOKEN set (contents: write).
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

STATE_TAG = "latest"
APK_RE = re.compile(
    r"^(?P<app>.+?)-(?P<arch>arm64-v8a|armeabi-v7a|universal)-(?P<src>.+)-v(?P<ver>\d.*)\.apk$"
)


def gh(*args, check=True):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        print(f"gh {' '.join(args)} failed:\n{r.stderr}", file=sys.stderr)
        raise SystemExit(1)
    return r


def safe(s: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^A-Za-z0-9._-]+", "-", s)).strip("-.")


def release_exists(tag: str) -> bool:
    return gh("release", "view", tag, check=False).returncode == 0


def assets(tag: str) -> list[str]:
    r = gh("release", "view", tag, "--json", "assets", check=False)
    if r.returncode != 0:
        return []
    return [a["name"] for a in json.loads(r.stdout).get("assets", [])]


def all_release_tags() -> list[str]:
    r = gh("release", "list", "--limit", "1000", "--json", "tagName,createdAt", check=False)
    if r.returncode != 0:
        return []
    rows = sorted(json.loads(r.stdout), key=lambda x: x["createdAt"], reverse=True)
    return [x["tagName"] for x in rows]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apks-dir", required=True)
    ap.add_argument("--keep", type=int, default=2, help="per-app releases to keep")
    a = ap.parse_args()

    d = Path(a.apks_dir)
    manifest = d / "manifest.json"

    # GitHub rewrites spaces etc. in asset names; normalise first so names
    # stay stable, and keep manifest.json pointing at the new names.
    renames = {}
    for apk in d.glob("*.apk"):
        clean = safe(apk.stem) + ".apk"
        if clean != apk.name:
            apk.rename(d / clean)
            renames[apk.name] = clean
    if renames and manifest.exists():
        text = manifest.read_text(encoding="utf-8")
        for old_name, clean in renames.items():
            text = text.replace(json.dumps(old_name), json.dumps(clean))
        manifest.write_text(text, encoding="utf-8")
    apks = sorted(d.glob("*.apk"))

    if not release_exists(STATE_TAG):
        gh("release", "create", STATE_TAG, "--prerelease", "--latest=false",
           "--title", "Build state (all current APKs)",
           "--notes", "Internal state for the auto-build. Point Obtainium at the per-app releases instead.")

    tags = all_release_tags()
    for apk in apks:
        m = APK_RE.match(apk.name)
        if not m:
            print(f"skip (unrecognised name): {apk.name}")
            continue
        app, arch, src, ver = m["app"], m["arch"], m["src"], m["ver"]
        prefix = f"{app}-{arch}-"

        # 1) state release: upload, then drop superseded APKs for this app/arch
        gh("release", "upload", STATE_TAG, str(apk), "--clobber")
        for name in assets(STATE_TAG):
            if name.startswith(prefix) and name.endswith(".apk") and name != apk.name \
                    and APK_RE.match(name) and APK_RE.match(name)["app"] == app:
                gh("release", "delete-asset", STATE_TAG, name, "-y", check=False)

        # 2) per-app release for Obtainium
        tag = safe(f"{app}-{arch}-v{ver}")
        title = f"{app} {arch} v{ver}"
        if release_exists(tag):
            gh("release", "upload", tag, str(apk), "--clobber")
        else:
            gh("release", "create", tag, str(apk), "--latest=false",
               "--title", title, "--notes", f"{app} {ver} ({arch}), patched with {src}.")
            tags.insert(0, tag)
        print(f"published {apk.name} -> {tag}")

        # prune older per-app releases
        mine = [t for t in tags if t.startswith(safe(f"{app}-{arch}-v"))]
        for old in mine[a.keep:]:
            gh("release", "delete", old, "-y", "--cleanup-tag", check=False)
            tags.remove(old)
            print(f"pruned {old}")

    if manifest.exists():
        gh("release", "upload", STATE_TAG, str(manifest), "--clobber")
        print("uploaded manifest.json")


if __name__ == "__main__":
    main()
