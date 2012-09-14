%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define hdfdir %mpidir

%define oname libcf
%define priority 40
Name: %oname-mpi
Version: 1.0
Release: alt1.beta1.2011092223
Summary: Manipulating of scientific data files which conform to the CF conventions
License: Open source
Group: File tools
Url: http://www.unidata.ucar.edu/software/libcf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel liblapack-devel gcc-fortran libuuid-devel
BuildPreReq: libcurl-devel libnetcdf-mpi-devel

%description
The netCDF CF Library, or libCF, uses the netCDF API to aid in the
creation, processing and sharing of scientific data files which conform
to the Climate and Forecast (CF) conventions.

%package devel
Summary: Development files of libCF, the netCDF CF Library
Group: System/Libraries
Requires: %name = %version-%release

%description devel
The netCDF CF Library, or libCF, uses the netCDF API to aid in the
creation, processing and sharing of scientific data files which conform
to the Climate and Forecast (CF) conventions.

This package contains development files of libCF.

%package -n python-module-%name
Summary: Python bindings for libCF, the netCDF CF Library
Group: Development/Python
Requires: %name = %version-%release
Conflicts: python-module-%oname

%description -n python-module-%name
The netCDF CF Library, or libCF, uses the netCDF API to aid in the
creation, processing and sharing of scientific data files which conform
to the Climate and Forecast (CF) conventions.

This package contains python bindings for libCF.

%package examples
Summary: Examples for libCF, the netCDF CF Library
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
The netCDF CF Library, or libCF, uses the netCDF API to aid in the
creation, processing and sharing of scientific data files which conform
to the Climate and Forecast (CF) conventions.

This package contains examples for libCF.

%prep
%setup

sed -i 's|@HDFDIR@|%hdfdir|' setup.py.in

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags $(nc-config --cflags) -I%mpidir/include
export CPPFLAGS="%optflags"
%autoreconf
%configure \
	--includedir=%hdfdir/include \
	--libdir=%hdfdir/lib \
	--enable-static=no \
	--enable-docs \
	--enable-f90 \
	--with-netcdf=%hdfdir \
	--with-blas-lib=-lopenblas \
	--with-lapack-lib=-llapack \
	--enable-parallel
%make_build

%python_build_debug

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

%python_install

install -d %buildroot%hdfdir/bin
install -m755 examples/.libs/* %buildroot%hdfdir/bin
%make -C examples clean

%files
%doc COPYRIGHT
%hdfdir/lib/*.so.*

%files devel
%hdfdir/include
%hdfdir/lib/*.so

%files examples
%doc examples
%hdfdir/bin

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.beta1.2011092223
- Initial build for Sisyphus

