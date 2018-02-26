Name: taucs
Version: 2.2
Release: alt9
Summary: C library of sparse linear solvers
License: MIT
Group: Sciences/Mathematics
Url: http://www.tau.ac.il/~stoledo/taucs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: liblapack-goto-devel libmetis-devel
BuildPreReq: gcc-fortran

%description
TAUCS is a C library of sparse linear solvers.

Features: Multifrontal Supernodal Cholesky Factorization, Left-Looking
Supernodal Cholesky Factorization, Drop-Tolerance Incomplete-Cholesky
Factorization, LDL^T Factorization, Out-of-Core, Left-Looking Supernodal
Sparse Cholesky Factorization, Out-of-Core Sparse LU with Partial
Pivoting Factor and Solve, Ordering Codes and Interfaces to Existing
Ordering Codes, Matrix Operations, Matrix Input/Output, Matrix
Generators, Iterative Solvers, Vaidya's Preconditioners, Recursive
Vaidya's Preconditioners, Multilevel-Support-Graph Preconditioners.

%package doc
Summary: Documentation for TAUCS
Group: Documentation
BuildArch: noarch

%description doc
TAUCS is a C library of sparse linear solvers.

This package documentation for TAUCS.

%package -n lib%name
Summary: Shared library of TAUCS
Group: System/Libraries

%description -n lib%name
TAUCS is a C library of sparse linear solvers.

This package contains shared library of TAUCS.

%package -n lib%name-devel
Summary: Development files of TAUCS
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
TAUCS is a C library of sparse linear solvers.

This package contains development files of TAUCS.

%package -n lib%name-devel-static
Summary: Static library of TAUCS
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
TAUCS is a C library of sparse linear solvers.

This package contains static library of TAUCS.

%prep
%setup
rm -fR $(find ./ -name CVS) external/lib
rm -f progs/taucs_cilk_test.c

%build
./configure
%make_build
rm -fR bin
mkdir -p lib/linux/tmp
pushd lib/linux/tmp
ar x ../lib%name.a
g77 -shared * \
	-lmetis -llapack -lgoto2 \
	-Wl,-soname,lib%name.so.0 -o ../lib%name.so.0.0.0
ln -s lib%name.so.0.0.0 ../lib%name.so.0
ln -s lib%name.so.0 ../lib%name.so
rm -f *
popd
rmdir lib/linux/tmp
%make_build

%install
install -d %buildroot%_bindir
for i in direct iter taucs_run; do
	install -m755 bin/linux/$i %buildroot%_bindir
done

install -d %buildroot%_libdir
cp -P lib/linux/* %buildroot%_libdir/

install -d %buildroot%_includedir
install -p -m644 src/*.h build/linux/*.h %buildroot%_includedir

install -d %buildroot%_docdir/%name
install -p -m644 doc/%name.pdf %buildroot%_docdir/%name

%files
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files doc
%_docdir/%name

%changelog
* Sat Sep 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt9
- Rebuilt with metis 5.0.1
- Disabled devel-static package

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt8
- Rebuilt with GotoBLAS2 1.13-alt3

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt7
- Built with GotoBLAS2 instead of ATLAS

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt6
- Rebuilt with metis 4.0.1-alt9

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt5
- Rebuilt for debuginfo

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt4
- Fixed underlinking of libraries

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt3
- Rebuilt with reformed Metis

* Sat Oct 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt2
- Fixed headers for gcc 4.4

* Sun Sep 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1
- Initial build for Sisyphus

