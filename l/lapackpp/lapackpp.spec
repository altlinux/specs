Name: lapackpp
Version: 2.5.4
Release: alt1.svn20110615
Summary: LAPACK++ is a library for high performance linear algebra computations
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://lapackpp.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://lapackpp.svn.sourceforge.net/svnroot/lapackpp/lapackpp/trunk
Source: %name-%version.tar.gz

BuildPreReq: gcc-fortran liblapack-goto-devel gcc-c++
BuildPreReq: doxygen graphviz

%description
LAPACK++ is a library for high performance linear algebra computations.
This version includes support for solving linear systems using LU,
Cholesky, QR matrix factorizations, for real and complex matrices.

%package -n lib%name
Summary: Shared libraries of LAPACK++
Group: System/Libraries

%description -n lib%name
LAPACK++ is a library for high performance linear algebra computations.
This version includes support for solving linear systems using LU,
Cholesky, QR matrix factorizations, for real and complex matrices.

This package contains shared libraries of LAPACK++.

%package -n lib%name-devel
Summary: Development files of LAPACK++
Group: Development/C++
Requires: lib%name = %version-%release
Requires: liblapack-goto-devel

%description -n lib%name-devel
LAPACK++ is a library for high performance linear algebra computations.
This version includes support for solving linear systems using LU,
Cholesky, QR matrix factorizations, for real and complex matrices.

This package contains development files of LAPACK++.

%package -n lib%name-devel-doc
Summary: Documentation for LAPACK++
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
LAPACK++ is a library for high performance linear algebra computations.
This version includes support for solving linear systems using LU,
Cholesky, QR matrix factorizations, for real and complex matrices.

This package contains development documentation for LAPACK++.

%prep
%setup

%build
./autogen.sh
%configure \
	--with-lapackpp-prefix=%prefix \
	--with-blas=goto2
%make_build

%make_build -C testing tCmplxSolve tEigSolve tGenSolve tSpdSolve tSymmSolve

doxygen

%install
%makeinstall_std

%check
pushd testing
./lapack++_test
popd

%files -n lib%name
%doc AUTHORS COPYING ChangeLog NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_aclocaldir/*

%files -n lib%name-devel-doc
%doc api-doc/html/*

%changelog
* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt1.svn20110615
- New snapshot

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt1.svn20101110.2
- Built with GotoBLAS2 instead of ATLAS

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt1.svn20101110.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt1.svn20101110
- Version 2.5.4

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt1.svn20100314.1
- Rebuilt for soname set-versions

* Fri Sep 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt1.svn20100314
- Initial build for Sisyphus

