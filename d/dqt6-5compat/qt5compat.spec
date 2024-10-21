%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module dqt5compat

Name: dqt6-5compat
Version: 6.7.2
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt6 - Qt5 compatibility layer
Url: http://qt.io/
License:  GPL-3.0-only or LGPL-3.0-only

Source: %qt_module-everywhere-src-%version.tar

# find librares
%add_findprov_lib_path %_dqt6_libdir

BuildRequires(pre): rpm-macros-dqt6
BuildRequires(pre): dqt6-tools
BuildRequires: cmake glibc-devel libxkbcommon-x11-devel libicu-devel
BuildRequires: dqt6-base-devel dqt6-shadertools-devel dqt6-declarative-devel

%description
Porting support from Qt5 to Qt6.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: dqt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: dqt6-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libdqt6-core5compat
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libdqt6-core = %_dqt6_version
AutoProv: no,lib
Provides: %name = %EVR
Obsoletes: %name < %EVR
%description -n libdqt6-core5compat
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%DQ6build
%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
mkdir -p %buildroot%_dqt6_docdir
cp -a BUILD/share/doc/dqt6/* %buildroot%_dqt6_docdir ||:
%endif

# relax depends on plugins files
for f in %buildroot/%_dqt6_libdir/cmake/Qt?*/{*,}/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*

%files -n libdqt6-core5compat
%_dqt6_libdir/libQt?Core5Compat.so.*
%_dqt6_archdatadir/qml/Qt5Compat/

%files devel
%_dqt6_headerdir/QtCore5Compat/
%_dqt6_libdir/lib*.so
%_dqt6_libdatadir/lib*.so
%_dqt6_libdir/lib*.prl
%_dqt6_libdatadir/lib*.prl
%_dqt6_libdir/cmake/Qt*/
%_dqt6_archdatadir/mkspecs/modules/*.pri
%_dqt6_archdatadir/metatypes/qt6*.json
%_dqt6_archdatadir/modules/*.json
%_dqt6_libdir/pkgconfig/Qt?*.pc

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif
%_dqt6_examplesdir/*

%changelog
* Mon Oct 21 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Apr 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt2
- relax depends on plugins files when build with

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Mon Apr 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- initial build
