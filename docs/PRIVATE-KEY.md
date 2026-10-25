# Signing with your own private key

By default every APK is signed with the shared `keystore/public.jks` (password `public`).
Anyone can sign a file with that key, so Android would accept it as an update to your apps.
A private key fixes that. If no private key is configured, the builder keeps using the public one.

> **Switching keys means reinstalling.** Android refuses updates signed with a different key,
> so each already-installed app must be uninstalled once (app data is deleted) and reinstalled.

## 1. Create the key (once, on your own computer)

Needs Java (`sudo apt install default-jre-headless` on Debian/ChromeOS Linux).

```
keytool -genkeypair -v -keystore release.jks -alias release \
  -keyalg RSA -keysize 4096 -validity 36500
```

Pick a strong password. When asked for the key password, press Enter to reuse it.

**Back up `release.jks` and the password somewhere safe (password manager).**
If you lose them, you have to reinstall every app again. Never commit the file.

## 2. Turn it into text for GitHub

```
base64 -w0 release.jks
```

Copy the single long line it prints.

## 3. Add four repository secrets

GitHub repo > **Settings** > **Secrets and variables** > **Actions** > **New repository secret**:

| Secret name | Value |
|---|---|
| `KEYSTORE_BASE64` | the long base64 line from step 2 |
| `KEYSTORE_PASSWORD` | the keystore password |
| `KEY_ALIAS` | `release` |
| `KEY_PASSWORD` | the key password (same as the keystore password if you pressed Enter) |

## 4. Rebuild and reinstall

Run the builds again (Actions > Manual Patch and Update, or wait for the daily run).
The log shows `Signing with the private keystore` when it works.
Then uninstall and reinstall each app you use.

## Going back

Delete the `KEYSTORE_BASE64` secret and the builder returns to the public key.
(Apps signed with the private key would then need reinstalling again.)
