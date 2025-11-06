%define _unpackaged_files_terminate_build 1

%define soname 1

Name: recastnavigation
Version: 1.6.0
Release: alt1

Summary: Navigation-mesh toolset for games
License: Zlib
Group: Graphics
Url: https://recastnav.com/
Vcs: https://github.com/recastnavigation/recastnavigation

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake >= 3.0
BuildRequires: gcc-c++
BuildRequires: libGLU-devel
BuildRequires: libSDL2-devel
BuildRequires: ctest

%description
Recast is a state of the art navigation mesh construction toolset for games.
Recast is accompanied by Detour, a pathfinding and spatial reasoning toolkit.
You can use any navigation mesh with Detour, but of course the data generated
with Recast fits perfectly.

%package devel
Summary: Include Files for Recastnavigation Libraries
Group: Development/C++

%description devel
This package contains files and libraries needed for development with
recastnavigation libraries.

%package -n libDebugUtils%soname
Summary: Debug Utilities Library for Recastnavigation
Group: Development/C++

%description -n libDebugUtils%soname
This package contains the debug utilities library for the recastnavigation.

%package -n libDetour%soname
Summary: Detour Library for Recastnavigation
Group: Graphics

%description -n libDetour%soname
This package contains the detour library part of recastnavigation.

%package -n libDetourCrowd%soname
Summary: Detour Crowd Library for Recastnavigation
Group: Graphics

%description -n libDetourCrowd%soname
This package contains the detour crowd library part of recastnavigation.

%package -n libDetourTileCache%soname
Summary: Detour Tile Cache Library for Recastnavigation
Group: Graphics

%description -n libDetourTileCache%soname
This package contains the detour tile cache library part of recastnavigation.

%package -n libRecast%soname
Summary: Recast Library for Recastnavigation
Group: Graphics

%description -n libRecast%soname
This package contains the recast library part of recastnavigation.

%prep
%setup

%build
%add_optflags "-ffat-lto-objects"
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DRECASTNAVIGATION_DEMO=OFF \
    -DRECASTNAVIGATION_EXAMPLES=OFF \
    %nil

%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc License.txt
%doc README.md
%_libdir/libDebugUtils.so
%_libdir/libDetour.so
%_libdir/libDetourCrowd.so
%_libdir/libDetourTileCache.so
%_libdir/libRecast.so
%_includedir/recastnavigation
%_libdir/pkgconfig/recastnavigation.pc
%_libdir/cmake/recastnavigation

%files -n libDebugUtils%soname
%_libdir/libDebugUtils.so.%soname
%_libdir/libDebugUtils.so.%version

%files -n libDetour%soname
%_libdir/libDetour.so.%soname
%_libdir/libDetour.so.%version

%files -n libDetourCrowd%soname
%_libdir/libDetourCrowd.so.%soname
%_libdir/libDetourCrowd.so.%version

%files -n libDetourTileCache%soname
%_libdir/libDetourTileCache.so.%soname
%_libdir/libDetourTileCache.so.%version

%files -n libRecast%soname
%_libdir/libRecast.so.%soname
%_libdir/libRecast.so.%version

%changelog
* Thu Nov 6 2025 Pavel Petrykin <silverducks@altlinux.org> 1.6.0-alt1
- Initial build for Alt Linux.
