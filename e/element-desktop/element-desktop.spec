Name: element-desktop
Version: 1.12.30
Release: alt1

Summary: A glossy Matrix collaboration client

License: AGPL-3.0-only
Group: Networking/Instant messaging
Url: https://element.io/

# Source-url: https://github.com/element-hq/element-web/archive/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from
# etersoft-build-utils. ask me about description using: lav@etersoft.ru
Source1: %name-development-%version.tar
Source2: copy-runtime.py
Source3: element-desktop.desktop
Patch0: element-desktop-system-electron.patch

AutoReq:yes,nonodejs,nonodejs_native,nomono
AutoReq:nopython,nomingw32,nomingw64,noshebang

# node_modules vendored on x86_64 (native rollup bindings are arch-specific)
ExclusiveArch: x86_64


BuildRequires: /proc
BuildRequires: /usr/bin/node
BuildRequires: node-devel node-gyp node-typescript python3
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust libsqlcipher-devel pkgconfig
BuildRequires: electron

BuildRequires: element-web = %version

Provides: riot-desktop = %version-%release
Obsoletes: riot-desktop

%description
Element Desktop is a Matrix client for desktop platforms with Element Web
at its core. It supports encrypted secret storage and local message search.

%prep
%setup -a1
%patch0 -p1
# Use system tools without package-manager self-downloads.
python3 - <<'PY'
import json
p = 'package.json'
d = json.load(open(p))
d.pop('packageManager', None)
d.pop('devEngines', None)
json.dump(d, open(p, 'w'), indent=2)
PY
# Ensure all dependencies are hoisted to root node_modules
echo "shamefully-hoist=true" >> .npmrc
mkdir webapp
cp -aL /var/www/html/element-web/. webapp/
# Use the system TypeScript implementation throughout the build.
find node_modules -type l \( -name typescript -o -path '*/@typescript/old' \) \
    -exec ln -sfn /usr/lib/node_modules/typescript '{}' \;

%build
export PATH=$(pwd)/node_modules/.bin:$PATH
export NODE_PATH=$(pwd)/node_modules
# Build native addons against system libraries and Node-API, offline.
cd "$(readlink -f node_modules/@matrix-org/seshat)"
%rust_build --locked
cp target/release/libmatrix_seshat.so index.node
cd -
cd "$(readlink -f node_modules/pkcs11js)"
/usr/bin/node-gyp rebuild --nodedir=/usr
cd -

cd apps/desktop
/usr/bin/tsc
node scripts/copy-res.ts
asar pack ../../webapp webapp.asar
cd -
mkdir desktop-runtime
cp apps/desktop/package.json desktop-runtime/
cp -a apps/desktop/lib desktop-runtime/
mkdir desktop-runtime/build
cp apps/desktop/build/icon.png desktop-runtime/build/
python3 %SOURCE2 apps/desktop desktop-runtime

%check
# Load the production copies, including the locally compiled Node-API addons.
node -e "require('./desktop-runtime/node_modules/@matrix-org/seshat'); require('./desktop-runtime/node_modules/pkcs11js');"
node -e "require('node:module').createRequire(require('node:path').resolve('desktop-runtime/node_modules/@sentry/electron/package.json'))('@sentry/node');"
node --input-type=module -e "import { createRequire } from 'node:module'; import { resolve } from 'node:path'; const require = createRequire(resolve('desktop-runtime/node_modules/@sentry/electron/package.json')); await import(require.resolve('@sentry/node').replace('/build/cjs/', '/build/esm/'));"

test -f webapp/config.json && test ! -L webapp/config.json
test "$(cat webapp/version)" = "%version" || test "$(cat webapp/version)" = "v%version"

%install
mkdir -p %buildroot%_libdir/element-desktop/
cp -a desktop-runtime/* %buildroot%_libdir/element-desktop/
cp apps/desktop/webapp.asar %buildroot%_libdir/element-desktop/
install -Dm644 apps/desktop/build/icon.png %buildroot%_iconsdir/hicolor/512x512/apps/element-desktop.png
install -Dm644 %SOURCE3 %buildroot%_desktopdir/element-desktop.desktop
mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/element-desktop <<'EOF'
#!/bin/sh
exec /usr/bin/electron %_libdir/element-desktop "$@"
EOF
chmod 755 %buildroot%_bindir/element-desktop
ln -s element-desktop %buildroot%_bindir/riot-desktop

%files
%doc README.md
%_bindir/element-desktop
%_bindir/riot-desktop
%_libdir/element-desktop/
%_desktopdir/element-desktop.desktop
%_iconsdir/hicolor/*/apps/element-desktop.png

%changelog
* Wed Oct 07 2026 Vitaly Lipatov <lav@altlinux.ru> 1.12.30-alt1
- new version 1.12.30 (closes: #45590).
- Build from the shared upstream repository using the element-web RPM.
- Automate offline dependency preparation and use system Electron and TypeScript.
- SECURITY: update bundled Web (CVE-2023-28103, CVE-2023-28427, CVE-2023-30609, CVE-2023-37259).
- SECURITY: update bundled Web (CVE-2024-42347, CVE-2024-42369, CVE-2024-47771, CVE-2024-50336, CVE-2024-51749, CVE-2024-51750, CVE-2025-59161).

* Wed Mar 29 2023 Sergey V. Markov <markow@altlinux.org> 1.11.25-alt1
- new version 1.11.25 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.7-alt1
- new version 1.9.7 (with rpmrb script)

* Mon Oct 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1 (with rpmrb script)

* Mon Sep 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- new version 1.8.5 (with rpmrb script)

* Mon Sep 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- new version (1.8.4) with rpmgs script
- switch to electron13
- CVE-2021-40823, CVE-2021-40824

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.30-alt1
- new version 1.7.30 (with rpmrb script)

* Tue Mar 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.23-alt1
- new version 1.7.23 (with rpmrb script)

* Wed Mar 03 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.22-alt1
- new version 1.7.22 (with rpmrb script)

* Wed Feb 24 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.21-alt1
- new version 1.7.21 (with rpmrb script)

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.12-alt1
- new version 1.7.12 (with rpmrb script)

* Mon Oct 12 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- new version 1.7.9 (with rpmrb script)

* Tue Sep 15 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- new version 1.7.7 (with rpmrb script)

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- new version 1.7.5 (with rpmrb script)

* Sun Aug 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4 (with rpmrb script)

* Wed Aug 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script) (ALT bug 38786)

* Sat Jul 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.8-alt1
- new version 1.6.8 (with rpmrb script)

* Tue Jun 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.7-alt1
- new version 1.6.7 (with rpmrb script)

* Tue Jun 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt1
- new version 1.6.6 (with rpmrb script)

* Sat Jun 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.4-alt1
- new version 1.6.4 (with rpmrb script)

* Thu Jun 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt1
- new version 1.6.3 (with rpmrb script)

* Fri May 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- new version (1.6.2) with rpmgs script

* Fri Apr 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.15-alt1
- new version 1.5.15 (with rpmrb script)

* Wed Oct 16 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Wed Sep 04 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version 1.3.3 (with rpmrb script)

* Thu Jun 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Mar 10 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- build new version from sources

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- initial release for ALT Sisyphus
