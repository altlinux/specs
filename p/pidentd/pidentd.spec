Name: pidentd
Version: 3.0.19
Release: alt1

Summary: An implementation of the RFC1413 identification server.
Copyright: Public domain/GPL
Group: System/Servers
Source: ftp://ftp.lysator.liu.se/pub/unix/ident/servers/%name-%version.tar.gz
Source1: identd.conf
Source2: pidentd.xinetd
Source3: identd.init

Patch1: pidentd-3.0.19-dummy.patch
Patch2: pidentd-3.0.11-nossl.patch
Patch3: pidentd-3.0.14-droproot.patch 

Requires: xinetd
PreReq: shadow-utils chkconfig

%description
The %name package contains identd, which implements the RFC1413
identification server. Identd looks up specific TCP/IP connections
and returns either the user name or other information about the
process that owns the connection.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf
%configure --with-threads=yes
%make_build

%install
mkdir -p $RPM_BUILD_ROOT{%_sbindir,%_mandir/man8}
%makeinstall

ln -s identd $RPM_BUILD_ROOT%_sbindir/in.identd
ln -s identd.8 $RPM_BUILD_ROOT%_mandir/man8/in.identd.8

install -p -m640 -D %SOURCE1 $RPM_BUILD_ROOT%_sysconfdir/identd.conf
install -p -m640 -D %SOURCE2 $RPM_BUILD_ROOT%_sysconfdir/xinetd.d/auth
install -p -m755 -D %SOURCE3 $RPM_BUILD_ROOT%_initdir/identd

%pre                                                                                                  
/usr/sbin/useradd -r -g proc -d /dev/null -s /dev/null -n %name &>/dev/null ||:

%post
%post_service identd

%preun
%preun_service identd


%files
%config(noreplace) %_sysconfdir/identd.conf
%config(noreplace) %_sysconfdir/xinetd.d/*
%config %_initdir/identd
%_sbindir/*
%_mandir/man?/*
%doc *BUGS ChangeLog FAQ INSTALL README Y2K doc/*.txt

%changelog
* Sat Jun 03 2006 Denis Ovsienko <pilot@altlinux.ru> 3.0.19-alt1
- building the latest version
- fixing #7746
- rediffed pidentd-3.0.8-dummy.patch to pidentd-3.0.19-dummy.patch

* Fri Nov 12 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.16-alt1.2
- removed buildreq on libelf
- try to fix #416

* Thu Jun 03 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.16-alt1.1
- fixed #4148

* Tue Jun 17 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0.16-alt1
- 3.0.16
- use new format for init-script

* Fri Oct 25 2002 Stanislav Ievlev <inger@altlinux.ru> 3.0.14-alt6
- rebuild with gcc3

* Tue Feb 12 2002 Stanislav Ievlev <inger@altlinux.ru> 3.0.14-alt5
- added user and group creation in pre section
- fix typo

* Mon Dec 10 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.14-alt4
- key generation future removed

* Thu Dec 06 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.14-alt3
- fix again

* Tue Dec 04 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.14-alt2
- fix scripts

* Wed Dec 06 2000 Dmitry V. Levin <ldv@fandra.org> 3.0.12-ipl1mdk
- 3.0.12

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 3.0.11-ipl6mdk
- Updated xinet support.

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 3.0.11-ipl5mdk
- Dropped inetd support, rewritten xinetd support.
- RE and Fandra adaptions.

* Thu Jul 20 2000 François Pons <fpons@mandrakesoft.com> 3.0.11-5mdk
- fixed man pages location.
- removed /usr/bin/perl requires.

* Mon Jul 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.11-4mdk
- Don't build with crypto.

* Sat Jul 15 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.11-3mdk
- Remove ugly perl -pe in %post.
- Add config.files.

* Mon Jul 12 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 3.0.11-2mdk
- makeinstall macro
- macroszifications

* Mon Jun 12 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 3.0.11-1mdk
- updated to 3.0.11
- removed 3.0.10 security patch (fixed in 3.0.11)

* Mon Apr 03 2000 François Pons <fpons@mandrakesoft.com> 3.0.10-1mdk
- spec file update.
- updated with 3.0.10 and rh patches.

* Sat Apr 01 2000 François Pons <fpons@mandrakesoft.com> 2.8.5-8mdk
- updated Group.

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMp check/build

* Fri Jul 09 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- add example cfg
- refixed dangling BuildRoot in man page
- add to cooker

* Wed Jun 02 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Added pidentd+fm-1.1 patch for masq support

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.8.5.
- fix dangling BuildRoot in man page (#1458).

* Thu Nov 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.8.4.

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- updated to 2.7

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
