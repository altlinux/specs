%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%global optflags_lto %optflags_lto -ffat-lto-objects
%global optflags %optflags -Ofast

Name: hpl
Version: 2.3
Release: alt1

Summary: The Linpack Benchmark

Group: Sciences/Other
License: BSD-4-Clause
Url: https://www.netlib.org/benchmark/hpl/

Source: %name-%version.tar

BuildRequires: libopenblas-devel liblapack-devel
BuildRequires: openmpi-devel autoconf-archive

%global desc \
HPL is a software package that solves a (random) dense linear system \
in double precision (64 bits) arithmetic on distributed-memory \
computers. It can thus be regarded as a portable as well as freely \
available implementation of the High Performance Computing Linpack\
Benchmark.

%description
%desc

%package devel-static
Summary: The Linpack Benchmark development files
Group: Sciences/Other

%description devel-static
%desc

This package contains libhpl.a and manual pages with its API documentation.

%package doc
Summary: The Linpack Benchmark development files
Group: Sciences/Other

%description doc
%desc

This package contains HPL HTML documentation.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export MPICC=mpicc
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pD -m0644 -t %buildroot%_man3dir man/man3/*.3
install -pD -m0644 -t %buildroot%_docdir/%name-%version/www www/*
install -p -m0644 -t %buildroot%_docdir/%name-%version \
    AUTHORS BUGS COPYING HISTORY NEWS README THANKS TUNING \
    testing/ptest/HPL.dat

%files
%_bindir/*
%exclude %_docdir/%name-%version/www
%_docdir/%name-%version/*

%files devel-static
%_libdir/*.a
%_man3dir/*

%files doc
%_docdir/%name-%version/www

%changelog
* Sat Nov 02 2024 Andrew Savchenko <bircoph@altlinux.org> 2.3-alt1
- Initial version.
