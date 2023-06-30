%define _unpackaged_files_terminate_build 1

Name:    gz-physics
Version: 5.3.1
Release: alt2

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
BuildRequires: libdart-devel
BuildRequires: liburdfdom-devel
BuildRequires: libfmt-devel
BuildRequires: libode-devel

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
cp -a %_cmake__builddir/fake/install/%_lib/ign-physics-*/engine-plugins/libignition-physics-*-plugin.so %_cmake__builddir
cp -a %_cmake__builddir/fake/install/%_lib/*.so* %_cmake__builddir

%install
%ninja_install -C "%_cmake__builddir"
rm -f %buildroot%_libdir/*-plugin.so*
# undefined symbol: _ZN18btStaticPlaneShapeC1ERK9btVector3f
rm -rf %buildroot%_libdir/ign-physics-*/engine-plugins/libignition-physics*-bullet-plugin.so*
rm -f %buildroot%_libdir/pkgconfig/ignition-physics*-bullet-plugin.pc

%files -n lib%name
%doc AUTHORS README.md
%_libdir/lib*.so.*
%_libdir/lib*.so
%_libdir/ign-physics-*

%files -n lib%{name}-devel
%_includedir/ignition/*
%_libdir/cmake/*
%_libdir/pkgconfig/*.pc

%changelog
* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt2
- Moved .so files to main package.
- Built with DART.

* Sun May 28 2023 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- Initial build for Sisyphus.
