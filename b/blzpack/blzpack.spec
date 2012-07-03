%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.4.0
Name: blzpack
Version: 04.00
Release: alt9
Summary: Block LancZos PACKage
License: BSD
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~osni/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://crd.lbl.gov/~osni/Codes/blzpack.zip

BuildPreReq: liblapack-devel libparmetis-devel
BuildPreReq: %mpiimpl-devel unzip

%description
BLZPACK (for Block LancZos PACKage) is a set of subprograms written
in standard Fortran 77 intended for the computation of eigenvalues
eig and eigenvectors (x) of the "standard" eigenvalue problem

       (A)*(x) - eig*(x) = (0)

or of the "generalized" eigenvalue problem

       (A)*(x) - eig*(B)*(x) = (0)

where (A) and (B) are N x N real, sparse, symmetric matrices, eig an
eigenvalue, and (x) an eigenvector. It is assumed that there exists 
a linear combination of (A) and (B) which is positive definite to
guarantee that all eigenvalues are real.

%package -n lib%name
Summary: Shared library of BLZPACK
Group: System/Libraries

%description -n lib%name
BLZPACK (for Block LancZos PACKage) is a set of subprograms written
in standard Fortran 77 intended for the computation of eigenvalues
eig and eigenvectors (x) of the "standard" eigenvalue problem

       (A)*(x) - eig*(x) = (0)

or of the "generalized" eigenvalue problem

       (A)*(x) - eig*(B)*(x) = (0)

where (A) and (B) are N x N real, sparse, symmetric matrices, eig an
eigenvalue, and (x) an eigenvector. It is assumed that there exists 
a linear combination of (A) and (B) which is positive definite to
guarantee that all eigenvalues are real.

This package contains shared library of BLZPACK.

%package -n lib%name-devel
Summary: Development library of BLZPACK
Group: Development/Other
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
BLZPACK (for Block LancZos PACKage) is a set of subprograms written
in standard Fortran 77 intended for the computation of eigenvalues
eig and eigenvectors (x) of the "standard" eigenvalue problem

       (A)*(x) - eig*(x) = (0)

or of the "generalized" eigenvalue problem

       (A)*(x) - eig*(B)*(x) = (0)

where (A) and (B) are N x N real, sparse, symmetric matrices, eig an
eigenvalue, and (x) an eigenvector. It is assumed that there exists 
a linear combination of (A) and (B) which is positive definite to
guarantee that all eigenvalues are real.

This package contains development library of BLZPACK.

%package examples
Summary: Examples for BLZPACK
Group: Development/Documentation
BuildArch: noarch

%description examples
BLZPACK (for Block LancZos PACKage) is a set of subprograms written
in standard Fortran 77 intended for the computation of eigenvalues
eig and eigenvectors (x) of the "standard" eigenvalue problem

       (A)*(x) - eig*(x) = (0)

or of the "generalized" eigenvalue problem

       (A)*(x) - eig*(B)*(x) = (0)

where (A) and (B) are N x N real, sparse, symmetric matrices, eig an
eigenvalue, and (x) an eigenvector. It is assumed that there exists 
a linear combination of (A) and (B) which is positive definite to
guarantee that all eigenvalues are real.

This package contains examples for BLZPACK.

%package -n lib%name-devel-doc
Summary: Documentation for BLZPACK
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
BLZPACK (for Block LancZos PACKage) is a set of subprograms written
in standard Fortran 77 intended for the computation of eigenvalues
eig and eigenvectors (x) of the "standard" eigenvalue problem

       (A)*(x) - eig*(x) = (0)

or of the "generalized" eigenvalue problem

       (A)*(x) - eig*(B)*(x) = (0)

where (A) and (B) are N x N real, sparse, symmetric matrices, eig an
eigenvalue, and (x) an eigenvector. It is assumed that there exists 
a linear combination of (A) and (B) which is positive definite to
guarantee that all eigenvalues are real.

This package contains development documentation for BLZPACK.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir
./creator -mpi

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_libdir
install -d %buildroot%_docdir/lib%name-%version/examples

install -m644 lib/*.a %buildroot%_libdir
mv doc/README doc/README.doc
install -p -m644 README license.txt doc/* \
	%buildroot%_docdir/lib%name-%version
cp -fR drv/* %buildroot%_docdir/lib%name-%version/examples

# shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../lib%name.a
mpif77 -shared * \
	-Wl,-rpath,%mpidir/lib -lgoto2 \
	-Wl,-soname,lib%name.so.%somver -o ../lib%name.so.%sover
rm -f *
popd
rmdir tmp
ln -s lib%name.so.%sover lib%name.so.%somver
ln -s lib%name.so.%somver lib%name.so
popd

%files
%doc %dir %_docdir/lib%name-%version
%doc %_docdir/lib%name-%version/README
%doc %_docdir/lib%name-%version/license.txt

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

%files -n lib%name-devel-doc
%doc %dir %_docdir/lib%name-%version
%doc %_docdir/lib%name-%version/*
%exclude %_docdir/lib%name-%version/README
%exclude %_docdir/lib%name-%version/license.txt
%exclude %_docdir/lib%name-%version/examples

%files examples
%doc %dir %_docdir/lib%name-%version
%doc %_docdir/lib%name-%version/examples

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt9
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt8
- Fixed RPATH

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt7
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt6
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt5
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt4
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt3
- Fixed overlinking of libraries

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt2
- Added shared library

* Sun Jul 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt1
- Initial build for Sisyphus

