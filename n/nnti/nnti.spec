%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: nnti
Version: 2.0
Release: alt1.git20150304.1
Summary: NNTI 2.0 downstream from private Trilinos repository
License: BSD
Group: Development/Other
Url: https://github.com/eisenhauer/nnti

# https://github.com/eisenhauer/nnti.git
Source: %name-%version.tar

BuildPreReq: cmake ctest %mpiimpl-devel

%description
NNTI 2.0 downstream from private Trilinos repository (Trilinos I/O
Support).

%package -n lib%name
Summary: NNTI 2.0 downstream from private Trilinos repository
Group: System/Libraries

%description -n lib%name
NNTI 2.0 downstream from private Trilinos repository (Trilinos I/O
Support).

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
NNTI 2.0 downstream from private Trilinos repository (Trilinos I/O
Support).

This package contains development files of %name.

%prep
%setup

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
%add_optflags -I%mpidir/include

cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DTPL_ENABLE_MPI:BOOL=ON \
	-DMPIDIR:PATH=%mpidir \
	.
%make_build VERBOSE=1

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Fri Sep 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0-alt1.git20150304.1
- Fixed build.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20150304
- Initial build for Sisyphus

