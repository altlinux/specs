Name: corectrl
Version: 1.2.2
Release: alt1

Summary: Core control application

Group: Graphics
License: GPLv3
Url: https://github.com/Lurkki14/tuxclocker

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://gitlab.com/corectrl/corectrl/-/archive/v%version/corectrl-v%version.tar.bz2
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake extra-cmake-modules
BuildRequires: kf5-kauth-devel kf5-kcoreaddons-devel kf5-karchive-devel
BuildRequires: qt5-declarative-devel qt5-charts-devel qt5-tools-devel qt5-svg-devel
BuildRequires: libbotan-devel
BuildRequires: libdrm-devel

# https://stackoverflow.com/questions/50172835/how-do-i-use-cmake-to-ensure-a-c14-compiler-links-with-the-experimental-filesy
BuildRequires: libstdc++-devel-static

%description
CoreCtrl is a Free and Open Source GNU/Linux application that allows you to control
with ease your computer hardware using application profiles.
It aims to be flexible, comfortable and accessible to regular users.

%prep
%setup
%__subst "s|LIBRARY DESTINATION lib|LIBRARY DESTINATION %_lib|" src/CMakeLists.txt

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_libdir/lib%name.so
/usr/libexec/kauth/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*x*/apps/corectrl.svg
%_datadir/metainfo/*
/usr/share/polkit-1/actions/*
/usr/share/dbus-1/system-services/*
/usr/share/dbus-1/system.d/*

%changelog
* Sun Jan 23 2022 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- new version 1.1.4 (with rpmrb script)

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- new version 1.1.3 (with rpmrb script)

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Wed May 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt1
- new version 1.0.9 (with rpmrb script)

* Mon Feb 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.7-alt1
- initial build for ALT Sisyphus
