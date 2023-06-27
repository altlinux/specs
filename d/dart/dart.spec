%define _unpackaged_files_terminate_build 1

Name:    dart
Version: 6.13.0
Release: alt1

Summary: DART: Dynamic Animation and Robotics Toolkit
License: BSD-2-Clause
Group:   Development/C++
Url:     https://github.com/dartsim/dart

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: dart-alt-cmake-dir.patch

ExcludeArch: %ix86 armh

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: eigen3
BuildRequires: libOpenSceneGraph-devel
BuildRequires: libassimp-devel
BuildRequires: libbullet3-devel
BuildRequires: libccd-devel
BuildRequires: libfcl-devel
BuildRequires: libflann-devel
BuildRequires: libfmt-devel
BuildRequires: libfreeglut-devel
BuildRequires: libitk-devel
BuildRequires: libnlopt-devel
BuildRequires: libode-devel
BuildRequires: libtinyxml2-devel
BuildRequires: liburdfdom-devel
BuildRequires: pybind11-devel

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

%package -n python3-module-dartpy
Summary: DART Python bindings
Group: Development/Python3

%description -n python3-module-dartpy
%summary

%package docs
Summary: Documentation for %name
Group: Documentation

%description docs
%summary

%prep
%setup
%patch0 -p1

%build
%add_optflags -Wno-error=overloaded-virtual=
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
subst 's/eigen/eigen3/' %buildroot%_libdir/pkgconfig/%name.pc

%files -n lib%name
%doc README.md
%_libdir/lib*.so.*

%files -n lib%{name}-devel
%_includedir/*
%_libdir/lib*.so
%_libdir/cmake/%name
%_libdir/pkgconfig/%name.pc
%_datadir/%name/package.xml

%files -n python3-module-dartpy
%_libdir/python3/site-packages/dartpy.*.so

%files docs
%_defaultdocdir/%name

%changelog
* Thu May 25 2023 Andrey Cherepanov <cas@altlinux.org> 6.13.0-alt1
- Initial build for Sisyphus.
