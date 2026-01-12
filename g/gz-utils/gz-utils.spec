%define _unpackaged_files_terminate_build 1
%define soversion 4

Name: gz-utils
Version: 4.0.0
Release: alt1

Summary: Classes and functions for robot applications
License: Apache-2.0
Group: Development/C++
Url: https://gazebosim.org/libs/utils/
Vcs: https://github.com/gazebosim/gz-utils

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libspdlog-devel
BuildRequires: cli11-devel
BuildRequires: ctest

%description
Gazebo Utils, a component of Gazebo, provides general purpose classes and
functions designed for robotic applications.

%package -n libgz-utils%soversion
Summary: Library of gz-utils
Group: System/Libraries

%description -n libgz-utils%soversion
This package contains primary shared library of gz-utils

%package -n libgz-utils-log%soversion
Summary: Shared library gz-utils-log of gz-utils
Group: System/Libraries

%description -n libgz-utils-log%soversion
This package contains shared library gz-utils-log of gz-utils

%package -n libgz-utils-devel
Summary: Development files for gz-utils
Group: Development/C++

%description -n libgz-utils-devel
This package contains development files for gz-utils

%prep
%setup

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%check
%ctest

%files -n libgz-utils%soversion
%doc AUTHORS README.md
%_libdir/libgz-utils.so.%soversion
%_libdir/libgz-utils.so.%version

%files -n libgz-utils-log%soversion
%_libdir/libgz-utils-log.so.%soversion
%_libdir/libgz-utils-log.so.%version

%files -n libgz-utils-devel
%_includedir/gz/
%_libdir/cmake/gz-utils*
%_libdir/pkgconfig/gz-utils.pc
%_libdir/pkgconfig/gz-utils-cli.pc
%_libdir/pkgconfig/gz-utils-log.pc
%_libdir/libgz-utils*.so

%changelog
* Fri Dec 19 2025 Pavel Petrykin <silverducks@altlinux.org> 4.0.0-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version.

* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt2
- Moved .so files to main package.

* Fri May 26 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus.
