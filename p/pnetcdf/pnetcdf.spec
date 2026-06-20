%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define mpiimpl mpich
%define mpidir %_libdir/%mpiimpl

%define sover 7

Name: pnetcdf
Version: 1.14.1
Release: alt1

Summary: Parallel netCDF: A High Performance API for NetCDF File Access
License: NetCDF
Group: File tools

Url: https://parallel-netcdf.github.io/
VCS: https://github.com/Parallel-NetCDF/PnetCDF
Source: %name-%version.tar

BuildRequires(pre): %mpiimpl-devel
BuildRequires: flex gcc-fortran
BuildRequires: libtool

%description
Parallel netCDF (PnetCDF) is a library providing high-performance I/O
while still maintaining file-format compatibility with Unidata's NetCDF.

NetCDF gives scientific programmers a space-efficient and portable means
for storing data. However, it does so in a serial manner, making it
difficult to achieve high I/O performance. By making some small changes
to the API specified by NetCDF, we can use MPI-IO and its collective
operations.

%package -n lib%name%sover
Summary: Shared library of Parallel netCDF
Group: System/Libraries

%description -n lib%name%sover
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
Requires: lib%name%sover = %EVR
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
# ALT ships libtool 2.4.x; upstream only asserts a newer version, no 2.5 features used
sed -i -e 's/LT_PREREQ(\[2\.5\.4\])/LT_PREREQ([2.4.2])/' configure.ac
rm -fR autom4te.cache

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags %optflags_shared -DNDEBUG -Df2cFortran -I%mpidir/lib
export FCFLAGS="%optflags -fallow-argument-mismatch"
export F90FLAGS="%optflags"
# sequential utility programs (ncvalidator, ncoffsets, cdfdiff, pnetcdf_version)
# are built with SEQ_CC and default to no flags - give them %optflags so they
# carry debug info like the rest
export SEQ_CFLAGS="%optflags"
%autoreconf
%configure \
	--with-mpi=%mpidir \
	--enable-shared \
	--disable-static \
	--enable-mpi-io-test \
	--enable-fortran \
	--enable-strict \
	%nil

%make

%install
source %mpidir/bin/mpivars.sh
export LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall

# fix libdir in pkg-config file on lib64 systems
sed -i -e "s|\${exec_prefix}/lib\b|\${exec_prefix}/lib%_libsuff|" %buildroot%_pkgconfigdir/*.pc

# drop libtool archives and static libs
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/*.a

%files
%doc COPYRIGHT CREDITS README*
%_bindir/*
%_man1dir/*

%files -n lib%name%sover
%_libdir/*.so.%sover
%_libdir/*.so.%sover.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_man3dir/*
%_pkgconfigdir/*.pc

%files -n lib%name-devel-doc
%doc doc/*.md doc/*.txt examples

%changelog
* Sat Jun 20 2026 Anton Farygin <rider@altlinux.org> 1.14.1-alt1
- 1.8.1 -> 1.14.1

* Mon Sep 30 2024 Michael Shigorin <mike@altlinux.org> 1.8.1-alt4
- Minor spec cleanup
  + ...and a release bump to facilitate upgrade of the e2k fork.

* Fri Apr 05 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.8.1-alt3.1
- The compiler for e2k finally knowns -fallow-argument-mismatch.

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

