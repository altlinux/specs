%define sover 0

Name: liblinpack
Version: 20090217
Release: alt5
Summary: Analyze and solve linear equations and linear least-squares probles
License: Free
Group: System/Libraries
Url: http://www.netlib.org/linpack/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-fortran liblapack-goto-devel

%description
LINPACK is a collection of Fortran subroutines that analyze and
solve linear equations and linear least-squares probles.  The
package solves linear systems whose matrices are general, banded,
symmetric indefinite, symmetric positive definite, triangular,
and tridiagonal square.  In addition, the package computes
the QR and singular value decompositions of rectangular matrices
and applies them to least-squares problems.  LINPACK uses
column-oriented algorithms to increase efficiency by preserving
locality of reference.

LINPACK was designed for supercomputers in use in the 1970s and
early 1980s.  LINPACK has been largely superceded by LAPACK
which has been designed to run efficiently on shared-memory, vector
supercomputers.

%package devel
Summary: Development files of LINPACK
Group: Development/Other
Requires: %name = %version-%release

%description devel
LINPACK is a collection of Fortran subroutines that analyze and
solve linear equations and linear least-squares probles.  The
package solves linear systems whose matrices are general, banded,
symmetric indefinite, symmetric positive definite, triangular,
and tridiagonal square.  In addition, the package computes
the QR and singular value decompositions of rectangular matrices
and applies them to least-squares problems.  LINPACK uses
column-oriented algorithms to increase efficiency by preserving
locality of reference.

This package contains development files of LINPACK.

%package devel-static
Summary: Static library of LINPACK
Group: Development/Other
Requires: %name-devel = %version-%release

%description devel-static
LINPACK is a collection of Fortran subroutines that analyze and
solve linear equations and linear least-squares probles.  The
package solves linear systems whose matrices are general, banded,
symmetric indefinite, symmetric positive definite, triangular,
and tridiagonal square.  In addition, the package computes
the QR and singular value decompositions of rectangular matrices
and applies them to least-squares problems.  LINPACK uses
column-oriented algorithms to increase efficiency by preserving
locality of reference.

This package contains static library of LINPACK.

%prep
%setup

%build
%make_build

%install
install -d %buildroot%_libdir
install -m644 *.a %buildroot%_libdir

mkdir %buildroot%_libdir/tmp
pushd %buildroot%_libdir/tmp
for i in %name; do
	ar x ../$i.a
	g77 -shared * -Wl,-soname,$i.so.%sover -o ../$i.so.%sover \
		-llapack -lgoto2
	ln -s $i.so.%sover ../$i.so
	rm -f *
done
popd
rmdir %buildroot%_libdir/tmp

%files
%doc comment index-2009-02-17 permission readme
%_libdir/*.so.*

%files devel
%_libdir/*.so

#files devel-static
#_libdir/*.a

%changelog
* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090217-alt5
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090217-alt4
- Rebuilt for debuginfo

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090217-alt3
- Rebuilt for soname set-versions

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090217-alt2
- Added shared library

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090217-alt1
- Initial build for Sisyphus
