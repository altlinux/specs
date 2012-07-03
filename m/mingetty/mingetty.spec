Name: mingetty
Version: 1.01
Release: alt3

Summary: A compact getty program for virtual consoles only
License: GPL
Group: System/Base
Packager: Dmitry V. Levin <ldv@altlinux.org>

# This url is no longer valid:
# ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemons/
Source: mingetty-%version.tar

Patch1: mingetty-1.00-alt-Makefile.patch
Patch2: mingetty-1.01-owl-logname.patch
Patch3: mingetty-1.00-owl-alt-syslog.patch
Patch4: mingetty-1.00-owl-alt-bound.patch
Patch5: mingetty-1.00-alt-read_eof.patch
Patch6: mingetty-1.01-suse-owl-alt-vhangup.patch
Patch7: mingetty-1.01-alt-logname_valid_characters.patch
Patch8: mingetty-1.01-alt-progname.patch
Patch9: mingetty-1.01-alt-std_fd.patch
Patch10: mingetty-1.01-alt-release.patch

Requires: login >= 0:0.60-alt1

%description
The mingetty program is a lightweight, minimalist getty program for
use only on virtual consoles.  mingetty lacks certain functionality
needed for serial lines (you may use the mgetty program in that case).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
make

%install
make install

%files
/sbin/mingetty
%_man8dir/*

%changelog
* Sat Apr 07 2007 Dmitry V. Levin <ldv@altlinux.org> 1.01-alt3
- Updated progname patch.

* Mon Mar 10 2003 Dmitry V. Levin <ldv@altlinux.org> 1.01-alt2
- Added '\R' special char support.

* Mon Feb 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1.01-alt1
- Updated to 1.01, updated patches.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 1.00-alt2
- Rebuilt in new environment.

* Mon Jun 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1.00-alt1
- Updated code to 1.00, updated patches.
- Dropped "unpriv" patch (unneeded for a long time).
- Removed patches (merged upstream):
  0.9.4-isprint, 0.9.4-glibc, 0.9.4-wtmplock.
- Now passes the username to login via LOGNAME, requires patched
  login >= 0:0.60-alt1 (Owl).
- Check for vhangup(2) return status (SuSe, Owl).
- Disable wtmp locking (SuSe, Owl).
- Changed logname validation rule.
- Strict open flags for 0-1-2 descriptors.

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.4-ipl17mdk
- Rebuilt.

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.4-ipl16mdk
- Requires: login.

* Tue May 08 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9.4-ipl15mdk
- Added patches from Owl.
- Added progname patch.

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 0.9.4-ipl14mdk
- FHSification.

* Thu Jan 27 2000 Dmitry V. Levin <ldv@fandra.org>
- get_logname patch
- unpriv patch
- optimal manpages compressing
- Fandra adaptions

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixed build problems on intel and alpha for manhattan

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
~- built against glibc
