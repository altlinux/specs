%define _unpackaged_files_terminate_build 1
%define soversion 7
%define soversion_integrators 6
%define soversion_linear 5
%define soversion_nonlinear 4

%def_with check

Name: sundials
Version: 7.4.0
Release: alt1

Summary: Suite of nonlinear and differential-algebraic equation solvers
License: BSD-3-Clause
Group: Sciences/Mathematics
Url: https://computing.llnl.gov/projects/sundials
VCS: https://github.com/LLNL/sundials.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-fortran
BuildRequires: liblapack-devel libsuitesparse-devel libgomp-devel

%if_with check
BuildRequires: gcc-c++ ctest libgtest-devel
%endif

%description
SUNDIALS provides time integrators and nonlinear solvers for ordinary
and differential-algebraic equations. This build includes Scilab's
numerical extensions and uses system LAPACK, SuiteSparse KLU and OpenMP.

%package -n libsundials-core%soversion
Summary: SUNDIALS core utilities
Group: System/Libraries

%description -n libsundials-core%soversion
This package contains the SUNDIALS core utilities shared library.

%package -n libsundials-arkode%soversion_integrators
Summary: SUNDIALS ARKODE additive Runge-Kutta integrator
Group: System/Libraries

%description -n libsundials-arkode%soversion_integrators
This package contains the SUNDIALS ARKODE additive Runge-Kutta integrator
shared library.

%package -n libsundials-cvode%soversion
Summary: SUNDIALS CVODE ordinary differential equation solver
Group: System/Libraries

%description -n libsundials-cvode%soversion
This package contains the SUNDIALS CVODE ordinary differential equation solver
shared library.

%package -n libsundials-cvodes%soversion
Summary: SUNDIALS CVODES solver with sensitivity analysis
Group: System/Libraries

%description -n libsundials-cvodes%soversion
This package contains the SUNDIALS CVODES solver with sensitivity analysis
shared library.

%package -n libsundials-ida%soversion
Summary: SUNDIALS IDA differential-algebraic equation solver
Group: System/Libraries

%description -n libsundials-ida%soversion
This package contains the SUNDIALS IDA differential-algebraic equation solver
shared library.

%package -n libsundials-idas%soversion_integrators
Summary: SUNDIALS IDAS solver with sensitivity analysis
Group: System/Libraries

%description -n libsundials-idas%soversion_integrators
This package contains the SUNDIALS IDAS solver with sensitivity analysis
shared library.

%package -n libsundials-kinsol%soversion
Summary: SUNDIALS KINSOL nonlinear system solver
Group: System/Libraries

%description -n libsundials-kinsol%soversion
This package contains the SUNDIALS KINSOL nonlinear system solver shared
library.

%package -n libsundials-nvecmanyvector%soversion
Summary: SUNDIALS ManyVector implementation
Group: System/Libraries

%description -n libsundials-nvecmanyvector%soversion
This package contains the SUNDIALS ManyVector implementation shared library.

%package -n libsundials-nvecopenmp%soversion
Summary: SUNDIALS OpenMP vector implementation
Group: System/Libraries

%description -n libsundials-nvecopenmp%soversion
This package contains the SUNDIALS OpenMP vector implementation shared
library.

%package -n libsundials-nvecserial%soversion
Summary: SUNDIALS serial vector implementation
Group: System/Libraries

%description -n libsundials-nvecserial%soversion
This package contains the SUNDIALS serial vector implementation shared
library.

%package -n libsundials-sunmatrixband%soversion_linear
Summary: SUNDIALS band matrix implementation
Group: System/Libraries

%description -n libsundials-sunmatrixband%soversion_linear
This package contains the SUNDIALS band matrix implementation shared library.

%package -n libsundials-sunmatrixdense%soversion_linear
Summary: SUNDIALS dense matrix implementation
Group: System/Libraries

%description -n libsundials-sunmatrixdense%soversion_linear
This package contains the SUNDIALS dense matrix implementation shared library.

%package -n libsundials-sunmatrixsparse%soversion_linear
Summary: SUNDIALS sparse matrix implementation
Group: System/Libraries

%description -n libsundials-sunmatrixsparse%soversion_linear
This package contains the SUNDIALS sparse matrix implementation shared
library.

%package -n libsundials-sunlinsolband%soversion_linear
Summary: SUNDIALS band linear solver
Group: System/Libraries

%description -n libsundials-sunlinsolband%soversion_linear
This package contains the SUNDIALS band linear solver shared library.

%package -n libsundials-sunlinsoldense%soversion_linear
Summary: SUNDIALS dense linear solver
Group: System/Libraries

%description -n libsundials-sunlinsoldense%soversion_linear
This package contains the SUNDIALS dense linear solver shared library.

%package -n libsundials-sunlinsolklu%soversion_linear
Summary: SUNDIALS SuiteSparse KLU linear solver
Group: System/Libraries

%description -n libsundials-sunlinsolklu%soversion_linear
This package contains the SUNDIALS SuiteSparse KLU linear solver shared
library.

%package -n libsundials-sunlinsollapackband%soversion_linear
Summary: SUNDIALS LAPACK band linear solver
Group: System/Libraries

%description -n libsundials-sunlinsollapackband%soversion_linear
This package contains the SUNDIALS LAPACK band linear solver shared library.

%package -n libsundials-sunlinsollapackdense%soversion_linear
Summary: SUNDIALS LAPACK dense linear solver
Group: System/Libraries

%description -n libsundials-sunlinsollapackdense%soversion_linear
This package contains the SUNDIALS LAPACK dense linear solver shared library.

%package -n libsundials-sunlinsolpcg%soversion_linear
Summary: SUNDIALS preconditioned conjugate gradient linear solver
Group: System/Libraries

%description -n libsundials-sunlinsolpcg%soversion_linear
This package contains the SUNDIALS preconditioned conjugate gradient linear
solver shared library.

%package -n libsundials-sunlinsolspbcgs%soversion_linear
Summary: SUNDIALS stabilized bi-conjugate gradient linear solver
Group: System/Libraries

%description -n libsundials-sunlinsolspbcgs%soversion_linear
This package contains the SUNDIALS stabilized bi-conjugate gradient linear
solver shared library.

%package -n libsundials-sunlinsolspfgmr%soversion_linear
Summary: SUNDIALS flexible GMRES linear solver
Group: System/Libraries

%description -n libsundials-sunlinsolspfgmr%soversion_linear
This package contains the SUNDIALS flexible GMRES linear solver shared
library.

%package -n libsundials-sunlinsolspgmr%soversion_linear
Summary: SUNDIALS GMRES linear solver
Group: System/Libraries

%description -n libsundials-sunlinsolspgmr%soversion_linear
This package contains the SUNDIALS GMRES linear solver shared library.

%package -n libsundials-sunlinsolsptfqmr%soversion_linear
Summary: SUNDIALS transpose-free QMR linear solver
Group: System/Libraries

%description -n libsundials-sunlinsolsptfqmr%soversion_linear
This package contains the SUNDIALS transpose-free QMR linear solver shared
library.

%package -n libsundials-sunnonlinsolfixedpoint%soversion_nonlinear
Summary: SUNDIALS fixed-point nonlinear solver
Group: System/Libraries

%description -n libsundials-sunnonlinsolfixedpoint%soversion_nonlinear
This package contains the SUNDIALS fixed-point nonlinear solver shared
library.

%package -n libsundials-sunnonlinsolnewton%soversion_nonlinear
Summary: SUNDIALS Newton nonlinear solver
Group: System/Libraries

%description -n libsundials-sunnonlinsolnewton%soversion_nonlinear
This package contains the SUNDIALS Newton nonlinear solver shared library.

%package devel
Summary: Development files for SUNDIALS
Group: Development/C
Requires: libsundials-core%soversion = %EVR
Requires: libsundials-arkode%soversion_integrators = %EVR
Requires: libsundials-cvode%soversion = %EVR
Requires: libsundials-cvodes%soversion = %EVR
Requires: libsundials-ida%soversion = %EVR
Requires: libsundials-idas%soversion_integrators = %EVR
Requires: libsundials-kinsol%soversion = %EVR
Requires: libsundials-nvecmanyvector%soversion = %EVR
Requires: libsundials-nvecopenmp%soversion = %EVR
Requires: libsundials-nvecserial%soversion = %EVR
Requires: libsundials-sunmatrixband%soversion_linear = %EVR
Requires: libsundials-sunmatrixdense%soversion_linear = %EVR
Requires: libsundials-sunmatrixsparse%soversion_linear = %EVR
Requires: libsundials-sunlinsolband%soversion_linear = %EVR
Requires: libsundials-sunlinsoldense%soversion_linear = %EVR
Requires: libsundials-sunlinsolklu%soversion_linear = %EVR
Requires: libsundials-sunlinsollapackband%soversion_linear = %EVR
Requires: libsundials-sunlinsollapackdense%soversion_linear = %EVR
Requires: libsundials-sunlinsolpcg%soversion_linear = %EVR
Requires: libsundials-sunlinsolspbcgs%soversion_linear = %EVR
Requires: libsundials-sunlinsolspfgmr%soversion_linear = %EVR
Requires: libsundials-sunlinsolspgmr%soversion_linear = %EVR
Requires: libsundials-sunlinsolsptfqmr%soversion_linear = %EVR
Requires: libsundials-sunnonlinsolfixedpoint%soversion_nonlinear = %EVR
Requires: libsundials-sunnonlinsolnewton%soversion_nonlinear = %EVR
Requires: liblapack-devel libsuitesparse-devel libgomp-devel

%description devel
Headers, linker symlinks, CMake configuration and pkg-config metadata
for developing applications using SUNDIALS. Internal headers required
by Scilab are included under sundials/internal.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DSUNDIALS_INDEX_SIZE=64 \
    -DSUNDIALS_PRECISION=DOUBLE \
    -DENABLE_LAPACK=ON \
    -DBLA_SIZEOF_INTEGER=4 \
    -DENABLE_KLU=ON \
    -DENABLE_OPENMP=ON \
    -DBUILD_TESTING=%{with check} \
    -DEXAMPLES_ENABLE_C=%{with check} \
    -DEXAMPLES_ENABLE_CXX=OFF \
    -DEXAMPLES_INSTALL=OFF \
    -DSUNDIALS_TEST_ENABLE_UNIT_TESTS=%{with check} \
    -DSUNDIALS_TEST_ENABLE_GTEST=%{with check} \
    -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
    -DSUNDIALS_TEST_ENABLE_DIFF_OUTPUT=OFF
%cmake_build

%install
%cmake_install
rm %buildroot%_includedir/sundials/LICENSE %buildroot%_includedir/sundials/NOTICE

%check
export OMP_NUM_THREADS=2
%ctest

%files -n libsundials-core%soversion
%doc LICENSE NOTICE
%_libdir/libsundials_core.so.%soversion
%_libdir/libsundials_core.so.%soversion.*

%files -n libsundials-arkode%soversion_integrators
%doc LICENSE NOTICE
%_libdir/libsundials_arkode.so.%soversion_integrators
%_libdir/libsundials_arkode.so.%soversion_integrators.*

%files -n libsundials-cvode%soversion
%doc LICENSE NOTICE
%_libdir/libsundials_cvode.so.%soversion
%_libdir/libsundials_cvode.so.%soversion.*

%files -n libsundials-cvodes%soversion
%doc LICENSE NOTICE
%_libdir/libsundials_cvodes.so.%soversion
%_libdir/libsundials_cvodes.so.%soversion.*

%files -n libsundials-ida%soversion
%doc LICENSE NOTICE
%_libdir/libsundials_ida.so.%soversion
%_libdir/libsundials_ida.so.%soversion.*

%files -n libsundials-idas%soversion_integrators
%doc LICENSE NOTICE
%_libdir/libsundials_idas.so.%soversion_integrators
%_libdir/libsundials_idas.so.%soversion_integrators.*

%files -n libsundials-kinsol%soversion
%doc LICENSE NOTICE
%_libdir/libsundials_kinsol.so.%soversion
%_libdir/libsundials_kinsol.so.%soversion.*

%files -n libsundials-nvecmanyvector%soversion
%doc LICENSE NOTICE
%_libdir/libsundials_nvecmanyvector.so.%soversion
%_libdir/libsundials_nvecmanyvector.so.%soversion.*

%files -n libsundials-nvecopenmp%soversion
%doc LICENSE NOTICE
%_libdir/libsundials_nvecopenmp.so.%soversion
%_libdir/libsundials_nvecopenmp.so.%soversion.*

%files -n libsundials-nvecserial%soversion
%doc LICENSE NOTICE
%_libdir/libsundials_nvecserial.so.%soversion
%_libdir/libsundials_nvecserial.so.%soversion.*

%files -n libsundials-sunmatrixband%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunmatrixband.so.%soversion_linear
%_libdir/libsundials_sunmatrixband.so.%soversion_linear.*

%files -n libsundials-sunmatrixdense%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunmatrixdense.so.%soversion_linear
%_libdir/libsundials_sunmatrixdense.so.%soversion_linear.*

%files -n libsundials-sunmatrixsparse%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunmatrixsparse.so.%soversion_linear
%_libdir/libsundials_sunmatrixsparse.so.%soversion_linear.*

%files -n libsundials-sunlinsolband%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsolband.so.%soversion_linear
%_libdir/libsundials_sunlinsolband.so.%soversion_linear.*

%files -n libsundials-sunlinsoldense%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsoldense.so.%soversion_linear
%_libdir/libsundials_sunlinsoldense.so.%soversion_linear.*

%files -n libsundials-sunlinsolklu%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsolklu.so.%soversion_linear
%_libdir/libsundials_sunlinsolklu.so.%soversion_linear.*

%files -n libsundials-sunlinsollapackband%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsollapackband.so.%soversion_linear
%_libdir/libsundials_sunlinsollapackband.so.%soversion_linear.*

%files -n libsundials-sunlinsollapackdense%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsollapackdense.so.%soversion_linear
%_libdir/libsundials_sunlinsollapackdense.so.%soversion_linear.*

%files -n libsundials-sunlinsolpcg%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsolpcg.so.%soversion_linear
%_libdir/libsundials_sunlinsolpcg.so.%soversion_linear.*

%files -n libsundials-sunlinsolspbcgs%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsolspbcgs.so.%soversion_linear
%_libdir/libsundials_sunlinsolspbcgs.so.%soversion_linear.*

%files -n libsundials-sunlinsolspfgmr%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsolspfgmr.so.%soversion_linear
%_libdir/libsundials_sunlinsolspfgmr.so.%soversion_linear.*

%files -n libsundials-sunlinsolspgmr%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsolspgmr.so.%soversion_linear
%_libdir/libsundials_sunlinsolspgmr.so.%soversion_linear.*

%files -n libsundials-sunlinsolsptfqmr%soversion_linear
%doc LICENSE NOTICE
%_libdir/libsundials_sunlinsolsptfqmr.so.%soversion_linear
%_libdir/libsundials_sunlinsolsptfqmr.so.%soversion_linear.*

%files -n libsundials-sunnonlinsolfixedpoint%soversion_nonlinear
%doc LICENSE NOTICE
%_libdir/libsundials_sunnonlinsolfixedpoint.so.%soversion_nonlinear
%_libdir/libsundials_sunnonlinsolfixedpoint.so.%soversion_nonlinear.*

%files -n libsundials-sunnonlinsolnewton%soversion_nonlinear
%doc LICENSE NOTICE
%_libdir/libsundials_sunnonlinsolnewton.so.%soversion_nonlinear
%_libdir/libsundials_sunnonlinsolnewton.so.%soversion_nonlinear.*

%files devel
%doc README.md
%_includedir/arkode/
%_includedir/cvode/
%_includedir/cvodes/
%_includedir/ida/
%_includedir/idas/
%_includedir/kinsol/
%_includedir/nvector/
%_includedir/sunadjointcheckpointscheme/
%_includedir/sunadaptcontroller/
%_includedir/sundials/
%_includedir/sunlinsol/
%_includedir/sunmatrix/
%_includedir/sunmemory/
%_includedir/sunnonlinsol/
%_libdir/libsundials_*.so
%_libdir/cmake/sundials/
%_pkgconfigdir/sundials.pc

%changelog
* Tue Nov 10 2026 Ajrat Makhmutov <rauty@altlinux.org> 7.4.0-alt1
- First build for ALT.
