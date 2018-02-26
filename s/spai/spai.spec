%define somver 0
%define sover %somver.3.2
Name: spai
Version: 3.2
Release: alt6
Summary: SParse Approximate Inverse Preconditioner
License: GPL v2
Group: Sciences/Mathematics
Url: http://www.computational.unibas.ch/software/spai/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.computational.unibas.ch/software/spai/spai-3.2.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: gcc-fortran openmpi-devel
BuildPreReq: liblapack-goto-devel

%description
Given a sparse matrix A the SPAI Algorithm computes a sparse approximate inverse
M by minimizing || AM - I || in the Frobenius norm. The approximate inverse is
computed explicitly and can then be applied as a preconditioner to an iterative
method. The sparsity pattern of the approximate inverse is either fixed a priori
or captured automatically:

  * Fixed sparsity: The sparsity pattern of M is either banded or a subset of
  the sparsity pattern of A.
  * Adaptive sparsity: The algorithm proceeds until the 2-norm of each column of
  AM-I is less than eps. By varying eps the user controls the quality and the
  cost of computing the preconditioner. Usually the optimal eps lies between 0.5
  and 0.7.

A very sparse preconditioner is very cheap to compute but may not lead to much
improvement, while if M becomes rather dense it becomes too expensive to
compute. The optimal preconditioner lies between these two extremes and is
problem and computer architecture dependent.

The approximate inverse M can also be used as a robust (parallel) smoother for
(algebraic) multi-grid methods.

%package -n lib%name
Summary: Shared library of SPAI
Group: System/Libraries

%description -n lib%name
Given a sparse matrix A the SPAI Algorithm computes a sparse approximate inverse
M by minimizing || AM - I || in the Frobenius norm. The approximate inverse is
computed explicitly and can then be applied as a preconditioner to an iterative
method.

This package contains shared library of SPAI.

%package -n lib%name-devel
Summary: Development files of SPAI
Group: Development/Other
Requires: %name = %version-%release
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
Given a sparse matrix A the SPAI Algorithm computes a sparse approximate inverse
M by minimizing || AM - I || in the Frobenius norm. The approximate inverse is
computed explicitly and can then be applied as a preconditioner to an iterative
method.

This package contains development files of SPAI.

%package -n lib%name-devel-static
Summary: Static library of SPAI
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
Given a sparse matrix A the SPAI Algorithm computes a sparse approximate inverse
M by minimizing || AM - I || in the Frobenius norm. The approximate inverse is
computed explicitly and can then be applied as a preconditioner to an iterative
method.

This package contains static library of SPAI.

%package -n lib%name-devel-doc
Summary: Documentation for SPAI
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Given a sparse matrix A the SPAI Algorithm computes a sparse approximate inverse
M by minimizing || AM - I || in the Frobenius norm. The approximate inverse is
computed explicitly and can then be applied as a preconditioner to an iterative
method.

This package contains development documentation for SPAI.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure \
	--with-blas="-lgoto2" \
	--with-lapack="-llapack" \
	--with-mpi
%make_build

%install
%makeinstall_std

mv %buildroot%_bindir/convert %buildroot%_bindir/%name-convert

install -d %buildroot%_datadir/%name
install -p -m644 data/*.mm %buildroot%_datadir/%name

install -d %buildroot%_includedir/%name
install -p -m644 src/*.h *.h %buildroot%_includedir/%name

# shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../lib%name.a
gcc -shared * -llapack -lgoto2 -lm \
	-Wl,-soname,lib%name.so.%somver -o ../lib%name.so.%sover
rm -f *
popd
rmdir tmp
ln -s lib%name.so.%sover lib%name.so.%somver
ln -s lib%name.so.%somver lib%name.so
popd

%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt6
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt5
- Rebuilt for debuginfo

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt4
- Rebuilt for soname set-versions

* Sat Sep 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt3
- Added shared library

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt2
- Rebuild with PIC

* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1
- Initial build for Sisyphus
