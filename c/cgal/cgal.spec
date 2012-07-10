%define somver 9
%define sover %somver.0.0
Name: cgal
Version: 4.0.2
Release: alt1
Summary: Easy access to efficient and reliable geometric algorithms
License: Free for non-commertial using
Group: Sciences/Mathematics
Url: http://www.cgal.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: https://gforge.inria.fr/frs/download.php/27641/CGAL-%version.tar.gz
Source1: https://gforge.inria.fr/frs/download.php/31180/CGAL-4.0.2-doc_html.tar.gz
Source2: https://gforge.inria.fr/frs/download.php/27646/cgal_manual.pdf
Source4: cmk.txt
Source5: %name.pc

Requires: lib%name = %version-%release

BuildPreReq: gcc-c++ gcc-fortran cmake libqt4-devel qt4-devel
BuildPreReq: boost-devel libgmp-devel libgmpxx-devel
BuildPreReq: libGLU-devel libGL-devel libmpfr-devel
BuildPreReq: zlib-devel qt3-devel libX11 phonon-devel
BuildPreReq: liblapack-devel libtaucs-devel

%description
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

%package -n lib%name
Summary: Shared libraries of CGAL
Group: System/Libraries

%description -n lib%name
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

This Package contains shared libraries of CGAL.

%package -n lib%name-qt3
Summary: Shared libraries of CGAL (Qt3 interface)
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-qt3
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

This Package contains shared libraries of CGAL (Qt3 interface).

%package -n lib%name-qt4
Summary: Shared libraries of CGAL (Qt4 interface)
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-qt4
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

This Package contains shared libraries of CGAL (Qt4 interface).

%package -n lib%name-devel
Summary: Development files of CGAL
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

This Package contains developemnt files of CGAL.

%package -n lib%name-qt3-devel
Summary: Development files of CGAL (Qt3 interface)
Group: Development/C++
Requires: lib%name-devel = %version-%release
Requires: lib%name-qt3 = %version-%release

%description -n lib%name-qt3-devel
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

This Package contains developemnt files of CGAL (Qt3 interface).

%package -n lib%name-qt4-devel
Summary: Development files of CGAL (Qt4 interface)
Group: Development/C++
Requires: lib%name-devel = %version-%release
Requires: lib%name-qt4 = %version-%release

%description -n lib%name-qt4-devel
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

This Package contains developemnt files of CGAL (Qt4 interface).

%package devel-doc
Summary: Documentation for CGAL
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

Thid package contains development documentation for CGAL.

%prep
%setup
install -p -m644 %SOURCE1 %SOURCE2 %SOURCE4 ./
mv cmk.txt CMakeCache.txt

install -p -m644 %SOURCE5 .
sed -i 's|@VERSION@|%version|g' %name.pc
sed -i 's|@LIBDIR@|%_libdir|g' %name.pc

%build
cmake -D CMAKE_INSTALL_PREFIX=%prefix .
%make_build VERBOSE=1
#make_build -C demo
#make -C examples


%install
install -d %buildroot%_docdir/%name
%makeinstall_std

cp -fR doc_html %buildroot%_docdir/%name
install -d %buildroot%_docdir/%name
install -p -m644 %SOURCE2 %buildroot/%_docdir/%name

pushd %buildroot%_docdir/%name
tar -xf %SOURCE1
popd

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

install -d %buildroot%_pkgconfigdir
install -p -m644 %name.pc %buildroot%_pkgconfigdir

%files
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*_Qt?.so.*

%files -n lib%name-qt3
%_libdir/*_Qt3.so.*

%files -n lib%name-qt4
%_libdir/*_Qt4.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%exclude %_libdir/*_Qt?.so
%_libdir/CGAL
%_pkgconfigdir/*

%files -n lib%name-qt3-devel
%_libdir/*_Qt3.so

%files -n lib%name-qt4-devel
%_libdir/*_Qt4.so

%files devel-doc
%doc AUTHORS CHANGES* LICENSE* README examples
%doc %_docdir/%{name}*

%changelog
* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt5
- Rebuilt with new GMP

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt4
- Rebuilt with Boost 1.49.0

* Mon Mar 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3
- Version 4.0 (release)

* Fri Feb 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2.beta1
- Built without OSMesa

* Mon Feb 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.beta1
- Version 4.0-beta1

* Thu Dec 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt2
- Version 3.9 (release), thnx iv@

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt1.beta1
- Version 3.9-beta1

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt2
- Rebuilt with Boost 1.47.0

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt1
- Version 3.8

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt6
- Built with GotoBLAS2 instead of ATLAS

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt5
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt4
- Rebuilt with Boost 1.46.1

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt3
- Rebuilt for debuginfo

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt2
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt1
- Version 3.7

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6-alt1
- Version 3.6

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt3
- Rebuilt with new Boost

* Thu Dec 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt2
- Add pkg-config file

* Thu Dec 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt0.M51.1
- port into branch 5.1

* Thu Dec 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1
- Initial build for Sisyphus

