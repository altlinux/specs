%define _unpackaged_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name:    hpcc
Version: 1.5.0
Release: alt1

Summary: HPC Challenge Benchmark
License: BSD-3-Clause
Group:   Monitoring
Url:     https://github.com/icl-utk-edu/hpcc

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: openmpi-devel
BuildRequires: libopenblas-devel
BuildRequires: hevea
BuildRequires: python2-base

Requires: openmpi

%description
The High Performance Computing (HPC) Challenge benchmark runs a suite
of 7 tests that measure the performance of CPU, memory and network for
HPC clusters.  Amongst others, it includes the High-Performance LINPACK
(HPL) benchmark, used by the Top500 ranking (http://www.top500.org/).

%prep
%setup
%patch -p1
cp -v _hpccinf.txt hpccinf.txt

%build

mpi-selector --yes --set %mpiimpl
source %mpidir/bin/mpivars.sh

make arch=ALTLinux \
     CFLAGS="$RPM_OPT_FLAGS" \
     CC=%mpidir/bin/mpicc \
     LINKER=%mpidir/bin/mpif90
make readme

%install
install -pDm 755 hpcc %buildroot%_bindir/%name
install -pDm 644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc hpccinf.txt
%doc hpl/BUGS hpl/TODO hpl/TUNING hpl/www README.ALT README.txt README.html
%_bindir/%name
%_man1dir/%name.*

%changelog
* Fri Jan 31 2025 Nikolay Strelkov <snk@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus
