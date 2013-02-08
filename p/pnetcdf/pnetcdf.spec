%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define sover 0

Name: pnetcdf
Version: 1.3.1
Release: alt1
Summary: Parallel netCDF: A High Performance API for NetCDF File Access
License: Open source
Group: File tools
Url: http://trac.mcs.anl.gov/projects/parallel-netcdf
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel flex

%description
Parallel netCDF (PnetCDF) is a library providing high-performance I/O
while still maintaining file-format compatibility with Unidata's NetCDF.

NetCDF gives scientific programmers a space-efficient and portable means
for storing data. However, it does so in a serial manner, making it
difficult to achieve high I/O performance. By making some small changes
to the API specified by NetCDF, we can use MPI-IO and its collective
operations.

%package -n lib%name
Summary: Shared library of Parallel netCDF
Group: System/Libraries

%description -n lib%name
Parallel netCDF (PnetCDF) is a library providing high-performance I/O
while still maintaining file-format compatibility with Unidata's NetCDF.

NetCDF gives scientific programmers a space-efficient and portable means
for storing data. However, it does so in a serial manner, making it
difficult to achieve high I/O performance. By making some small changes
to the API specified by NetCDF, we can use MPI-IO and its collective
operations.

This package contains shared library of Parallel netCDF.

%package -n lib%name-devel
Summary: Development files of Parallel netCDF
Group: Development/Other
Requires: lib%name = %version-%release
Requires: %mpiimpl-devel

%description -n lib%name-devel
Parallel netCDF (PnetCDF) is a library providing high-performance I/O
while still maintaining file-format compatibility with Unidata's NetCDF.

NetCDF gives scientific programmers a space-efficient and portable means
for storing data. However, it does so in a serial manner, making it
difficult to achieve high I/O performance. By making some small changes
to the API specified by NetCDF, we can use MPI-IO and its collective
operations.

This package contains development files of Parallel netCDF.

%package -n lib%name-devel-doc
Summary: Documentation and examples for Parallel netCDF
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Parallel netCDF (PnetCDF) is a library providing high-performance I/O
while still maintaining file-format compatibility with Unidata's NetCDF.

NetCDF gives scientific programmers a space-efficient and portable means
for storing data. However, it does so in a serial manner, making it
difficult to achieve high I/O performance. By making some small changes
to the API specified by NetCDF, we can use MPI-IO and its collective
operations.

This package contains development documentation and examples for
Parallel netCDF.

%prep
%setup
rm -fR autom4te.cache

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags %optflags_shared -DNDEBUG -Df2cFortran
%autoreconf
%configure \
	--with-mpi=%mpidir \
	--enable-mpi-io-test \
	--enable-fortran \
	--enable-strict
%ifarch x86_64
LIB_SUFFIX=64
%endif
%make SOVER=%sover LIB_SUFFIX=$LIB_SUFFIX

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%ifarch x86_64
LIB_SUFFIX=64
%endif
%makeinstall LIB_SUFFIX=$LIB_SUFFIX

%files
%doc COPYRIGHT CREDITS README*
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_man3dir/*

%files -n lib%name-devel-doc
%doc doc/*.pdf doc/*.txt examples

%changelog
* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

