%def_disable clang
%def_enable docs

Name: dwayland
Version: 5.24.3.1.4
Release: alt2

Summary: Qt-style API to interact with the DDE wayland-client and wayland-server

License: GPL-2.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dwayland

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-kf5 rpm-build-ninja
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake extra-cmake-modules
BuildRequires: qt5-base-devel qt5-wayland-devel
BuildRequires: kf5-kwayland-devel
BuildRequires: deepin-wayland-protocols-devel deepin-wayland-protocols
BuildRequires: wayland-protocols
%if_enabled docs
BuildRequires: doxygen qt5-tools-devel qt5-doc
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

%K5cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_PREFIX_PATH=%_qt5_prefix \
    -DCMAKE_INSTALL_LIBDIR=%_K5lib \
    %if_enabled docs
    -DBUILD_QCH=ON \
    %endif
%nil
cmake --build BUILD -j%__nprocs

%install
DESTDIR=%buildroot cmake --install BUILD
sed -i 's|includes =  .*|includes = %_includedir/DWayland/Client|' \
    %buildroot%_libdir/qt5/mkspecs/modules/qt_DWaylandClient.pri

%files common
%doc README.md
%_datadir/qlogging-categories5/dwayland.*

%files -n libDWaylandClient5
%_libdir/libDWaylandClient.so.5*

%files -n libDWaylandServer5
%_libdir/libDWaylandServer.so.5*

%if_enabled docs
%files docs
%_datadir/doc/qt5/DWayland.*
%endif

%files devel
%_includedir/dwayland_version.h
%_includedir/DWayland/
%_libdir/cmake/DWayland/
%_libdir/qt5/mkspecs/modules/qt_DWaylandClient.pri
%_libdir/libDWaylandClient.so
%_libdir/libDWaylandServer.so

%changelog
* Wed Jan 25 2023 Leontiy Volodin <lvol@altlinux.org> 5.24.3.1.4-alt2
- Fixed DWayland Client detection.

* Thu Jan 12 2023 Leontiy Volodin <lvol@altlinux.org> 5.24.3.1.4-alt1
- Initial build for ALT Sisyphus.
