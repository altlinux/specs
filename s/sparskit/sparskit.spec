%define somver 0
%define sover %somver.2.0

Name: sparskit
Version: 2.0.20190610
Release: alt3
Summary: A basic tool-kit for sparse matrix computations (Version 2)
License: LGPL
Group: Sciences/Mathematics
Url: http://www-users.cs.umn.edu/~saad/software/SPARSKIT/

Source: %name-%version.tar
Source1: funcs.f
Patch1:  0001-makefile.patch
Patch2:  0002-skip-ccn.patch

Requires: lib%name = %version-%release
BuildPreReq: gcc-fortran liblapack-devel

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
%patch1 -p2
%patch2 -p2
sed -i 's|@SOMVER@|%somver|g' makefile
sed -i 's|@SOVER@|%sover|g' makefile
#tar -cf src.tar $(find ./ -type f|egrep -v 'DOC\/')
install -p -m644 %SOURCE1 .

%build

%make_build all
./dotests

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_docdir/lib%name-devel
##tar -xf $OLDPWD/src.tar

cp -P libskit.* %buildroot%_libdir/
install -p -m644 DOC/* %buildroot%_docdir/lib%name-devel



%files -n lib%name
%doc LGPL README logfile
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

%files -n lib%name-devel-doc
%_docdir/lib%name-devel


%changelog
* Mon Jan 18 2021 Vladislav Zavjalov <slazav@altlinux.org> 2.0.20190610-alt3
- 0002-skip-ccn.patch: skip ORDERINGS/ccn.f (fix build with GCC10,
  recommendation by Yousef Saad, upstream).

* Fri Oct 16 2020 Vladislav Zavjalov <slazav@altlinux.org> 2.0.20190610-alt2
- 0001-makefile.patch: fix dependencies for parallel build

* Sun Sep 20 2020 Vladislav Zavjalov <slazav@altlinux.org> 2.0.20190610-alt1
- Updated (2019.06.10), use version 2.0.20190610
- Do not pack sources in -doc package
- Do npot pack test programs in /usr/bin (remove sparskit package)
- Extract all Makefile modifications into a seperate patch

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt8
- Updated
- Disabled devel-static package

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt7
- Built with OpenBLAS instead of GotoBLAS2

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

