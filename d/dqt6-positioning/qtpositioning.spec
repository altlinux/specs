%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module dqtpositioning

Name: dqt6-positioning
Version: 6.10.3
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt6 - QtPositioning component
Url: http://qt.io/
License: GPL-3.0-or-later

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-dqt6 dqt6-tools
BuildRequires: clang-devel
BuildRequires: cmake glibc-devel dqt6-declarative-devel dqt6-serialport-devel
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: libicu-devel zlib-devel libssl-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libdqt6-qmlcompiler libdqt6-quicktest libdqt6-help

# find librares
%add_findprov_lib_path %_dqt6_libdir

%description
The Qt Positioning API gives developers the ability to determine a position
by using a variety of possible sources, including satellite, or wifi, or
 text file, and so on. That information can then be used to for example
determine a position on a map. In addition satellite information can be
retrieved and area based monitoring can be performed.

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

%package -n libdqt6-positioningquick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libdqt6-core = %_dqt6_version
#Requires: dqt6-quickcontrols
%description -n libdqt6-positioningquick
%summary

%package -n libdqt6-positioning
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-positioning
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%DQ6build \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    #
%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
#%make -C BUILD DESTDIR=%buildroot install_docs ||:
mkdir -p %buildroot/%_docdir/dqt6/
cp -ar BUILD/share/doc/dqt6/* %buildroot/%_docdir/dqt6/
%endif

%files common
%doc LICENSES/*

%files -n libdqt6-positioning
%_dqt6_libdir/libQt?Positioning.so.*
%_dqt6_qmldir/QtPositioning/
%_dqt6_plugindir/position/

%files -n libdqt6-positioningquick
%_dqt6_libdir/libQt?PositioningQuick.so.*

%files devel
%_dqt6_headerdir/QtPositioning/
%_dqt6_headerdir/QtPositioningQuick/
%_dqt6_libdir/libQt*.so
%_dqt6_libdatadir/libQt*.so
%_dqt6_libdir/libQt*.prl
%_dqt6_libdatadir/libQt*.prl
%_dqt6_libdir/cmake/Qt*/
%_dqt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_dqt6_archdatadir/metatypes/qt*.json
%_dqt6_archdatadir/modules/*.json
%_dqt6_libdir/pkgconfig/Qt?*.pc

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif
%_dqt6_examplesdir/*

%changelog
* Tue Jun 09 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.3-alt0.dde.1
- merge with new version

* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Wed Feb 25 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.2-alt0.dde.1
- merge with new version

* Thu Feb 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- new version

* Tue Jan 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.1-alt1
- new version

* Fri Nov 21 2025 Leontiy Volodin <lvol@altlinux.org> 6.9.3-alt0.dde.1
- merge with new version

* Thu Nov 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.3-alt1
- new version

* Tue Aug 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt1
- new version

* Thu Aug 07 2025 Leontiy Volodin <lvol@altlinux.org> 6.9.1-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Jun 03 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.1-alt1
- new version

* Thu Feb 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Fri Feb 23 2024 Michael Shigorin <mike@altlinux.org> 6.6.2-alt1.1
- spec: drop obsolete e2kv3-only hack for old lcc

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Tue Jun 07 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
