Name: finger
Version: 1.3
Release: alt1.0

Summary: Show user information (client)
License: BSD
Group: Networking/Other
Url: http://ftp.suse.com/pub/people/kukuk/ipv6

Source: %url/finger-bsd-%version.tar.bz2
Source1: %name.xinetd

%package server
Summary: A Server for Showing User Information
Group: System/Servers

%description
Finger is a utility that allows users to see information about system
users (login name, home directory, name, and more), on local and remote
systems. The %name package includes a standard finger client.

%description server
Finger is a utility that allows users to see information about system
users (login name, home directory, name, and more), on local and remote
systems. The %name-server package includes a standard finger server.
The server daemon (%{name}d) usually runs from %_sysconfdir/xinetd.d/%name.

You should install %name-server if your system is used by multiple users
and you'd like finger information to be available.

%prep
%setup -q -n finger-bsd-%version

%build
%configure
%make_build

%install
install -D -m640 %SOURCE1 $RPM_BUILD_ROOT%_sysconfdir/xinetd.d/%name
%makeinstall

%find_lang finger-bsd

%files -f finger-bsd.lang
%attr(711,root,root) %_bindir/*
%_man1dir/*

%files server
%config(noreplace) %_sysconfdir/xinetd.d/%name
%attr(711,root,root) %_sbindir/*
%_man8dir/*

%changelog
* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.3-alt1.0
- Automated rebuild.

* Mon Oct 03 2005 Victor Forsyuk <force@altlinux.ru> 1.3-alt1
- Switch to OpenBSD finger ported to Linux by Thorsten Kukuk (SUSE).

* Fri Sep 27 2002 Rider <rider@altlinux.ru> 0.17-ipl4mdk
- rebuild

* Sat Feb 24 2001 Dmitry V. Levin <ldv@fandra.org> 0.17-ipl3mdk
- Fixed build with glibc-2.2.2

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 0.17-ipl2mdk
- RE adaptions.

* Sat Sep 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.17-2mdk
- Re
- Add xinetd support.
- Merge with rh patches.

* Fri Aug 04 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.17-1mdk
- rebuild with new version
- use sbindir macro

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.16-2mdk
- BM, macros
- bzip2 source

* Sun Apr 02 2000 Jerome Martin <jerome@mandrakesoft.com> 0.16-1mdk
- Updates to version 0.16
- specfile cleanup
- groups and spec-helper
- splited into server and client packages

* Tue Jul 06 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build for new environement (Rel: 27mdk).

* Thu Apr  8 1999 Jeff Johnson <jbj@redhat.com>
- fix process table filled DOS attack (#1271)
- fix pts display problems (#1987 partially)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- fix error message typo.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added check for getpwnam() failure

