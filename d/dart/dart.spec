%define _unpackaged_files_terminate_build 1
%def_without dartpy

Name:    dart
Version: 6.15.0
Release: alt1

Summary: DART: Dynamic Animation and Robotics Toolkit
License: BSD-2-Clause
Group:   Development/C++
Url:     https://github.com/dartsim/dart

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: dart-alt-cmake-dir.patch
Patch1: dart-alt-python3.12.patch
Patch2: dart-disable-download-pybind11.patch
Patch3: dart-alt-disable-octomap.patch
Patch4: dart-alt-disable-python-tests.patch

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
BuildRequires: python3-module-pybind11

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

%if_with dartpy
%package -n python3-module-dartpy
Summary: DART Python bindings
Group: Development/Python3

%description -n python3-module-dartpy
%summary
%endif

%package docs
Summary: Documentation for %name
Group: Documentation

%description docs
%summary

%prep
%setup
%autopatch -p1

%build
%add_optflags -Wno-error=overloaded-virtual=
%cmake -GNinja -Wno-dev \
       -DBUILD_TESTING=OFF \
%if_with dartpy
       -DDART_BUILD_DARTPY=ON \
       -Dpybind11_FOUND=ON
%endif

%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc README.md
%_libdir/lib*.so.*

%files -n lib%{name}-devel
%_includedir/*
%_libdir/lib*.so
%_libdir/cmake/%name
%_libdir/pkgconfig/%name.pc
%_datadir/%name/package.xml

%if_with dartpy
%files -n python3-module-dartpy
%_libdir/python3/site-packages/dartpy.*.so
%endif

%files docs
%_defaultdocdir/%name

%changelog
* Fri Jan 10 2025 Andrey Cherepanov <cas@altlinux.org> 6.15.0-alt1
- New version.
- Disable dartpy build.

* Sat Jul 06 2024 Andrey Cherepanov <cas@altlinux.org> 6.14.4-alt1
- New version.

* Thu Jun 27 2024 Andrey Cherepanov <cas@altlinux.org> 6.14.1-alt1
- New version.

* Wed Jun 26 2024 Andrey Cherepanov <cas@altlinux.org> 6.14.0-alt1
- New version.

* Mon Mar 18 2024 Andrey Cherepanov <cas@altlinux.org> 6.13.2-alt1
- New version.

* Fri Jan 05 2024 Andrey Cherepanov <cas@altlinux.org> 6.13.1-alt1
- New version.

* Thu May 25 2023 Andrey Cherepanov <cas@altlinux.org> 6.13.0-alt1
- Initial build for Sisyphus.
