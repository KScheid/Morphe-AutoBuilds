<div align="center">

# 🔧 Automated Android Build Pipeline

[![Daily Build](https://img.shields.io/github/actions/workflow/status/KScheid/Morphe-AutoBuilds/patch.yml?label=Daily%20Build&style=for-the-badge&color=2ea44f)](https://github.com/KScheid/Morphe-AutoBuilds/actions/workflows/patch.yml)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/KScheid/Morphe-AutoBuilds?style=for-the-badge&color=orange)](LICENSE)





<p align="center">
  <sub>Personal fork of <a href="https://github.com/RookieEnough/Morphe-AutoBuilds">RookieEnough/Morphe-AutoBuilds</a> — all credit for the original pipeline goes to its author. See <a href="#-changes-in-this-fork">changes in this fork</a>.</sub>
</p>

<p align="center">
  <strong>Config-driven CI builds for Android</strong><br>
  Multi-source • Multi-architecture • GitHub Actions Powered
</p>

<p align="center">
A sophisticated, automated pipeline that assembles installable Android applications for <strong>non-rooted devices</strong>. The system fetches build tooling, downloads base APKs from multiple sources, applies community build configurations, and produces architecture-specific outputs.
</p>

[![Report Bug](https://img.shields.io/badge/Report%20Bug-0A0A0A?style=flat&logo=github&logoColor=white)](https://github.com/KScheid/Morphe-AutoBuilds/issues)
[![Request Feature](https://img.shields.io/badge/Request%20Feature-0A0A0A?style=flat&logo=github&logoColor=white)](https://github.com/KScheid/Morphe-AutoBuilds/issues)


</div>

---

## ⚡ At a Glance

> **Note:** Builds are produced automatically every day at 06:00 UTC for **personal use** and published as releases on this repo, one release per app (installable with Obtainium). See the [Disclaimer](#️-disclaimer--legal) below.

### 📱 Supported Apps & Architectures

The full list of supported apps lives in [`patch-config.json`](patch-config.json) (31 apps at the time of writing). Each app can target `arm64-v8a`, `armeabi-v7a`, and/or `universal` builds, configured in [`arch-config.json`](arch-config.json).

<!-- OBTAINIUM-START -->
## 📲 Add to Obtainium (one tap)

Open this page on your phone with [Obtainium](https://github.com/ImranR98/Obtainium) installed, tap an app, and confirm. Each link adds this repo as the source with a filter so only that app's releases are tracked.

| App | Build | Link |
|---|---|---|
| AccuBattery | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.digibites.accubattery%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22AccuBattery%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eaccubattery%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Adobe Scan | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.adobe.scan.android%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Adobe%20Scan%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eadobe-scan%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Alto's Odyssey | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.noodlecake.altosodyssey%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Alto%27s%20Odyssey%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Ealtos-odyssey%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Amazon Shopping | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.amazon.mShop.android.shopping%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Amazon%20Shopping%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eamazon-shopping%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| AnyTracker | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.shervinkoushan.anyTracker%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22AnyTracker%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eanytracker%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| AutoZen | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.zenthek.autozen%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22AutoZen%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eautozen%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Beta Maniac | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22it.mirko.beta%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Beta%20Maniac%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Ebeta-maniac%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Brave | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.brave.browser%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Brave%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Ebrave%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| CapCut | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.lemon.lvoverseas%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22CapCut%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Ecapcut%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Discord | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.discord%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Discord%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Ediscord%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| File Tree Size | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.devone.filetreesize%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22File%20Tree%20Size%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Efile-tree-size%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Firefox | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22org.mozilla.firefox%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Firefox%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Efirefox%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Flexcil | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.flexcil.flexcilnote%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Flexcil%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eflexcil%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| FolderSync | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22dk.tacit.android.foldersync.lite%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22FolderSync%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Efoldersync%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Instagram | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.instagram.android%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Instagram%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Einstagram%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Medium | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.medium.reader%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Medium%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Emedium%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| MyScript Notes | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.myscript.nebo%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22MyScript%20Notes%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Emyscript-notes%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| nzb360 | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.kevinforeman.nzb360%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22nzb360%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Enzb360%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Plague Inc. | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.miniclip.plagueinc%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Plague%20Inc.%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eplague-inc%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Reddit | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.reddit.frontpage%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Reddit%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Ereddit%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Rocket Money | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.truebill%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Rocket%20Money%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Erocket-money%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Sleep as Android | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.urbandroid.sleep%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Sleep%20as%20Android%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Esleep-as-android%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Slopes | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.consumedbycode.slopes%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Slopes%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eslope%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| StandBy Mode | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22br.com.zetabit.ios_standby%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22StandBy%20Mode%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Estandby-mode%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Stellarium | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.noctuasoftware.stellarium_free%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Stellarium%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Estellarium%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| The Battle of Polytopia | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22air.com.midjiwan.polytopia%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22The%20Battle%20of%20Polytopia%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Epolytopia%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Today Weather | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22mobi.lockdown.weather%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Today%20Weather%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Etoday-weather%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Wallverse | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.wallverse.wallpapers%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Wallverse%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Ewallverse%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| Windy | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22com.windyty.android%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22Windy%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Ewindy%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| YouTube | `universal` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22app.morphe.android.youtube%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22YouTube%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eyoutube%20universal%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
| YouTube Music | `arm64-v8a` | [Add to Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22app.morphe.android.apps.youtube.music%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FKScheid%2FMorphe-AutoBuilds%22%2C%22author%22%3A%22KScheid%22%2C%22name%22%3A%22YouTube%20Music%22%2C%22additionalSettings%22%3A%22%7B%5C%22filterReleaseTitlesByRegEx%5C%22%3A%20%5C%22%5Eyoutube-music%20arm64-v8a%20v%5C%22%2C%20%5C%22autoApkFilterByArch%5C%22%3A%20false%2C%20%5C%22versionExtractionRegEx%5C%22%3A%20%5C%22%5E.%2A-v%28%5C%5C%5C%5Cd.%2A%29%24%5C%22%2C%20%5C%22matchGroupToUse%5C%22%3A%20%5C%22%241%5C%22%2C%20%5C%22versionDetection%5C%22%3A%20true%2C%20%5C%22fallbackToOlderReleases%5C%22%3A%20true%2C%20%5C%22includePrereleases%5C%22%3A%20false%7D%22%7D) |
<!-- OBTAINIUM-END -->

---

## ✨ Key Features

This repository utilizes a robust Python-based pipeline to ensure high reliability and optimization.

* **Fully Automated:** GitHub Actions workflow executes daily at 06:00 UTC, requiring zero manual intervention.
* **Architecture Optimization:** Builds specific `arm64-v8a`, `armeabi-v7a`, and `universal` APKs to reduce file size and improve performance on target devices.
* **Multi-Source Strategy:** Intelligent fetching from APKMirror, APKPure, and Uptodown ensures high success rates even if one source is down.
* **Granular Build Control:** Simple text-based configuration allows for precise inclusion or exclusion of specific build options.
* **Smart Failover:** The system automatically switches download sources if a fetch attempt fails.
* **Auto-Signing:** All APKs are signed with a consistent public keystore, making them ready to install immediately.
* **Clean Release Cycle:** Previous releases are replaced rather than archived, preventing clutter and making it easy for external managers (like Orion) to track updates.

---

## 🛠️ Repository Structure

```text
Morphe-AutoBuilds/
├── .github/workflows/      # GitHub Actions automation
│   ├── patch.yml           # Daily automated builds (06:00 UTC)
│   └── manual-patch.yml    # Manual trigger workflow
├── apps/                   # APK source configurations
│   ├── apkmirror/          # APKMirror definitions
│   ├── apkpure/            # APKPure definitions
│   └── uptodown/           # UptoDown definitions
├── patches/                # Build option rules
├── sources/                # Morphe tool source definitions
├── src/                    # Core Python build logic
├── arch-config.json        # Architecture build matrix
├── patch-config.json       # App build configuration
└── requirements.txt        # Project dependencies

```

---

## ⚙️ Configuration Guide

This builder is highly configurable. You can adjust the following files to customize the build output.

### 1. App Selection (`patch-config.json`)

Define which applications the pipeline should attempt to build.

```json
{
  "patch_list": [
    { "app_name": "youtube", "source": "morphe" },
    { "app_name": "youtube-music", "source": "morphe" },
    { "app_name": "X", "source": "crimera" }
  ]
}

```

### 2. Architecture Matrix (`arch-config.json`)

Specify which CPU architectures to target for each application.

```json
[
  {
    "app_name": "youtube",
    "source": "morphe",
    "arches": ["arm64-v8a", "armeabi-v7a", "universal"]
  },
  {
    "app_name": "youtube-music",
    "source": "morphe",
    "arches": ["arm64-v8a", "armeabi-v7a"]
  }
]

```

### 3. Source Definitions

Located in the `apps/` directory. Example for `apps/apkmirror/youtube.json`:

```json
{
  "org": "google-inc",
  "name": "youtube",
  "type": "APK",
  "arch": "universal",
  "dpi": "nodpi",
  "package": "com.google.android.youtube",
  "version": ""
}

```

### Play Store update protection

TikTok, Twitter and X builds set `android:versionCode` to `2147483647` before
alignment and signing, matching Morphe's **Disable Play Store updates** patch.
Package IDs, `versionName`, patch selection and the existing signing key stay
unchanged. This prevents ordinary higher-version Play Store update offers; it
is not a root-level detach and does not erase Play Store's cached listings.

Future protected builds can replace protected installs at the same version code.
Returning to a stock/lower-version-code build requires uninstalling first (with
potential data loss). Orion's current update detection compares `versionName`,
so the fixed code does not hide newer Orion versions. When first deploying this
change, force a full rebuild so the incremental release does not carry over old
APKs.

Requires Android SDK `zipalign` with 16 KB page-alignment support alongside
`apksigner`. Run the offline regression check with
`python tests/test_play_updates.py`.

### 4. Build Options

Located in `patches/`. Example for `patches/youtube-morphe.txt`. Use `+` to force include and `-` to exclude.

```text
# Essential options
+ microg-support
+ premium-heading
+ hide-infocard-suggestions

# Exclusions
- custom-branding
- amoled

```

---

## 🚀 Local Build Instructions

If you prefer to build the APKs on your own machine, follow these steps.

### Prerequisites

* Python 3.11 or higher
* Java Runtime Environment (JRE)
* `zip` utility
* `apksigner` (part of Android SDK Build-Tools)

### Installation & Execution

1. **Clone the repository:**
```bash
git clone https://github.com/KScheid/Morphe-AutoBuilds.git
cd Morphe-AutoBuilds

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt
pip install requests beautifulsoup4

```


3. **Run the build:**
You can build for a specific app and source.
```bash
export APP_NAME="youtube"
export SOURCE="morphe"
python -m src

```


4. **Target specific architecture (Optional):**
```bash
export APP_NAME="youtube"
export SOURCE="morphe"
export ARCH="arm64-v8a"  # Options: arm64-v8a, armeabi-v7a, universal
python -m src

```



---

## 🔄 GitHub Actions Workflows

### Daily Automated Build (`patch.yml`)

* **Schedule:** Runs daily at 06:00 UTC.
* **Function:** Iterates through all configured apps and architectures.
* **Output:** Refreshed build outputs for the configured apps.

### Manual Build (`manual-patch.yml`)

* **Trigger:** Manually via the GitHub Actions "Run workflow" button.
* **Capabilities:**
* Target specific apps.
* Target specific architectures.
* Force specific APK versions.
* Option to update the public release or just build artifacts.



---

## 🤝 Contributing

Contributions to improve the toolchain or add support for new apps are welcome.

1. **Fork** the repository.
2. **Create** a feature branch (`git checkout -b feature/new-app`).
3. **Test** your changes locally using the Python scripts.
4. **Commit** your changes (`git commit -m "Add support for new-app"`).
5. **Push** to the branch (`git push origin feature/new-app`).
6. **Open** a Pull Request.

---

## 🔀 Changes in this fork

This is a personal fork of [RookieEnough/Morphe-AutoBuilds](https://github.com/RookieEnough/Morphe-AutoBuilds), licensed under the same GPL-3.0. Main differences:

* **Different app list:** `patch-config.json` and `arch-config.json` hold the apps I use, with extra patch sources under `sources/`.
* **One-tap Obtainium links:** the table above is generated by `scripts/generate_obtainium_links.py` from `obtainium-apps.json`.
* **GitHub downloads by version:** `src/github.py` accepts a `{version}` tag template and an exact `asset` name (used for Brave).
* **ReVanced-style sources with `.mpp` patches:** the builder accepts `.mpp` bundles as a fallback.
* **Patch choices:** premium unlocks are enabled for Plague Inc., Adobe Scan and Brave Origin (`patches/*.txt`).

## 💙 Support the original author

The pipeline was created by RookieEnough. If you want to support their work:

<p align="center">
  <a href="https://ko-fi.com/rookie_z" target="_blank"><img src="https://storage.ko-fi.com/cdn/kofi6.png?v=6" height="30" style="height:30px; border-radius:8px; display:inline-block;" alt="Donate via Ko-fi" /></a>
  &nbsp;&nbsp;
  <a href="https://buymeachai.ezee.li/RookieZ" target="_blank"><img src="https://raw.githubusercontent.com/TakiShiwa/donate-with-upi/ffbb38749891aeb62e758a3692698e346e3df2da/Button/SVG/UPI-light-blue-01.svg" height="30" style="height:30px; border-radius:8px; display:inline-block;" alt="Donate via UPI" /></a>
  <br />
  <a href="https://paypal.me/RookieEnough" target="_blank"><img src="https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png" height="50" style="height:50px; border-radius:8px; display:inline-block; margin-top:8px;" alt="Donate via PayPal" /></a>
</p>

---

## ⚠️ Disclaimer & Legal

> **Important:** This repository is a build-automation toolkit. It contains **no APK files, no binaries, and no copyrighted media** of any kind. Nothing here is a downloadable app.

* **No binaries hosted:** All build outputs are produced locally or in CI and are never committed to this repository.
* **Educational purpose:** The workflows and scripts are provided for educational and research purposes, to demonstrate automated Android build pipelines.
* **Affiliation:** This project is **not** affiliated with the Morphe Team or with any app publisher whose software it can process.
* **Your responsibility:** You are responsible for complying with the licenses and terms of service of the apps and build sources you choose to use. Do not redistribute builds in ways that violate those terms.
* **Use at your own risk:** Builds are generated automatically from third-party sources and may contain experimental features.
* **GmsCore:** Morphe's MicroG-RE is required for these non-root apps to function correctly.

---

<div align="center">

**If you found this project helpful, please consider giving it a ⭐ Star.**  
<br>
**Made with 💜 by RookieZ**

