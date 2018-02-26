
Name: shorewall
Version: 4.4.23.3
Release: alt3
Summary: Shoreline Firewall is an iptables-based firewall for Linux systems.
License: GPLv2
Group: Security/Networking
Url: http://www.shorewall.net/
Source0: %name-%version.tar.bz2
Source1: shorewall.init
Source3: shorewall-control
Source4: shorewall-README.ALT.RU.UTF8

Packager: Alexey Shabalin <shaba@altlinux.ru>

BuildArch: noarch
Requires: iptables iproute2
Provides: shorewall-common = %version-%release
Obsoletes: shorewall-common < %version-%release
Provides: shorewall-compiler = %version-%release
Obsoletes: shorewall-compiler < %version-%release
Obsoletes: shorewall-compiler-perl < %version-%release
Obsoletes: shorewall-compiler-shell < %version-%release


%description
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

%prep
%setup -q

%install
PREFIX=%buildroot DEST=%_initdir SYSTEMD=Yes %_buildshell install.sh
install -m 0755 -p %SOURCE1 %buildroot%_initdir/%name
install -D -m 0755 %SOURCE3 %buildroot%_controldir/%name
install -m 0644 %SOURCE4 README.ALT.RU.UTF8

mkdir -p %buildroot%perl_vendor_privlib
mv -f %buildroot%_datadir/%name/Shorewall %buildroot%perl_vendor_privlib/

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING INSTALL changelog.txt releasenotes.txt Samples Contrib
%doc README.ALT.RU.UTF8
/sbin/%name
%config %_initdir/%name
%systemd_unitdir/*.service
%dir %_sysconfdir/%name
%attr(0600,root,root) %config(noreplace) %_sysconfdir/%name/[a-z]*
%attr(0600,root,root) %_sysconfdir/%name/Makefile
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_controldir/%name
%dir %_datadir/%name
%dir %_datadir/%name/configfiles
%_datadir/%name/*
%dir %_localstatedir/%name
%perl_vendor_privlib/Shorewall
%_datadir/%name/compiler.pl

%_man5dir/*
%_man8dir/*

%changelog
* Wed Oct 05 2011 Alexey Shabalin <shaba@altlinux.ru> 4.4.23.3-alt3
- only root have access to config files

* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 4.4.23.3-alt2
- drop all %%attr

* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 4.4.23.3-alt1
- 4.4.23.3

* Fri Dec 17 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.15.1-alt1
- 4.4.15.1

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.13.1-alt1
- 4.4.13.1

* Thu Feb 11 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.6-alt1
- 4.4.6

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.4.2-alt1
- 4.4.4.2

* Fri Nov 06 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt1
- 4.4.3

* Thu Oct 29 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.2.4-alt1
- 4.4.2.4
- Obsoletes shorewall-compiler-perl and shorewall-compiler-shell

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.2.3-alt1
- 4.4.2.3

* Fri Oct 02 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.1.2-alt1
- 4.4.1.2
- current stable release 4.4
- the shorewall-common, shorewall-shell and shorewall-perl packages
  are discontinued and replaced with a single Shorewall package
  which combines the functions of shorewall-common and Shorewall-perl
- the shell-based compiler is retired

* Thu Jun 04 2009 Alexey Shabalin <shaba@altlinux.ru> 4.2.9-alt1
- 4.2.9

* Mon Apr 20 2009 Alexey Shabalin <shaba@altlinux.ru> 4.2.8-alt1
- 4.2.8

* Mon Dec 22 2008 Alexey Shabalin <shaba@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Fri Oct 17 2008 Alexey Shabalin <shaba@altlinux.ru> 4.2.0-alt1
- 4.2.0 (new STABLE release series)

* Wed Jun 18 2008 Alexey Shabalin <shaba@altlinux.ru> 3.4.8-alt1
- 3.4.8

* Thu Nov 08 2007 Alexey Shabalin <shaba@altlinux.ru> 3.4.7-alt2
- apply patch patch-3.4.7-1.diff from errata

* Wed Oct 10 2007 Alexey Shabalin <shaba@altlinux.ru> 3.4.7-alt1
- 3.4.7

* Thu Sep 20 2007 Alexey Shabalin <shaba@altlinux.ru> 3.4.6-alt1
- 3.4.6

* Fri Jul 20 2007 Alexey Shabalin <shaba@altlinux.ru> 3.4.5-alt1
- 3.4.5

* Sun Jul 15 2007 Alexey Shabalin <shaba@altlinux.ru> 3.4.4-alt6
- 3.4.4-6

* Fri Jun 22 2007 Alexey Shabalin <shaba@altlinux.ru> 3.4.4-alt1
- 3.4.4-1
- fix control

* Sat Jun 02 2007 Alexey Shabalin <shaba@altlinux.ru> 3.4.3-alt1
- 3.4.3
- add %%patch1 - fix work tcrules with multiport

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 3.4.2-alt1
- 3.4.2
- remove patches
- add manpages

* Thu Mar 01 2007 Alexey Shabalin <shaba@altlinux.ru> 3.2.9-alt1
- Initial build for Sisyphus
