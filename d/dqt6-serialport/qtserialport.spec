%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module dqtserialport

Name: dqt6-serialport
Version: 6.10.3
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt6 - SerialPort component
Url: http://qt.io/
License: LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-dqt6 dqt6-tools
BuildRequires: clang-devel
BuildRequires: cmake glibc-devel dqt6-base-devel dqt6-tools-devel
BuildRequires: vulkan-headers libdqt6-widgets libdqt6-qml libdqt6-help
BuildRequires: pkgconfig(libudev)

# find librares
%add_findprov_lib_path %_dqt6_libdir

%description
Qt Serial Port provides the basic functionality, which includes configuring,
I/O operations, getting and setting the control signals of the RS-232 pinouts.

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

%package -n libdqt6-serialport
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libdqt6-serialport
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

%files -n libdqt6-serialport
%_dqt6_libdir/libQt?SerialPort.so.*

%files devel
%_dqt6_headerdir/Qt*/
%_dqt6_libdatadir/libQt*.so
%_dqt6_libdatadir/libQt*.prl
%_dqt6_libdir/libQt*.so
%_dqt6_libdir/libQt*.prl
%_dqt6_libdir/cmake/Qt*/
%_dqt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_dqt6_archdatadir/metatypes/qt6*.json
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

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Mon Jun 06 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
