# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libcpucycles
Version: 20230105
Release: alt1
Summary: Microlibrary for counting CPU cycles
License: CC0
Group: Development/C
Url: https://cpucycles.cr.yp.to/

Source: %name-%version.tar
BuildRequires: python3

%description
libcpucycles is a public-domain microlibrary for counting CPU
cycles. Cycle counts are not as detailed as Falk diagrams but are the
most precise timers available to typical software; they are central
tools used in understanding and improving software performance.

The libcpucycles API is simple: include <cpucycles.h>, call cpucycles()
to receive a long long whenever desired, and link with -lcpucycles.

Internally, libcpucycles understands machine-level cycle counters for
amd64 (both PMC and TSC), arm32, arm64 (both PMC and VCT), mips64,
ppc32, ppc64, riscv32, riscv64, sparc64, and x86. libcpucycles also
understands four OS-level mechanisms, which give varying levels of
accuracy: mach_absolute_time, perf_event, CLOCK_MONOTONIC, and, as a
fallback, microsecond-resolution gettimeofday.

When the program first calls cpucycles(), libcpucycles automatically
benchmarks the available mechanisms and selects the mechanism that
does the best job. Subsequent cpucycles() calls are thread-safe and
very fast. An accompanying cpucycles-info program prints a summary of
cycle-counter accuracy.

%package devel
Summary: Develpment files for %name
Group: Development/C

%description devel
%summary.

%prep
%setup

%build
cd libcpucycles
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
echo "gcc %optflags -fPIC -fwrapv -fvisibility=hidden" > compilers/default
./configure --prefix=%buildroot/usr
sed -i 's/\bgcc\b/set -x \&\& &/' $(grep -r -w gcc -I -l build)
%make_build

%install
cd libcpucycles
%makeinstall_std
rm %buildroot/usr/lib/libcpucycles.a
# Fix incorrect installs.
[ -d %buildroot%_libdir ] || mv %buildroot/usr/lib %buildroot%_libdir
mkdir -p %buildroot%_mandir
mv %buildroot/usr/man/man3 %buildroot%_man3dir

%define _customdocdir %_docdir/%name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir PATH=%buildroot%_bindir
cpucycles-info

%files
%_libdir/libcpucycles.so.*

%files devel
%doc libcpucycles/doc/*.md
%_bindir/cpucycles-info
%_includedir/cpucycles.h
%_libdir/libcpucycles.so
%_man3dir/cpucycles.3*

%changelog
* Thu Jan 05 2023 Vitaly Chikunov <vt@altlinux.org> 20230105-alt1
- First import 20230105 (2023-01-05).
