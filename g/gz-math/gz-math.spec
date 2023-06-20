%define _unpackaged_files_terminate_build 1

Name:    gz-math
Version: 6.14.0
Release: alt1

Summary: General purpose math library for robot applications
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-math

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: eigen3
BuildRequires: swig
BuildRequires: python3-dev
BuildRequires: python3-module-pybind11

%description
Gazebo Math provides a wide range of functionality, including:
* Type-templated pose, matrix, vector, and quaternion classes.
* Shape representations along with operators to compute volume, density, size
  and other properties.
* Classes for material properties, mass, inertial, temperature, PID, kmeans,
  spherical coordinates, and filtering.
* Optional Eigen component that converts between a few Eigen and Gazebo Math
  types.

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

%package -n python3-module-%name
Summary: Python bindings for %name
Group: Development/Python3

%description -n python3-module-%name
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
%_libdir/lib*.so.*

%files -n lib%{name}-devel
%_includedir/ignition/math6
%_libdir/lib*.so
%_libdir/cmake/ignition-math6*
%_libdir/pkgconfig/*.pc

%files -n python3-module-%name
%_libdir/python/ignition/*.so

%changelog
* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 6.14.0-alt1
- Initial build for Sisyphus.
