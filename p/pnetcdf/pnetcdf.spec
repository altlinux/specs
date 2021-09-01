%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define sover 0

Name: pnetcdf
Version: 1.8.1
Release: alt3
Summary: Parallel netCDF: A High Performance API for NetCDF File Access
License: Open source
Group: File tools
Url: http://trac.mcs.anl.gov/projects/parallel-netcdf

Source: %name-%version.tar

Patch1: %name-%version-alt-build.patch

BuildRequires(pre): %mpiimpl-devel
BuildRequires: flex gcc-fortran
BuildRequires: ghostscript-utils texlive-latex-base
BuildRequires: tex(dehypht.tex)

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
Requires: lib%name = %EVR
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
%patch1 -p2
rm -fR autom4te.cache

%build
sed -i -e "s|@LIB_SUFFIX@|%_libsuff|g" pnetcdf_pc.in

mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags %optflags_shared -DNDEBUG -Df2cFortran -I%mpidir/lib
export FCFLAGS="%optflags"
%ifnarch %e2k
export FCFLAGS="$FCFLAGS -fallow-argument-mismatch"
%endif
export F90FLAGS="%optflags"
%autoreconf
%configure \
	--with-mpi=%mpidir \
	--enable-mpi-io-test \
	--enable-fortran \
	--enable-strict \
	%nil

%make SOVER=%sover LIB_SUFFIX=%_libsuff
%make -C doc

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall SOVER=%sover LIB_SUFFIX=%_libsuff

# fix pkg-config file
sed -i -e "s|%buildroot||" %buildroot%_pkgconfigdir/*.pc

rm -f %buildroot%_libdir/*.so.
rm -f %buildroot%_libdir/*.a

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
%_pkgconfigdir/*.pc

%files -n lib%name-devel-doc
%doc doc/*.pdf doc/*.txt examples

%changelog
* Wed Sep 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.1-alt3
- Fixed build with LTO.

* Tue Apr 13 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.1-alt2.3
- Fixed -fallow-argument-mismatch for %%e2k arches.

* Thu Apr 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.1-alt2.2
- Fixed FTBFS.

* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2.1
- NMU: applied logoved fixes

* Tue Jul 02 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2
- NMU: fixed LIB_SUFFIX= on non-x86_64

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.1-alt1
- Updated to upstream version 1.8.1.

* Thu Mar 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1
- Version 1.6.0

* Wed Jul 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Version 1.5.0

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.pre1
- Version 1.5.0.pre1

* Mon Nov 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

