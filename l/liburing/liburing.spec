# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: liburing
Version: 2.7
Release: alt1
Summary: The io_uring library
License: (GPL-2.0-only AND LGPL-2.1-or-later) OR MIT
Group: System/Libraries
Url: http://git.kernel.dk/cgit/liburing
# Author's Vcs and CI: https://github.com/axboe/liburing

Source: %name-%version.tar
Patch: liburing-e2k.patch

BuildRequires: gcc-c++
%{?!_without_check:%{?!_disable_check:BuildRequires: strace /proc rpm-build-vm iproute2}}

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

liburing provides helpers to setup and teardown io_uring instances,
and also a simplified interface for applications that don't need
(or want) to deal with the full kernel side implementation.

%package devel
Summary: Development files for Linux-native io_uring I/O access library
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%prep
%setup
%ifarch %e2k
%patch -p1
%endif

%build
%add_optflags %(getconf LFS_CFLAGS) -ffat-lto-objects
./configure \
	--prefix=%_prefix \
	--includedir=%_includedir \
	--libdir=%_libdir \
	--libdevdir=%_libdir \
	--mandir=%_mandir \
	%nil
%make_build --no-print-directory CFLAGS="%optflags" V=1

%install
%makeinstall_std V=1
rm %buildroot%_libdir/liburing*.a
# Reuse probe test as a tool to test that io_uring is available.
install -Dp test/probe.t %buildroot%_bindir/io_uring_ok

%check
uname -rm
# List of available probes
test/probe.t
strace -v test/probe.t

# Almost all tests fail on ppc64le, so there is no point to even try.
%ifnarch %e2k
TEST_EXCLUDE="
%ifarch aarch64
	accept-non-empty.t
%endif
%ifarch ppc64le
	buf-ring-nommap.t
	no-mmap-inval.t
	recv-multishot.t
	reg-fd-only.t
	send-zerocopy.t
%endif
%ifarch %ix86
	sqpoll-sleep.t
%endif
" vm-run --ext4 make runtests
%endif

%define _customdocdir %_docdir/%name

%files
%_bindir/io_uring_ok
%_libdir/liburing*.so.*
%doc LICENSE

%files devel
%doc README COPYING COPYING.GPL SECURITY.md CHANGELOG examples/*.c
%exclude %_docdir/%name/LICENSE
%_includedir/liburing*
%_libdir/liburing*.so
%_pkgconfigdir/liburing*.pc
%_man2dir/io_uring*.2*
%_man3dir/IO_URING*.3*
%_man3dir/__io_uring*.3*
%_man3dir/io_uring*.3*
%_man7dir/io_uring.7*

%changelog
* Sat Aug 17 2024 Vitaly Chikunov <vt@altlinux.org> 2.7-alt1
- Update to liburing-2.7 (2024-08-16).

* Wed May 01 2024 Vitaly Chikunov <vt@altlinux.org> 2.6-alt1
- Update to liburing-2.6 (2024-04-30).

* Sun Nov 05 2023 Vitaly Chikunov <vt@altlinux.org> 2.5-alt1
- Update to liburing-2.5 (2023-11-04).

* Sun Jun 11 2023 Vitaly Chikunov <vt@altlinux.org> 2.4-alt1
- Update to liburing-2.4-0-gb4ee310 (2023-06-09).
- FFI support.
- Nolibc build (default selected by the upstream, which turns off hardening).

* Thu Apr 27 2023 Michael Shigorin <mike@altlinux.org> 2.3-alt3
- E2K: fix build (ilyakurdyukov@).

* Thu Jan 26 2023 Vitaly Chikunov <vt@altlinux.org> 2.3-alt2
- Add 'io_uring_ok' tool.

* Thu Nov 03 2022 Vitaly Chikunov <vt@altlinux.org> 2.3-alt1
- Update to liburing-2.3 (2022-10-26).
- spec: Better strace run in %%check.

* Tue Aug 09 2022 Vitaly Chikunov <vt@altlinux.org> 2.2-alt1
- Update to liburing-2.2 (2022-06-23).
- Do not install static library (liburing.a).

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
