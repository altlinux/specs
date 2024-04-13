# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: lzfse
Version: 1.0
Release: alt1
Summary: LZFSE compression library and command line tool
License: BSD-3-Clause
Group: Archiving/Compression
Url: https://github.com/lzfse/lzfse
Requires: liblzfse = %EVR

Source: %name-%version.tar
Patch1: soname.patch
BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
%{?!_without_check:%{?!_disable_check:
BuildRequires: ctest
}}

%description
LZFSE is a Lempel-Ziv style data compression algorithm using Finite State
Entropy coding. It targets similar compression rates at higher compression and
decompression speed compared to deflate using zlib.

%package -n liblzfse
Summary: Library for %name
Group: System/Libraries

%description -n liblzfse
%summary.

%package -n liblzfse-devel
Summary: Development files for lib%name
Group: Development/C
Requires: liblzfse = %EVR

%description -n liblzfse-devel
%summary.

%prep
%setup
%autopatch -p1

%build
%ifarch x86_64
%add_optflags -fanalyzer
%endif
%add_optflags %(getconf LFS_CFLAGS)
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%_bindir/lzfse

%files -n liblzfse
%doc LICENSE
%_libdir/liblzfse.so.*

%files -n liblzfse-devel
%_includedir/lzfse.h
%_libdir/liblzfse.so

%changelog
* Sun Apr 14 2024 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- First import lzfse-1.0-2-ge634ca5 (2017-05-22).
