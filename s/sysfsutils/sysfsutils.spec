# vim: set ft=spec: -*- rpm-spec -*-

%def_enable static

%define _unpackaged_files_terminate_build 1

Name: sysfsutils
Version: 2.1.0
Release: alt6.1

%define lib_name libsysfs
%define docdir %_docdir/%lib_name-%version

Summary: Utility suite to enjoy sysfs
Group: System/Kernel and hardware
License: GPL
Url: http://linux-diag.sourceforge.net/Sysfsutils.html
Packager: Alexey I. Froloff <raorn@altlinux.org>

Requires: %lib_name = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Source1: sysfs.conf
Source2: sysfs.init

%package -n %lib_name
Summary: Main library for %name
License: LGPL
Group: System/Libraries

%package -n %lib_name-devel
Summary: Headers for developing programs that will use %lib_name
License: LGPL
Group: Development/C
Requires: %lib_name = %version-%release

%package -n %lib_name-devel-static
Summary: Static library for developing programs that will use %lib_name
License: LGPL
Group: Development/C
Requires: %lib_name-devel = %version-%release
Obsoletes: %lib_name-static-devel

%description
This package's purpose is to provide a set of utilities for interfacing
with sysfs, a virtual filesystem in Linux kernel versions 2.5+ that
provides a tree of system devices.  While a filesystem is a very useful
interface, we've decided to provide a stable programming interface that
will hopefully make it easier for applications to query system devices
and their attributes.

%description -n %lib_name
This package contains the library needed to run programs dynamically
linked with %lib_name.

%description -n %lib_name-devel
This package contains the headers that programmers will need to develop
applications which will use %lib_name.

%description -n %lib_name-devel-static
This package contains the static library that programmers will need to
develop applications which will use %lib_name.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	%{subst_enable static}
%make_build

%check
%make_build -k check

%install
mkdir -p %buildroot{/%_lib,%docdir,%_sysconfdir,%_initdir}

%makeinstall_std

v=`objdump -p %buildroot%_libdir/%lib_name.so |awk '/SONAME/ {print $2}'`
[ -n "$v" ]
mv -v %buildroot%_libdir/%lib_name.so.* %buildroot/%_lib
ln -sf "../../%_lib/$v" %buildroot%_libdir/%lib_name.so

install -p -m644 %_sourcedir/sysfs.conf %buildroot%_sysconfdir/sysfs.conf
install -p -m755 %_sourcedir/sysfs.init %buildroot%_initdir/sysfs

install -p -m644 AUTHORS CREDITS ChangeLog NEWS TODO docs/*.txt %buildroot%docdir/
bzip2 -9f %buildroot%docdir/{ChangeLog,*.txt}

%post
%post_service sysfs

%preun
%preun_service sysfs

%files
%config(noreplace) %_sysconfdir/sysfs.conf
%_initdir/sysfs
%_bindir/*
%_man1dir/*

%files -n %lib_name
/%_lib/%lib_name.so.*
%dir %docdir
%docdir/[A-Z]*

%files -n %lib_name-devel
%_libdir/%lib_name.so
%_includedir/*
%dir %docdir
%docdir/[a-z]*

%if_enabled static
%files -n %lib_name-devel-static
%_libdir/%lib_name.a
%endif

%changelog
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
