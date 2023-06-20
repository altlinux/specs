Name:    gz-plugin
Version: 1.4.0
Release: alt1

Summary: Cross-platform C++ library for dynamically loading plugins
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-plugin

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libstdc++-devel-static

%description
Library for registering plugin libraries and dynamically loading them at
runtime. Gazebo Plugin is a component in the Gazebo framework, a set of
libraries designed to rapidly develop robot applications.

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
%_datadir/gz/gz1.completion.d/*.sh
%_datadir/ignition/*.yaml

%files -n lib%{name}-devel
%_includedir/ignition/plugin1
%_libdir/lib*.so
%_libdir/cmake/ignition-plugin*
%_libdir/pkgconfig/*.pc

%changelog
* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
