#!/usr/bin/env python3
"""Generate one-tap Obtainium links for every app in patch-config.json and
write them into the README between the OBTAINIUM markers.

Usage: python scripts/generate_obtainium_links.py
App display names / package IDs live in obtainium-apps.json.
"""
import json
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/KScheid/Morphe-AutoBuilds"
REDIRECT = "https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/"
START, END = "<!-- OBTAINIUM-START -->", "<!-- OBTAINIUM-END -->"


def link(app: str, arch: str, info: dict) -> str:
    # Release titles look like "youtube universal v21.20.405".
    settings = {
        "filterReleaseTitlesByRegEx": f"^{re.escape(app)} {re.escape(arch)} v".replace("\\-", "-"),
        "autoApkFilterByArch": False,
        # Release tags look like "instagram-arm64-v8a-v447.0.0.55.81". Extract
        # just "447.0.0.55.81" so it matches the installed versionName and
        # Obtainium does not fall back to a "pseudo-version".
        "versionExtractionRegEx": r"^.*-v(\d.*)$",
        "matchGroupToUse": "$1",
        "versionDetection": True,
        "fallbackToOlderReleases": True,
        "includePrereleases": False,
    }
    cfg = {
        "id": info["id"],
        "url": REPO_URL,
        "author": "KScheid",
        "name": info["name"],
        "additionalSettings": json.dumps(settings),
    }
    return REDIRECT + urllib.parse.quote(json.dumps(cfg, separators=(",", ":")), safe="")


def main() -> None:
    apps = json.loads((ROOT / "obtainium-apps.json").read_text(encoding="utf-8"))
    arches = {a["app_name"]: a["arches"][0] for a in json.loads((ROOT / "arch-config.json").read_text())}
    rows = []
    for entry in json.loads((ROOT / "patch-config.json").read_text())["patch_list"]:
        app = entry["app_name"]
        if app not in apps:
            print(f"skip {app}: add it to obtainium-apps.json")
            continue
        info = apps[app]
        arch = arches.get(app, "universal")
        rows.append((info["name"], f"| {info['name']} | `{arch}` | [Add to Obtainium]({link(app, arch, info)}) |"))
    rows.sort(key=lambda r: r[0].lower())
    block = "\n".join([
        START,
        "## 📲 Add to Obtainium (one tap)",
        "",
        "Open this page on your phone with [Obtainium](https://github.com/ImranR98/Obtainium) installed, tap an app, and confirm. "
        "Each link adds this repo as the source with a filter so only that app's releases are tracked.",
        "",
        "| App | Build | Link |",
        "|---|---|---|",
        *[r[1] for r in rows],
        END,
    ])
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    if START in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, text, flags=re.S)
    else:
        marker = "---\n\n## ✨ Key Features"
        text = text.replace(marker, block + "\n\n" + marker, 1) if marker in text else text + "\n\n" + block + "\n"
    readme.write_text(text, encoding="utf-8")
    print(f"wrote {len(rows)} links")


if __name__ == "__main__":
    main()
