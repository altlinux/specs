# vim: set ft=spec: -*- rpm-spec -*-
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define sover 2
Name: sysfsutils
Version: 2.1.1
Release: alt1
Summary: Utilities for interfacing with sysfs
Group: System/Kernel and hardware
License: GPL-2.0
Url: http://linux-diag.sourceforge.net/Sysfsutils.html
Vcs: https://github.com/linux-ras/sysfsutils
Requires: libsysfs%sover = %EVR

Source: %name-%version.tar

%package -n libsysfs%sover
Summary: Library for interfacing with sysfs
License: LGPL-2.1-or-later
Group: System/Libraries
Obsoletes: libsysfs < %EVR

%package -n libsysfs-devel
Summary: Headers for developing programs that will use libsysfs
License: LGPL-2.1-or-later
Group: Development/C
Requires: libsysfs%sover = %EVR

%description
This package's purpose is to provide a set of utilities for interfacing
with sysfs, a virtual filesystem in Linux kernel versions 2.5+ that
provides a tree of system devices.  While a filesystem is a very useful
interface, we've decided to provide a stable programming interface that
will hopefully make it easier for applications to query system devices
and their attributes.

%description -n libsysfs%sover
This package contains the library needed to run programs dynamically
linked with libsysfs.

%description -n libsysfs-devel
This package contains the headers that programmers will need to develop
applications which will use libsysfs.

%prep
%setup

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --disable-static
%make_build

%install
mkdir -p %buildroot{/%_lib,%_sysconfdir,%_initdir,%_unitdir}

%makeinstall_std

v=`objdump -p %buildroot%_libdir/libsysfs.so |awk '/SONAME/ {print $2}'`
[ -n "$v" ]
mv -v %buildroot%_libdir/libsysfs.so.* %buildroot/%_lib
ln -sf "../../%_lib/$v" %buildroot%_libdir/libsysfs.so

%check
# Only compiles examples but does not run them.
%make_build check

%files
%doc COPYING cmd/GPL
%_bindir/*
%_man1dir/*.1*

%files -n libsysfs%sover
%doc AUTHORS CREDITS lib/LGPL
/%_lib/libsysfs.so.%sover
/%_lib/libsysfs.so.%sover.*

%files -n libsysfs-devel
%doc docs/*.txt TODO README
%_libdir/libsysfs.so
%_includedir/*
%_pkgconfigdir/libsysfs.pc

%changelog
* Fri May 26 2023 Vitaly Chikunov <vt@altlinux.org> 2.1.1-alt1
- Update to v2.1.1-13-g085bba6 (2021-07-23).
- Do not package libsysfs-devel-static.
- Enabled LFS support.
- Do not package (Debianish) sysfs sysv/systemd services.

* Wed Oct 27 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.1.0-alt9
- FTBFS: build with LTO

* Wed Jul  1 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.0-alt8
- Add systemd unit file (ALT#31048)

* Tue Jul 08 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt7
- NMU: update init script:
  + do not auto enable service
  + add LSB header

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1.0-alt6.1.qa1
- NMU: rebuilt for updated dependencies.

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt6.1
- Rebuilt for debuginfo

* Mon Nov 09 2009 Alexey I. Froloff <raorn@altlinux.org> 2.1.0-alt6
- spec cleanup

* Sun Jul 06 2008 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt5
- Applied patch from Deb#481015, better symlink resolving (closes: #16274)
- Try to add trailing newline if attribute setting fails

* Tue Apr 15 2008 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt4
- Do not package test programs (closes: #13428)

* Thu Feb 22 2007 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt3
- Shared library moved from %%_libdir to /%%_lib (closes: #10891)

* Sat Feb 03 2007 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt2
- Fix header location

* Tue Jan 30 2007 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt1
- [2.1.0]
- Spec cleanup, removed summary/description translations (use packages-info-i18n)
- static-devel subpackage renamed to devel-static
- Disabled klibc in configure.ac
- Added symbol version script, thanx to at@, ldv@, vsu@
- Applied get_mnt_path_check.patch from debian:
 + sysfs_get_mnt_path(): Check that sysfs is actually mounted and fail if
   not. Fixes behavioural breakage compared to 1.3.
- Added /etc/sysfs.conf and sysfs service (idea taken from debian)
- Do not package dlist_test program

* Tue Dec 20 2005 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- new version

* Wed Jun 22 2005 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- new version

* Wed Nov 17 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt2
- Corrected package license information.
- Corrected interpackage dependencies.
- Changed documentation packaging.

* Thu Nov 11 2004 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- update by Alexey Morozov:
    - New version (1.2.0)
    - Header files moved to %_includedir/sysfs
    - Russian translation added to spec

* Fri Jul 23 2004 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2
- patch for use headers libsysfs-devel from C++ code

* Thu May 20 2004 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- first build for Sisyphus
