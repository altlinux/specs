# -*- mode: rpm-spec; mode: folding -*-
# vim: set ft=spec:
# vim600: set fdm=marker:

#%%define patchlevel rc14

Name: dhcp
Version: 3.0.7
Release: alt8
Epoch: 1

Summary: Dynamic Host Configuration Protocol (DHCP) distribution
License: BSD-style
Group: System/Servers
Url: http://www.isc.org/sw/dhcp/

%define srcname dhcp-%version%{?patchlevel:%patchlevel}
Source0: ftp://ftp.isc.org/isc/dhcp/%srcname.tar
Source1: dhcp-dynamic-dns-examples.tar
Source2: dhcpd.conf.sample
Source3: update_dhcp.pl
Source4: dhcpd.init
Source5: dhcrelay.init
Source6: dhclient-enter-hooks
Source7: dhclient-exit-hooks
Source8: dhcpd.sysconfig
Source9: dhcrelay.sysconfig
Source10: dhcpd.chroot.all
Source11: dhcpd.chroot.conf
Source12: dhcpd.chroot.lib
Source13: sethostname.sh

Patch: dhcp-%version-%release.patch

# due to copy_resolv_conf/copy_resolv_lib
BuildPreReq: chrooted >= 0.3

BuildPreReq: groff-base, libcap-devel

# Chrooted environments
%define ROOT %_localstatedir/%name

%package common
Summary: Dynamic Host Configuration Protocol (DHCP) distribution
Group: System/Servers
BuildArch: noarch

%package client
Summary: The ISC DHCP client daemon
Group: System/Servers
PreReq: %name-common = %epoch:%version-%release

%package server
Summary: The ISC DHCP server daemon
Group: System/Servers
PreReq: %name-common = %epoch:%version-%release
Requires: /var/empty
Provides: %name = %epoch:%version-%release
Obsoletes: dhcp, dhcpd

%package relay
Summary: The ISC DHCP relay daemon
Group: System/Servers
PreReq: %name-common = %epoch:%version-%release
Requires: /var/empty

%package omshell
Summary: The ISC DHCP OMAPI command shell tool
Group: System/Servers
PreReq: %name-common = %epoch:%version-%release

%package devel
Summary: Development headers and static libraries for the dhcpctl API
Group: Development/Other
Requires: dhcp-common = %epoch:%version-%release

# {{{ descriptions
%description
The ISC Dynamic Host Configuration Protocol distribution provides a
freely redistributable reference implementation of all aspects of the
DHCP protocol.

%description common
The ISC Dynamic Host Configuration Protocol distribution provides a
freely redistributable reference implementation of all aspects of the
DHCP protocol.

This package contains files and directories common for the ISC DHCP
client, server and relay subpackages.

%description client
The Internet Software Consortium DHCP Client, dhclient, provides a
means for configuring one or more network interfaces using the Dynamic
Host Configuration Protocol, BOOTP protocol, or if these protocols
fail, by statically assigning an address.

%description server
The Internet Software Consortium DHCP Server, dhcpd, implements the
Dynamic Host Configuration Protocol (DHCP) and the Internet Bootstrap
Protocol (BOOTP).  DHCP allows hosts on a TCP/IP network to request
and be assigned IP addresses, and also to discover information about
the network to which they are attached.  BOOTP provides similar
functionality, with certain restrictions.

%description relay
The Internet Software Consortium DHCP Relay Agent, dhcrelay, provides a
means for relaying DHCP and BOOTP requests from a subnet to which no
DHCP server is directly connected to one or more DHCP servers on other
subnets.

You will have to define the environment variable SERVERS and optionally
OPTIONS in /etc/sysconfig/dhcrelay before starting the server.

%description omshell
The OMAPI Command Shell, omshell, provides an interactive way to connect
to, query, and possibly change, the ISC DHCP Server's state via OMAPI,
the Object Management API.  By using OMAPI and omshell, you do not have
to stop, make changes, and then restart the DHCP server, but can make
the changes while the server is running.  Omshell provides a way of
accessing OMAPI.

%description devel
DHCP devel contains header files and static libraries for developing
with the Internet Software Consortium (ISC) dhcpctl API.

# }}}

%prep
%setup -n %srcname -a1
%patch -p1

install -pm644 %_sourcedir/update_dhcp.pl .
find -type f -print0 |
	xargs -r0 grep -EZl '(/etc|ETCDIR)/(dhclient|dhcpd|dhcrelay)' -- |
	xargs -r0 sed -i 's,\(/etc\|ETCDIR\)/\(dhclient\|dhcpd\|dhcrelay\),\1/%name/\2,g' --
find client -type f -not -name Makefile\* -print0 |
	xargs -r0 grep -FZl DBDIR -- |
	xargs -r0 sed -i 's,DBDIR,%ROOT/dhclient/state,g' --
find server -type f -not -name Makefile\* -print0 |
	xargs -r0 grep -FZl DBDIR -- |
	xargs -r0 sed -i 's,DBDIR,%ROOT/dhcpd/state,g' --

%build
%add_optflags -fpie -fno-strict-aliasing -Wno-unused -Werror -Dlint
./configure --copts "%optflags"
%make_build CC=%__cc DEBUG=

# {{{ install

%install
rln()
{
	local target=$1 && shift
	local source=$1 && shift
	target=`relative "$target" "$source"`
	ln -snf "$target" "%buildroot$source"
}

mkdir -p %buildroot{%ROOT,/etc/{sysconfig,%name/dhclient.d}}
%makeinstall_std \
	INSTALL='install -pm644' \
	MANINSTALL='$(INSTALL)' \
	LIBDIR=%_libdir \
	INCDIR=%_includedir \
	ADMMANDIR=%_mandir/man8 \
	FFMANDIR=%_mandir/man5 \
	LIBMANDIR=%_mandir/man3 \
	USRMANDIR=%_mandir/man1 \
	#

# dhcpd
install -pD -m755 %_sourcedir/dhcpd.init \
	%buildroot%_initdir/dhcpd
install -pD -m644 %_sourcedir/dhcpd.sysconfig \
	%buildroot/etc/sysconfig/dhcpd
install -pD -m600 %_sourcedir/dhcpd.conf.sample \
	%buildroot/etc/%name/dhcpd.conf.sample
mkdir -p %buildroot%ROOT/dhcpd/state
touch %buildroot%ROOT/dhcpd/state/dhcpd.leases
# Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature.
mkdir -p %buildroot%ROOT/dhcpd/dev
mksock %buildroot%ROOT/dhcpd/dev/log
mkdir -p %buildroot/etc/syslog.d
ln -s %ROOT/dhcpd/dev/log %buildroot/etc/syslog.d/dhcpd
# Resolver infrastructure
for n in all conf lib; do
	install -pD -m750 "%_sourcedir/dhcpd.chroot.$n" \
		"%buildroot/etc/chroot.d/dhcpd.$n"
done
%__subst -p 's,%%ROOT,%ROOT/dhcpd,g' "%buildroot/etc/chroot.d/"*
mkdir -p %buildroot%ROOT/dhcpd{/etc,/%_lib,/var/{nis,yp/binding}}
touch %buildroot%ROOT/dhcpd{/etc/{localtime,hosts,services,{host,nsswitch,resolv}.conf},/var/nis/NIS_COLD_START}

# dhcrelay
install -pD -m755 %_sourcedir/dhcrelay.init \
	%buildroot%_initdir/dhcrelay
install -pD -m644 %_sourcedir/dhcrelay.sysconfig \
	%buildroot/etc/sysconfig/dhcrelay

# dhclient
rln /sbin/dhclient-script /etc/%name/
install -m755 %_sourcedir/dhclient-enter-hooks \
	%buildroot/etc/%name/
install -m755 %_sourcedir/dhclient-exit-hooks \
	%buildroot/etc/%name/
mkdir -p %buildroot%ROOT/dhclient/state
touch %buildroot%ROOT/dhclient/state/dhclient.leases
echo '# DHCP client config file' > %buildroot/etc/%name/dhclient.conf
chmod 644 %buildroot/etc/%name/dhclient.conf
mkdir -p %buildroot/etc/%name/dhclient.d
echo '#!/bin/sh' > %buildroot/etc/%name/dhclient.d/enter001.null-hook
echo '#!/bin/sh' > %buildroot/etc/%name/dhclient.d/exit001.null-hook
install -pm644 %_sourcedir/sethostname.sh \
	%buildroot/etc/%name/dhclient.d/enter010.sethostname
chmod 644 %buildroot/etc/%name/dhclient.d/*

# docs
%define docdir %_docdir/%srcname
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
cp -a LICENSE README RELNOTES update_dhcp.pl doc \
	%buildroot%docdir/

# }}}

# {{{ scripts

%pre common
/usr/sbin/groupadd -r -f %name

%pre client
rm -f /var/run/dhclient.restart
if [ $1 -ge 2 ] && /sbin/start-stop-daemon --stop --test --exec /sbin/dhclient --pidfile /var/run/dhclient.pid --user root >/dev/null 2>&1; then
	touch /var/run/dhclient.restart
fi

# relocate dhcp.d
if [ ! -d /etc/%name/dhclient.d -a -d /etc/%name/dhcp.d ]; then
	mv -v /etc/%name/dhcp.d /etc/%name/dhclient.d
fi

# relocate dhclient.leases
if [ ! -f %ROOT/dhclient/state/dhclient.leases -a -f %ROOT/dhclient.leases ]; then
	mkdir -p %ROOT/dhclient/state
	cp -pv %ROOT/dhclient.leases %ROOT/dhclient/state/
fi

%post client
if [ -f /var/run/dhclient.restart ]; then
	rm -f /var/run/dhclient.restart
	echo 'Please restart the ISC DHCP client daemon manually.'
fi

%pre server
/usr/sbin/useradd -r -n -g %name -d %ROOT/dhcpd -s /dev/null -c 'The ISC DHCP server daemon' dhcpd >/dev/null 2>&1 ||:
rm -f /var/run/dhcpd.restart
# stop _old_ dhcpd if running
if [ $1 -eq 1 ] && [ -x %_initdir/dhcpd ] && %_initdir/dhcpd status >/dev/null 2>&1; then
	%_initdir/dhcpd condstop && touch /var/run/dhcpd.restart ||:
fi

# relocate dhcpd.conf
if [ ! -f /etc/%name/dhcpd.conf -a -f /etc/dhcpd.conf ]; then
	mkdir -p /etc/%name
	mv -v /etc/dhcpd.conf /etc/%name/
fi

# relocate dhcpd.leases
if [ ! -f %ROOT/dhcpd/state/dhcpd.leases -a -f %ROOT/dhcpd.leases ]; then
	mkdir -p %ROOT/dhcpd/state
	mv -v %ROOT/dhcpd.leases %ROOT/dhcpd/state/
fi

if [ $1 = 0 ]; then
	rm -f %ROOT/dhcpd/%_lib/* %ROOT/dhcpd/var/yp/binding/*
fi

%post server
/etc/chroot.d/dhcpd.all
%post_service dhcpd
if [ -f /var/run/dhcpd.restart ]; then
	rm -f /var/run/dhcpd.restart
	%_initdir/dhcpd start ||:
fi

%preun server
%preun_service dhcpd

%triggerpostun -- %name
[ $1 = 0 ] || exit 0
/sbin/chkconfig --add dhcpd

%pre relay
/usr/sbin/useradd -r -n -g %name -d /var/empty -s /dev/null -c 'The ISC DHCP relay daemon' dhcrelay >/dev/null 2>&1 ||:
rm -f /var/run/dhcrelay.restart
if [ $1 -ge 2 ] && [ -x %_initdir/dhcrelay ] && %_initdir/dhcrelay status >/dev/null 2>&1; then
	%_initdir/dhcrelay condstop && touch /var/run/dhcrelay.restart ||:
fi

%post relay
if [ -f /var/run/dhcrelay.restart ]; then
	rm -f /var/run/dhcrelay.restart
	%_initdir/dhcrelay start ||:
else
	%post_service dhcrelay
fi

%preun relay
%preun_service dhcrelay

# }}}

# {{{ files

%files common
%dir %ROOT
%dir /etc/%name
%dir %docdir
%docdir/[A-Z]*
%docdir/doc

%files client
%config /etc/%name/dhclient-*-hooks
%config(noreplace) /etc/%name/dhclient.d
%config(noreplace) /etc/%name/dhclient.conf
/etc/%name/dhclient-script
/sbin/dhclient*
%_man5dir/dhclient.*
%_man8dir/dhclient*
%attr(700,root,dhcp) %dir %ROOT/dhclient
%attr(700,root,dhcp) %dir %ROOT/dhclient/state
%attr(644,root,dhcp) %config(noreplace) %verify(not md5 mtime size) %ROOT/dhclient/state/dhclient.leases

%files server
/etc/syslog.d/*
%config /etc/chroot.d/dhcpd.*
%config %_initdir/dhcpd
%config(noreplace) /etc/sysconfig/dhcpd
%_sbindir/dhcpd
%_man5dir/dhcpd.*
%_man5dir/dhcp-options.*
%_man5dir/dhcp-eval.*
%_man8dir/dhcpd.*
%attr(0750,root,dhcp) %dir %ROOT/dhcpd
%attr(1770,root,dhcp) %dir %ROOT/dhcpd/state
%attr(0644,dhcpd,dhcp) %config(noreplace) %verify(not md5 mtime size) %ROOT/dhcpd/state/dhcpd.leases
%dir %attr(0710,root,dhcp) %ROOT/dhcpd/dev
%ghost %attr(666,root,root) %ROOT/dhcpd/dev/*
# Resolver infrastructure
%dir %ROOT/dhcpd/%_lib
%dir %ROOT/dhcpd/etc
%ghost %verify(not md5 mtime size) %ROOT/dhcpd/etc/*
%dir %ROOT/dhcpd/var
%dir %ROOT/dhcpd/var/nis
%ghost %config(missingok) %verify(not md5 mtime size) %ROOT/dhcpd/var/nis/NIS_COLD_START
%dir %ROOT/dhcpd/var/yp
%dir %ROOT/dhcpd/var/yp/binding
%dir /etc/%name
%doc /etc/%name/dhcpd.conf.sample
%dir %docdir
%docdir/update_dhcp.pl

%files relay
%config %_initdir/dhcrelay
%config(noreplace) /etc/sysconfig/dhcrelay
%_sbindir/dhcrelay
%_man8dir/dhcrelay.*

%files omshell
%_bindir/omshell
%_man1dir/omshell.*
  
%files devel
%_includedir/*
%_libdir/lib*.a
%_man3dir/*

# }}}

%changelog
* Fri Dec 02 2011 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt8
- Fixed build on Linux 3.x.

* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt7
- Minor specfile cleanup.

* Wed Dec 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt6
- %name-common: packaged as noarch.

* Wed Dec 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt5
- Fixed build with gcc-4.5.

* Thu Jul 16 2009 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt4
- server/dhcp.c (ack_lease): Imported fix for potential
  premature server termination (Christoph Biedl; CVE-2009-1892).

* Wed Jul 15 2009 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt3
- dhclient: Imported upstream fix for potential stack-based
  buffer overflow (CVE-2009-0692).

* Tue May 12 2009 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt2
- Fixed build with fresh toolchain (by Dmitry Afanasov).

* Thu May 29 2008 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt1
- Updated to 3.0.7 release.

* Thu Oct 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.6-alt2
- Replaced contrib/sethostname.sh with clean implementation.
- Disabled startup scripts by default (#11858).
- Simplified lowering privileges algorithm.

* Mon Jul 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.6-alt1
- Updated to 3.0.6 release.

* Mon Nov 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.5-alt1
- Updated to 3.0.5 release.
- Imported a bounds checking patch from Owl.

* Fri Oct 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.5-alt0.3
- Updated to 3.0.5 rc3.
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Tue Sep 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.5-alt0.2
- Updated to 3.0.5 rc2.

* Thu Jun 08 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.4-alt1
- Updated to 3.0.4 release.
- Packaged libdst.a (#8990).

* Wed Oct 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.3-alt1
- Updated to 3.0.3 release.
- Updated patches.
- Imported few patches from RH's dhcp-3.0.3-10 package.
- dhcpd, dhcrelay: Fixed daemonize code.
- dhcpd: Enhanced droppriv patch to handle failover protocol
  (fixes #8346).

* Mon Apr 18 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.2-alt1
- Updated to 3.0.2 release.
- Updated patches.
- Fixed license tag (distributable -> BSD-like).
- Provided the proper support contact information.
- dhcp-server:
  + disabled %%verify check for files which are
    ususally changed after package installation.
  + relocated dhcpd.conf.sample to /etc/%name/,
    changed startup script to point at this sample
    when needed (#5676).

* Thu Oct 28 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.1-alt12
- dhcp-server: Package /etc/syslog.d/%name symlink.

* Thu Aug 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.1-alt11
- dhcp-server: Complemented resolver infrastructure added
  in previous release.

* Wed Aug 11 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.1-alt10
- Updated to 3.0.1 release.
- Added resolver infrastructure to the dhcpd chroot jail.

* Mon Jul  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.0.1-alt9
- fixed #4665

* Sun Jun 27 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.0.1-alt8
- 3.0.1rc14
- applying changes from Dmitry V. Levin <ldv@altlinux.org> :
  + Renamed dhcp subpackage to dhcp-server subpackage.
  + Merged -devel-static subpackage into -devel subpackage.
  + Merged Owl patches:
    rh-owl-alt-script, owl-man, owl-alt-warnings, owl-alt-drop_priv.
  + Implemented chroot jailing for dhcpd and dhcrelay by default;
    changed location of leases files.
  + Rewritten startup scripts to new rc scheme;
    removed extra ifconfig logic for a while.
  + Updated summaries and descriptions.
  + Corrected interpackage dependencies.
  + Moved update_dhcp.pl script to %%doc.
  + Relocated documentation to %_docdir/%srcname.
  + Changed default dhcpd config location to /etc/%name/dhcpd.conf.
  + Changed /etc/%name/dhcp.d to /etc/%name/dhclient.d.
  + Specfile cleanup.

* Wed Jun 23 2004 Grigory Milev <week@altlinux.ru> 1:3.0.1-alt7.rc14
- new version released

* Thu Feb 26 2004 Grigory Milev <week@altlinux.ru> 1:3.0.1-alt6.rc13
- new version released
- fix start/stop dhcprelay script
- fix start/stop dhcp script

* Mon Apr 21 2003 Grigory Milev <week@altlinux.ru> 1:3.0.1-alt5
- new version released (3.0.1rc11)
- added config dir /etc/dhcp && hooks dir /etc/dhcp/dhcp.d
- added dhclient-enter-hooks && dhclient-exit-hooks

* Mon Dec  9 2002 Grigory Milev <week@altlinux.ru> 1:3.0.1-alt4
- new rc version released
- security patch added: Potential Vulnerabilities in ISC DHCPD [VU#284857]

* Wed Oct 30 2002 Stanislav Ievlev <inger@altlinux.ru> 1:3.0.1-alt3
- real changelog fix. Grigory, please use normal add_changelog util

* Fri Oct 25 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt2
- rebuild with gcc3.2
- mv dhclient-script to /sbin
  make link /sbin/dhclient-script -> /etc/dhclient-script for compatible

* Wed Oct 23 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt1
- rebuild with gcc3

* Wed May 15 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.8
- new rc version released with security patches

* Tue Mar 26 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.7
- make dhcpd.leases as noreplace config file

* Thu Mar 21 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.6
- Fixed init script to work with chkconfig

* Thu Feb 21 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.5
- rewriten init script, for correct work with ethernet
  aliases (ex: eth0:1) and subnet test for available
  in dhcpd.conf (thanks to Vadim Illarionov <DIMMeach@NewMail.ru>)

* Wed Feb 20 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.4
- fixed init script
- remake post and preun scripts

* Fri Feb 15 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.3
- fixed post uninstall script

* Tue Feb 12 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.2
- correct init script for find interfaces from ifcfg scripts
- if you need dhcp on some interface, add DHCP=yes to ifcfg script
- minor spec cleanup

* Mon Nov 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.0.1-alt0.1
- 3.0.1rc3
- Added devel, devel-static, omshell, relay & common packages

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 2.0pl5-ipl2mdk
- RE adaptions.

* Fri Nov 17 2000 Florin Grad <florin@mandrakesoft.com> 2.0pl5-2mdk
- chkconfig is now set to 3,4,5

* Mon Nov 06 2000 Florin Grad <florin@mandrakesoft.com> 2.0pl5-1mdk
- Mandrake adaptations. this is the actual stable version

* Sun Sep 10 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.0pl5
- redo buildroot patch

* Wed Aug 30 2000 Matt Wilson <msw@redhat.com>
- rebuild to cope with glibc locale binary incompatibility, again

* Mon Aug 14 2000 Preston Brown <pbrown@redhat.com>
- check for existence of /var/lib/dhcpd.leases in initscript before starting

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- rebuild to cope with glibc locale binary incompatibility

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jul  7 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- /etc/rc.d/init.d -> /etc/init.d
- fix /var/state/dhcp -> /var/lib/dhcp

* Fri Jun 16 2000 Preston Brown <pbrown@redhat.com>
- condrestart for initscript, graceful upgrades.

* Thu Feb 03 2000 Erik Troan <ewt@redhat.com>
- gzipped man pages
- marked /etc/rc.d/init.d/dhcp as a config file

* Mon Jan 24 2000 Jakub Jelinek <jakub@redhat.com>
- fix booting of JavaStations
  (reported by Pete Zaitcev <zaitcev@metabyte.com>).
- fix SIGBUS crashes on SPARC (apparently gcc is too clever).

* Fri Sep 10 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %preun, not %postun

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Fri Jun 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.0.

* Fri Jun 18 1999 Bill Nottingham <notting@redhat.com>
- don't run by default

* Wed Jun  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.0b1pl28.

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- copy the source file in %prep, not move

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Mon Jan 11 1999 Erik Troan <ewt@redhat.com>
- added a sample dhcpd.conf file
- we don't need to dump rfc's in /usr/doc

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- modify dhcpd.init to exit if /etc/dhcpd.conf is not present

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- Upgraded to 2.0b1pl6 (patch1 no longer needed).

* Thu Jun 11 1998 Erik Troan <ewt@redhat.com>
- applied patch from Chris Evans which makes the server a bit more paranoid
  about dhcp requests coming in from the wire

* Mon Jun 01 1998 Erik Troan <ewt@redhat.com>
- updated to dhcp 2.0b1pl1
- got proper man pages in the package

* Tue Mar 31 1998 Erik Troan <ewt@redhat.com>
- updated to build in a buildroot properly
- don't package up the client, as it doens't work very well <sigh>

* Tue Mar 17 1998 Bryan C. Andregg <bandregg@redhat.com>
- Build rooted and corrected file listing.

* Mon Mar 16 1998 Mike Wangsmo <wanger@redhat.com>
- removed the actual inet.d links (chkconfig takes care of this for us)
  and made the %postun section handle upgrades.

* Mon Mar 16 1998 Bryan C. Andregg <bandregg@redhat.com>
- First package.

