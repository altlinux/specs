%define rev 0

Name: openblas
Version: 0.2.5
Release: alt1.git20121127
Summary: Optimized BLAS library based on GotoBLAS2 1.13 
License: BSD
Group: Sciences/Mathematics
Url: https://github.com/xianyi/OpenBLAS
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://github.com/xianyi/OpenBLAS
Source: %name-%version.tar

#set_gcc_version 4.5
#BuildPreReq: gcc4.5-fortran
BuildPreReq: gcc-fortran

%description
GotoBLAS2 has been released by the Texas Advanced Computing Center as
open source software under the BSD license. This product is no longer
under active development by TACC, but it is being made available to the
community to use, study, and extend. GotoBLAS2 uses new algorithms and
memory techniques for optimal performance of the BLAS routines. The
changes in this final version target new architecture features in
microprocessors and interprocessor communication techniques; also, NUMA
controls enhance multi-threaded execution of BLAS routines on node.

OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD
version. OpenBLAS is an open source project supported by Lab of Parallel
Software and Computational Science, ISCAS.

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

OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD
version. OpenBLAS is an open source project supported by Lab of Parallel
Software and Computational Science, ISCAS.

This package contains shared library of OpenBLAS.

%package -n lib%name-devel
Summary: Development files of GotoBLAS2
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
GotoBLAS2 has been released by the Texas Advanced Computing Center as
open source software under the BSD license. This product is no longer
under active development by TACC, but it is being made available to the
community to use, study, and extend. GotoBLAS2 uses new algorithms and
memory techniques for optimal performance of the BLAS routines. The
changes in this final version target new architecture features in
microprocessors and interprocessor communication techniques; also, NUMA
controls enhance multi-threaded execution of BLAS routines on node.

OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD
version. OpenBLAS is an open source project supported by Lab of Parallel
Software and Computational Science, ISCAS.

This package contains development files of OpenBLAS.

%prep
%setup

# more verbose
sed -i "s<-ln <ln <" Makefile

# fix path to libpthread.so*
sed -i 's|@LIB@|%_lib|g' c_check

# tune soname version
#sed -i 's|@REV@|%rev|g' exports/Makefile

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
		DYNAMIC_ARCH=1 \
		NO_LAPACK=1

%install
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name

install -m644 *-r*.so %buildroot%_libdir
pushd %buildroot%_libdir
ln -s *-r*.so lib%name.so.%rev
ln -s lib%name.so.%rev lib%name.so
popd

sed -i 's|^//\(include.*\)|#\1|' cblas.h
sed -i 's|^#include "common.h"||' cblas.h
install -p -m644 *.h %buildroot%_includedir/%name

%files -n lib%name
%doc README* *.txt
%_libdir/*-r*.so
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%exclude %_libdir/*-r*.so
%_includedir/*

%changelog
* Tue Nov 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20121127
- Version 0.2.5

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

