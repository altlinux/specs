# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libdeflate
Version: 1.10
Release: alt1
Summary: Heavily optimized library for DEFLATE/zlib/gzip compression and decompression
License: MIT
Group: System/Libraries
Url: https://github.com/ebiggers/libdeflate

Source: %name-%version.tar

BuildRequires: zlib-devel

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
sed -i s/-fomit-frame-pointer// Makefile

%build
%add_optflags %(getconf LFS_CFLAGS)
# It's sensitive to build options, avoid "Rebuilding due to new settings".
%global build_settings CFLAGS="%optflags" PREFIX=%_prefix LIBDIR=%_libdir USE_SHARED_LIB=1
%make_build %build_settings all test_programs V=1

%install
%makeinstall_std %build_settings V=1
rm %buildroot%_libdir/%name.a

%check
%make_build %build_settings check V=1

%files
%doc COPYING
%_libdir/libdeflate.so.*

%files devel
%doc NEWS.md README.md
%_includedir/libdeflate.h
%_libdir/libdeflate.so
%_pkgconfigdir/libdeflate.pc

%files utils
%_bindir/libdeflate-*

%changelog
* Sat Mar 26 2022 Vitaly Chikunov <vt@altlinux.org> 1.10-alt1
- Update to v1.10 (2022-02-06).

* Mon Nov 29 2021 Vitaly Chikunov <vt@altlinux.org> 1.8-alt1
- First import of v1.8-5-ga62d361 (2021-11-23).
