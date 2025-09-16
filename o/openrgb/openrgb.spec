%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%ifnarch %ix86
%set_verify_elf_method strict
%endif

Name: openrgb
Version: 1.0
Release: alt1.rc2

%define org_name org.%name.OpenRGB

Summary: Open source RGB lighting control that doesn't depend on manufacturer software

License: GPL-2.0-only
Group: System/Configuration/Other
Url: https://gitlab.com/CalcProgrammer1/OpenRGB
Vcs: https://gitlab.com/CalcProgrammer1/OpenRGB

# Source-url: https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_%version/OpenRGB-release_%version.tar.bz2
Source: %name-%version.tar
Patch: %name-alt-no-strip.patch

BuildRequires(pre): rpm-macros-qt6 rpm-macros-systemd

BuildRequires: libhidapi-devel libusb-devel
BuildRequires: libmbedtls13-devel
BuildRequires: qt6-tools qt6-base-devel

%description
Open source RGB lighting control that doesn't depend on manufacturer software.

Supports a wide variety of RGB components, peripherals, accessories, and lights
across many manufacturers.

%prep
%setup
%patch -p2
# just to be sure
subst "s|/usr/lib/udev/rules.d|%_udevrulesdir|g" ResourceManager.cpp
subst "s|/etc/systemd/system|%_unitdir|g" OpenRGB.pro

%build
export QMAKE_CXXFLAGS_RELEASE='%optflags'
%qmake_qt6 OpenRGB.pro
%make_build V=1

%install
%make_install INSTALL_ROOT=%buildroot install

%files
%_unitdir/%name.service
%_udevrulesdir/60-%name.rules
%_bindir/%name
%_desktopdir/%org_name.desktop
%_datadir/metainfo/%org_name.metainfo.xml
%_iconsdir/hicolor/128x128/apps/%org_name.png

%changelog
* Tue Sep 16 2025 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt1.rc2
- 1.0rc2.
- qt5->qt6.

* Wed Sep 10 2025 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt1.rc1
- 1.0rc1.
- enable debuginfo.
- spec cleanup.

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
