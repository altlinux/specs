Name:    gz-plugin
Version: 2.0.0
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
BuildRequires: libgz-utils-devel >= 2.0.0

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
%_libdir/lib*.so
%_datadir/gz/gz*.completion.d/*.sh
%_datadir/gz/*.yaml
%_prefix/libexec/gz/plugin*/gz-plugin

%files -n lib%{name}-devel
%_includedir/gz/plugin*
%_libdir/cmake/gz-plugin*
%_libdir/pkgconfig/*.pc

%changelog
* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt2
- Moved .so files to main package.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
