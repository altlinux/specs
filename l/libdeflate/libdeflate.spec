# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libdeflate
Version: 1.18
Release: alt1

Summary: Heavily optimized library for DEFLATE/zlib/gzip compression and decompression
License: MIT
Group: System/Libraries
Url: https://github.com/ebiggers/libdeflate

Source: %name-%version.tar

%define valgrind_arches %ix86 x86_64 aarch64
# armh is excluded due to https://bugzilla.altlinux.org/43475
# ppc64le is excluded due to requirement on glibc-core-debuginfo

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: zlib-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: banner
%ifarch %valgrind_arches
BuildRequires: /proc
BuildRequires: valgrind
%endif
}}

%description
libdeflate is a library for fast, whole-buffer DEFLATE-based compression
and decompression.

The supported formats are:

    DEFLATE (raw)
    zlib (a.k.a. DEFLATE with a zlib wrapper)
    gzip (a.k.a. DEFLATE with a gzip wrapper)

libdeflate is heavily optimized. It is significantly faster than the zlib
library, both for compression and decompression, and especially on x86
processors. In addition, libdeflate provides optional high compression
modes that provide a better compression ratio than the zlib's "level 9".

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
%summary.

%package utils
Summary: Command-line programs which use libdeflate
Group: Archiving/Compression

%description utils
libdeflate itself is a library, but the following command-line programs
which use this library are also provided:

libdeflate-gzip (or libdeflate-gunzip), a program which mostly behaves
like the standard equivalent, except that it does not yet have good
streaming support and therefore does not yet support very large files

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS) -Werror
%ifnarch %e2k
# unsupported as of lcc 1.25
%add_optflags -fanalyzer
%endif
# It's sensitive to build options, avoid "Rebuilding due to new settings".
%cmake \
	-DLIBDEFLATE_BUILD_STATIC_LIB=OFF \
	-DLIBDEFLATE_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
banner check
%cmake_build --target test

export PATH=%buildroot%_bindir:$PATH LD_LIBRARY_PATH=%buildroot%_libdir
libdeflate-gzip -V

%ifarch %valgrind_arches
%define valgrind valgrind -q --error-exitcode=2
# Unfortunately `--extra-debuginfo-path=` does not work with %%buildroot.
%else
%define valgrind time
%endif
set -o pipefail
head -11111111c /dev/urandom > test-file
b2sum test-file | tee test-file.b2sum
cp test-file test-file-copy
gzip -c test-file-copy |
	%valgrind libdeflate-gunzip |
	%valgrind libdeflate-gzip |
	gunzip > test-file
b2sum test-file
b2sum --check test-file.b2sum

%files
%doc COPYING
%_libdir/libdeflate.so.*

%files devel
%doc NEWS.md README.md
%_includedir/libdeflate.h
%_libdir/libdeflate.so
%_pkgconfigdir/libdeflate.pc
%_libdir/cmake/libdeflate

%files utils
%_bindir/libdeflate-*

%changelog
* Sat Mar 25 2023 Vitaly Chikunov <vt@altlinux.org> 1.18-alt1
- Update to v1.18 (2023-03-23).

* Sun Sep 11 2022 Vitaly Chikunov <vt@altlinux.org> 1.14-alt1
- Update to v1.14 (2022-09-10).

* Mon Sep 05 2022 Michael Shigorin <mike@altlinux.org> 1.13-alt2
- E2K: avoid lcc-unsupported option
- Minor spec cleanup

* Mon Aug 08 2022 Vitaly Chikunov <vt@altlinux.org> 1.13-alt1
- Update to v1.13 (2022-08-04).

* Mon Jun 13 2022 Vitaly Chikunov <vt@altlinux.org> 1.12-alt1
- Update to v1.12 (2022-06-12).
- This release focuses on improving the performance of the CRC-32 and
  Adler-32 checksum algorithms on x86 and ARM (both 32-bit and 64-bit).

* Thu May 26 2022 Vitaly Chikunov <vt@altlinux.org> 1.11-alt1
- Update to v1.11 (2022-05-23).

* Sat Mar 26 2022 Vitaly Chikunov <vt@altlinux.org> 1.10-alt1
- Update to v1.10 (2022-02-06).

* Mon Nov 29 2021 Vitaly Chikunov <vt@altlinux.org> 1.8-alt1
- First import of v1.8-5-ga62d361 (2021-11-23).
