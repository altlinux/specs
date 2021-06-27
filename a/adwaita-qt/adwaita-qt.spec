Name: adwaita-qt
Version: 1.3.1
Release: alt1
Summary: Adwaita theme for Qt-based applications
License: LGPL-2.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/MartinBriza/adwaita-qt
Packager: Anton Midyukov <antohami@altlinux.org>

Source: adwaita-qt-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel

Requires: adwaita-qt5
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

%prep
%setup

%build
%define _cmake__builddir %_target_platform-qt5
%cmake
%cmake_build

%install
%define _cmake__builddir %_target_platform-qt5
%cmake_install

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

%files
%changelog
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
