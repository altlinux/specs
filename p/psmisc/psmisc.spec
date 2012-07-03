Name: psmisc
Version: 22.13
Release: alt1

Summary: Utilities for managing processes on your system
License: GPLv2+
Group: System/Base
Url: http://sourceforge.net/projects/%name/
# git://git.altlinux.org/gears/p/psmisc.git
Source: %name-%version-%release.tar

%def_enable selinux
BuildRequires: libncurses-devel %{?_enable_selinux:libselinux-devel}

%description
This package contains utilities for managing processes on your system:
pstree, killall and fuser.  The pstree command displays a tree structure
of all of the running processes on your system.  The killall command
sends a specified signal (SIGTERM if nothing is specified) to processes
identified by name.  The fuser command identifies the PIDs of processes
that are using specified files or filesystems.

%prep
%setup -n %name-%version-%release
mkdir -p m4

%build
%autoreconf
%configure %{subst_enable selinux}
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/sbin
mv %buildroot%_bindir/fuser %buildroot/sbin/
ln -s ../../sbin/fuser %buildroot%_bindir/

pushd %buildroot%_bindir/
ln -sf pstree pstree.x11
popd

%find_lang %name

%files -f %name.lang
/sbin/*
%_bindir/*
%_man1dir/*
%doc AUTHORS ChangeLog README

%changelog
* Tue Apr 05 2011 Dmitry V. Levin <ldv@altlinux.org> 22.13-alt1
- Updated to v22.13-7-g64e6225.
- Packaged %_bindir/fuser symlink (closes: #11762).
- Enabled selinux support.

* Sun Nov 19 2006 Dmitry V. Levin <ldv@altlinux.org> 22.3-alt1
- Updated to 22.3.
- Fixed a few uninitialized read errors.

* Tue May  2 2006 Ilya Evseev <evseev@altlinux.ru> 22.2-alt1
- updated to new version 22.2

* Thu Jan 12 2006 Ilya Evseev <evseev@altlinux.ru> 22.1-alt1
- updated to new version 22.1, revisite patchset:
   + rewrite patch #1 (hrrrr..),
   + obsolete patch #5 (included to upstream).

* Tue Nov  8 2005 Ilya Evseev <evseev@altlinux.ru> 21.8-alt1
- updated to new version 21.8, revisite P1 (fuser patch)

* Tue Nov  1 2005 Ilya Evseev <evseev@altlinux.ru> 21.7-alt1
- updated to new version, revisite patchset:
   + patch #1 is rewritten from scratch
   + patches #3 and #4 are removed because they are included to upstream

* Mon Sep 19 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.6-alt3
- Added patch #5: prevent failures on validation of generated signal names list
  (fails incorrectly in hasher environment even signames.h is fine)

* Mon Sep 12 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.6-alt2
- Added russian language messages file

* Sun Mar 15 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.6-alt1
- Updated to 21.6, revisited patches: P3

* Tue Jan 18 2005 Dmitry V. Levin <ldv@altlinux.org> 21.5-alt3
- Implemented support for restricted proc kernel patch (Owl).

* Fri Jan 14 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.5-alt2
- remove actually unneeded dependency from C++

* Sun Jan  9 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.5-alt1
- Updated to 21.5

* Sat Jan 03 2004 Dmitry V. Levin <ldv@altlinux.org> 21.4-alt1
- Updated to 21.4
- Updated patches.
- Fixed potential null dereference bug introduced in 21.4.

* Thu Dec 26 2002 Dmitry V. Levin <ldv@altlinux.org> 21.2-alt2
- (Owl) Fixed the segfault in pstree(1) when asked to report
  information for a user, but entry with PID 1 (init) is
  inaccessible, thanks to (GalaxyMaster).
- Fixed build with fresh autotools.

* Tue Oct 22 2002 Dmitry V. Levin <ldv@altlinux.org> 21.2-alt1
- Updated to 21.2

* Mon Jun 24 2002 Dmitry V. Levin <ldv@altlinux.org> 21-alt2
- Patched to link with libtinfo.

* Sun May 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 21-alt1
- 21

* Wed Mar 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 20.2-alt1
- 20.2
- License and url's changed
- useless man(1) pidof removed, it conflicts with man(8) from SysVinit
  package.

* Mon Apr 02 2001 Dmitry V. Levin <ldv@altlinux.ru> 20.1-alt1
- 20.1

* Tue Dec 26 2000 Dmitry V. Levin <ldv@fandra.org> 19-ipl3mdk
- FHSification.

* Wed May 17 2000 Dmitry V. Levin <ldv@fandra.org> 19-ipl2mdk
- Fixed: kill patch.
- RE adaptions.

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 19-2mdk
- Fix bad tag value.

* Tue Mar 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 19-1mdk
- Version update (19)
- Use default Mandrake Optimisations.
- Patch the Makefile for psmisc rpm to be compiled by non root user.
- bziped psmisc-17-buildroot.patch

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Move fuser to /sbin(r).

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Sat Mar 13 1999 Michael Maher <mike@redhat.com>
- updated package

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- renamed the patch file .patch instead of .spec

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to psmisc version 17
- buildrooted

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from version 11 to version 16
- spec file cleanups

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
