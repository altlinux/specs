Name: cloudcli
Version: 1.37.8
Release: alt1

Summary: Web UI for coding agent command-line sessions

License: AGPL-3.0-or-later
Group: Networking/WWW
URL: https://github.com/siteboon/claudecodeui
# Source-url: https://github.com/siteboon/claudecodeui/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: README.ALT
Source3: cloudcli.in
Source4: cloudcli-check-binaries.py
Source5: cloudcli-desktop
Source6: ai.cloudcli.desktop.desktop
Patch: cloudcli-system-commands.patch

ExcludeArch: %ix86

AutoReq: yes,nonodejs,nomono,nopython,nopython3,nomingw32,nomingw64,nogir-js,nogir-python,nolua,noshell,noperl
AutoProv: no
Requires: /usr/bin/rg /usr/bin/git

BuildRequires: rpm-build-nodejs npm node-devel node-gyp gcc-c++ /proc esbuild = 0.28.2 rollup

%description
CloudCLI is a web interface for managing Claude Code, Codex, Cursor CLI
and OpenCode sessions.

%package desktop
Summary: Electron desktop UI for CloudCLI
Group: Development/Tools
Requires: cloudcli = %EVR
Requires: electron

%description desktop
CloudCLI desktop application. It uses the system Electron and runs the
CloudCLI local server with the system Node.js runtime.

%prep
%setup -a1
%patch -p1
# The predownload hook records the adjusted web/server dependency lockfile.
cp %SOURCE2 .
python3 %SOURCE4 node_modules
# Build-time native tools come exclusively from source-built ALT packages.
rm -rf node_modules/rollup
ln -s /usr/lib/node_modules/rollup node_modules/rollup

%build
# esbuild's JS loader rejects the literal /usr/bin/esbuild path.
ln -s %_bindir/esbuild esbuild-system
export ESBUILD_BINARY_PATH="$PWD/esbuild-system"
export npm_config_nodedir=/usr
export npm_config_build_from_source=true
for addon in node-pty bcrypt better-sqlite3; do
    (cd node_modules/$addon && node-gyp rebuild --nodedir=/usr)
done
npm run build

%check
node --test dist-server/server/modules/auth/tests/auth.service.test.js \
    dist-server/server/modules/cli/tests/cli.service.test.js
node -e "require('better-sqlite3')(':memory:').close(); require('bcrypt'); require('node-pty')"

%install
# Prune by the installed lock metadata without npm re-resolving the SDK's
# removed CLI dependency or trying to download anything in hasher.
python3 - <<'PYPRUNE'
import json
from pathlib import Path
import shutil
lock = json.loads(Path('node_modules/.package-lock.json').read_text())
for name, metadata in lock['packages'].items():
    if not (metadata.get('dev') or metadata.get('devOptional')):
        continue
    path = Path(name)
    if path.is_symlink():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)
PYPRUNE
rm -rf node_modules/@openai/codex
# Browser monitoring is already bundled by Vite. Its unused CLI pulls in
# desktop/compiler tooling, including precompiled WebAssembly assets.
rm -rf node_modules/{react-scan,react-doctor,playwright-core,yoga-layout} \
    node_modules/@astrojs/compiler
find node_modules -name '*.wasm' -delete
find node_modules -xtype l -delete
# Source-built addons are the only native files retained in the RPM.
for addon in node-pty bcrypt better-sqlite3; do
    find node_modules/$addon/build -type f ! -name '*.node' -delete
    rm -rf node_modules/$addon/{src,deps,prebuilds} \
        node_modules/$addon/build/Release/obj.target
done
rm -f node_modules/better-sqlite3/build/Release/test_extension.node
find node_modules -type f \( -name '*.o' -o -name '*.a' -o \
    -name '*.h' -o -name '*.hpp' -o -name '*.cc' -o -name '*.cpp' -o \
    -name '*.gyp' -o -name '*.gypi' \) -delete
python3 %SOURCE4 node_modules --allow-built
install -d %buildroot%_libdir/node_modules/%name
cp -a dist dist-server public server shared scripts node_modules package.json \
    %buildroot%_libdir/node_modules/%name/
# Runtime modules are data; the single public executable supplies Node deps.
find %buildroot%_libdir/node_modules/%name -type f -exec chmod 644 '{}' +
install -d %buildroot%_bindir
sed 's|@LIBDIR@|%_libdir|g' %SOURCE3 > %buildroot%_bindir/%name
chmod 755 %buildroot%_bindir/%name
install -d %buildroot%_libdir/node_modules/%name/electron
cp -a electron/{main.js,preload.cjs,cloud.js,desktopWindow.js,desktopNotifications.js,localServer.js,serverInstaller.js,tabs.js,viewHost.js,launcher} %buildroot%_libdir/node_modules/%name/electron/
install -d %buildroot%_bindir
sed 's|@LIBDIR@|%_libdir|g' %SOURCE5 > %buildroot%_bindir/cloudcli-desktop
chmod 755 %buildroot%_bindir/cloudcli-desktop
install -d %buildroot%_datadir/applications %buildroot%_datadir/icons/hicolor/512x512/apps
install -m 644 %SOURCE6 %buildroot%_datadir/applications/ai.cloudcli.desktop.desktop
install -m 644 public/logo-512.png %buildroot%_datadir/icons/hicolor/512x512/apps/ai.cloudcli.desktop.png

%files
%doc README.md README.ALT LICENSE NOTICE
%_bindir/%name
%dir %_libdir/node_modules
%exclude %_libdir/node_modules/%name/electron
%_libdir/node_modules/%name/

%files desktop
%_bindir/cloudcli-desktop
%_datadir/applications/ai.cloudcli.desktop.desktop
%_datadir/icons/hicolor/512x512/apps/ai.cloudcli.desktop.png
%_libdir/node_modules/%name/electron/

%changelog
* Thu Nov 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.37.8-alt1
- add the cloudcli-desktop Electron subpackage using system Electron.
- initial build for Sisyphus.
- exclude ix86: rollup is unavailable on this architecture.
