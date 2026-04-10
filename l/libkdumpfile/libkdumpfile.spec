# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define kdumpid_version 1.7
Name: libkdumpfile
Version: 0.5.6
Release: alt1
Summary: Kernel coredump file access
License: GPL-2.0-or-later or LGPL-3.0-or-later
Group: System/Libraries
Url: https://codeberg.org/ptesarik/pykdumpfile

Source: %name-%version.tar

BuildRequires: binutils-devel
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
Requires: kdumpid = %kdumpid_version-%release%{?disttag::%disttag}

%description utils
%summary.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
%summary.

%package -n kdumpid
Summary: Identify any kernel core dump file
Group: Development/Kernel
Requires: %name = %EVR
Version: %kdumpid_version

%description -n kdumpid
The kdumpid utility can be used to find out the exact kernel architecture and
version of an unknown kernel core dump.

This utility should provide a fast and reliable method to find out the most
important information about an unknown kernel crash dump, such as the
architecture and kernel release. Think of it as a kind of "file" utility for
kernel dumps.

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
tools/kdumpid/kdumpid --version | grep -P 'kdumpid version \Q%kdumpid_version\E$'
%make_build check

%files
%doc README.md NEWS COPYING*
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

%files -n kdumpid
%_bindir/kdumpid
%_man1dir/kdumpid.1*

%changelog
* Fri Apr 10 2026 Vitaly Chikunov <vt@altlinux.org> 0.5.6-alt1
- Update to v0.5.6 (2025-11-05).

* Sun Nov 19 2023 Vitaly Chikunov <vt@altlinux.org> 0.5.4-alt1
- Update to v0.5.4 (2023-11-18).

* Tue Nov 07 2023 Vitaly Chikunov <vt@altlinux.org> 0.5.3-alt1
- Update to v0.5.3 (2023-11-06).

* Wed Jul 19 2023 Vitaly Chikunov <vt@altlinux.org> 0.5.2-alt1
- Update to v0.5.2 (2023-07-17).

* Tue Jan 24 2023 Vitaly Chikunov <vt@altlinux.org> 0.5.1-alt1
- Update to v0.5.1 (2023-01-21).

* Mon Nov 21 2022 Vitaly Chikunov <vt@altlinux.org> 0.5.0-alt1
- First import v0.5.0 (2022-08-12).
