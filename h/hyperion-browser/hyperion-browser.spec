# SPDX-License-Identifier: MIT
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: hyperion-browser
Version: 1.0.15
Release: alt1

Summary: Anti-detect Multibrowser with Clean Chromium Core
License: MIT
Group: Networking/WWW
Url: https://github.com/Linchevatel/hyperion-browser
ExclusiveArch: x86_64

Source0: %name-%version.tar
Patch0: hyperion-browser-1.0.15-alt-disable-inapp-update.patch
Patch1: hyperion-browser-1.0.15-alt-system-electron.patch

BuildRequires(pre): rpm-build-python3

Requires: libnss
Requires: libgtk+3
Requires: libalsa
Requires: libXScrnSaver
Requires: libxkbcommon
Requires: electron


%description
Hyperion is an anti-detect multi-profile browser client
with hardware fingerprint spoofing, clean Chromium engine, and proxy management.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build

%install
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_desktopdir

cp -r * %buildroot%_libdir/%name/

# Create wrapper launcher script
echo '#!/bin/sh' > %buildroot%_bindir/%name
echo 'exec %_libdir/%name/hyperion-app "$@"' >> %buildroot%_bindir/%name
chmod 0755 %buildroot%_bindir/%name

install -pm0644 hyperion-browser.desktop %buildroot%_desktopdir/%name.desktop

for s in 16 24 32 48 64 128 256; do
    mkdir -p %buildroot%_iconsdir/hicolor/${s}x${s}/apps
    if [ -f "assets/icons/${s}x${s}.png" ]; then
        install -pm0644 "assets/icons/${s}x${s}.png" %buildroot%_iconsdir/hicolor/${s}x${s}/apps/%name.png
    fi
done

%files
%_bindir/%name
%_libdir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Wed Sep 23 2026 Oleg Obidin <nofex@altlinux.org> 1.0.15-alt1
- Initial build for ALT Linux Sisyphus.
