Name: seafile-client
Version: 9.0.5
Release: alt1

Summary: Seafile gui client on QT bassed

Group: Networking/File transfer
License: Apache License
Url: https://github.com/haiwen/seafile-client

Packager: Denis Baranov <baraka@altlinux.ru>

# Source-url: https://github.com/haiwen/seafile-client/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: seafile.desktop

Patch: seafile-client-no-return-error.patch
Patch2: 86ebea086c6b78738b3140c922c909331d2b9a94.patch

ExclusiveArch: %qt6_qtwebengine_arches

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt6
BuildRequires(pre): rpm-macros-qt6-webengine

BuildRequires: cmake
BuildRequires: doxygen graphviz

BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6WebEngineCore)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)

BuildRequires: qt6-imageformats

BuildRequires: libseafile-devel >= %version

# see CMakeLists.txt
BuildRequires: pkgconfig(sqlite3) >= 3.0.0
BuildRequires: pkgconfig(jansson) >= 2.2.1
BuildRequires: pkgconfig(libsearpc) >= 1.0
BuildRequires: pkgconfig(openssl) >= 0.98
#BuildRequires: pkgconfig(libseafile) >= 1.7
BuildRequires: pkgconfig(libevent) >= 2.0
BuildRequires: pkgconfig(zlib) >= 1.2.0


Requires: seafile >= %EVR
Conflicts: libseafile <= 2.0.4

%description
Seafile desktop gui client.
Seafile is a full-fledged document collaboration platform.

%prep
%setup
%patch -p2
%patch2 -p1
# https://github.com/haiwen/seafile-client/pull/1346
subst '1iADD_DEFINITIONS(-DGLIB_VERSION_MIN_REQUIRED=GLIB_VERSION_2_26)' CMakeLists.txt
cp %SOURCE1 data/

%build
export PATH=%_qt6_bindir:$PATH
%cmake
%cmake_build

%install
%cmakeinstall_std
ln -s seafile-applet %buildroot%_bindir/%name

%find_lang %name

%files -f %name.lang
%_bindir/seafile-applet
%_bindir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*

%changelog
* Sun Mar 03 2024 Vitaly Lipatov <lav@altlinux.ru> 9.0.5-alt1
- new version 9.0.5
- switch to Qt6 build

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 8.0.6-alt1
- new version 8.0.6 (with rpmrb script)

* Sat Dec 18 2021 Vitaly Lipatov <lav@altlinux.ru> 8.0.5-alt1
- new version 8.0.5 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 8.0.3-alt1
- new version 8.0.3 (with rpmrb script)

* Sun Apr 18 2021 Vitaly Lipatov <lav@altlinux.ru> 8.0.2-alt1
- new version 8.0.2 (with rpmrb script)
- fix build with glib2 >= 2.67.3

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.10-alt1
- new version 7.0.10 (with rpmrb script)

* Fri Aug 21 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.9-alt1
- new version 7.0.9 (with rpmrb script)

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.8-alt1
- new version 7.0.8 (with rpmrb script)

* Tue May 12 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.7-alt1
- new version 7.0.7 (with rpmrb script)

* Wed Feb 19 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.6-alt1
- new version 7.0.6 (with rpmrb script)

* Sat Jan 18 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.5-alt1
- new version 7.0.5 (with rpmrb script)

* Mon Oct 14 2019 Vitaly Lipatov <lav@altlinux.ru> 7.0.2-alt2
- add russian localization to the desktop file (ALT bug 33772)

* Fri Aug 30 2019 Vitaly Lipatov <lav@altlinux.ru> 7.0.2-alt1
- new version 7.0.2 (with rpmrb script)

* Wed Jun 12 2019 Vitaly Lipatov <lav@altlinux.ru> 7.0.1-alt1
- new version 7.0.1 (with rpmrb script)

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 6.2.11-alt1
- new version 6.2.11 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 6.2.9-alt1
- new version 6.2.9 (with rpmrb script)

* Tue Sep 11 2018 Vitaly Lipatov <lav@altlinux.ru> 6.2.5-alt1
- new version 6.2.5 (with rpmrb script)

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 6.2.4-alt1
- new version 6.2.4 (with rpmrb script)
- drop ccnet from buildreqs

* Sat Jul 21 2018 Vitaly Lipatov <lav@altlinux.ru> 6.2.2-alt1
- new version 6.2.2 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.8-alt1
- new version 6.1.8 (with rpmrb script)

* Fri Apr 06 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.7-alt1
- new version 6.1.7 (with rpmrb script)

* Tue Mar 13 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.6-alt1
- new version 6.1.6 (with rpmrb script)

* Sun Feb 25 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.5-alt1
- new version 6.1.5 (with rpmrb script)

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 6.1.4-alt1
- new version 6.1.4 (with rpmrb script)

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 6.1.3-alt1
- new version 6.1.3 (with rpmrb script)

* Mon Feb 13 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.3-alt1
- new version 6.0.3 (with rpmrb script)

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt1
- new version 5.1.4 (with rpmrb script)

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.3-alt1
- new version 5.1.3 (with rpmrb script)

* Tue May 17 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script)
- build with Qt5, update buildreqs

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.4-alt1
- new version 5.0.4 (with rpmrb script)

* Fri Nov 21 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.11-alt1
- new version 3.1.11 (with rpmrb script)

* Sun Aug 31 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt2
- rebuild with rebuilt libseafile

* Thu Aug 28 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt1
- new version 3.1.5 (with rpmrb script)

* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt1
- new version 3.1.4 (with rpmrb script)

* Mon Jan 20 2014 Denis Baranov <baraka@altlinux.ru> 2.1.1-alt1
- Update to version 2.1.1

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.6-alt1
- Initial build gui client for ALTLinux
