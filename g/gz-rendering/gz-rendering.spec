%define _unpackaged_files_terminate_build 1                                                                           

Name:    gz-rendering
Version: 7.4.0
Release: alt1

Summary: C++ library designed to provide an abstraction for different rendering engines. It offers unified APIs for creating 3D graphics applications
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-rendering

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: 0001-Fix-missing-header-in-latest-gcc-build-853.patch

ExcludeArch: %ix86

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libfreeimage-devel
BuildRequires: libogre-devel
BuildRequires: libGL-devel
BuildRequires: libgz-math-devel >= 6.0.0
BuildRequires: libgz-common-devel
BuildRequires: libgz-plugin-devel

%description
Gazebo Rendering is a C++ library designed to provide an abstraction for
different rendering engines. It offers unified APIs for creating 3D graphics
applications.

%package -n lib%name
Summary: Library of %name
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%{name}-devel
%summary

%prep
%setup
%patch0 -p1

%build
%cmake -GNinja -Wno-dev \
       -DBUILD_TESTING=OFF
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc AUTHORS README.md
%_libdir/lib*.so.*
%_libdir/lib*.so
#_libdir/ign-rendering-*
%_datadir/gz/gz-rendering*

%files -n lib%{name}-devel
%_includedir/gz/rendering*
%_libdir/cmake/*
%_libdir/pkgconfig/*.pc

%changelog
* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 7.4.0-alt1
- New version.

* Wed Jun 28 2023 Andrey Cherepanov <cas@altlinux.org> 6.6.0-alt2
- Moved .so files to main package.
- FTBFS: fixed build with GCC 13.x.
- Disabled test build.

* Sat May 27 2023 Andrey Cherepanov <cas@altlinux.org> 6.6.0-alt1
- Initial build for Sisyphus.
