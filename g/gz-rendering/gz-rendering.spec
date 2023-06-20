%define _unpackaged_files_terminate_build 1                                                                           

Name:    gz-rendering
Version: 6.6.0
Release: alt1

Summary: C++ library designed to provide an abstraction for different rendering engines. It offers unified APIs for creating 3D graphics applications
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-rendering

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

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

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc AUTHORS README.md
%_libdir/lib*.so.*
%_datadir/ignition/ignition-rendering*/media/materials/textures/com.png

%files -n lib%{name}-devel
%_includedir/ignition/rendering*
%_libdir/lib*.so
%_libdir/cmake/*
%_libdir/pkgconfig/*.pc

%changelog
* Sat May 27 2023 Andrey Cherepanov <cas@altlinux.org> 6.6.0-alt1
- Initial build for Sisyphus.
