%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname slepc
%define scalar_type real
%define ldir %_libdir/petsc-%scalar_type

%define somver 3
%define sover %somver.2.0
Name: %oname-%scalar_type
Version: 3.2_p5
Release: alt2
Summary: Scalable Library for Eigenvalue Problem Computations (%scalar_type scalars)
License: LGPL v3
Group: Sciences/Mathematics
Url: http://www.grycap.upv.es/slepc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz
Source1: %oname.pc

Requires: lib%name-devel = %version-%release
Requires: petsc-%scalar_type

BuildRequires(pre): rpm-build-python
BuildPreReq: chrpath libpetsc-%scalar_type-devel libprimme-devel
BuildPreReq: %mpiimpl-devel gcc-fortran libgfortran-devel
BuildPreReq: libstdc++-devel libatlas-devel libsz2-devel libparpack-mpi-devel
BuildPreReq: liblapack-goto-devel gcc-c++ libscalapack-devel libX11-devel
BuildPreReq: libXt-devel libsowing-devel boost-devel python-module-fiat
BuildPreReq: libparmetis-devel libblacs-devel libspooles-devel
BuildPreReq: libtetgen-devel zlib-devel libblocksolve95-devel
BuildPreReq: libtriangle-devel libsuperlu_dist-devel libsuitesparse-devel
BuildPreReq: libsuperlu-devel liby12m-devel
BuildPreReq: cproto libchaco-devel
BuildPreReq: libtau-devel libmtl4-devel libmpe2-devel boost-python-devel
BuildPreReq: libplapack-devel python-devel petsc-%scalar_type-sources
%if %scalar_type == real
BuildPreReq: libblzpack-devel libtrlan-devel 
BuildPreReq: libscotch-devel libmumps-devel libpastix-devel
BuildPreReq: ffc libhypre-devel libspai-devel libparms-devel
BuildPreReq: libblopex-devel libhdf5-mpi-devel python-module-numpy
BuildPreReq: libexpat-devel
BuildPreReq: libnetcdf-mpi-devel
BuildPreReq: libsundials-devel
BuildPreReq: libsprng1-devel
%endif
%if %scalar_type == complex
BuildPreReq: libfftw3-mpi-devel
%endif

%description
SLEPc is a software library for the solution of large scale sparse eigenvalue
problems on parallel computers. It is an extension of PETSc and can be used for
either standard or generalized eigenproblems, with real or complex arithmetic.
It can also be used for computing a partial SVD of a large, sparse, rectangular
matrix.

SLEPc is based on the PETSc data structures and it employs the MPI standard for
message-passing communication. It is being developed by the High Performance
Networking and Computing Group (GRyCAP) of Universidad Politecnica de Valencia
(Spain).

%package -n lib%name
Summary: Shared library of SLEPc (%scalar_type scalars)
Group: System/Libraries
Requires: libpetsc-%scalar_type >= 3.0.0_p8-alt1
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name
SLEPc is a software library for the solution of large scale sparse eigenvalue
problems on parallel computers. It is an extension of PETSc and can be used for
either standard or generalized eigenproblems, with real or complex arithmetic.
It can also be used for computing a partial SVD of a large, sparse, rectangular
matrix.

SLEPc is based on the PETSc data structures and it employs the MPI standard for
message-passing communication. It is being developed by the High Performance
Networking and Computing Group (GRyCAP) of Universidad Politecnica de Valencia
(Spain).

This package contains shared library of SLEPc.

%package -n lib%name-devel
Summary: Development files of SLEPc (%scalar_type scalars)
Group: Development/Other
Requires: lib%name = %version-%release
Requires: libpetsc-%scalar_type-devel >= 3.0.0_p8-alt1
Requires: libprimme-devel %mpiimpl-devel
%if "%scalar_type" == "real"
Requires: libblzpack-devel libtrlan-devel 
%endif

%description -n lib%name-devel
SLEPc is a software library for the solution of large scale sparse eigenvalue
problems on parallel computers. It is an extension of PETSc and can be used for
either standard or generalized eigenproblems, with real or complex arithmetic.
It can also be used for computing a partial SVD of a large, sparse, rectangular
matrix.

SLEPc is based on the PETSc data structures and it employs the MPI standard for
message-passing communication. It is being developed by the High Performance
Networking and Computing Group (GRyCAP) of Universidad Politecnica de Valencia
(Spain).

This package contains development files of SLEPc.

%package -n lib%oname-devel-doc
Summary: Documentation for SLEPc
Group: Development/Documentation
BuildArch: noarch

%description -n lib%oname-devel-doc
SLEPc is a software library for the solution of large scale sparse eigenvalue
problems on parallel computers. It is an extension of PETSc and can be used for
either standard or generalized eigenproblems, with real or complex arithmetic.
It can also be used for computing a partial SVD of a large, sparse, rectangular
matrix.

SLEPc is based on the PETSc data structures and it employs the MPI standard for
message-passing communication. It is being developed by the High Performance
Networking and Computing Group (GRyCAP) of Universidad Politecnica de Valencia
(Spain).

This package contains development documentation for SLEPc.

%package -n %oname-examples
Summary: Examples for SLEPc
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-examples
SLEPc is a software library for the solution of large scale sparse eigenvalue
problems on parallel computers. It is an extension of PETSc and can be used for
either standard or generalized eigenproblems, with real or complex arithmetic.
It can also be used for computing a partial SVD of a large, sparse, rectangular
matrix.

SLEPc is based on the PETSc data structures and it employs the MPI standard for
message-passing communication. It is being developed by the High Performance
Networking and Computing Group (GRyCAP) of Universidad Politecnica de Valencia
(Spain).

This package contains examples for SLEPc.

%prep
%setup
cp %SOURCE1 %name.pc

for i in $(find ./ -name makefile); do
	sed -i 's|\-@|-|' $i
	sed -i 's|@\$|$|' $i
done

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|" config/primme.py

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

export SLEPC_DIR=$PWD
%if "%scalar_type" == "real"
ADDLIBS="-ldprimme -ltrlan_mpi -lblzpack -lparpack_MPI-LINUX -lBLOPEX"
%else
ADDLIBS="-lzprimme -lparpack_MPI-LINUX -lBLOPEX"
%endif
sed -i "s|@ADDLIBS@|$ADDLIBS|" makefile
ARPACKLIBS="-lparpack_MPI-LINUX,-lscalapack,-larpack_LINUX,-lblacs"

export PETSC_ARCH=linux-gnu
./configure --prefix=$PETSC_LDIR \
%if "%scalar_type" == "real"
	--with-blzpack \
	--with-trlan \
%endif
	--with-arpack \
	--with-arpack-flags=$ARPACKLIBS \
	--with-arpack-dir=%_libdir \
	--with-primme \
%if "%scalar_type" == "real"
	--with-primme-flags="-ldprimme" \
%else
	--with-primme-flags="-lzprimme" \
%endif
	--with-primme-dir=%_libdir
%make_build SOVER="%sover" SOMVER="%somver"

%install
source %mpidir/bin/mpivars.sh
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

export SLEPC_DIR=$PWD
export PETSC_ARCH=linux-gnu
%make_install SLEPC_DESTDIR=%buildroot%ldir \
	SOVER="%sover" SOMVER="%somver" \
	install

pushd %buildroot$PETSC_LDIR/lib
chrpath -r %ldir/lib:%mpidir/lib lib%oname.so.%sover
ln -s lib%oname.so.%sover lib%oname.so.%somver
ln -s lib%oname.so.%somver lib%oname.so
popd

%if "%scalar_type" == "real"
install -d %buildroot%_docdir/lib%oname-%version
rm docs/makefile*
cp -fR docs/* %buildroot%_docdir/lib%oname-%version

for i in eps qep svd st ip
do
	install -d %buildroot%_docdir/lib%oname-%version/examples/$i
	cp -fR src/$i/examples/* \
		%buildroot%_docdir/lib%oname-%version/examples/$i
done
%endif

# pkg-config

sed -i 's|@PETSC_DIR@|%ldir|g' %name.pc
sed -i 's|@VERSION@|%version|g' %name.pc
sed -i 's|@PYVER@|%_python_version|g' %name.pc
install -d %buildroot%_pkgconfigdir
install -m644 %name.pc %buildroot%_pkgconfigdir/

%files
%doc COPYING COPYING.LESSER README

%files -n lib%name
%ldir/lib/*.so.*

%files -n lib%name-devel
%ldir/lib/*.so
%ldir/include/*
%ldir/conf/*
%_pkgconfigdir/*

%if "%scalar_type" == "real"
%files -n lib%oname-devel-doc
%doc %dir %_docdir/lib%oname-%version
%doc %_docdir/lib%oname-%version/*
%exclude %_docdir/lib%oname-%version/examples

%files -n %oname-examples
%doc %dir %_docdir/lib%oname-%version
%doc %_docdir/lib%oname-%version/examples
%endif

%changelog
* Fri Jul 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p5-alt2
- Rebuilt with OpenMPI 1.6

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p5-alt1
- Version 3.2-p5

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p4-alt1
- Version 3.2-p4

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p3-alt1
- Version 3.2-p3

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p6-alt2
- Rebuilt

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p6-alt1
- Version 3.1-p6
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Sun Mar 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p4-alt3
- Rebuilt for debuginfo

* Thu Nov 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p4-alt2
- Fixed link with BLACS

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p4-alt1
- Version 3.1-p4

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p0-alt4
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p0-alt3
- Fixed overlinking of libraries

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p0-alt2
- Fixed pkg-config file

* Thu Aug 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p0-alt1
- Version 3.1-p0
- Rebuilt with blopex

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt4
- Rebuilt without blopex

* Thu Dec 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt3
- Rebuilt with SuperLU 4.0

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt1.M51.1
- Port for branch 5.1

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt2
- Rebuilt with Trilinos v10

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt1
- Version 3.0.0-p7 (ALT #22176)

* Thu Sep 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p5-alt1
- Version 3.0.0-p5
- Rebuilt with shared libraries of requirements instead of static
- Set default Eigenproblem Solver = POWER

* Fri Aug 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p4-alt4
- Added pkg-config file

* Thu Aug 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p4-alt3
- Rebuild with PETSc-3.0.0_p7-alt5

* Sat Jul 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p4-alt2
- Removed %_bindir/%name.sh into libpetsc-%scalar_type package

* Mon Jul 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p4-alt1
- Initial build for Sisyphus
