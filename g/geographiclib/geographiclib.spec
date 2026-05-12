%define _unpackaged_files_terminate_build 1
%define abiversion 26

Name: geographiclib
Version: 2.7
Release: alt2

Summary: Small geodesic and triaxial ellipsoid computation library
License: MIT
Group: Sciences/Geosciences
URL: https://github.com/geographiclib/geographiclib
Vcs: https://github.com/geographiclib/geographiclib.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake automake gcc-c++
BuildRequires: doxygen
BuildRequires: ctest

%description
GeographicLib is a small C++ library for
- geodesic and rhumb line calculations;
- conversions between geographic, UTM, UPS, MGRS, geocentric, and local
cartesian coordinates;
- gravity (e.g., EGM2008) and geomagnetic field (e.g.,WMM2020) calculations;
- computations on a triaxial ellipsoid.

%package -n libgeographiclib-devel
Summary: Development files and libraries for GeographicLib
Group: Development/C++

%description -n libgeographiclib-devel
This package contains headers and libraries for GeographicLib.

%package -n libgeographiclib%abiversion
Summary: Libraries for geographiclib
Group: Development/C++

%description -n libgeographiclib%abiversion
Shared libraries for geographiclib.

%package doc
Summary: Documentation for GeographicLib
Group: Development/Documentation

%description doc
This package contains doxygen-generated html API documentation for the
GeographicLib library.

%prep
%setup
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' CMakeLists.txt
%endif

%build
%cmake -DBUILD_SHARED_LIBS=ON \
       -DBUILD_DOCUMENTATION=ON \
       -DCMAKE_INSTALL_LIBDIR=%_libdir \
       -DCMAKEDIR=%_lib/cmake/GeographicLib \
       -DPKGDIR=%_lib/pkgconfig \
       -DGEOGRAPHICLIB_PRECISION=2 \
       #

%cmake_build
%cmake_build --target testprograms
%cmake_build --target tests

%install
%cmake_install

%check
%ifarch x86_64 aarch64
%ctest
%endif

%files
%doc README.md LICENSE.txt NEWS
%_bindir/Cart3Convert
%_bindir/CartConvert
%_bindir/Conformal3Proj
%_bindir/ConicProj
%_bindir/GeoConvert
%_bindir/Geod3Solve
%_bindir/GeodSolve
%_bindir/GeodesicProj
%_bindir/GeoidEval
%_bindir/Gravity
%_bindir/IntersectTool
%_bindir/MagneticField
%_bindir/Planimeter
%_bindir/RhumbSolve
%_bindir/TransverseMercatorProj
%_sbindir/geographiclib-get-geoids
%_sbindir/geographiclib-get-gravity
%_sbindir/geographiclib-get-magnetic
%_man1dir/*
%_man8dir/*

%files -n libgeographiclib%abiversion
%_libdir/libGeographicLib.so.%abiversion
%_libdir/libGeographicLib.so.%abiversion.2.1

%files -n libgeographiclib-devel
%_includedir/GeographicLib
%_cmakedir/GeographicLib
%_pkgconfigdir/geographiclib.pc
%_libdir/libGeographicLib.so

%files doc
%doc %_defaultdocdir/GeographicLib
%doc %_defaultdocdir/GeographicLib-dev

%changelog
* Tue May 12 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.7-alt2
- e2k build fix

* Tue Jan 13 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2.7-alt1
- Initial build.
