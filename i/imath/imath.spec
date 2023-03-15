%define lname imath
%define libsover 29
%define libimath lib%lname%libsover
Name: %lname
Version: 3.1.6
Release: alt3

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
Provides: libimath29-devel = %EVR
Obsoletes: libimath29-devel < %EVR

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
Provides: libimath29-doc = %EVR
Obsoletes: libimath29-doc < %EVR

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

%package -n %libimath
Summary: %lname library
Group: System/Libraries
%description -n %libimath
%lname library.


%prep
%setup

%build
%cmake \
    -DPYTHON:BOOL=ON \
    -DDOCS=ON

%cmake_build

%install
%cmake_install

# relax depends on binary files
for f in %buildroot/%_libdir/cmake/Imath/*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

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
* Wed Mar 15 2023 Sergey V Turchin <zerg@altlinux.org> 3.1.6-alt3
- relax depends on binary files

* Tue Mar 14 2023 Sergey V Turchin <zerg@altlinux.org> 3.1.6-alt2
- rename from libimath29

* Mon Jan 23 2023 Alexander Burmatov <thatman@altlinux.org> 3.1.6-alt1
- Initial build for Sisyphus.
