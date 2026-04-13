%define _unpackaged_files_terminate_build 1

Name: inav-configurator
Version: 9.0.1
Release: alt2

Summary: Configuration tool for the INAV flight control system
Group: Engineering
License: GPL-3.0
URL: https://inavflight.github.io
VCS: https://github.com/iNavFlight/inav-configurator.git

Source0: %name-%version.tar
Source1: %name-%version-predownloaded.tar
Source2: inav-configurator.desktop

Patch1: %name-%version-%release.patch
Patch2: add-electron-zip-dir.patch

ExclusiveArch: x86_64

BuildRequires: /proc
BuildRequires: node
BuildRequires: yarn
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
BuildRequires: libopus-devel
BuildRequires: at-spi2-atk
BuildRequires: libat-spi2-core

%description
INAV Configurator is a cross-platform configuration tool for the INAV flight
control system.

Various types of aircraft are supported by the tool and by INAV, e.g.
quadcopters, hexacopters, octocopters, and fixed-wing aircraft.

%prep
%setup -a1
%autopatch -p1

cp %SOURCE2 .

%build
yarn run package

%install
# Remove unused arches
rm -rf out/INAV\ Configurator-linux-x64/resources/app/.vite/build/node_natives/node_modules/@serialport/bindings-cpp/prebuilds/android-arm*
rm -rf out/INAV\ Configurator-linux-x64/resources/app/.vite/build/node_natives/node_modules/@serialport/bindings-cpp/prebuilds/darwin-x64+arm64
rm -rf out/INAV\ Configurator-linux-x64/resources/app/.vite/build/node_natives/node_modules/@serialport/bindings-cpp/prebuilds/win-32*
rm -rf out/INAV\ Configurator-linux-x64/resources/app/.vite/build/node_natives/node_modules/@serialport/bindings-cpp/prebuilds/linux-arm*
rm -rf out/INAV\ Configurator-linux-x64/resources/app/.vite/build/node_natives/node_modules/@serialport/bindings-cpp/prebuilds/linux-x64/@serialport+bindings-cpp.musl.node

mkdir -p %buildroot%_libdir/inav-configurator
cp -a out/INAV\ Configurator-linux-x64/* %buildroot%_libdir/inav-configurator

install -m644 -D inav-configurator.desktop %buildroot%_desktopdir/inav-configurator.desktop
install -m644 -D images/inav_icon_128.png %buildroot%_iconsdir/inav-configurator.png

mkdir -p %buildroot%_bindir

cat << EOF > %buildroot%_bindir/inav-configurator
#!/bin/bash
exec %_libdir/inav-configurator/inav-configurator
EOF

chmod +x %buildroot%_bindir/inav-configurator

%files
%doc README.md LICENSE
%_bindir/inav-configurator
%_libdir/inav-configurator
%_desktopdir/inav-configurator.desktop
%_iconsdir/inav-configurator.png

%changelog
* Mon Apr 13 2026 Grant Makyan <karonus@altlinux.org> 9.0.1-alt2
- Add ERSI map and remove Yandex Maps.

* Thu Feb 19 2026 Grant Makyan <karonus@altlinux.org> 9.0.1-alt1
- First build for ALT.
