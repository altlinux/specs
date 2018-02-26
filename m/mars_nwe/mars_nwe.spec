%define max_connections 16
%define max_files 256
%define binderydir %_localstatedir/%name/bd
%define sname nwserv

Name: mars_nwe
Version: 0.99
Release: alt4

Summary: NetWare file and print servers which run on Linux systems.
License: GPL
Group: System/Servers

Url: http://www.compu-art.de/mars_nwe/
Source:  ftp://ftp.compu-art.de/mars_nwe/mars_nwe-0.99.pl21.tar.bz2
Source1: %name-mk.li.gz
Source2: %name-config.h.in.gz
Source3: %name-%sname.conf.bz2
Source5: %name.init.gz
Source6: %name.log
Patch0: %name-0.99pl21-tools.patch.gz
Patch1: %name-glibc21.patch.bz2
Patch2: %name-0.99.pl19-buffer.patch.bz2
Patch3: %name-0.99.pl20-emutli1.patch.gz

Conflicts: mars-nwe
Obsoletes: mars-nwe

# Automatically added by buildreq on Tue Oct 03 2006
BuildRequires: libgdbm-devel

%description
The %name (MARtin Stover's NetWare Emulator) package enables Linux
to provide both file and print services for NetWare clients (i.e.,
providing the services of a Novell NetWare file server). %name
allows the sharing of files between Linux machines and Novell NetWare
clients, using NetWare's native IPX protocol suite.

%prep
%setup -n %name
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
gzip -dc %SOURCE1 > mk.li
gzip -dc %SOURCE1 \
%ifarch x86_64
    | sed -e 's|/lib/|/lib64/|g' \
%endif
    > mk.li
chmod 755 mk.li
gzip -dc %SOURCE2 \
    | sed -e 's/@MAX_CONNECTIONS@/%max_connections/' \
	  -e 's/@MAX_FILES@/%max_files/' \
	  -e 's|@PATHNAME_BINDERY@|%binderydir|' > config.h

%build
%make_build CFLAGS="%optflags"

%install
install -d -m 0700 %buildroot{%_localstatedir/%name/sys/{login,mail,print,public,system},%binderydir}
install -d -m 0755 %buildroot{/var/run,%_logdir,%_sysconfdir,%_sbindir}
:> %buildroot%_logdir/%name.log
chmod 0644 %buildroot%_logdir/%name.log
:> %buildroot/var/run/%name.routes
chmod 0644 %buildroot/var/run/%name.routes
install -m 0644 examples/%sname.stations %buildroot%_sysconfdir/
install -s -m 0755 %sname nwconn ncpserv nwclient nwbind %buildroot%_sbindir/
bzip2 -dc %SOURCE3 > %buildroot%_sysconfdir/%sname.conf
chmod 0600 %buildroot%_sysconfdir/%sname.conf
install -d -m 0755 %buildroot%_initdir
install -d -m 0750 %buildroot%_sysconfdir/logrotate.d
gzip -dc %SOURCE5 > %buildroot%_initdir/%name
chmod 0755 %buildroot%_initdir/%name
install -m 0644 %SOURCE6 %buildroot%_sysconfdir/logrotate.d/%name.log

%post
%post_service %name ||:

%preun
%preun_service %name ||:

%files
%doc README doc examples
%dir %_localstatedir/%name
%_localstatedir/%name/sys
%dir %binderydir
%ghost %_logdir/%name.log
%ghost /var/run/%name.routes
%config(noreplace) %_sysconfdir/%sname.conf
%config(noreplace) %_sysconfdir/%sname.stations
%config(noreplace) %_sysconfdir/logrotate.d/%name.log
%_sbindir/*
%_initdir/*

%changelog
* Mon Sep 14 2009 Michael Shigorin <mike@altlinux.org> 0.99-alt4
- rebuilt for Sisyphus

* Wed Oct 25 2006 Led <led@altlinux.ru> 0.99-alt3
- fixed x86_64 build

* Wed Oct 04 2006 Led <led@altlinux.ru> 0.99-alt2
- fixed nwserv.conf

* Tue Oct 03 2006 Led <led@altlinux.ru> 0.99-alt1
- 0.99pl21
- added %name-0.99.pl20-emutli1.patch
- added %name-0.99pl21-tools.patch.gz
- cleaned up and fixed spec
- fixed init-script

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 0.99pl20-ipl3mdk
- rebuild

* Wed Jan 10 2001 AEN <aen@logic.ru>
- RE adaptations

* Mon Jan 01 2001 Stefan van der Eijk <s.vandereijk@chello.nl> 0.99pl20-1mdk
- updated to 0.99pl20
- changed source path to current ftp site
- use correct permisions for the source files (chown while building)
- modified mars_nwe-mk.li: CPP="cc -E" --> CPP="cpp -traditional"
- modified mars_nwe-glibc21.patch (thanks RedHat)
- use RedHat's mars_nwe-0.99.pl19-buffer.patch
- remove /tmp/mars_nwe.err in %%clean
- some macro's

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.99pl17-4mdk
- automatically added BuildRequires

* Tue Mar 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.99pl17-3mdk
- clean specfile 

* Thu Nov 04 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release
- Fixed defattrs

* Tue Sep 14 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- redo Mandrake adaptions

* Fri Sep  3 1999 Bill Nottingham <notting@redhat.com>
- add patch to fix some buffer overflows.

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.99.pl17

* Thu Jun 10 1999 Dale Lovelace <dale@redhat.com>
- fixed logrotate script

* Mon May 24 1999 Bill Nottingham <notting@redhat.com>
- update to 0.99.pl16

* Thu May 13 1999 Bill Nottingham <notting@redhat.com>
- actually update source to 0.99.pl15. Doh!

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate fixes

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Mar  9 1999 Bill Nottingham <notting@redhat.com>
- update to 0.99.pl15

* Tue Feb 23 1999 Bill Nottingham <notting@redhat.com>
- update to 0.99.pl14

* Tue Aug 18 1998 Cristian Gafton <gafton@redhat.com>
- buildroot

* Sun May 10 1998 Alan Cox <alan@redhat.com>
- Made it compile with 2.1.* kernels and also gcc 2.0.7 where sysv_signal
  is correctly hidden as __sysv_signal.

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 0.99pl6
- enhanced initscripts

* Tue Jan 13 1998 Erik Troan <ewt@redhat.com>
- use sysv_signal everywhere instead of normal signal -- this makes signal
  handlers not block signals, which mars_nwe expects
- changed _ to - in name of logrotate config file

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated for chkconfig
- doesn't start by default
- added status, restart options to init script

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
