%define lname imath
%define libsover 29
%define libimath lib%lname%libsover
Name: %libimath
Version: 3.1.6
Release: alt1

Summary: Imath is library of 2D and 3D vector, matrix, and math operations for graphics
License: BSD-3-Clause
Group: System/Libraries
URL: https://github.com/AcademySoftwareFoundation/Imath

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-module-setuptools
BuildRequires: boost-python3-devel
BuildRequires: python3-module-numpy
BuildRequires: doxygen
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-breathe
BuildRequires: python3-module-sphinx-sphinx-build-symlink

%description
Imath is a basic, light-weight, and efficient C++ representation of
2D and 3D vectors and matrices and other simple but useful mathematical
objects, functions, and data types common in computer graphics applications,
including the "half" 16-bit floating-point type.

Imath also includes optional python bindings for all types and functions,
including optimized implementations of vector and matrix arrays.

%package devel
Summary: Imath is library of 2D and 3D vector, matrix, and math operations for graphics
Group: Development/C++
Conflicts: ilmbase-devel

%description devel
Imath is a basic, light-weight, and efficient C++ representation of
2D and 3D vectors and matrices and other simple but useful mathematical
objects, functions, and data types common in computer graphics applications,
including the "half" 16-bit floating-point type.

Imath also includes optional python bindings for all types and functions,
including optimized implementations of vector and matrix arrays.

%package doc
Summary: Documentation for Imath
Group: Documentation
BuildArch: noarch

%description doc
Imath is a basic, light-weight, and efficient C++ representation of
2D and 3D vectors and matrices and other simple but useful mathematical
objects, functions, and data types common in computer graphics applications,
including the "half" 16-bit floating-point type.

Imath also includes optional python bindings for all types and functions,
including optimized implementations of vector and matrix arrays.

This package contains documentation for Imath.

%package -n python3-module-%lname
Summary: Imath python3 module
Group: Development/Python3

%description -n python3-module-%lname
Imath also includes optional python bindings for all types and functions,
including optimized implementations of vector and matrix arrays.

%package -n python3-module-%lname-devel
Summary: Imath python3 module
Group: Development/Python3

%description -n python3-module-%lname-devel
Imath also includes optional python bindings for all types and functions,
including optimized implementations of vector and matrix arrays

%prep
%setup

%build
%cmake \
    -DPYTHON:BOOL=ON \
    -DDOCS=ON

%cmake_build

%install
%cmake_install

%files
%_libdir/libImath*.so.%libsover
%_libdir/libImath*.so.%libsover.*

%files devel
%_includedir/Imath/Imath*.h
%_includedir/Imath/half*.h
%_pkgconfigdir/Imath.pc
%_libdir/cmake/Imath/*.cmake
%_libdir/libImath*.so

%files doc
%doc %_defaultdocdir/Imath

%files -n python3-module-%lname
%python3_sitelibdir/*.so
%_libdir/libPy*.so.*

%files -n python3-module-%lname-devel
%_libdir/libPy*.so
%_pkgconfigdir/PyImath.pc
%_includedir/Imath/Py*.h

%changelog
* Mon Jan 23 2023 Alexander Burmatov <thatman@altlinux.org> 3.1.6-alt1
- Initial build for Sisyphus.
