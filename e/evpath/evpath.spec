%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define mver 4

Name: evpath
Version: %mver.0.82
Release: alt1.rev20547.svn20150305
Summary: Event transport middleware layer
License: BSD
Group: Development/Other
Url: http://www.cc.gatech.edu/systems/projects/EVPath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.research.cc.gatech.edu/kaos/evpath/trunk
# login: anon
# password: anon
Source: %name-%version.tar

BuildPreReq: cmake libenet0-devel %mpiimpl-devel libcercs_env-devel
BuildPreReq: libatl-devel libffs-devel libdill-devel libdf_shm-devel
BuildPreReq: libnnti-devel doxygen graphviz ctest gcc-c++

%description
EVpath is designed to be an event transport middleware layer.
Specifically, it is designed to allow for the easy implementation of
overlay networks, with active data processing, routing and management at
all points in the overlay.

EVpath specifically does not encompass global overlay creation,
management or destruction functions. Rather it focusses on providing
efficient environment for routine transport, while providing interfaces
necessary for external management layers.

%package -n lib%name
Summary: Event transport middleware layer
Group: System/Libraries

%description -n lib%name
EVpath is designed to be an event transport middleware layer.
Specifically, it is designed to allow for the easy implementation of
overlay networks, with active data processing, routing and management at
all points in the overlay.

EVpath specifically does not encompass global overlay creation,
management or destruction functions. Rather it focusses on providing
efficient environment for routine transport, while providing interfaces
necessary for external management layers.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
EVpath is designed to be an event transport middleware layer.
Specifically, it is designed to allow for the easy implementation of
overlay networks, with active data processing, routing and management at
all points in the overlay.

This package contains development files of %name.

%package tests
Summary: Tests for %name
Group: Development/Other
Requires: lib%name = %EVR

%description tests
EVpath is designed to be an event transport middleware layer.
Specifically, it is designed to allow for the easy implementation of
overlay networks, with active data processing, routing and management at
all points in the overlay.

This package contains tests for %name.

%package examples
Summary: Examples for %name
Group: Development/Other
Requires: lib%name = %EVR

%description examples
EVpath is designed to be an event transport middleware layer.
Specifically, it is designed to allow for the easy implementation of
overlay networks, with active data processing, routing and management at
all points in the overlay.

This package contains examples for %name.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description docs
EVpath is designed to be an event transport middleware layer.
Specifically, it is designed to allow for the easy implementation of
overlay networks, with active data processing, routing and management at
all points in the overlay.

This package contains documentation for %name.

%prep
%setup

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
	-DLIB_INSTALL_DIR_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DBUILD_SHARED_STATIC:STRING=SHARED \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DTARGET_CNL:BOOL=ON \
	-DCERCS_USE_INSTALLED:BOOL=ON \
	-DMAJVER=%mver \
	.
%make_build VERBOSE=1

pushd doc
doxygen
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

rm -fR examples/CMakeFiles *tests/CMakeFiles
install -d %buildroot%_libdir/%name
cp -fR examples *tests %buildroot%_libdir/%name/

%files -n lib%name
%doc stone.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*

%files tests
%dir %_libdir/%name
%_libdir/%name/*tests

%files examples
%dir %_libdir/%name
%_libdir/%name/examples

%files docs
%doc doc/*.pdf doc/html

%changelog
* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.82-alt1.rev20547.svn20150305
- Initial build for Sisyphus

