%def_disable clang
%def_enable docs

Name: dwayland
Version: 5.25.0
Release: alt2

Summary: Qt-style API to interact with the DDE wayland-client and wayland-server

License: GPL-2.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dwayland

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake extra-cmake-modules
BuildRequires: dqt5-base-devel dqt5-wayland-devel
BuildRequires: deepin-wayland-protocols-devel deepin-wayland-protocols
BuildRequires: wayland-protocols
%if_enabled docs
BuildRequires: doxygen dqt5-tools-devel dqt5-doc
%endif

%description
DWayland provides two libraries:
- DWayland::Client;
- DWaylandServer.
As the names suggest they implement a Client respectively a Server API
for the Wayland protocol. The API is Qt-styled removing the needs to interact
with a for a Qt developer uncomfortable low-level C-API.

%package common
Summary: Qt library wrapper for Wayland libraries - data files
Group: Graphical desktop/Other
BuildArch: noarch

%description common
DWayland provides a Qt-style Server library wrapper for
the Wayland libraries.

%package -n libDWaylandClient5
Summary: Qt library wrapper for Wayland libraries
Group: System/Libraries

%description -n libDWaylandClient5
DWayland provides a Qt-style Server library wrapper for
the Wayland libraries.

%package -n libDWaylandServer5
Summary: Qt library wrapper for Wayland libraries
Group: System/Libraries

%description -n libDWaylandServer5
DWayland provides a Qt-style Server library wrapper for
the Wayland libraries.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description docs
The package provides the documentation for %name.

%package devel
Summary: Development package for %name
Group: Development/C++

%description devel
Header files and libraries for %name.

%prep
%setup

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_PREFIX_PATH=%_dqt5_libdir/cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
    -DECM_MKSPECS_INSTALL_DIR=%_dqt5_archdatadir/mkspecs/modules \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DKDE_INSTALL_QTQCHDIR=%_datadir/doc/dqt5 \
    %if_enabled docs
    -DBUILD_QCH=ON \
    %endif
%nil
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install
sed -i 's|includes =  .*|includes = %_includedir/DWayland/Client|' \
    %buildroot%_dqt5_archdatadir/mkspecs/modules/qt_DWaylandClient.pri

%files common
%doc README.md
%_datadir/qlogging-categories5/dwayland.*

%files -n libDWaylandClient5
%_libdir/libDWaylandClient.so.5*

%files -n libDWaylandServer5
%_libdir/libDWaylandServer.so.5*

%if_enabled docs
%files docs
%_datadir/doc/dqt5/DWayland.*
%endif

%files devel
%_includedir/dwayland_version.h
%_includedir/DWayland/
%_libdir/cmake/DWayland/
%_dqt5_archdatadir/mkspecs/modules/qt_DWaylandClient.pri
%_libdir/libDWaylandClient.so
%_libdir/libDWaylandServer.so

%changelog
* Fri May 10 2024 Leontiy Volodin <lvol@altlinux.org> 5.25.0-alt2
- Built via separate qt5 instead system (ALT #48138).

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 5.25.0-alt1
- New version 5.25.0.

* Wed Jan 25 2023 Leontiy Volodin <lvol@altlinux.org> 5.24.3.1.4-alt2
- Fixed DWayland Client detection.

* Thu Jan 12 2023 Leontiy Volodin <lvol@altlinux.org> 5.24.3.1.4-alt1
- Initial build for ALT Sisyphus.
