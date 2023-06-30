Name:    gz-utils
Version: 1.5.1
Release: alt2

Summary: Classes and functions for robot applications
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-utils

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake

%description
Gazebo Utils, a component of Gazebo, provides general purpose classes and
functions designed for robotic applications.

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
%_libdir/lib*.so

%files -n lib%{name}-devel
%_includedir/ignition/utils1
%_libdir/cmake/*
%_libdir/pkgconfig/*.pc

%changelog
* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt2
- Moved .so files to main package.

* Fri May 26 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus.
