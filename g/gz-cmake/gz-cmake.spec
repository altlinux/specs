Name:    gz-cmake
Version: 2.16.0
Release: alt1

Summary: A set of CMake modules that are used by the C++-based Gazebo projects
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-cmake

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: gz-cmake-alt-fix-version-in-ignition-component.pc.in.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++

%description
ignition-cmake provides a set of cmake modules that are used by the C++-based
ignition projects. These modules help to control the quality and consistency of
the ignition projects' build systems.

These modules are tailored to the ignition projects, so their use for
non-ignition projects might be limited, but they may serve as a useful
reference for setting up a modern cmake build system using good practices.

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install
subst 's|^#!.*$|#!%__python3|' %buildroot%_datadir/ignition/ignition-cmake2/*/*.py

%files
%doc README.md
%_includedir/ignition/cmake2
%_datadir/cmake/ignition-cmake2
%_libdir/pkgconfig/*.pc
%_datadir/ignition

%changelog
* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt1
- Initial build for Sisyphus.
