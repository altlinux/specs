Name: lapack
Version: 3.8.0
Release: alt7
Epoch: 1

%define sover 4
%define soname lib%name.so.%sover
%def_without bootstrap

Summary: BLAS and LAPACK Fortran libraries for numerical linear algebra (with GotoBLAS2)
License: BSD
Group: Development/Other
Url: http://www.netlib.org/

Source: %name-%version.tar
Source1: manpages.tar

BuildRequires: cmake gcc-fortran libxblas-devel
%{!?_with_bootstrap:BuildRequires: libsuperlu-devel}
BuildRequires: libopenblas-devel

%package -n lib%name
Summary: BLAS and LAPACK Fortran libraries for numerical linear algebra (with GotoBLAS2)
Group: System/Libraries
Conflicts: lib%name-goto < %epoch:%version-%release
Obsoletes: lib%name-goto < %epoch:%version-%release
Obsoletes: liblapack3

%package -n lib%name-devel
Summary: BLAS and LAPACK Fortran libraries for numerical linear algebra (with GotoBLAS2)
Group: Development/Other
Requires: libopenblas-devel
Requires: lib%name = %epoch:%version-%release
Conflicts: lib%name-goto-devel
Obsoletes: lib%name-goto-devel

%package -n blas-man
Summary: BLAS and LAPACK Fortran libraries for numerical linear algebra (with GotoBLAS2)
Group: Development/Documentation
BuildArch: noarch
Conflicts: blas-man < %epoch:%version-%release
Obsoletes: blas-goto-man

%package -n lapack-man
Summary: BLAS and LAPACK Fortran libraries for numerical linear algebra (with GotoBLAS2)
Group: Development/Documentation
Requires: blas-man = %epoch:%version-%release
BuildArch: noarch
Conflicts: lapack-man < %epoch:%version-%release
Obsoletes: lapack-goto-man

%description
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision.

%description -n lib%name
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision.

%description -n lib%name-devel
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision.

%description -n blas-man
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision.

%description -n lapack-man
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision.

%prep
%setup -a1

export LC_COLLATE=C
ls manpages/blas/man/manl >blas.manpages
ls manpages/man/manl >lapack.manpages
comm -12 blas.manpages lapack.manpages >dup.manpages
(cd manpages/man/manl; xargs -r rm -v -- ) <dup.manpages || exit 1
rm blas.manpages lapack.manpages dup.manpages
rm -fR BLAS

%build
%add_optflags %optflags_shared
%cmake \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DBLAS_goto2_LIBRARY:FILEPATH=%_libdir/libopenblas.so \
	-DUSE_XBLAS:BOOL=ON \
	-DBUILD_DEPRECATED:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_STATIC_LIBS:BOOL=OFF \
	-DSOVER:STRING=%sover

%cmake_build

%install
%cmakeinstall_std

for f in manpages/blas/man/manl/*.l; do
	m=$(basename "$f" .l).3f
	install -pD -m644 $f %buildroot%_man3dir/"$m"
	echo %_man3dir/"$m*"
done >blas-man.files

for f in manpages/man/manl/*.l; do
	m=$(basename "$f" .l).3f
	# some lapack pages miss .TH header
	if grep -qs -i '^[.]TH[[:space:]]' "$f"; then
		install -pD -m644 $f %buildroot%_man3dir/"$m"
	else
		echo ".TH $(echo ${m%%.3f} |sed -e 's/.*/\U&/') 3" >%buildroot%_man3dir/"$m"
		cat "$f" >>%buildroot%_man3dir/"$m"
	fi
	echo %_man3dir/"$m*"
done >lapack-man.files

%files -n lib%name
%define _customdocdir %_docdir/lapack-3.1
%doc LICENSE README.md
%_libdir/%soname

%files -n lib%name-devel
%_libdir/liblapack.so
%dir %_libdir/cmake
%_libdir/cmake/*
%_pkgconfigdir/*

%files -n blas-man -f blas-man.files
%files -n lapack-man -f lapack-man.files

%changelog
* Wed Jan 19 2022 Michael Shigorin <mike@altlinux.org> 1:3.8.0-alt7
- use openblas on %%e2k

* Tue Dec 21 2021 Ivan A. Melnikov <iv@altlinux.org> 1:3.8.0-alt6
- Use openblas for %%mips

* Thu Oct 14 2021 Ivan A. Melnikov <iv@altlinux.org> 1:3.8.0-alt5
- Use openblas on riscv64
- Use libblas.so for %%mips

* Sat Jan 02 2021 Vladislav Zavjalov <slazav@altlinux.org> 1:3.8.0-alt4
- Remove Conflicts/Obsoletes itself in liblapack-devel

* Thu Feb 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.8.0-alt3
- exclude %%arm from crippled arches

* Tue Feb 12 2019 Nikita Ermakov <arei@altlinux.org> 1:3.8.0-alt2
- Add bootstrap option
- Use libblas.so for %%arm %%e2k and riscv64 instead of libopenblas.so

* Thu May 24 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.8.0-alt1
- 3.8.0 released

* Thu Apr 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.5.0-alt2
- fixed build on AArch64

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.5.0-alt1
- Version 3.5.0

* Tue Mar 12 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.4.2-alt2
- built with libblas-devel on %arm architectures

* Tue Nov 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.4.2-alt1
- Version 3.4.2

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.4.1-alt1
- Version 3.4.1
- Built with OpenBLAS instead of GotoBLAS2

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.4.0-alt1
- Version 3.4.0

* Wed May 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3.1-alt2
- Fixed for dist-upgrade (ALT #25561)

* Wed Apr 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3.1-alt1
- Version 3.3.1

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3.0-alt6
- Renamed lapack-goto -> lapack

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt5.1
- Don't use embedded BLAS

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt5
- Built with GotoBLAS2 instead of ATLAS
- Built without static library

* Mon Apr 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3.0-alt5
- Rebuilt with ATLAS 3.9.35

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3.0-alt4
- Set %_libdir/lib%name.so as link

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3.0-alt3
- Added -g into compiler flags

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3.0-alt2
- Rebuilt for debuginfo

* Tue Dec 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3.0-alt1
- Version 3.3.0

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2.2-alt1
- Version 3.2.2

* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1:3.1.1-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for liblapack
  * postun_ldconfig for liblapack
  * postclean-05-filetriggers for spec file

* Tue Nov 04 2008 Alexey Tourbin <at@altlinux.ru> 1:3.1.1-alt3
- fixed building with gcc-4.3 (switched to "internal function etime")
- made blas-man and lapack-man packages noarch

* Mon Oct 29 2007 Alexey Tourbin <at@altlinux.ru> 1:3.1.1-alt2
- packaged static libraries (requested by Pavel A. Piminov);
  use e.g. "g77 -static test.f -llapack -lblas" for static linkage
- fixed missing .TH header in manual pages
- packaged blas-man and lapack-man apart from liblapack-devel
- changed src.rpm packaging to keep separate upstream tarball

* Thu Apr 19 2007 Alexey Tourbin <at@altlinux.ru> 1:3.1.1-alt1
- 3.1.0 -> 3.1.1
- changed manual page suffix from .3 to .3f

* Wed Dec 13 2006 Alexey Tourbin <at@altlinux.ru> 1:3.1.0-alt1
- 3.0 -> 3.1.0
- imported sources into git and adapted for gear
- packaged COPYING README lapack-3.1.0.changes
- changed License from "Distributable" to "BSD" (see COPYING)
- added version script for liblapack.so.3 (new routines under LAPACK_3.1)
- made use of makefiles again and made build process execute test suite
- compiled with default optimization flags instead of -Os

* Tue Jun 06 2006 Alexey Tourbin <at@altlinux.ru> 1:3.0-alt3
- rebuilt with -llapack_atlas -lblas from ATLAS
- enabled tesing (i586 only, xlintsts hangs on x86_64)

* Sat Jun 03 2006 Alexey Tourbin <at@altlinux.ru> 1:3.0-alt2
- rebuilt with gfortran

* Tue Apr 25 2006 Alexey Tourbin <at@altlinux.ru> 1:3.0-alt1
- back to official versioning
- use officially released tarball
- libification: lib%name, lib%name-devel, lib%name-devel-static
- abandon makefiles, custom %%build procedure
- compile with -Os to workaround g77 bugs (redhat #138447)
- complie dcabs1.f with -O0 (redhat #143420)
- added missing BLAS source files (drotm.f, drotmg.f, zdrot.f, etc.)
- added manual pages to lib%name-devel

* Sun Dec 01 2002 Vitaly Lugovsky <vsl@altlinux.ru> 2002-alt3
- rebuild

* Tue May 14 2002 Vitaly Lugovsky <vsl@altlinux.ru> 2002-alt2
- First release. It's generally needed by CERNLib, so we've
  only static version here.
