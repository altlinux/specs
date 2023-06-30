%define _unpackaged_files_terminate_build 1

Name:    gz-transport
Version: 11.4.0
Release: alt2

Summary: Transport library for component communication based on publication/subscription and service calls
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-transport

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel-static
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libgz-math-devel
BuildRequires: libgz-msgs-devel >= 8.0.0
BuildRequires: libgz-utils-devel
BuildRequires: libuuid-devel
BuildRequires: libsqlite3-devel
BuildRequires: libzeromq-cpp-devel
BuildRequires: protobuf-compiler
BuildRequires: lsb-release

%description
Gazebo Transport, a component of Gazebo, provides fast and efficient
asynchronous message passing, services, and data logging.

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
%_libexecdir/ruby/*
%_libdir/lib*.so.*
%_libdir/lib*.so
%_prefix/libexec/gz/transport*/ign-transport-*
%_datadir/gz/gz1.completion.d/*.sh
%_datadir/ignition/*.yaml
%_datadir/ignition/ignition-transport*

%files -n lib%{name}-devel
%_includedir/ignition/transport*
%_libdir/cmake/ignition-transport*
%_libdir/pkgconfig/*.pc

%changelog
* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 11.4.0-alt2
- Moved .so files to main package.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 11.4.0-alt1
- New version.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 8.4.0-alt1
- Initial build for Sisyphus.
