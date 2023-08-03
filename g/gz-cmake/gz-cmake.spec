Name:    gz-cmake
Version: 3.3.0
Release: alt1

Summary: A set of CMake modules that are used by the C++-based Gazebo projects
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-cmake

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++

%description
gz-cmake provides a set of cmake modules that are used by the C++-based Gazebo
projects. These modules help to control the quality and consistency of the
Gazebo projects' build systems.

These modules are tailored to the Gazebo projects, so their use for non-Gazebo
projects might be limited, but they may serve as a useful reference for setting
up a modern cmake build system using good practices.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
subst 's|^#!.*$|#!%__python3|' `find %buildroot%_datadir/gz/gz-cmake* -name \*.py`

%files
%doc README.md
%_includedir/gz/cmake*
%_datadir/cmake/gz-cmake*
%_libdir/pkgconfig/*.pc
%_datadir/gz

%changelog
* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt1
- Initial build for Sisyphus.
