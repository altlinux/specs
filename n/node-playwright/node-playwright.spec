Name: node-playwright
Version: 1.63.0
Release: alt1
Summary: Browser automation driver for Playwright

License: Apache-2.0 AND MIT AND ISC AND BSD-2-Clause AND BSD-3-Clause
Group: Development/Other
Url: https://playwright.dev/
# Source-url: https://github.com/microsoft/playwright/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: build-driver.py
Source2: %name-development-%version.tar
Patch1: 0001-system-node-modules.patch
Patch2: 0002-system-chromium.patch
Patch3: 0003-system-libwebp.patch
Patch4: 0004-system-xdg-open.patch
Patch5: 0005-headless-ozone.patch
# System Chromium is unavailable on i586.
ExcludeArch: %ix86
BuildRequires(pre): rpm-build-nodejs
BuildRequires: /usr/bin/node /usr/bin/esbuild /usr/bin/python3
# Retain the stable system interpreter requirement from the Python package.
Requires: node
# This release hides system modules through broken alternatives and embeds an
# unexpanded module path. Keep the standard Node package usable (finding #172).
Conflicts: node-nightly <= 25.8.2-alt3
# These commands are invoked from JavaScript, outside the RPM shell scanner.
Requires: /usr/bin/chromium /usr/bin/cwebp /usr/bin/dwebp /usr/bin/xdg-open

%description
Playwright provides browser automation for Chromium, Firefox and WebKit.
This package contains the JavaScript driver running on system Node.js.

%prep
%setup -a2
%autopatch -p1

%build
export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
python3 %SOURCE1

%install
install -d %buildroot%nodejs_sitelib/playwright-core %buildroot%_bindir
cp -a packages/playwright-core/{lib,types,index.js,index.mjs,index.d.ts,cli.js,browsers.json,package.json} %buildroot%nodejs_sitelib/playwright-core/
ln -s ../lib/node_modules/playwright-core/cli.js %buildroot%_bindir/playwright-core
chmod 755 %buildroot%nodejs_sitelib/playwright-core/cli.js
install -d %buildroot%_docdir/%name/npm
cp -a npm-licenses/. %buildroot%_docdir/%name/npm/
rm -f %buildroot%nodejs_sitelib/playwright-core/lib/*.meta.json

%check
node packages/playwright-core/cli.js --version
node packages/playwright-core/cli.js --help

%files
%doc LICENSE NOTICE README.md
%_docdir/%name/npm/
%_bindir/playwright-core
%nodejs_sitelib/playwright-core/

%changelog
* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 1.63.0-alt1
- initial build for ALT Sisyphus.
- bundle audited npm utility sources with system esbuild.
- replace npm open and its platform helpers with system xdg-open.
- use headless Ozone and software ANGLE for headless Linux Chromium.
- build architecture-dependent packages; exclude i586.

