# SPDX-License-Identifier: MIT
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# Upstream engine has no debug sections; exclude only its prebuilt files.
%add_debuginfo_skiplist %_libdir/hyperion-browser/bundle/chrome/*
%define engine_sha256 f021005c30b17502460d886e0f61aed4ae8ebd5af2d5c7d431ce1e1af423bc13

Name: hyperion-browser
Version: 1.0.23
Release: alt1
Summary: Anti-detect Multibrowser with bundled patched Chromium
License: MIT
Group: Networking/WWW
Url: https://github.com/Linchevatel/hyperion-browser
ExclusiveArch: x86_64

Source0: %name-%version.tar
# Store this exact release artifact as a separate gear source (copy rule).
Source1: https://github.com/Linchevatel/hyperion-browser/releases/download/v%version/hyperion-desktop-%version.x86_64.rpm
Patch0: disable-inapp-update.patch
Patch1: system-electron.patch
Patch2: bundled-engine-only.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: rpm cpio coreutils
# Install the engine's shared libraries for strict ELF verification.
BuildRequires: libnss libnspr libgio libatk at-spi2-atk libat-spi2-core
BuildRequires: libdbus libcups libxcb libxkbcommon libalsa libgbm
BuildRequires: libX11 libXext libcairo libpango libudev1
BuildRequires: libXcomposite libXdamage libXfixes libXrandr
Requires: libnss
Requires: libgtk+3
Requires: libalsa
Requires: libXScrnSaver
Requires: libxkbcommon
Requires: electron

%description
Hyperion is an anti-detect multi-profile browser client with hardware
fingerprint spoofing, a bundled patched Chromium engine and proxy management.
The Chromium engine is repacked from the official upstream Linux RPM.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

echo '%engine_sha256  %SOURCE1' | sha256sum -c -
mkdir engine-source
rpm2cpio %SOURCE1 > engine-source/payload.cpio
(cd engine-source && cpio -idm --no-absolute-filenames < payload.cpio)
rm engine-source/payload.cpio
test -x 'engine-source/opt/Hyperion Browser/resources/chrome/chrome'

%build

%install
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_desktopdir

# Keep the extracted upstream application/Electron out of the package.
for entry in *; do
    case "$entry" in engine-source) continue ;; esac
    cp -a "$entry" %buildroot%_libdir/%name/
done

# Replace the empty source-tree bundle with the complete upstream engine.
rm -rf %buildroot%_libdir/%name/bundle/chrome
mkdir -p %buildroot%_libdir/%name/bundle/chrome
cp -a 'engine-source/opt/Hyperion Browser/resources/chrome/.' \
    %buildroot%_libdir/%name/bundle/chrome/
test -x %buildroot%_libdir/%name/bundle/chrome/chrome
# Do not introduce a setuid executable implicitly when repacking binaries.
find %buildroot%_libdir/%name/bundle/chrome -type f -perm /6000 \
    -exec chmod u-s,g-s '{}' +

printf '#!/bin/sh\nexec %_libdir/%name/hyperion-app "$@"\n' \
    > %buildroot%_bindir/%name
chmod 0755 %buildroot%_bindir/%name
install -pm0644 hyperion-browser.desktop %buildroot%_desktopdir/%name.desktop

for s in 16 24 32 48 64 128 256; do
    if [ -f "assets/icons/${s}x${s}.png" ]; then
        install -Dm0644 "assets/icons/${s}x${s}.png" \
            %buildroot%_iconsdir/hicolor/${s}x${s}/apps/%name.png
    fi
done

%files
%_bindir/%name
%_libdir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Mon Oct 05 2026 Oleg Obidin <nofex@altlinux.org> 1.0.23-alt1
- New version 1.0.23 (Chromium core 154.0.8037.97).
- Fixes (ALT bug: 60786, 60785, 60784).

* Wed Sep 23 2026 Oleg Obidin <nofex@altlinux.org> 1.0.15-alt1
- Initial build for ALT Linux Sisyphus.
