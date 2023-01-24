# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libkdumpfile
Version: 0.5.1
Release: alt1
Summary: Kernel coredump file access
License: GPL-2.0-or-later or LGPL-3.0-or-later
Group: System/Libraries
Url: https://github.com/ptesarik/libkdumpfile

Source: %name-%version.tar

BuildRequires: liblzo2-devel
BuildRequires: libsnappy-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel

%description
%summary.

%package utils
Summary: Example utils for %name
Group: Development/Other
Requires: %name = %EVR

%description utils
%summary.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
%summary.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --disable-static --without-python
%make_build

%install
%makeinstall_std

%check
%make_build check

%define _customdocdir %_docdir/%name

%files
%doc COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc README.md NEWS
%_libdir/libaddrxlat.so.*
%_libdir/libkdumpfile.so.*

%files utils
%_bindir/dumpattr
%_bindir/listxendoms
%_bindir/showxlat

%files devel
%_includedir/libkdumpfile
%_libdir/libaddrxlat.so
%_libdir/libkdumpfile.so
%_pkgconfigdir/libaddrxlat.pc
%_pkgconfigdir/libkdumpfile.pc

%changelog
* Tue Jan 24 2023 Vitaly Chikunov <vt@altlinux.org> 0.5.1-alt1
- Update to v0.5.1 (2023-01-21).

* Mon Nov 21 2022 Vitaly Chikunov <vt@altlinux.org> 0.5.0-alt1
- First import v0.5.0 (2022-08-12).
