# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: adwaita-qt
Version: 1.4.2
Release: alt1
Summary: Adwaita theme for Qt-based applications
License: LGPL-2.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/MartinBriza/adwaita-qt

Source: adwaita-qt-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt6-base-devel

Requires: adwaita-qt5
Requires: adwaita-qt6
Obsoletes: adwaita-qt4

%description
%summary.

%package -n adwaita-qt5
Summary: Adwaita Qt5 theme
Group: Graphical desktop/GNOME

%description -n adwaita-qt5
Adwaita theme variant for applications utilizing Qt5

%package -n libadwaita-qt5
Summary: Adwaita Qt5 library
Group: Graphical desktop/GNOME

%description -n libadwaita-qt5
%summary.

%package -n libadwaita-qt5-devel
Summary: Development files for libadwaita-qt5
Group: Development/KDE and QT
Requires: libadwaita-qt5 = %EVR

%description -n libadwaita-qt5-devel
The libadwaita-qt5-devel package contains libraries and header files for
developing applications that use libadwaita-qt5.

%package -n adwaita-qt6
Summary: Adwaita Qt6 theme
Group: Graphical desktop/GNOME

%description -n adwaita-qt6
Adwaita theme variant for applications utilizing Qt6

%package -n libadwaita-qt6
Summary: Adwaita Qt6 library
Group: Graphical desktop/GNOME

%description -n libadwaita-qt6
%summary.

%package -n libadwaita-qt6-devel
Summary: Development files for libadwaita-qt6
Group: Development/KDE and QT
Requires: libadwaita-qt6 = %EVR

%description -n libadwaita-qt6-devel
The libadwaita-qt6-devel package contains libraries and header files for
developing applications that use libadwaita-qt6.

%prep
%setup

%build
%define _cmake__builddir %_target_platform-qt5
%cmake
%cmake_build

%define _cmake__builddir %_target_platform-qt6
%cmake -DUSE_QT6=true
%cmake_build

%install
%define _cmake__builddir %_target_platform-qt5
%cmake_install

%define _cmake__builddir %_target_platform-qt6
%cmake_install

rm %buildroot%_libdir/pkgconfig/adwaita-qt6.pc

%files -n adwaita-qt5
%doc LICENSE.LGPL2 README.md
%_qt5_archdatadir/plugins/styles/adwaita.so

%files -n libadwaita-qt5
%_libdir/libadwaitaqt.so.*
%_libdir/libadwaitaqtpriv.so.*

%files -n libadwaita-qt5-devel
%dir %_includedir/AdwaitaQt
%_includedir/AdwaitaQt/*.h
%dir %_libdir/cmake/AdwaitaQt
%_libdir/cmake/AdwaitaQt/*.cmake
%_pkgconfigdir/adwaita-qt.pc
%_libdir/libadwaitaqt.so
%_libdir/libadwaitaqtpriv.so

%files -n adwaita-qt6
%doc LICENSE.LGPL2 README.md
%_qt6_archdatadir/plugins/styles/adwaita.so

%files -n libadwaita-qt6
%_libdir/libadwaitaqt6.so.*
%_libdir/libadwaitaqt6priv.so.*

%files -n libadwaita-qt6-devel
%dir %_includedir/AdwaitaQt6
%_includedir/AdwaitaQt6/*.h
%dir %_libdir/cmake/AdwaitaQt6
%_libdir/cmake/AdwaitaQt6/*.cmake
#_pkgconfigdir/adwaita-qt6.pc
%_libdir/libadwaitaqt6.so
%_libdir/libadwaitaqt6priv.so

%files
%changelog
* Sun Aug 04 2024 Anton Midyukov <antohami@altlinux.org> 1.4.2-alt1
- New version 1.4.2 (Closes: 51048)

* Mon Jun 20 2022 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- new version 1.4.1
- initial build adwaita-qt6

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 1.3.1-alt1
- new version 1.3.1
- drop qt4 subpackage

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 1.1.4-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Jul 16 2020 Anton Midyukov <antohami@altlinux.org> 1.1.4-alt1
- new version 1.1.4

* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 1.1.3-alt1
- new version 1.1.3
- fix License tag

* Sun Jan 12 2020 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Mon Aug 12 2019 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Wed Jul 10 2019 Anton Midyukov <antohami@altlinux.org> 1.0.90-alt1
- new version 1.0.90

* Wed May 31 2017 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- new version 1.0

* Wed Apr 12 2017 Anton Midyukov <antohami@altlinux.org> 0.99-alt1
- new version 0.99

* Wed Mar 01 2017 Anton Midyukov <antohami@altlinux.org> 0.98-alt1
- new version 0.98

* Sun Sep 04 2016 Anton Midyukov <antohami@altlinux.org> 0.5-alt1
- new version 0.5
- remove qt-creator-menubar-fix.patch

* Tue Aug 30 2016 Anton Midyukov <antohami@altlinux.org> 0.4-alt1
- Initial build for Alt Linux Sisyphus (Thanks Fedora Team).
