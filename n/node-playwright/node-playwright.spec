# The checks need neither the network nor a browser.
%def_with check

Name: node-playwright
Version: 1.65.0
Release: alt1
Summary: Browser automation driver for Playwright

License: Apache-2.0 AND MIT AND ISC AND BSD-2-Clause AND BSD-3-Clause
Group: Development/Other
Url: https://playwright.dev/
# The source package is arch-dependent only for the browser packages,
# which are not built on i586: chromium and firefox are missing there.
# The driver itself is noarch and available on every architecture.
# Source-url: https://github.com/microsoft/playwright/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: build-driver.py
Source2: %name-development-%version.tar
Patch2: 0002-system-browsers.patch
Patch3: 0003-system-libwebp.patch
Patch4: 0004-system-xdg-open.patch
Patch5: 0005-headless-ozone.patch
BuildRequires(pre): rpm-build-nodejs
BuildRequires: /usr/bin/node /usr/bin/esbuild /usr/bin/python3
Requires: %name-core = %EVR

%description
Playwright provides browser automation for Chromium and Firefox.
This package installs node-playwright-core, the JavaScript driver
running on system Node.js. The browsers are not required: install
node-playwright-chromium, node-playwright-firefox or both, and
node-playwright-ffmpeg for video recording.

%package core
Summary: Browser automation driver for Playwright running on system Node.js
Group: Development/Other
BuildArch: noarch
# The driver runs on the system Node.js, the node package.
Requires: node
# node-nightly up to 25.8.2-alt3 breaks the node package next to it: its
# alternatives hide the system Node.js modules, and it embeds an
# unexpanded module path.
Conflicts: node-nightly <= 25.8.2-alt3
# These commands are invoked from JavaScript, outside the RPM shell scanner.
# The browsers and ffmpeg (video recording) are not required: the user
# installs the ones they use, and a launch without them names the package.
Requires: /usr/bin/cwebp /usr/bin/dwebp /usr/bin/xdg-open

%description core
Playwright provides browser automation for Chromium, Firefox and WebKit.
This package contains the JavaScript driver running on system Node.js.
It runs the system browsers, which it does not require: install
node-playwright-chromium, node-playwright-firefox or both. Firefox
must be the firefox package: the older firefox-esr does not support
the WebDriver BiDi protocol that Playwright uses. WebKit is not
available. Video recording needs node-playwright-ffmpeg.
"playwright-core mcp" runs the Playwright MCP server, and
"playwright-core cli" runs the Playwright command-line client.

# The minimal browser and ffmpeg versions are the ones this driver was
# checked with.
%ifnarch %ix86
%package chromium
Summary: Chromium browser for Playwright
Group: Development/Other
Requires: %name = %EVR
Requires: chromium >= 156

%description chromium
This package installs the system Chromium for Playwright.

%package firefox
Summary: Firefox browser for Playwright
Group: Development/Other
Requires: %name = %EVR
# The older firefox-esr lacks the WebDriver BiDi support Playwright uses.
Requires: firefox >= 160

%description firefox
This package installs the system Firefox for Playwright.

%package ffmpeg
Summary: FFmpeg for Playwright video recording
Group: Development/Other
Requires: %name = %EVR
Requires: ffmpeg >= 2:9.0

%description ffmpeg
This package installs the system FFmpeg for Playwright video recording.
%endif

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
rm -f %buildroot%nodejs_sitelib/playwright-core/lib/*.meta.json

%check
node packages/playwright-core/cli.js --version
node packages/playwright-core/cli.js --help
node packages/playwright-core/cli.js cli --help
# The MCP server starts and lists its browser tools without a browser.
# It exits when stdin closes, so keep stdin open until the reply arrives.
mkfifo mcp.in
timeout 60 node packages/playwright-core/cli.js mcp < mcp.in > mcp.out &
mcp_pid=$!
exec 3> mcp.in
printf '%%s\n' >&3 \
	'{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"check","version":"0"}}}' \
	'{"jsonrpc":"2.0","method":"notifications/initialized"}' \
	'{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
for i in $(seq 60); do
	grep -q '"browser_navigate"' mcp.out && break
	sleep 1
done
exec 3>&-
wait $mcp_pid || :
grep -q '"browser_navigate"' mcp.out
# Browser downloads are disabled.
! node packages/playwright-core/cli.js install chromium > install.out 2>&1
grep -q 'Browser downloads are disabled in ALT Linux' install.out

%files

%files core
%doc LICENSE NOTICE README.md npm-licenses
%_bindir/playwright-core
%nodejs_sitelib/playwright-core/

%ifnarch %ix86
%files chromium

%files firefox

%files ffmpeg
%endif

%changelog
* Fri Nov 13 2026 Andrey Kuzma <kuzmaav@altlinux.org> 1.65.0-alt1
- Updated to 1.65.0.
- Moved the driver to the new noarch node-playwright-core package,
  available on i586 too; node-playwright now only requires it.
- Dropped the chromium requirement. Added node-playwright-chromium,
  node-playwright-firefox and node-playwright-ffmpeg (video recording)
  to install the browsers and ffmpeg (not on i586).
- Added Firefox support over WebDriver BiDi (firefox, not firefox-esr).
- Added the "playwright-core mcp" MCP server and the
  "playwright-core cli" command-line client.

* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 1.63.0-alt1
- initial build for ALT Sisyphus.
- bundle audited npm utility sources with system esbuild.
- replace npm open and its platform helpers with system xdg-open.
- use headless Ozone and software ANGLE for headless Linux Chromium.
- build architecture-dependent packages; exclude i586.

