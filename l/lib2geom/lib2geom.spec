Name: lib2geom
Version: 1.2.2
Release: alt1
Epoch: 1

Summary: Easy to use 2D geometry library in C++
License: LGPLv2
Group: Development/C
Url: https://gitlab.com/inkscape/lib2geom

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://gitlab.com/inkscape/lib2geom/-/archive/%version/lib2geom-%version.tar.bz2
Source: %name-%version.tar

BuildRequires: boost-devel cmake gcc-c++ libdouble-conversion-devel libgsl-devel libgtest-devel libgtk+3-devel

%description
lib2geom (2Geom in private life) was initially a library developed for
Inkscape but will provide a robust computational geometry framework for
any application. It is not a rendering library, instead concentrating
on high level algorithms such as computing arc length.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
This package contains development files required
in development of the %name-based applications.


%prep
%setup
%ifarch %e2k
# lcc 1.25.15 barfs at include/2geom/ord.h:54 as of 1.1
sed -i 's,-Werror=return-type,,' CMakeLists.txt
%endif
# fix target lib dir (NB: looks like there are no CMAKE_CXX_FLAGS there in 1.1)
sed -i "s| lib/| %_lib/|g" CMakeLists.txt
sed -i 's,^SET(CMAKE_CXX_FLAGS ",SET(CMAKE_CXX_FLAGS "%optflags -fno-inline -fpermissive ,' CMakeLists.txt

%build
cmake \
	-D2GEOM_BUILD_SHARED=ON \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_SKIP_RPATH=ON \
	.
%make_build

%install
%makeinstall_std
sed -i "s|/lib$|/%_lib|" %buildroot%_pkgconfigdir/*

%files
%doc README.md NEWS.md
%_libdir/lib2geom.so.*

%files devel
%_includedir/2geom-*/
%_pkgconfigdir/*
%_libdir/lib2geom.so
%_libdir/cmake/2Geom/

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1:1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Tue Jun 08 2021 Michael Shigorin <mike@altlinux.org> 1:1.1-alt1.1
- E2K: ftbfs workaround

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 1:1.1-alt1
- new version (1.1) with rpmgs script

* Thu Feb 14 2019 Ivan Razzhivin <underwit@altlinux.org> 20081103-alt1.6
- GCC8 fix

* Tue Jul 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 20081103-alt1.5
- Fixed build with gcc-6

* Tue Jun 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20081103-alt1.4
- Fixed build with gcc 4.6

* Wed Mar 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 20081103-alt1.3
- rebuilt with refault optflags

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20081103-alt1.2
- Removed bad RPATH

* Fri Apr 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20081103-alt1.1
- Rebuilt for debuginfo

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 20081103-alt1
- new version (20081103)

* Sat May 31 2008 Vitaly Lipatov <lav@altlinux.ru> 20080530-alt1
- new version 20080530 (with rpmrb script)

* Mon Mar 31 2008 Vitaly Lipatov <lav@altlinux.ru> 20080331-alt1
- initial build for ALT Linux Sisyphus

