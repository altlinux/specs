
Name: shorewall6-lite
Version: 4.4.23.3
Release: alt3
Summary: Shoreline Firewall 6 Lite is an iptables-based firewall for Linux systems.
License: GPLv2
Group: Security/Networking
Url: http://www.shorewall.net/
Source0: %name-%version.tar.bz2
Source1: %name.init
Source3: %name-control

Packager: Alexey Shabalin <shaba@altlinux.ru>

BuildArch: noarch
Requires: iptables iproute2 iptables-ipv6

%description
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

Shorewall Lite is a companion product to Shorewall that allows network
administrators to centralize the configuration of Shorewall-based firewalls.

%prep
%setup -q

%install
PREFIX=%buildroot DEST=%_initdir SYSTEMD=Yes %_buildshell install.sh
install -m 0755 -p %SOURCE1 %buildroot%_initdir/%name
install -D -m 0755 %SOURCE3 %buildroot%_controldir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING changelog.txt releasenotes.txt
/sbin/%name
%config %_initdir/%name
%systemd_unitdir/*.service
%dir %_sysconfdir/%name
%attr(0600,root,root) %config(noreplace) %_sysconfdir/%name/[a-z]*
%attr(0600,root,root) %_sysconfdir/%name/Makefile
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_controldir/%name
%dir %_datadir/%name
%_datadir/%name/*
%dir %_localstatedir/%name
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

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.2-alt1
- 4.4.2

* Fri Oct 02 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- Initial build for Sisyphus
