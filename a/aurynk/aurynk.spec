%define _unpackaged_files_terminate_build 1

Name: aurynk
Version: 1.1.0
Release: alt2

Summary: Wirelessly connect, manage and control your Android devices from Linux
License: GPL-3.0-or-later
Group: Networking/Remote access
URL: https://github.com/IshuSinghSE/aurynk

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3

BuildRequires: meson
BuildRequires: cmake
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: pkgconfig(gio-2.0)

Requires: /usr/bin/adb
Requires: /usr/bin/scrcpy
Requires: python3-module-qrcode
Requires: python3-module-zeroconf

%filter_from_requires /typelib(gi)/d

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Aurynk is a modern Android device manager for Linux that allows you to
wirelessly pair and manage your Android devices using ADB (Android Debug Bridge).

Features:

* Wireless pairing via QR code
* Device information and specifications
* Screenshot capture
* Modern GTK4/libadwaita interface
* Easy device management

%prep
%setup
%patch -p1
sed -i "s|Categories=.*|Categories=Network;RemoteAccess;|" data/io.github.IshuSinghSE.aurynk.desktop.in
sed -i "s|data/icons/io.github.IshuSinghSE.aurynk.png|%_iconsdir/hicolor/128x128/apps/io.github.IshuSinghSE.aurynk.png|" README.md
sed -i "s|data/screenshots/|screenshots/|g" README.md

%build
%meson
%meson_build

%install
%meson_install

# # following debian/install for extra stuff
# Desktop entry
mkdir -p %buildroot%_desktopdir
cp -v data/io.github.IshuSinghSE.aurynk.desktop.in %buildroot%_desktopdir/io.github.IshuSinghSE.aurynk.desktop

# Metainfo
mkdir -p %buildroot%_datadir/metainfo/
cp -v data/io.github.IshuSinghSE.aurynk.metainfo.xml %buildroot%_datadir/metainfo/

# App and tray icons (all sizes)
mkdir -p %buildroot%_iconsdir/hicolor

for size in 128x128 16x16 24x24 256x256 32x32 48x48 512x512 64x64; do
  mkdir -p %buildroot%_iconsdir/hicolor/$size/apps
  cp -v data/icons/hicolor/$size/apps/io.github.IshuSinghSE.aurynk.png %buildroot%_iconsdir/hicolor/$size/apps/
done

mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
cp -v data/icons/hicolor/scalable/apps/io.github.IshuSinghSE.aurynk.svg %buildroot%_iconsdir/hicolor/scalable/apps/

for size in 16x16 24x24 32x32; do
  cp -v data/icons/hicolor/$size/apps/io.github.IshuSinghSE.aurynk.tray.png %buildroot%_iconsdir/hicolor/$size/apps/
done

# Styles
mkdir -p %buildroot%_datadir/%name
cp -v data/styles/aurynk.css %buildroot%_datadir/%name
cp -v data/styles/device_status.css %buildroot%_datadir/%name

# UI templates
cp -v data/ui/main_window.ui %buildroot%_datadir/%name
cp -v data/ui/device_details_window.ui %buildroot%_datadir/%name

# GResource
cp -v data/io.github.IshuSinghSE.aurynk.gresource.xml %buildroot%_datadir/%name

# Scripts
mkdir -p %buildroot%python3_sitelibdir/%name/scripts/
cp -v scripts/aurynk_tray.py %buildroot%python3_sitelibdir/%name/scripts/
rm -v %buildroot/usr/lib/python3/site-packages/scripts/aurynk_tray.py

%check
%meson_test

%files
%doc CHANGELOG.md LICENSE README.md data/screenshots
%_bindir/aurynk
%_desktopdir/io.github.IshuSinghSE.aurynk.desktop
%_iconsdir/hicolor/*/apps/io.github.IshuSinghSE.aurynk.png
%_iconsdir/hicolor/*/apps/io.github.IshuSinghSE.aurynk.*.png
%_iconsdir/hicolor/scalable/apps/io.github.IshuSinghSE.aurynk.svg
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/metainfo/io.github.IshuSinghSE.aurynk.metainfo.xml
%python3_sitelibdir/%name/

%changelog
* Thu Nov 27 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.0-alt2
- Put aurynk_tray.py into correct location, and enabled tray icon.

* Wed Nov 26 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
