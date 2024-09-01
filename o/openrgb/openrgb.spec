Name: openrgb
Version: 0.9
Release: alt3

Summary: Open source RGB lighting control that doesn't depend on manufacturer software

License: GPL-2.0-only
Group: System/Configuration/Other
Url: https://gitlab.com/CalcProgrammer1/OpenRGB

# Source-url: https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_%version/OpenRGB-release_%version.tar.bz2
Source: %name-%version.tar

#https://openrgb.org/releases/release_0.8/60-openrgb.rules
#Source1: 60-openrgb.rules

BuildRequires(pre): rpm-macros-qt5

BuildRequires: libhidapi-devel libusb-devel
BuildRequires: libmbedtls13-devel
BuildRequires: qt5-tools qt5-base-devel

%description
Open source RGB lighting control that doesn't depend on manufacturer software.

Supports a wide variety of RGB components, peripherals, accessories, and lights across many manufacturers.

%prep
%setup
# just to be sure
subst "s|/usr/lib/udev/rules.d|%_udevrulesdir|g" ResourceManager.cpp

%build
%qmake_qt5 OpenRGB.pro
%make_build

%install
mkdir -p %buildroot/%_udevrulesdir
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_desktopdir
mkdir -p %buildroot/%_iconsdir/hicolor/128x128/apps/
mkdir -p %buildroot/%_datadir/metainfo/

cp qt/OpenRGB.desktop %buildroot/%_desktopdir/OpenRGB.desktop
cp qt/OpenRGB.png %buildroot/%_iconsdir/hicolor/128x128/apps/OpenRGB.png
cp qt/org.openrgb.OpenRGB.metainfo.xml %buildroot/%_datadir/metainfo/org.openrgb.OpenRGB.metainfo.xml

%make_install INSTALL_ROOT=%buildroot install

%files
%_udevrulesdir/60-openrgb.rules
%_bindir/openrgb
%_desktopdir/OpenRGB.desktop
%_datadir/metainfo/org.openrgb.OpenRGB.metainfo.xml
%_iconsdir/hicolor/128x128/apps/OpenRGB.png

%changelog
* Sun Sep 01 2024 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt3
- fix packing udev rules

* Mon Feb 12 2024 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt2
- fix path to udev rules (thanks, nenderus@!)

* Fri Jul 14 2023 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- new version 0.9 (with rpmrb script)

* Sat May 20 2023 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt2
- build for Sisyphus

* Tue Nov 29 2022 Anton Shevtsov <shevtsov.anton@gmail.com> 0.8-alt1
- Initial build
