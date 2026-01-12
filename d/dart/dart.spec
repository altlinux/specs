%define _unpackaged_files_terminate_build 1
%define soversion 6.16
%def_without dartpy

Name:    dart
Version: 6.16.1
Release: alt1

Summary: DART: Dynamic Animation and Robotics Toolkit
License: BSD-2-Clause
Group:   Development/C++
Url:     https://github.com/dartsim/dart

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: dart-alt-cmake-dir.patch
Patch1: dart-alt-python3.12.patch
#Patch2: dart-disable-download-pybind11.patch
Patch3: dart-alt-disable-octomap.patch
Patch4: dart-alt-disable-python-tests.patch
# See https://github.com/dartsim/dart/issues/2332
Patch5: dart-6.16.1-upstream-bullet-includes-fix.patch
# Raycast fix is optional, however it should make the error clearer if this test fails
Patch6: dart-6.16.1-upstream-raycast-segfault-fix.patch

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
%if_with dartpy
BuildRequires: pybind11-devel
BuildRequires: python3-module-pybind11
%endif

BuildRequires: ctest
BuildRequires: libgtest
BuildRequires: libbenchmark-devel

%description
%summary

%package -n libdart%soversion
Summary: Library of dart
Group: System/Libraries

%description -n libdart%soversion
%summary

%package -n libdart-collision-bullet%soversion
Summary: Shared library libdart-collision-bullet
Group: System/Libraries

%description -n libdart-collision-bullet%soversion
This package contains shared library of dart: libdart-collision-bullet

%package -n libdart-collision-ode%soversion
Summary: Shared library libdart-collision-ode
Group: System/Libraries

%description -n libdart-collision-ode%soversion
This package contains shared library of dart: libdart-collision-ode

%package -n libdart-external-imgui%soversion
Summary: Shared library libdart-external-imgui
Group: System/Libraries

%description -n libdart-external-imgui%soversion
This package contains shared library of dart: libdart-external-imgui

%package -n libdart-external-lodepng%soversion
Summary: Shared library libdart-external-lodepng
Group: System/Libraries

%description -n libdart-external-lodepng%soversion
This package contains shared library of dart: libdart-external-lodepng

%package -n libdart-external-odelcpsolver%soversion
Summary: Shared library libdart-external-odelcpsolver
Group: System/Libraries

%description -n libdart-external-odelcpsolver%soversion
This package contains shared library of dart: libdart-external-odelcpsolver

%package -n libdart-gui-osg%soversion
Summary: Shared library libdart-gui-osg
Group: System/Libraries

%description -n libdart-gui-osg%soversion
This package contains shared library of dart: libdart-gui-osg

%package -n libdart-gui%soversion
Summary: Shared library libdart-gui
Group: System/Libraries

%description -n libdart-gui%soversion
This package contains shared library of dart: libdart-gui

%package -n libdart-optimizer-nlopt%soversion
Summary: Shared library libdart-optimizer-nlopt
Group: System/Libraries

%description -n libdart-optimizer-nlopt%soversion
This package contains shared library of dart: libdart-optimizer-nlopt

%package -n libdart-utils-urdf%soversion
Summary: Shared library libdart-utils-urdf
Group: System/Libraries

%description -n libdart-utils-urdf%soversion
This package contains shared library of dart: libdart-utils-urdf

%package -n libdart-utils%soversion
Summary: Shared library libdart-utils
Group: System/Libraries

%description -n libdart-utils%soversion
This package contains shared library of dart: libdart-utils

%package -n libdart-devel
Summary: Development files for dart
Group: Development/C++

%description -n libdart-devel
%summary

%if_with dartpy
%package -n python3-module-dartpy
Summary: DART Python bindings
Group: Development/Python3

%description -n python3-module-dartpy
%summary
%endif

%package docs
Summary: Documentation for dart
Group: Documentation

%description docs
%summary

%prep
%setup
%autopatch -p1

%build
%add_optflags -Wno-error=deprecated-declarations
%add_optflags -Wno-error=unused-variable
%cmake -GNinja -Wno-dev \
  -DBUILD_TESTING=ON \
  -DDART_VERBOSE=ON \
  -DDART_USE_SYSTEM_GOOGLETEST=ON \
  -DDART_USE_SYSTEM_GOOGLEBENCHMARK=ON \
%if_with dartpy
  -DDART_BUILD_DARTPY=ON \
  -Dpybind11_FOUND=ON
%endif

%ninja_build -C "%_cmake__builddir" all tests

%install
%ninja_install -C "%_cmake__builddir"

%check
# See https://github.com/dartsim/dart/issues/2332
%ctest \
  --exclude-regex "test_ForceDependentSlip" \
  #

%files -n libdart%soversion
%doc README.md
%_libdir/libdart.so.%soversion
%_libdir/libdart.so.%version

%files -n libdart-collision-bullet%soversion
%_libdir/libdart-collision-bullet.so.%soversion
%_libdir/libdart-collision-bullet.so.%version

%files -n libdart-collision-ode%soversion
%_libdir/libdart-collision-ode.so.%soversion
%_libdir/libdart-collision-ode.so.%version

%files -n libdart-external-imgui%soversion
%_libdir/libdart-external-imgui.so.%soversion
%_libdir/libdart-external-imgui.so.%version

%files -n libdart-external-lodepng%soversion
%_libdir/libdart-external-lodepng.so.%soversion
%_libdir/libdart-external-lodepng.so.%version

%files -n libdart-external-odelcpsolver%soversion
%_libdir/libdart-external-odelcpsolver.so.%soversion
%_libdir/libdart-external-odelcpsolver.so.%version

%files -n libdart-gui-osg%soversion
%_libdir/libdart-gui-osg.so.%soversion
%_libdir/libdart-gui-osg.so.%version

%files -n libdart-gui%soversion
%_libdir/libdart-gui.so.%soversion
%_libdir/libdart-gui.so.%version

%files -n libdart-optimizer-nlopt%soversion
%_libdir/libdart-optimizer-nlopt.so.%soversion
%_libdir/libdart-optimizer-nlopt.so.%version

%files -n libdart-utils-urdf%soversion
%_libdir/libdart-utils-urdf.so.%soversion
%_libdir/libdart-utils-urdf.so.%version

%files -n libdart-utils%soversion
%_libdir/libdart-utils.so.%soversion
%_libdir/libdart-utils.so.%version

%files -n libdart-devel
%_includedir/dart
%_libdir/libdart*.so
%_libdir/cmake/dart
%_libdir/pkgconfig/dart.pc
%_datadir/dart/package.xml

%if_with dartpy
%files -n python3-module-dartpy
%_libdir/python3/site-packages/dartpy.*.so
%endif

%files docs
%_defaultdocdir/dart

%changelog
* Fri Dec 19 2025 Pavel Petrykin <silverducks@altlinux.org> 6.16.1-alt1
- New version.

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
