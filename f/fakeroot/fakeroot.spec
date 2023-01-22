Name: fakeroot
Version: 1.29
Release: alt1

Summary: Run a command in an environment faking root privileges for file manipulation
License: GPLv3+
Group: Development/Other
Url: http://packages.qa.debian.org/f/fakeroot.html

# http://git.altlinux.org/people/ldv/packages/?p=fakeroot.git
Source: %name-%version-%release.tar

Requires: getopt
BuildRequires: gcc-c++, libacl-devel, libcap-devel
%{!?_without_check:%{!?_disable_check:BuildRequires: sharutils}}

%description
fakeroot runs a command in an environment were it appears to have root
privileges for file manipulation.  This is useful for allowing users to
createarchives (tar, ar, .rpm etc.) with files in them with root
permissions/ownership.  Without fakeroot one would have to have root
privileges to create the constituent files of the archives with the
correct permissions and ownership, and then pack them up, or one would
have to construct the archives directly, without using the archiver.

%prep
%setup -n %name-%version-%release
echo 'define(FAKEROOT_VERSION, %version)' >acinclude.m4

%build
grep -FZrl sys: test |
	xargs -r0 sed -i "s/sys:/bin:/g" --
grep -FZrl :sys test |
	xargs -r0 sed -i "s/:sys/:bin/g" --
mkdir build-aux
autoreconf -fisv
%configure --libdir=%_libdir/libfakeroot --enable-static=no
%make_build LIBCPATH=/%_lib/libc.so.6

%check
%make_build -k check VERBOSE=1

%install
%makeinstall libdir=%buildroot%_libdir/libfakeroot
find %buildroot%_libdir -type f -name \*.la -delete

%files
%_bindir/*
%_libdir/libfakeroot
%_mandir/man?/*
%doc doc/README* DEBUG

%changelog
* Sat Jan 21 2023 Dmitry V. Levin <ldv@altlinux.org> 1.29-alt1
- 1.28 -> 1.29.
- Wrap syscall function.

* Thu Apr 28 2022 Dmitry V. Levin <ldv@altlinux.org> 1.28-alt1
- 1.25.3 -> 1.28.
- Added support for stat-related *_time64 functions.

* Thu Feb 18 2021 Dmitry V. Levin <ldv@altlinux.org> 1.25.3-alt1
- 1.20.2 -> 1.25.3.

* Tue May 07 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.20.2-alt2
- Fixed build on ppc64le.

* Tue May 10 2016 Dmitry V. Levin <ldv@altlinux.org> 1.20.2-alt1
- 1.18.4 -> 1.20.2.
- Fixed irrelevant noise with recent changes in glibc.
- Added fts64 support.

* Wed Apr 17 2013 Dmitry V. Levin <ldv@altlinux.org> 1.18.4-alt1
- Updated to 1.18.4.

* Mon Apr 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.12.2-alt1
- Updated to 1.12.2.

* Wed Sep 24 2008 Dmitry V. Levin <ldv@altlinux.org> 1.9.6-alt2
- fakeroot: Fixed regression introduced in previous release.

* Mon Sep 22 2008 Dmitry V. Levin <ldv@altlinux.org> 1.9.6-alt1
- Updated to 1.9.6.
- fakeroot: Rewritten signal handling.

* Fri Apr 11 2008 Dmitry V. Levin <ldv@altlinux.org> 1.9.4-alt2
- faked: Rewritten signal handling to avoid race conditions.

* Thu Apr 03 2008 Dmitry V. Levin <ldv@altlinux.org> 1.9.4-alt1
- Updated to 1.9.4.

* Sun Jan 20 2008 Dmitry V. Levin <ldv@altlinux.org> 1.9-alt1
- Updated to 1.9.

* Mon Mar 05 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.10-alt2
- Optimized fakeroot wait loop fix.

* Mon Nov 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1.5.10-alt1
- Updated to 1.5.10.
- Fixed fakeroot wait loop.
- Fixed faked cleanup handler.

* Wed Oct 19 2005 Dmitry V. Levin <ldv@altlinux.org> 1.5.4-alt2
- Fixed faked daemonize code.

* Fri Oct 14 2005 Dmitry V. Levin <ldv@altlinux.org> 1.5.4-alt1
- Updated to 1.5.4.
- Rediffed patches.

* Wed Jun 15 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Updated to 1.3.

* Mon Jun 13 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt3
- Fixed "fakeroot -s".

* Mon Feb 14 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt2
- Wrap functions using default versioning.

* Tue Dec 07 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Updated to 1.2.
- Merged upstream patches:
  alt-fsugid.

* Fri Oct 22 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1.5-alt1
- Updated to 1.1.5.

* Sun Oct 17 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt1
- Updated to 1.1.2.
- Reviewed and updated patches.

* Thu Nov 27 2003 Dmitry V. Levin <ldv@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2, updated patches.
- Do not package .la files.

* Mon Sep 15 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt1
- Updated to 0.7.6

* Mon Jul 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.5-alt1
- Updated to 0.7.5

* Fri Jul 04 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.3-alt2
- Fixed trap usage in fakeroot script.

* Thu Jun 26 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.3-alt1
- Updated to 0.7.3
- Fixed fakeroot script to correct package dependencies.
- Fake setfsuid, setfsgid and setgroups (required for libtcb).
- Changed faking algorithm for other [sg]et*[ug]id functions,
  to better match real system behaviour.

* Mon May 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.9-alt2
- Updated build dependencies.

* Thu May 01 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.9-alt1
- Updated to 0.6.9.
- Fixed testsuit and enabled it by default.
- Updated summary and description.

* Thu Mar 13 2003 Alexander V. Nikolaev <avn@altlinux.org> 0.5.9-alt2
- Fix /usr/lib/libfakeroot permissions

* Mon Feb 10 2003 Alexander V. Nikolaev <avn@altlinux.org> 0.5.9-alt1
- New upstream version
- Add depends to getopt

* Mon Dec 16 2002 Alexander V. Nikolaev <avn@altlinux.org> 0.5.7-alt2
- Remove static libs

* Tue Dec 10 2002 Alexander V. Nikolaev <avn@altlinux.org> 0.5.7-alt1
- 0.5.7
