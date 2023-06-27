Name:    fcl
Version: 0.7.0
Release: alt1

Summary: Flexible Collision Library
License: BSD-3-Clause
Group:   Other
Url:     https://github.com/flexible-collision-library/fcl

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libccd-devel
BuildRequires: eigen3

%description
FCL is a library for performing three types of proximity queries on a pair of
geometric models composed of triangles.

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
%doc LICENSE CHANGELOG.md README.md
%_libdir/lib*.so.*
%_datadir/%name

%files -n lib%{name}-devel
%_includedir/*
%_libdir/lib*.so
%_libdir/cmake/*
%_libdir/pkgconfig/*.pc

%changelog
* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
