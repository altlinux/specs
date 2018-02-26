Name: libfblaslapack-devel
Version: 3.1.1
Release: alt6
Summary: BLAS/LAPACK in Fortran for being linked with PETSc
License: MIT
Group: Sciences/Mathematics
Url: http://www.mcs.anl.gov/petsc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ftp://ftp.mcs.anl.gov/pub/petsc/externalpackages/fblaslapack-3.1.1.tar.gz

BuildPreReq: gcc-fortran petsc-real

%description
BLAS/LAPACK in Fortran for being linked with PETSc.

%prep
%setup

%build
source %_bindir/petsc-real.sh
%make_build

%install
install -d %buildroot%_libdir

install -m644 *.a %buildroot%_libdir

%brp_strip_none %_libdir/*.a

%files
%_libdir/*.a

%changelog
* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt6
- Rebuilt for debuginfo

* Mon Aug 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt5
- Rebuilt with PETSc 3.1

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt4
- Updated sources at 2010/01/13

* Sun Aug 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt3
- Fixed using of ETIME subroutine

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt2
- Rebuild with PIC

* Fri Jun 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus

