%define oname freecfd
%define scalar_type real
%define ldir %_libexecdir/petsc-%scalar_type
%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

Name: %oname-%scalar_type
Version: 1.0.1
Release: alt7
Summary: Computational fluid dynamics (CFD) code (%scalar_type scalars)

Group: Sciences/Mathematics
License: GPL v3 or later
URL: http://www.freecfd.com/
Source: free-cfd-%version.tar.gz
Source1: README.txt
Source2: fcfd
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: %oname-common = %version-%release
Requires: libcgns-mpi libhdf5-mpi

BuildPreReq: python-module-petsc-config
BuildPreReq: %mpiimpl-devel libhdf5-mpi-devel libcgns-mpi-devel
BuildPreReq: libpetsc-%scalar_type-devel cmake chrpath
BuildPreReq: libtrilinos10-devel

%description
Free CFD is an open source computational fluid dynamics (CFD) code.
Features:

* 3D Unstructured: Free CFD can handle arbitrary polyhedral, mixed
  element type 3D unstructured grids.
* Parallel: ParMETIS is used for domain decomposition. Open MPI is used
  as the message passing interface.
* All Speed: OK, we know that this is too general a statement but let's
  say that the code can handle a Mach number of 3 as well as a Mach
  number of 0.001
* Density Based: AUSM+-up and Roe convective flux functions are
  currently available.
* Implicit: A fully impicit framework with first order, backward Euler
  time integration.
* Second Order Spatial Accuracy: Linear MUSCL reconstruction of the cell
  variables provide second order accuracy.
* Turbulence Models: A number of turbulence models ranging from basic
  k-epsilon to Menter's SST (Shear Stress Transport) are available.

%package -n %oname-common
Summary: Scalar type independent files of Free CFD
Group: Sciences/Mathematics
BuildArch: noarch

%description -n %oname-common
Free CFD is an open source computational fluid dynamics (CFD) code.

This package contains scalar type independent files of Free CFD.

%package -n %oname-examples
Summary: Examples for Free CFD
Group: Documentation
BuildArch: noarch

%description -n %oname-examples
Free CFD is an open source computational fluid dynamics (CFD) code.

This package contains examples for Free CFD.

%prep
%setup
install -m644 %SOURCE1 .

%build
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

pushd src
FLAGS="-I$PETSC_DIR/include -I%mpidir/include/metis -DLEGACY_SUPPORT"
FLAGS="$FLAGS %optflags"
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DPETSC_DIR:STRING=$PETSC_DIR \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DCMAKE_C_FLAGS="$FLAGS" \
	-DCMAKE_CXX_FLAGS="$FLAGS" \
	-DCMAKE_Fortran_FLAGS="$FLAGS" \
	.
sed -i "s|\(\-lpetsc\)|-L$PETSC_DIR/lib \1|g" \
	CMakeFiles/freecfd.dir/link.txt
%make_build
popd

%install
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std -C src

%if "%scalar_type" == "real"
install -d %buildroot%_bindir
install -m755 %SOURCE2 %buildroot%_bindir
%endif

pushd %buildroot$PETSC_DIR
for i in bin/*; do
	chrpath -r %mpidir/lib:$PETSC_DIR/lib $i
done
popd

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f

%filter_from_requires /^debug.*(libcgns\.so.*/s/^/libcgns-mpi-debuginfo\t/

%files
%doc README.txt doc/*
%ldir/bin/*

%if "%scalar_type" == "real"
%files -n %oname-common
%_bindir/*

%files -n %oname-examples
%doc examples/*
%endif

%changelog
* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt7
- Rebuilt with PETSc 3.2

* Mon Sep 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt6
- Rebuilt with parmetis 4.0

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt5
- Rebuilt with cgns 3.1.3

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt4
- Built with GotoBLAS2 instead of ATLAS

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt3
- Rebuilt for debuginfo

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Applied repocop fix for macos-resource-fork-file-in-package

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt4
- Rebuilt with PETSc 3.1

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt3
- Fix for new CGNS

* Thu Dec 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Rebuilt with Trilinos v10

* Mon Oct 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

