Name:    libccd
Version: 2.1
Release: alt1

Summary: Library for collision detection between two convex shapes
License: BSD-3-Clause
Group:   System/Libraries
Url:     https://github.com/danfis/libccd

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: libccd-2.1-ctest.patch
Patch1: libccd-2.1-pkgconfig.patch
Patch2: libccd-2.1-py3.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++

%description
libccd implements variation on Gilbert-Johnson-Keerthi algorithm plus Expand
Polytope Algorithm (EPA) and also implements algorithm Minkowski Portal
Refinement (MPR, a.k.a. XenoCollide) as described in Game Programming Gems 7.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
%summary

%prep
%setup
%autopatch -p1

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
rm -f %buildroot%_defaultdocdir/ccd/BSD-LICENSE

%files
%doc BSD-LICENSE README.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_libdir/ccd

%changelog
* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1
- Initial build for Sisyphus.
