%define _unpackaged_files_terminate_build 1

Name:    gz-msgs
Version: 8.7.0
Release: alt2

Summary: Messages for Gazebo robot simulation
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-msgs

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: %name-alt-ruby-scripts-install-dir.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libgz-math-devel
BuildRequires: protobuf-compiler

%description
Gazebo Messages: Protobuf messages and functions for robot applications.

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
ln -s /usr/include/google proto/google

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc AUTHORS README.md
%_libexecdir/ruby/*
%_libdir/lib*.so.*
%_libdir/lib*.so
%_datadir/gz/gz1.completion.d/*.sh
%_datadir/ignition/*.yaml

%files -n lib%{name}-devel
%_includedir/ignition/msgs*
%_libdir/cmake/ignition-msgs*
%_libdir/pkgconfig/*.pc

%changelog
* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt2
- Moved .so files to main package.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt1
- New version.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 5.11.0-alt1
- Initial build for Sisyphus.
