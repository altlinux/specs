%define oname Csdp
Name: Coin%oname
Version: 6.1.1
Release: alt1.svn20101110.3
Summary: A C Library for Semidefinite Programming
License: CPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/Csdp
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Csdp/trunk
Source: %oname-%version.tar.gz

BuildPreReq: gcc-fortran libgomp-devel
BuildPreReq: liblapack-goto-devel

Requires: lib%name = %version-%release

%description
CSDP is a library of routines that implements a predictor corrector
variant of the semidefinite programming algorithm of Helmberg, Rendl,
Vanderbei, and Wolkowicz. The main advantages of this code are that it
is written to be used as a callable subroutine, it is written in C for
efficiency, the code runs in parallel on shared memory multi-processor
systems, and it makes effective use of sparsity in the constraint
matrices.

%package -n lib%name
Summary: Shared libraries of COIN-OR CSDP
Group: System/Libraries
Conflicts: libmpeg4ip

%description -n lib%name
CSDP is a library of routines that implements a predictor corrector
variant of the semidefinite programming algorithm of Helmberg, Rendl,
Vanderbei, and Wolkowicz. The main advantages of this code are that it
is written to be used as a callable subroutine, it is written in C for
efficiency, the code runs in parallel on shared memory multi-processor
systems, and it makes effective use of sparsity in the constraint
matrices.

This package contains shared libraries of COIN-OR CSDP.

%package -n lib%name-devel
Summary: Development files of COIN-OR CSDP
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: libsdp-devel
Conflicts: libmpeg4ip-devel

%description -n lib%name-devel
CSDP is a library of routines that implements a predictor corrector
variant of the semidefinite programming algorithm of Helmberg, Rendl,
Vanderbei, and Wolkowicz. The main advantages of this code are that it
is written to be used as a callable subroutine, it is written in C for
efficiency, the code runs in parallel on shared memory multi-processor
systems, and it makes effective use of sparsity in the constraint
matrices.

This package contains development files of COIN-OR CSDP.

%package example
Summary: Example for COIN-OR CSDP
Group: Sciences/Mathematics
Requires: lib%name = %version-%release

%description example
CSDP is a library of routines that implements a predictor corrector
variant of the semidefinite programming algorithm of Helmberg, Rendl,
Vanderbei, and Wolkowicz. The main advantages of this code are that it
is written to be used as a callable subroutine, it is written in C for
efficiency, the code runs in parallel on shared memory multi-processor
systems, and it makes effective use of sparsity in the constraint
matrices.

This package contains example for COIN-OR CSDP.

%package docs
Summary: Documentation for COIN-OR CSDP
Group: Documentation
BuildArch: noarch

%description docs
CSDP is a library of routines that implements a predictor corrector
variant of the semidefinite programming algorithm of Helmberg, Rendl,
Vanderbei, and Wolkowicz. The main advantages of this code are that it
is written to be used as a callable subroutine, it is written in C for
efficiency, the code runs in parallel on shared memory multi-processor
systems, and it makes effective use of sparsity in the constraint
matrices.

This package contains documentation for COIN-OR CSDP.

%prep
%setup

%ifarch x86_64
ADDFLAG=-DBIT64
%endif
ADDFLAG="$ADDFLAG -I%_includedir/gotoblas -DXDOUBLE"
sed -i "s|@ADDFLAG@|$ADDFLAG|" */Makefile

%build
%make_build

export LD_LIBRARY_PATH=$PWD/lib
#make_build unitTest

%install
%makeinstall_std LIBDIR=%_libdir

mv %buildroot%_bindir/theta %buildroot%_bindir/theta.%oname

%files
%doc AUTHORS LICENSE README
%_bindir/*
%exclude %_bindir/csdp-example

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files docs
%doc doc/*.pdf

%files example
%doc example/*.c example/Makefile
%_bindir/csdp-example

%changelog
* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.svn20101110.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.svn20101110.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.svn20101110.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.svn20101110
- New snapshot

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.svn20100702.4
- Rebuilt for soname set-versions

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.svn20100702.3
- Fixed underlinking of libraries

* Tue Sep 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.svn20100702.2
- Added explicit conflict with libmpeg4ip

* Mon Sep 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.svn20100702.1
- Avoid conflict with dsdp

* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.svn20100702
- Initial build for Sisyphus

