%define oname gotoblas
%define rev 0

Name: %{oname}2
Version: 1.13
Release: alt7
Summary: The fastest implementations of the Basic Linear Algebra Subroutines
License: BSD
Group: Sciences/Mathematics
Url: http://www.tacc.utexas.edu/tacc-projects/gotoblas2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: GotoBLAS2-%{version}_bsd.tar

%set_gcc_version 4.5
BuildPreReq: gcc4.5-fortran

%description
GotoBLAS2 has been released by the Texas Advanced Computing Center as
open source software under the BSD license. This product is no longer
under active development by TACC, but it is being made available to the
community to use, study, and extend. GotoBLAS2 uses new algorithms and
memory techniques for optimal performance of the BLAS routines. The
changes in this final version target new architecture features in
microprocessors and interprocessor communication techniques; also, NUMA
controls enhance multi-threaded execution of BLAS routines on node.

%package -n lib%name
Summary: Shared library of GotoBLAS2
Group: System/Libraries

%description -n lib%name
GotoBLAS2 has been released by the Texas Advanced Computing Center as
open source software under the BSD license. This product is no longer
under active development by TACC, but it is being made available to the
community to use, study, and extend. GotoBLAS2 uses new algorithms and
memory techniques for optimal performance of the BLAS routines. The
changes in this final version target new architecture features in
microprocessors and interprocessor communication techniques; also, NUMA
controls enhance multi-threaded execution of BLAS routines on node.

This package contains shared library of GotoBLAS2.

%package -n lib%name-devel
Summary: Development files of GotoBLAS2
Group: Development/Other
Requires: lib%name = %version-%release
Provides: lib%oname-devel = %version-%release

%description -n lib%name-devel
GotoBLAS2 has been released by the Texas Advanced Computing Center as
open source software under the BSD license. This product is no longer
under active development by TACC, but it is being made available to the
community to use, study, and extend. GotoBLAS2 uses new algorithms and
memory techniques for optimal performance of the BLAS routines. The
changes in this final version target new architecture features in
microprocessors and interprocessor communication techniques; also, NUMA
controls enhance multi-threaded execution of BLAS routines on node.

This package contains development files of GotoBLAS2.

%prep
%setup

# more verbose
sed -i "s<-ln <ln <" Makefile

# fix path to libpthread.so*
sed -i 's|@LIB@|%_lib|g' c_check

# tune soname version
sed -i 's|@REV@|%rev|g' exports/Makefile

%build
FLAGS="%optflags %optflags_shared"
%ifarch x86_64
	BITS=64
%else
	BITS=32
%endif

FC="gfortran $FLAGS" F77="g77 $FLAGS" F_COMPILER="gfortran $FLAGS" \
	C_COMPILER="gcc $FLAGS" \
	%make_build SMP=1 \
%ifnarch x86_64
		STATIC_ALLOCATION=1 \
%else
		BINARY64=1 \
%endif
		BINARY=$BITS \
		ALLOC_HUGETLB=1 \
		DYNAMIC_ARCH=1

%install
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%oname

install -m644 *-r*.so %buildroot%_libdir
pushd %buildroot%_libdir
ln -s *-r*.so libgoto2.so.%rev
ln -s libgoto2.so.%rev libgoto2.so
popd

sed -i 's|^//\(include.*\)|#\1|' cblas.h
install -p -m644 *.h %buildroot%_includedir/%oname

%files -n lib%name
%doc 0*
%_libdir/*-r*.so
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%exclude %_libdir/*-r*.so
%_includedir/*

%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt7
- Fixed build

* Tue Apr 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt6
- Fixed cblas.h

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt5
- Use pthread instead of OpenMP (inspired by mike@)

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt4
- Rebuilt with multiarch support (thnx led@ and mike@)

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt3
- Rebuilt for BARCELONA cpu (x86_64)

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt2
- Set soname for library

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt1
- Initial build for Sisyphus (thnx mike@)

