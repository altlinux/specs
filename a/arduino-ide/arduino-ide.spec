%define _unpackaged_files_terminate_build 1

Name: arduino-ide
Version: 2.3.8
Release: alt1

Summary: IDE for Arduino boards and compatible microcontroller platforms.
Group: Education
License: AGPL-3.0
URL: https://arduino.cc
VCS: https://github.com/arduino/arduino-ide.git

Source0: %name-%version.tar
Source1: %name-%version-predownloaded.tar

Patch: %name-%version-%release.patch

ExclusiveArch: x86_64

BuildRequires: /proc
BuildRequires: node
BuildRequires: npm
BuildRequires: yarn
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: python3
BuildRequires: python3-module-setuptools
BuildRequires: libX11-devel
BuildRequires: libxkbfile-devel
BuildRequires: libsecret-devel
BuildRequires: libnss
BuildRequires: libnspr
BuildRequires: libdbus
BuildRequires: libatk
BuildRequires: libcups
BuildRequires: libdrm
BuildRequires: libgtk+3
BuildRequires: libpango
BuildRequires: libcairo
BuildRequires: libXcomposite
BuildRequires: libXdamage
BuildRequires: libXext
BuildRequires: libXfixes
BuildRequires: libXrandr
BuildRequires: libgbm
BuildRequires: libxkbcommon
BuildRequires: libalsa
BuildRequires: at-spi2-atk
BuildRequires: libat-spi2-core
BuildRequires: patchelf

%description
The Arduino Integrated Development Environment (IDE) is the official software
for programming Arduino microcontroller boards. Built on a Java-based
processing framework, it provides a streamlined, user-friendly interface for
both beginners and experienced developers.

%prep
%setup -a1
%autopatch -p1

mv -f ./.cache/.electron-gyp ~
mv -f ./.cache/theia-cli $TMPDIR/theia-cli

%build
yarn --cwd arduino-ide-extension build
yarn --cwd electron-app rebuild
yarn --cwd electron-app build
yarn --cwd electron-app package

%install
mkdir -p %buildroot%_libdir/arduino-ide
mkdir -p %buildroot%_bindir

# Uses not exists libnode for no reason.
rm electron-app/dist/linux-unpacked/resources/app/plugins/cortex-debug/extension/binary_modules/v12.14.1/linux/x64/node_modules/@serialport/bindings/build/Release/obj.target/bindings.node
rm electron-app/dist/linux-unpacked/resources/app/plugins/cortex-debug/extension/binary_modules/v12.14.1/linux/x64/node_modules/@serialport/bindings/build/Release/bindings.node

mv electron-app/dist/linux-unpacked/* %buildroot%_libdir/arduino-ide

cat << EOF > %buildroot%_bindir/arduino-ide
#!/bin/bash
exec %_libdir/arduino-ide/arduino-ide
EOF
chmod +x %buildroot%_bindir/arduino-ide

%ifarch x86_64
rm -rf %buildroot%_libdir/arduino-ide/resources/app/plugins/cortex-debug/extension/binary_modules/v12.14.1/linux/arm
rm -rf %buildroot%_libdir/arduino-ide/resources/app/plugins/cortex-debug/extension/binary_modules/v12.14.1/linux/arm64
%else
rm -rf %buildroot%_libdir/arduino-ide/resources/app/plugins/cortex-debug/extension/binary_modules/v12.14.1/linux/x64
%endif

install -m644 -D arduino-ide.desktop %buildroot%_desktopdir/arduino-ide.desktop
install -m644 -D %buildroot%_libdir/arduino-ide/resources/app/resources/icons/512x512.png %buildroot%_iconsdir/arduino-ide.png

%files
%doc README.md LICENSE.txt
%_bindir/arduino-ide
%_libdir/arduino-ide
%_desktopdir/arduino-ide.desktop
%_iconsdir/arduino-ide.png

%changelog
* Mon May 25 2026 Grant Makyan <karonus@altlinux.org> 2.3.8-alt1
- Add timeouts and allow degraded startup startup offline.
- Update Arduino IDE to version 2.3.8.

* Tue Feb 17 2026 Grant Makyan <karonus@altlinux.org> 2.3.7-alt2
- Revert 2.3.8 commit.

* Thu Jan 27 2026 Grant Makyan <karonus@altlinux.org> 2.3.7-alt1
- First build for ALT.
