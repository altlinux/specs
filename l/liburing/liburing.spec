# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: liburing
Version: 2.1
Release: alt1

Summary: Linux-native io_uring I/O access library
License: (GPL-2.0-only AND LGPL-2.1-or-later) OR MIT
Group: System/Libraries

Url: http://git.kernel.dk/cgit/liburing
Source: %name-%version.tar
BuildRequires: gcc-c++
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc}}

%description
Provides native async IO for the Linux 5.1+ kernel, in a fast
and efficient manner, for both buffered and O_DIRECT.

liburing provides helpers to setup and teardown io_uring instances,
and also a simplified interface for applications that don't need
(or want) to deal with the full kernel side implementation.

%package devel
Summary: Development files for Linux-native io_uring I/O access library
Group: Development/C

%description devel
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%package devel-static
Summary: Static library for developing apps using Linux-native io_uring
Group: Development/C
Requires: %name-devel

%description devel-static
This package contains the static library needed to develop statically
linked programs that use Linux-native io_uring.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS) -ffat-lto-objects
./configure \
	--prefix=%_prefix \
	--includedir=%_includedir \
	--libdir=%_libdir \
	--libdevdir=%_libdir \
	--mandir=%_mandir \
	#
%make_build --no-print-directory CFLAGS="%optflags" V=1

%install
%makeinstall_std V=1

%ifnarch ppc64le %e2k
# Almost all tests fail on ppc64le, so there is no point to even try.
%check
make runtests
%endif

%files
%_libdir/liburing.so.*
%doc COPYING

%files devel
%doc README LICENSE
%_includedir/*
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man2dir/*
%_man3dir/*
%_man7dir/*

%files devel-static
%_libdir/%name.a

%changelog
* Sun Oct 24 2021 Vitaly Chikunov <vt@altlinux.org> 2.1-alt1
- Update to liburing-2.1 (2021-09-09).
- Fix LTO build.

* Sat Jun 05 2021 Vitaly Chikunov <vt@altlinux.org> 2.0-alt1
- Update to liburing-2.0 (2021-02-28).

* Wed Nov 25 2020 Alexey Shabalin <shaba@altlinux.org> 0.7-alt1
- new version 0.7

* Thu Apr 30 2020 Alexey Shabalin <shaba@altlinux.org> 0.6-alt1
- Updated to upstream commit 8171778c835b6be517c314cf23dd1f5ae061a117.

* Mon Jun 17 2019 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt4
- Updated to upstream commit 043ea2257fb692324f1cb491ae092cdcb311732a.

* Mon May 20 2019 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt3
- Updated to upstream commit 375bed76ba7292122f828fbf49c2b530506fdce8
  that adds support for all mainline architectures.

* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- added ExclusiveArch: since aarch64 is not supported yet

* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- built for sisyphus (based on upstream spec with cleanups)

* Tue Jan 8 2019 Jens Axboe <axboe@kernel.dk> - 0.1
- Initial version
