%define _unpackaged_files_terminate_build 1

Name:    gz-fuel-tools
Version: 8.0.2
Release: alt2

Summary: A client library and command line tools for interacting with Gazebo Fuel servers
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-fuel-tools

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libgz-common-devel
BuildRequires: libgz-math-devel
BuildRequires: libgz-msgs-devel
BuildRequires: gz-tools
BuildRequires: libyaml-devel
BuildRequires: libjsonrpccpp-devel
BuildRequires: libzip-devel

%description
Gazebo Fuel Tools is composed by a client library and command line tools for
interacting with Gazebo Fuel servers.

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
%_datadir/gz/*.yaml
%_datadir/gz/fuel_tools*
%_datadir/gz/gz-fuel_tools*

%files -n lib%{name}-devel
%_includedir/gz/fuel_tools*
%_libdir/cmake/gz-fuel_tools*
%_libdir/pkgconfig/*.pc

%changelog
* Mon Dec 18 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt2
- Packaged gz-fuel_tools8/gz-fuel_tools8.tag.xml.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 7.2.2-alt2
- Moved .so files to main package.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 7.2.2-alt1
- New version.

* Mon May 22 2023 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- Initial build for Sisyphus.
