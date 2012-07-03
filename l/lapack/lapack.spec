Name: lapack
Version: 3.4.0
Epoch: 1
Release: alt1

Summary: BLAS and LAPACK Fortran libraries for numerical linear algebra (with GotoBLAS2)
License: BSD
Group: Development/Other

URL: http://www.netlib.org/
Source: %name-%version.tar
Source1: manpages.tar
Source2: zla_rpvgrw.f
Source3: sla_rpvgrw.f
Source4: cla_rpvgrw.f
Source5: dla_rpvgrw.f
Patch: lapack-3.1.1-alt3.qa1.patch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: gcc-fortran libgotoblas-devel cmake libgomp-devel
BuildPreReq: libsuperlu-devel

BuildPreReq: libxblas-devel

%package -n lib%name
Summary: BLAS and LAPACK Fortran libraries for numerical linear algebra (with GotoBLAS2)
Group: System/Libraries
Provides: lib%name-goto = %epoch:%version-%release
Conflicts: lib%name-goto < %epoch:%version-%release
Obsoletes: lib%name-goto < %epoch:%version-%release
Obsoletes: liblapack3

%package -n lib%name-devel
Summary: BLAS and LAPACK Fortran libraries for numerical linear algebra (with GotoBLAS2)
Group: Development/Other
Provides: lib%name-goto-devel = %epoch:%version-%release
Requires: libgotoblas-devel
Requires: lib%name = %epoch:%version-%release
Conflicts: lib%name-devel < %epoch:%version-%release
Obsoletes: lib%name-devel < %epoch:%version-%release
Conflicts: lib%name-goto-devel < %epoch:%version-%release
Obsoletes: lib%name-goto-devel < %epoch:%version-%release

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
%setup
%patch -p1

install -m644 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 SRC
tar -xf %SOURCE1

export LC_COLLATE=C
ls manpages/blas/man/manl >blas.manpages
ls manpages/man/manl >lapack.manpages
comm -12 blas.manpages lapack.manpages >dup.manpages
(cd manpages/man/manl; xargs -r rm -v -- ) <dup.manpages || exit 1
rm blas.manpages lapack.manpages dup.manpages
rm -fR BLAS

%build
# whether to use the ALTAS optimized routines
%def_with atlas
%define soname liblapack.so.4

# for rpm -bc --short-circuit, rebuild test suite with liblapack.a
rm -f TESTING/x*

FLAGS="-g -pipe -Wall -O3 %optflags_shared -pthread"
cmake \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_C_FLAGS:STRING="$FLAGS" \
	-DCMAKE_CXX_FLAGS:STRING="$FLAGS" \
	-DCMAKE_Fortran_FLAGS:STRING="$FLAGS" \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DUSEXBLAS:BOOL=ON \
	.
%make_build
grep -r --include='*.out' -i fail . |tee 1.err

# liblapack.a is now ready; if we use the ATLAS optimized routines,
# we want to exclude certain *.o from the shared library and make it
# link with -llapack_atlas

%if_with atlas
rm -f *.o
ar x lib/liblapack.a
nm -D %_libdir/libgoto2.so >sym
awk 'NF==3&&sub(/_$/,"",$3)&&$3!~/_/{print$3".o"}' <sym >dups
rm -fv `sort -u dups`
g77 -shared *.o \
	-o %soname -Wl,-soname=%soname -Wl,--version-script=liblapack.map \
	-lgoto2 -lxblas -Wl,-z,defs
#rm SRC/liblapack.a
#ar rcu SRC/liblapack.a *.o
#ranlib SRC/liblapack.a
rm *.o

# rerun test suite against the shared library combo
#LD_LIBRARY_PATH=$PWD make -C BLAS/TESTING LAPACKLIB='%soname -lgoto2'
#grep -r --include='*.out' -i fail . |tee 2.err

%else # without atlas
g77 -shared -Wl,--whole-archive SRC/liblapack.a -Wl,--no-whole-archive \
	-o %soname -Wl,-soname=%soname -Wl,--version-script=liblapack.map \
	-lgoto2 -lxblas -Wl,-z,defs
%endif

%install
install -pD -m755 %soname %buildroot%_libdir/%soname
%if_with atlas
#install -pD -m644 SRC/liblapack.a %buildroot%_libdir/liblapack_.a
ln -s %soname %buildroot%_libdir/liblapack.so
#echo 'GROUP(%_libdir/liblapack_.a %_libdir/liblapack_atlas.a)' >%buildroot%_libdir/liblapack.a
%else
#install -pD -m644 SRC/liblapack.a %buildroot%_libdir/liblapack.a
ln -s %soname %buildroot%_libdir/liblapack.so
%endif

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
%doc LICENSE README
%_libdir/%soname

%files -n lib%name-devel
%_libdir/liblapack.so

%files -n blas-man -f blas-man.files
%files -n lapack-man -f lapack-man.files

%changelog
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
