%define soname 0
%define oname nlopt

Name: lib%{oname}%soname
Version: 2.9.1
Release: alt2

Summary: Shared library of NLopt (legacy)

License: MIT and LGPLv2
Group: System/Legacy libraries
Url: https://github.com/stevengj/nlopt

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/stevengj/nlopt/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

%description
Legacy shared library libnlopt.so.0 for backward compatibility.
Use libnlopt1 for new development.

%prep
%setup

%build
%cmake \
    -DNLOPT_PYTHON=OFF \
    -DNLOPT_OCTAVE=OFF \
    -DNLOPT_MATLAB=OFF \
    -DNLOPT_GUILE=OFF \
    -DNLOPT_FORTRAN=OFF \
    -DBUILD_SHARED_LIBS=ON \
    %nil
%cmake_build

%install
%cmakeinstall_std
# Keep only the versioned library
rm -rf %buildroot%_includedir
rm -f %buildroot%_libdir/*.so
rm -rf %buildroot%_libdir/cmake
rm -rf %buildroot%_libdir/pkgconfig
rm -rf %buildroot%_man3dir

%files
%_libdir/lib%oname.so.%soname
%_libdir/lib%oname.so.%soname.*

%changelog
* Tue Mar 10 2026 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt2
- rebuild as legacy libnlopt0 (soname 0) per Shared Libs Policy

* Tue Dec 03 2024 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt1
- new version 2.9.1 (with rpmrb script)

* Mon Aug 07 2023 Vitaly Lipatov <lav@altlinux.ru> 2.7.1-alt1
- new version 2.7.1, switched to cmake build, rewrote spec
- no more separate libnlopt_cxx library (libnlopt-cxx subpackage)

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1
- Version 2.4.2

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1
- Version 2.4

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1
- Initial build for Sisyphus
