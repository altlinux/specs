%define _unpackaged_files_terminate_build 1
%define soversion 9

Name: gz-math
Version: 9.2.0
Release: alt1

Summary: General purpose math library for robot applications
License: Apache-2.0
Group: Development/C++
Url: https://gazebosim.org/libs/math/
Vcs: https://github.com/gazebosim/gz-math

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libgz-utils-devel >= 2.0.0
BuildRequires: eigen3
BuildRequires: swig
BuildRequires: python3-dev
BuildRequires: python3-module-pybind11
BuildRequires: python3-module-pytest
BuildRequires: ctest

%description
Gazebo Math provides a wide range of functionality, including:
* Type-templated pose, matrix, vector, and quaternion classes.
* Shape representations along with operators to compute volume, density, size
  and other properties.
* Classes for material properties, mass, inertial, temperature, PID, kmeans,
  spherical coordinates, and filtering.
* Optional Eigen component that converts between a few Eigen and Gazebo Math
  types.

%package -n libgz-math%soversion
Summary: Library of gz-math
Group: System/Libraries

%description -n libgz-math%soversion
This package contains library libgz-math of gz-math.

%package -n libgz-math-devel
Summary: Development files for gz-math
Group: Development/C++

%description -n libgz-math-devel
This package contains development files of gz-math.

%package -n python3-module-gz-math
Summary: Python bindings for gz-math
Group: Development/Python3

%description -n python3-module-gz-math
This package contains python bindings for gz-math.

%prep
%setup

%build
%cmake \
    -GNinja \
    -Wno-dev \
    -DUSE_SYSTEM_PATHS_FOR_PYTHON_INSTALLATION=ON \
    #
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libgz-math%soversion
%doc AUTHORS README.md
%_libdir/libgz-math.so.%soversion
%_libdir/libgz-math.so.%version

%files -n libgz-math-devel
%_includedir/gz/math%soversion
%_cmakedir/gz-math
%_cmakedir/gz-math-all
%_cmakedir/gz-math-eigen3
%_pkgconfigdir/gz-math.pc
%_pkgconfigdir/gz-math-eigen3.pc
%_libdir/libgz-math.so

%files -n python3-module-gz-math
%python3_sitelibdir/gz

%changelog
* Mon Aug 10 2026 Pavel Petrykin <silverducks@altlinux.org> 9.2.0-alt1
- New version.
- Enable python bindings.

* Thu Nov 13 2025 Pavel Petrykin <silverducks@altlinux.org> 9.0.0-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 8.0.0-alt1
- New version.

* Mon Oct 02 2023 Andrey Cherepanov <cas@altlinux.org> 7.3.0-alt1
- New version.

* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 7.2.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 6.14.0-alt2
- Moved .so files to main package.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 6.14.0-alt1
- Initial build for Sisyphus.
