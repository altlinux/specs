Name: libutempter
Version: 1.1.6
Release: alt2

Summary: A privileged helper for utmp/wtmp updates
License: LGPLv2+
Group: System/Libraries

Source: %name-%version.tar

Provides: utempter = 0.5.2
Obsoletes: utempter

%define helperdir %_libexecdir/utempter

%description
This library provides interface for terminal emulators such as
screen and xterm to record user sessions to utmp and wtmp files.

%package devel
Summary: Development environment for utempter
Group: Development/C
Requires: %name = %version-%release
Provides: utempter-devel = %version
Obsoletes: utempter-devel

%package devel-static
Summary: Static utempter library
Group: Development/C
Requires: %name-devel = %version-%release
Provides: utempter-devel-static = %version
Obsoletes: utempter-devel-static

%description devel
This package contains development files required to build
utempter-based software.

%description devel-static
This package contains static library required to build
statically linked utempter-based software.

%prep
%setup

%build
%make_build CFLAGS="%optflags" \
	libdir="%_libdir" libexecdir="%_libexecdir"

%install
%makeinstall_std \
	libdir="%_libdir" libexecdir="%_libexecdir"

%pre
/usr/sbin/groupadd -r -f utmp
/usr/sbin/groupadd -r -f utempter

%files
%_libdir/*.so.*
%attr(710,root,utempter) %dir %helperdir
%attr(2711,root,utmp) %helperdir/*
%doc README

%files devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

%files devel-static
%_libdir/*.a

%changelog
* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1.6-alt2
- Rebuilt for debuginfo.

* Thu Nov 04 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.6-alt1
- Added manpages documenting the utempter interface, based on
  documentation from FreeBSD libulog.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.1.5-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Removed redundant dependencies.

* Sun Feb 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.5-alt1
- Removed cvsid tags.
- README: Described differences between provided libutempter interfaces.
- Fixed FreeBSD support:
  + utempter.c (main): Be consistent and use ptsname(3) on non-glibc systems too.
  + utempter.c (write_uwtmp_record) [__FreeBSD__]: Fix ut.ut_time initialization.

* Fri Dec 09 2005 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- Enabled almost all diagnostics supported by gcc and fixed all
  issues found by gcc-3.4.4-alt3.
- Added FreeBSD support, based on patches from Gentoo/FreeBSD.
- Makefile:
  + Fixed few portability issues reported by Gentoo developers.
- libutempter: Linked with -Wl,-z,defs.
- utempter:
  + Fixed struct utmp initialization on 64-bit architectures
    with 32-bit backwards compatibility enabled (like x86_64).
  + Linked with -Wl,-z,now, i.e., marked it to tell the dynamic
    linker to resolve all symbols when the program is started.
    Suggested by Gentoo developers.

* Thu Aug 18 2005 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt1
- Restricted list of global symbols exported by the library.
- Updated FSF postal address.

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt1
- Added multilib support.

* Fri Feb 14 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt1
- iface.c: don't block SIGCHLD; redefine signal handler instead.

* Mon Dec 23 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt1
- Changed soname back to libutempter.so.0, introduced versioning.

* Tue Sep 24 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-alt1
- If helper execution fails, try saved group ID.

* Tue May 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.6-alt1
- New function: utempter_set_helper.

* Mon Dec 10 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.5-alt1
- iface.c: block SIGCHLD instead of redefine signal handler.

* Wed Nov 21 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.4-alt1
- utempter.h: do not use "__attribute ((unused))".

* Tue Nov 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.3-alt1
- Added compatibility declarations to ease upgrade of old applications.
- Added small README file.
- Corrected provides.

* Thu Nov 08 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.2-alt1
- Added compatibility library to ease upgrade of old applications.

* Mon Nov 05 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.1-alt1
- Indented code a bit (Solar request).

* Mon Oct 15 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.0-alt1
- Rewritten the code completely.
- Renamed to libutempter.
- Corrected the package description.
- FHSificated (yes, there are no more %_sbindir/utempter).
- Libificated.

* Fri Oct 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.5.2-alt4
- %_libdir/utempter sounds better so use it as helper directory.

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.5.2-alt3
- Specfile cleanup.
- Owl-compatible changes:
  + added utempter group;
  + utempter binary moved to %_libdir/utempter.d,
    owned by group utempter with 710 permissions.

* Thu Jun 28 2001 Sergie Pugachev <fd_rag@altlinux.ru> 0.5.2-alt1
- new version

* Tue Dec 05 2000 AEN <aen@logic.ru>
- build for RE

* Tue Jul 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.1-4mdk
- BM

* Fri May 19 2000 Pixel <pixel@mandrakesoft.com> 0.5.1-3mdk
- add -devel
- add soname
- spec helper cleanup

* Sat Apr 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.5.1-2mdk
- changed group

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 0.5.1
- fix utmp as group 22.
- strip utempter.
- defattr to root.

* Thu Jun 10 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Fri Jun  4 1999 Jeff Johnson <jbj@redhat.com>
- ignore SIGCHLD while processing utmp.

