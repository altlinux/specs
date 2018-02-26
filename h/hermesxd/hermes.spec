%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%def_enable docs

%define oname hermes
Name: %{oname}xd
Version: 20110822
Release: alt6
Summary: hp-FEM library
License: GPL, BSD
Group: Sciences/Mathematics
Url: http://hpfem.org/hermes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hpfem/hermes.git
Source: %name-%version.tar

BuildPreReq: cmake libnumpy-devel python-module-Cython chrpath
BuildPreReq: gcc-c++ liblapack-devel gcc-fortran libsuitesparse-devel
BuildPreReq: libGL-devel libGLU-devel libglew-devel libloca10-devel
BuildPreReq: libmumps-devel libsuperlu-devel libtrilinos10-devel
BuildPreReq: %mpiimpl-devel python-devel python-module-sphinx-devel
BuildPreReq: libkomplex10-devel libexodusii-devel boost-devel
BuildPreReq: libqd-devel libvtk-devel libvtk-python-devel
BuildPreReq: libhdf5-mpi-devel libnetcdf-mpi-devel
BuildPreReq: libGLUT-devel
#BuildPreReq: libpetsc-complex-devel libpetsc-real-devel

%description
Hermes is a C++ library for rapid development of adaptive hp-FEM / hp-DG
solvers. Novel hp-adaptivity algorithms are designed to solve a large
variety of problems ranging from ODE and stationary linear PDE to
complex time-dependent nonlinear multiphysics PDE systems. The library
comes with a free interactive Online Laboratory where users can run
their models remotely. Detailed user documentation enhanced with many
benchmarks and examples allow the users to employ Hermes without being
experts in object-oriented programming, finite element methods, or in
the theory of partial differential equations. There is an active user
community where users get their questions answered quickly.

%package -n lib%name
Summary: Shared libraries of hermes
Group: System/Libraries

%description -n lib%name
Hermes is a C++ library for rapid development of adaptive hp-FEM / hp-DG
solvers. Novel hp-adaptivity algorithms are designed to solve a large
variety of problems ranging from ODE and stationary linear PDE to
complex time-dependent nonlinear multiphysics PDE systems. The library
comes with a free interactive Online Laboratory where users can run
their models remotely. Detailed user documentation enhanced with many
benchmarks and examples allow the users to employ Hermes without being
experts in object-oriented programming, finite element methods, or in
the theory of partial differential equations. There is an active user
community where users get their questions answered quickly.

This package contains shared libraries of hermes.

%package -n lib%name-devel
Summary: Development files of hermes
Group: Development/C++
BuildArch: noarch

%description -n lib%name-devel
Hermes is a C++ library for rapid development of adaptive hp-FEM / hp-DG
solvers. Novel hp-adaptivity algorithms are designed to solve a large
variety of problems ranging from ODE and stationary linear PDE to
complex time-dependent nonlinear multiphysics PDE systems. The library
comes with a free interactive Online Laboratory where users can run
their models remotely. Detailed user documentation enhanced with many
benchmarks and examples allow the users to employ Hermes without being
experts in object-oriented programming, finite element methods, or in
the theory of partial differential equations. There is an active user
community where users get their questions answered quickly.

This package contains development files of hermes.

%package -n python-module-%oname
Summary: Python modules of hermes
Group: Development/Python

%description -n python-module-%oname
Hermes is a C++ library for rapid development of adaptive hp-FEM / hp-DG
solvers. Novel hp-adaptivity algorithms are designed to solve a large
variety of problems ranging from ODE and stationary linear PDE to
complex time-dependent nonlinear multiphysics PDE systems. The library
comes with a free interactive Online Laboratory where users can run
their models remotely. Detailed user documentation enhanced with many
benchmarks and examples allow the users to employ Hermes without being
experts in object-oriented programming, finite element methods, or in
the theory of partial differential equations. There is an active user
community where users get their questions answered quickly.

This package contains python module of hermes.

%if_enabled docs

%package -n python-module-%oname-pickles
Summary: Pickles for hermes
Group: Development/Python

%description -n python-module-%oname-pickles
Hermes is a C++ library for rapid development of adaptive hp-FEM / hp-DG
solvers. Novel hp-adaptivity algorithms are designed to solve a large
variety of problems ranging from ODE and stationary linear PDE to
complex time-dependent nonlinear multiphysics PDE systems. The library
comes with a free interactive Online Laboratory where users can run
their models remotely. Detailed user documentation enhanced with many
benchmarks and examples allow the users to employ Hermes without being
experts in object-oriented programming, finite element methods, or in
the theory of partial differential equations. There is an active user
community where users get their questions answered quickly.

This package contains pickles for hermes.

%package doc
Summary: Documentation for hermes
Group: Development/Documentation
BuildArch: noarch

%description doc
Hermes is a C++ library for rapid development of adaptive hp-FEM / hp-DG
solvers. Novel hp-adaptivity algorithms are designed to solve a large
variety of problems ranging from ODE and stationary linear PDE to
complex time-dependent nonlinear multiphysics PDE systems. The library
comes with a free interactive Online Laboratory where users can run
their models remotely. Detailed user documentation enhanced with many
benchmarks and examples allow the users to employ Hermes without being
experts in object-oriented programming, finite element methods, or in
the theory of partial differential equations. There is an active user
community where users get their questions answered quickly.

This package contains documentation for hermes.

%endif

%prep
%setup

#rm -f hermes3d/src/loader/hdf5.cpp hermes3d/src/loader/exodusii.cpp

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

FLAGS="%optflags -I%mpidir/include -I%_includedir/suitesparse"
FLAGS="$FLAGS -I%_includedir/exodusii -I%_includedir/vtk-5.8"
FLAGS="$FLAGS -fno-strict-aliasing"
cmake -DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="$FLAGS" \
	-DCMAKE_CXX_FLAGS:STRING="$FLAGS" \
	-DCMAKE_Fortran_FLAGS:STRING="$FLAGS" \
	-DBLAS_blas_LIBRARY:FILEPATH=-lgoto2 \
	-DBLAS_cblas_LIBRARY:FILEPATH=-lgoto2 \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DWITH_SUPERLU:BOOL=ON \
	-DSUPERLU_ROOT:PATH="%prefix" \
	-DSUPERLU_LIBRARY:STRING="superlu_4.0" \
	-DJUDY_INCLUDE_DIR:STRING="%_includedir" \
	-DJUDY_LIBRARY:STRING="Judy" \
	-DWITH_UMFPACK:BOOL=ON \
	-DWITH_MPI:BOOL=ON \
	-DMPI_LIBRARIES:STRING="-L%mpidir/lib -Wl,-R%mpidir/lib -lmpi" \
	-DMPI_INCLUDE_PATH:PATH="%mpidir/include" \
	.
%make VERBOSE=1

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -d %buildroot%python_sitelibdir
mv %buildroot%_libexecdir/python/* \
	%buildroot%python_sitelibdir/

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/*.so %buildroot/%_libdir/
%endif
for i in %buildroot%_libdir/*.so; do
	chrpath -r %mpidir/lib $i ||:
done
for i in %buildroot%python_sitelibdir/*/*.so
do
	chrpath -r %mpidir/lib $i || chrpath -d $i
done

%if_enabled docs
# doc

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
%make html
%make pickle
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files -n lib%name
%doc AUTHORS README*
%_libdir/*.so

%files -n lib%name-devel
%_includedir/*

%files -n python-module-%oname
%python_sitelibdir/*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle

%files doc
%doc doc/_build/html/*

%files -n python-module-%oname-pickles
%python_sitelibdir/%oname/pickle
%endif

%changelog
* Sun May 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110822-alt6
- Fixed build

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110822-alt5
- Rebuilt with Trilinos 10.10.0

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110822-alt4
- Fixed RPATH

* Wed Nov 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110822-alt3
- Fixed build

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110822-alt2
- Rebuilt with pickles

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20110822-alt1.1
- Rebuild with Python-2.7

* Wed Aug 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110822-alt1
- New snapshot

* Sun Jun 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110517-alt1
- Initial build for Sisyphus

