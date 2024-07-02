%define _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: shorewall6-lite
Version: 5.2.8
Release: alt2
Summary: Shoreline Firewall 6 Lite is an iptables-based firewall for Linux systems.
License: GPLv2
Group: Security/Networking
Url: http://www.shorewall.net/
Source: %name-%version.tar.bz2
Source3: %name-control

BuildArch: noarch
Requires: shorewall-core iptables-ipv6
Provides: shoreline_firewall = %version-%release

BuildRequires: perl-Digest-SHA

%description
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

Shorewall Lite is a companion product to Shorewall that allows network
administrators to centralize the configuration of Shorewall-based firewalls.

%prep
%setup -n %name-%version
sed -i "s|SERVICEDIR=/lib/systemd/system|SERVICEDIR=%_unitdir|g" shorewallrc.alt

%build
%install
./configure.pl --host=%_vendor \
               --prefix=%prefix \
               --perllibdir=%perl_vendorlib \
               --libexecdir=%_libexecdir \
               --sbindir=%_sbindir

DESTDIR=%buildroot ./install.sh

install -D -m 0755 %SOURCE3 %buildroot%_controldir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING changelog.txt releasenotes.txt
%_sbindir/%name
%_initdir/%name
%_unitdir/%name.service
%dir %_sysconfdir/%name
%attr(0644,root,root) %config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_controldir/%name
%dir %_datadir/%name
%_datadir/%name/*
%dir %_localstatedir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/*
%_man5dir/*
%_man8dir/*

%changelog
* Tue Jul 02 2024 Alexey Shabalin <shaba@altlinux.org> 5.2.8-alt2
- Fix systemd unit path.

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 5.2.8-alt1
- 5.2.8

* Mon Mar 25 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.3.2-alt1
- 5.2.3.2

* Thu Feb 07 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.2-alt1
- 5.2.2

* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.1.4-alt1
- 5.2.1.4

* Fri Nov 16 2018 Alexey Shabalin <shaba@altlinux.org> 5.2.1.1-alt1
- 5.2.1.1

* Wed Jul 18 2018 Alexey Shabalin <shaba@altlinux.org> 5.2.1-alt0.Beta2
- 5.2.1-Beta2

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
