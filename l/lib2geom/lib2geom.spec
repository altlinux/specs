Name: lib2geom
Version: 20081103
Release: alt1.4

Summary: A robust computational geometry framework for Inkscape

License: LGPL
Group: Development/C
Url: http://lib2geom.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://inkscape.modevia.com/2geom/src/%name%version.tar.bz2
Patch0: %name-no-rpath.patch
Patch1: %name-20081103-alt-gc4.6.patch

# Automatically added by buildreq on Mon Mar 31 2008
BuildRequires: boost-devel ccmake gcc-c++ libgsl-devel libgtk+2-devel

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
%setup -q -n %name
%patch0 -p2
%patch1 -p2
# fix target lib dir
sed -i "s| lib| %_lib|g" src/2geom/CMakeLists.txt
sed -i 's,^SET(CMAKE_CXX_FLAGS ",SET(CMAKE_CXX_FLAGS "%optflags -fno-inline ,' CMakeLists.txt

%build
cmake \
	-D 2GEOM_BUILD_SHARED=ON \
	-D CMAKE_INSTALL_PREFIX=%_prefix \
	-D MAKE_SKIP_RPATH:BOOL=OFF \
	.
%make_build

%install
%makeinstall_std

%files
%doc HACKING.txt TODO
%_libdir/lib2geom.so.3.0

%files devel
%_includedir/2geom-0.3/
%_pkgconfigdir/*
%_libdir/lib2geom.so

%changelog
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

