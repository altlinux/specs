Name: xtoolwait
Version: 1.3
Release: alt2
Serial: 1

Summary: A utility which aims to decrease X session startup time
License: GPL
Group: System/Configuration/Other
Packager: Fr. Br. George <george@altlinux.ru>

Source: ftp://ftp.x.org/contrib/utilities/%name-%version.tar.bz2
Source1: %name.ALT.Makefile
# Thanks Debian for the patch
Patch0: xtoolwait_1.3-6.2.diff
Patch1:	%name.embed.patch

# Automatically added by buildreq on Sat Jul 29 2006
BuildRequires: libX11-devel

%description
Xtoolwait is a utility which starts an X client in the background, waits
for a window to be mapped on the root window, and then exits.  Xtoolwait
can improve performance for users who start a bunch of X clients
automatically (for example, xterm, xlock, xconsole, whatever) when the
X session starts.

Install xtoolwait if you'd like to try to speed up the startup time for
X sessions.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp %SOURCE1 Makefile

%build
%make

%install
%makeinstall

%files
%doc README
%_x11bindir/%name
%_x11mandir/man?/*

%changelog
* Tue Sep 21 2010 Fr. Br. George <george@altlinux.ru> 1:1.3-alt2
- Try to fix #15635

* Mon Jun 09 2008 Fr. Br. George <george@altlinux.ru> 1:1.3-alt1.1
- Rebuild with 4.1 branch

* Mon Aug 21 2006 Fr. Br. George <george@altlinux.ru> 1:1.3-alt1
- Change 'mdk' release to 'alt'.
- Add 'Packager:' tag.

* Sat Jul 29 2006 Fr. Br. George <george@altlinux.ru> 1.3-ipl7mdk
- Rebuild from Debian source.

* Wed Oct 16 2002 Stanislav Ievlev <inger@altlinux.ru> 1.3-ipl6mdk
- rebuild with gcc3

* Mon Mar 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.3-ipl5mdk
- Rebuilt

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.3-3mdk
- automatically added BuildRequires

* Tue Mar 28 2000 dam's <damien@mandrakesoft.com> 1.3-2mdk
- Release.

* Fri Nov 5 1999 dam's <damien@mandrakesoft.com>
- Version 1.3

* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build new version for 6.0

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new version

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
