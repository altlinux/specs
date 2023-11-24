%define _unpackaged_files_terminate_build 1

Name:    gz-physics
Version: 6.4.0
Release: alt1.2

Summary: Abstract physics interface designed to support simulation and rapid development of robot applications
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-physics

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

ExcludeArch: %ix86 armh

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libsdformat-devel >= 12.0.0
BuildRequires: libgz-math-devel
BuildRequires: libgz-utils-devel
BuildRequires: libgz-plugin-devel
BuildRequires: libgz-common-devel
BuildRequires: libbullet3-devel
BuildRequires: libbenchmark-devel
%ifnarch %e2k
BuildRequires: libdart-devel
%endif
BuildRequires: liburdfdom-devel
BuildRequires: libfmt-devel
BuildRequires: libode-devel
BuildRequires: zlib-devel
BuildRequires: libminizip-devel
BuildRequires: libpoly2tri-devel

%description
%summary

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
%add_optflags -I%_includedir/bullet
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"
cp -a %_cmake__builddir/fake/install/%_lib/gz-physics-*/engine-plugins/libgz-physics-*-plugin.so %_cmake__builddir
cp -a %_cmake__builddir/fake/install/%_lib/*.so* %_cmake__builddir

%install
%ninja_install -C "%_cmake__builddir"
rm -f %buildroot%_libdir/*-plugin.so*
rm -f %buildroot%_prefix/libexec/gz/physics*/COMMON_TEST*
# undefined symbol: _ZN18btStaticPlaneShapeC1ERK9btVector3f
rm -f %buildroot%_libdir/gz-physics-*/engine-plugins/libgz-physics*-bullet-*plugin.so*
rm -f %buildroot%_libdir/pkgconfig/gz-physics*-bullet-*plugin.pc

%files -n lib%name
%doc AUTHORS README.md
%_libdir/lib*.so.*
%_libdir/lib*.so
%_libdir/gz-physics-*

%files -n lib%{name}-devel
%_includedir/gz/*
%_libdir/cmake/*
%_libdir/pkgconfig/*.pc

%changelog
* Wed Nov 22 2023 L.A. Kostis <lakostis@altlinux.ru> 6.4.0-alt1.2
- BR: remove stbi (not used).

* Thu Aug 24 2023 Michael Shigorin <mike@altlinux.org> 6.4.0-alt1.1
- E2K: build without dart

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 6.4.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt2
- Moved .so files to main package.
- Built with DART.

* Sun May 28 2023 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- Initial build for Sisyphus.
