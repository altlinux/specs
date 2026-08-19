%define _unpackaged_files_terminate_build 1
%define electron_version 42.4.0
%define electron_abi 146
%define arduino_cli_version 1.5.1

Name: arduino-ide
Version: 2.3.10
Release: alt1

Summary: IDE for Arduino boards and compatible microcontroller platforms.
Group: Education
License: AGPL-3.0
URL: https://arduino.cc
VCS: https://github.com/arduino/arduino-ide.git

Source0: %name-%version.tar
Source1: %name-%version-predownloaded.tar

Patch: %name-%version-%release.patch
Patch1: system-electron-skip-theia-ffmpeg.patch
Patch2: system-electron-drivelist-lazy-bindings.patch
Patch3: system-electron-disable-node-pty-native.patch
Patch4: system-native-node-modules.patch

ExcludeArch: %ix86

BuildRequires: /proc
BuildRequires: node
BuildRequires: yarn
BuildRequires: electron = %electron_version
BuildRequires: libsecret
BuildRequires: libxkbfile

Requires: electron = %electron_version
Requires: arduino-cli
Requires: arduino-fwuploader
Requires: arduino-language-server
Requires: clangd
Requires: clang-tools
Requires: ripgrep
Requires: node-parcel-watcher
Requires: node-keytar
Requires: node-native-keymap

%description
The Arduino Integrated Development Environment (IDE) is the official software
for programming Arduino microcontroller boards. Built on a Java-based
processing framework, it provides a streamlined, user-friendly interface for
both beginners and experienced developers.

%prep
%setup -a1
%autopatch -p1

%build
yarn --cwd arduino-ide-extension build
yarn rebuild:browser

mkdir -p $TMPDIR/electron-dist
find %_libdir/electron -mindepth 1 -maxdepth 1 ! -name chrome-sandbox \
  -exec cp -a -t $TMPDIR/electron-dist {} +

THEIA_SYSTEM_ELECTRON=1 \
  THEIA_SYSTEM_PARCEL_WATCHER=1 \
  THEIA_SYSTEM_NATIVE_NODE_MODULES=1 \
  yarn --cwd electron-app build
ARDUINO_CLI_VERSION=%arduino_cli_version \
  ELECTRON_VERSION=%electron_version \
  ELECTRON_DIST=$TMPDIR/electron-dist \
  yarn --cwd electron-app package

%install
mkdir -p %buildroot%_libdir/arduino-ide/resources
mkdir -p %buildroot%_bindir

appdir=$(find electron-app/dist -mindepth 3 -maxdepth 3 -type d \
  -path '*/resources/app' -print -quit)
test -n "$appdir"
rm -f "$appdir"/plugins/cortex-debug/extension/options-doc.py
rm -f "$appdir"/plugins/cortex-debug/extension/serial-port-build.sh
rm -rf "$appdir"/plugins/cortex-debug/extension/binary_modules

mv "$appdir" %buildroot%_libdir/arduino-ide/resources/app

cat << EOF > %buildroot%_bindir/arduino-ide
#!/bin/bash
exec %_bindir/electron %_libdir/arduino-ide/resources/app "\$@"
EOF
chmod +x %buildroot%_bindir/arduino-ide

install -m644 -D arduino-ide.desktop %buildroot%_desktopdir/arduino-ide.desktop
install -m644 -D %buildroot%_libdir/arduino-ide/resources/app/resources/icons/512x512.png %buildroot%_iconsdir/arduino-ide.png

%files
%doc README.md LICENSE.txt
%_bindir/arduino-ide
%_libdir/arduino-ide
%_desktopdir/arduino-ide.desktop
%_iconsdir/arduino-ide.png

%changelog
* Wed Aug 19 2026 Grant Makyan <karonus@altlinux.org> 2.3.10-alt1
- Update Arduino IDE to version 2.3.10.

* Wed Jul 08 2026 Grant Makyan <karonus@altlinux.org> 2.3.8-alt3
- Use system native Node.js modules.
- Exclude ix86 from build.
- Find packaged application resources by path.

* Sat Jun 27 2026 Grant Makyan <karonus@altlinux.org> 2.3.8-alt2
- Build with the system Electron package.
- Drop vendored Electron runtime and cached Electron headers.
- Use the system Arduino CLI package.

* Mon May 25 2026 Grant Makyan <karonus@altlinux.org> 2.3.8-alt1
- Add timeouts and allow degraded startup startup offline.
- Update Arduino IDE to version 2.3.8.

* Tue Feb 17 2026 Grant Makyan <karonus@altlinux.org> 2.3.7-alt2
- Revert 2.3.8 commit.

* Thu Jan 27 2026 Grant Makyan <karonus@altlinux.org> 2.3.7-alt1
- First build for ALT.
