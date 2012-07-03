Summary: An easy to use but powerfull iptables stateful firewall
Name: firehol
Version: 1.282
Release: alt2.cvs20090219
License: GPL
Group: System/Configuration/Networking
Source0: %name-%version.tar
Source1: ftp_ssl.conf
# checkout 2009-04-11
Source2: RESERVED_IPS
Patch1: firehol.sh-alt-iptables.patch
Patch2: firehol.sh-alt-init.patch
Patch3: firehol.sh-alt-init-prio.patch
Patch4: alt-get-iana.patch
Patch5: alt-check-iana.patch
Url: http://firehol.sourceforge.net

Packager: L.A. Kostis <lakostis@altlinux.ru>

BuildArch: noarch

Requires: which

%description
FireHOL uses an extremely simple but powerfull way to define firewall
rules which it turns into complete stateful iptables firewalls.  FireHOL
is a generic firewall generator, meaning that you can design any kind of
local or routing stateful packet filtering firewalls with ease.

Install FireHOL if you want an easy way to configure stateful packet
filtering firewalls on Linux hosts and routers.

You can run FireHOL with the 'helpme' argument, to get a configuration
file for the system run, which you can modify according to your needs.

The default configuration file will allow only client traffic on all
interfaces.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p2
%patch5 -p2

%build
%install
rm -rf doc/create_services.sh
mkdir -p %buildroot%_sysconfdir/firehol/examples
mkdir -p %buildroot%_sysconfdir/firehol/services
mkdir -p %buildroot%_initdir
install -m 750 firehol.sh %buildroot%_initdir/firehol
install -m 640 examples/client-all.conf %buildroot%_sysconfdir/firehol/firehol.conf
mkdir -p %buildroot/%_man1dir
mkdir -p %buildroot/%_man5dir
install -m 644 man/firehol.1 %buildroot/%_mandir/man1/
install -m 644 man/firehol.conf.5 %buildroot/%_mandir/man5/
install -m 640 %SOURCE1 %buildroot%_sysconfdir/firehol/services/
install -m 640 %SOURCE2 %buildroot%_sysconfdir/firehol/
install -m 644 examples/home-adsl.conf %buildroot%_sysconfdir/firehol/examples/home-adsl.conf
install -m 644 examples/home-dialup.conf %buildroot%_sysconfdir/firehol/examples/home-dialup.conf
install -m 644 examples/office.conf %buildroot%_sysconfdir/firehol/examples/office.conf
install -m 644 examples/server-dmz.conf %buildroot%_sysconfdir/firehol/examples/server-dmz.conf
install -m 644 examples/client-all.conf %buildroot%_sysconfdir/firehol/examples/client-all.conf
install -m 644 examples/lan-gateway.conf %buildroot%_sysconfdir/firehol/examples/lan-gateway.conf

%pre
%post
if [ -f %_sysconfdir/firehol.conf -a ! -f %_sysconfdir/firehol/firehol.conf ]
then
	mv -f %_sysconfdir/firehol.conf %_sysconfdir/firehol/firehol.conf
	echo
	echo
	echo "FireHOL has now its configuration in %_sysconfdir/firehol/firehol.conf"
	echo "Your existing configuration has been moved to its new place."
	echo
fi
%post_service firehol

%preun
%preun_service firehol

%files
%doc README TODO COPYING ChangeLog WhatIsNew
%dir %_sysconfdir/firehol
%dir %_sysconfdir/firehol/examples
%dir %_sysconfdir/firehol/services
%_sysconfdir/firehol/services/*
%_initdir/firehol
%_man1dir/*
%_man5dir/*
%config(noreplace) %_sysconfdir/firehol/firehol.conf
%config(noreplace) %_sysconfdir/firehol/RESERVED_IPS
%_sysconfdir/firehol/examples/*
%doc adblock.sh get-iana.sh check-iana.sh
%doc doc/*

%changelog
* Tue Aug 24 2010 L.A. Kostis <lakostis@altlinux.ru> 1.282-alt2.cvs20090219
- Added patches:
  + {alt-get-iana,alt-check-iana}.patch: update to latest
    iana assignments URL and file format.

* Sat Apr 11 2009 L.A. Kostis <lakostis@altlinux.ru> 1.282-alt1.cvs20090219
- 2009-02-19 CVS snapshot.
- update RESERVED_IPS list.

* Fri Aug 29 2008 L.A. Kostis <lakostis@altlinux.ru> 1.268-alt1.cvs20080809
- 2008-08-09 CVS snapshot.
- add -iana scripts to documentation.
- add RESERVED_IPS as static file (feel free to update it manually/by cron).

* Sun Apr 29 2007 L.A. Kostis <lakostis@altlinux.ru> 1.226-alt3.cvs20070210
- update IANA ipv4 reserved address space.

* Sun Mar 18 2007 L.A. Kostis <lakostis@altlinux.ru> 1.226-alt2.cvs20070210
- fix start/stop init priority:
  - make it start early after network and stop before network.

* Sun Feb 11 2007 L.A. Kostis <lakostis@altlinux.ru> 1.226-alt1.cvs20070210
- initial build for ALTLinux.
- 2007-02-10 CVS snapshot.
- add ftp ssl/tls support services.
