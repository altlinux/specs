%define somver 0
%define sover %somver.2.0
Name: sparskit
Version: 2.0
Release: alt6
Summary: A basic tool-kit for sparse matrix computations (Version 2)
License: LGPL
Group: Sciences/Mathematics
Url: http://www-users.cs.umn.edu/~saad/software/SPARSKIT/sparskit.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www-users.cs.umn.edu/~saad/software/SPARSKIT/SPARSKIT2.tar.gz
Source1: funcs.f

Requires: lib%name = %version-%release
BuildPreReq: gcc-fortran liblapack-goto-devel

%description
SPARSKIT is a package of FORTRAN subroutines for working with sparse
matrices. It includes general sparse matrix manipulation routines as
well as a few iterative solvers.

%package -n lib%name
Summary: Shared library of SPARSKIT (sparse matrix toolkit)
Group: System/Libraries

%description -n lib%name
SPARSKIT is a package of FORTRAN subroutines for working with sparse
matrices. It includes general sparse matrix manipulation routines as
well as a few iterative solvers.

This package contains shared library of SPARSKIT.

%package -n lib%name-devel
Summary: Development files of SPARSKIT (sparse matrix toolkit)
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
SPARSKIT is a package of FORTRAN subroutines for working with sparse
matrices. It includes general sparse matrix manipulation routines as
well as a few iterative solvers.

This package contains development files of SPARSKIT.

%package -n lib%name-devel-static
Summary: Static library of SPARSKIT (sparse matrix toolkit)
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
SPARSKIT is a package of FORTRAN subroutines for working with sparse
matrices. It includes general sparse matrix manipulation routines as
well as a few iterative solvers.

This package contains static library of SPARSKIT.

%package -n lib%name-devel-doc
Summary: Documentation for SPARSKIT (sparse matrix toolkit)
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
SPARSKIT is a package of FORTRAN subroutines for working with sparse
matrices. It includes general sparse matrix manipulation routines as
well as a few iterative solvers.

This package contains development documentation for SPARSKIT.

%prep
%setup
sed -i 's|@SOMVER@|%somver|g' makefile
sed -i 's|@SOVER@|%sover|g' makefile
tar -cf src.tar $(find ./ -type f|egrep -v 'DOC\/')
install -p -m644 %SOURCE1 .

%build
%make funcs.o
%make_build all
./dotests

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_docdir/lib%name-devel/sources

install -m755 $(find ./ -name '*.ex') %buildroot%_bindir
chmod -x libskit.*
cp -P libskit.* %buildroot%_libdir/
install -p -m644 DOC/* %buildroot%_docdir/lib%name-devel

pushd %buildroot%_docdir/lib%name-devel/sources
tar -xf $OLDPWD/src.tar
popd

%files
%doc LGPL README logfile
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%changelog
* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt6
- Rebuilt with GotoBLAS2 1.13-alt3

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt5
- Built with GotoBLAS2 instead of ATLAS

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt4
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt3
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Rebuilt for soname set-versions

* Sun Oct 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

