%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%def_disable testing
%global qt_module dqthttpserver

Name: dqt6-httpserver
Version: 6.10.3
Release: alt0.dde.1

Summary: Qt Extension: Qt HTTP Server
Group: System/Libraries
License: GPL-3.0-only
Url: https://www.qt.io/

Source: %qt_module-everywhere-src-%version.tar
Patch0: alt-skip-some-http2-tests.patch

BuildRequires(pre): rpm-macros-dqt6
BuildRequires(pre): dqt6-tools
BuildRequires: cmake dqt6-base-devel
BuildRequires: libdqt6-network libdqt6-gui libdqt6-concurrent
BuildRequires: clang-devel libdqt6-qml libdqt6-help
%if_enabled testing
BuildRequires: ctest
%endif

# find libraries
%add_findprov_lib_path %_dqt6_libdir

%description
Qt HTTP Server supports building HTTP server functionality into an
application. Common use cases are exposing the application's
functionality through REST APIs, or making devices in a trusted
environment configurable also via HTTP.

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
Requires: %name-common
Requires: dqt6-base-devel
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use %name
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for %name

%package -n libdqt6-httpserver
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-httpserver
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
%patch0 -p1

%build
%DQ6build \
%if_enabled testing
    -DQT_BUILD_TESTS=%{?_enable_testing:ON}%{!?_enable_testing:OFF} \
%endif
    -DQT_GENERATE_SBOM:BOOL=OFF \
    #

%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
mkdir -p %buildroot/%_docdir/dqt6/
cp -ar BUILD/share/doc/dqt6/* %buildroot/%_docdir/dqt6/
%endif

%if_enabled testing
%check
CMAKE_TOOLCHAIN_FILE=%_dqt6_libdir/cmake/Qt6/qt.toolchain.cmake \
    ctest --test-dir BUILD %_smp_mflags
%endif

%files common
%doc LICENSES/*

%files -n lib%name
%_dqt6_libdir/libQt?HttpServer.so.*

%files devel
%_dqt6_headerdir/QtHttpServer/
%_dqt6_libdir/lib*.so
%_dqt6_libdir/lib*.prl
%_dqt6_libdatadir/lib*.so
%_dqt6_libdatadir/lib*.prl
%_dqt6_libdir/cmake/Qt?HttpServer*/
%_dqt6_libdir/cmake/Qt6BuildInternals/StandaloneTests/*HttpServer*.cmake
%_dqt6_archdatadir/mkspecs/modules/*httpserver*.pri
%_dqt6_archdatadir/metatypes/*httpserver*.json
%_dqt6_archdatadir/modules/*ttp?erver*.json
%_dqt6_libdir/pkgconfig/Qt?HttpServer.pc

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif
%_dqt6_examplesdir/*

%changelog
* Wed Oct 21 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.3-alt0.dde.1
- fork for independent deepin buildings

* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Thu Feb 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- new version

* Tue Jan 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.1-alt1
- new version

* Thu Nov 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.3-alt1
- new version

* Tue Aug 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt1
- new version

* Thu Jul 03 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.1-alt2
- build from tarball

* Tue Jun 24 2025 Evgeniy Gorbanyov <esgor@altlinux.org> 6.9.1-alt1
- Initial build for Sisyphus.
