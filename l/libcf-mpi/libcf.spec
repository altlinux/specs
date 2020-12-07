%define _unpackaged_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define hdfdir %mpidir

%define oname libcf
%define priority 40

Name: %oname-mpi
Version: 1.0
Release: alt3.beta1.2011092223

Summary: Manipulating of scientific data files which conform to the CF conventions
License: Open source
Group: File tools
Url: http://www.unidata.ucar.edu/software/libcf/

Source: %name-%version.tar
Patch0: port-to-python3.patch
Patch1: %oname-alt-fno-common.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: liblapack-devel gcc-fortran libuuid-devel
BuildRequires: libcurl-devel libnetcdf-mpi-devel

%description
The netCDF CF Library, or libCF, uses the netCDF API to aid in the
creation, processing and sharing of scientific data files which conform
to the Climate and Forecast (CF) conventions.

%package devel
Summary: Development files of libCF, the netCDF CF Library
Group: System/Libraries
Requires: %name = %EVR

%description devel
The netCDF CF Library, or libCF, uses the netCDF API to aid in the
creation, processing and sharing of scientific data files which conform
to the Climate and Forecast (CF) conventions.

This package contains development files of libCF.

%package -n python3-module-%name
Summary: Python bindings for libCF, the netCDF CF Library
Group: Development/Python3
Requires: %name = %EVR
Conflicts: python3-module-%oname

%description -n python3-module-%name
The netCDF CF Library, or libCF, uses the netCDF API to aid in the
creation, processing and sharing of scientific data files which conform
to the Climate and Forecast (CF) conventions.

This package contains python bindings for libCF.

%package examples
Summary: Examples for libCF, the netCDF CF Library
Group: Development/Documentation
Requires: %name = %EVR

%description examples
The netCDF CF Library, or libCF, uses the netCDF API to aid in the
creation, processing and sharing of scientific data files which conform
to the Climate and Forecast (CF) conventions.

This package contains examples for libCF.

%prep
%setup
%patch0 -p2
%patch1 -p2

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
	--enable-parallel \
	%nil

%make_build

%python3_build_debug

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

%python3_install

install -d %buildroot%hdfdir/bin
install -m755 examples/.libs/* %buildroot%hdfdir/bin
%make -C examples clean

# remove unpackaged files
find %buildroot -name '*.la' -delete
rm %buildroot%_prefix/pycf/libCFConfig.py

%files
%doc COPYRIGHT
%hdfdir/lib/*.so.*

%files devel
%hdfdir/include
%hdfdir/lib/*.so

%files examples
%doc examples
%hdfdir/bin

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Mon Dec 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt3.beta1.2011092223
- Fixed build with -fno-common.

* Tue Mar 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2.beta1.2011092223.1
- Porting to python3.

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1.beta1.2011092223.1
- Rebuilt with libnetcdf11-mpi.

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.beta1.2011092223
- Initial build for Sisyphus

