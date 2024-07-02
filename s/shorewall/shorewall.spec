%define _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: shorewall
Version: 5.2.8
Release: alt2
Summary: Shoreline Firewall is an iptables-based firewall for Linux systems.
License: GPLv2
Group: Security/Networking
Url: http://www.shorewall.net/
Source: %name-%version.tar.bz2
Source3: shorewall-control
Source4: shorewall-README.ALT.RU.UTF8

BuildArch: noarch
Requires: shorewall-core
Provides: shorewall-common = %version-%release
Obsoletes: shorewall-common < %version-%release
Provides: shorewall-compiler = %version-%release
Obsoletes: shorewall-compiler < %version-%release
Obsoletes: shorewall-compiler-perl < %version-%release
Obsoletes: shorewall-compiler-shell < %version-%release
Provides: shoreline_firewall = %version-%release

BuildRequires: perl-Digest-SHA

%description
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

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
install -m 0644 %SOURCE4 README.ALT.RU.UTF8
touch %buildroot%_sysconfdir/%name/isusable

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING INSTALL changelog.txt releasenotes.txt Samples Contrib
%doc README.ALT.RU.UTF8
%_initdir/%name
%_unitdir/%name.service
%dir %_sysconfdir/%name
%attr(0600,root,root) %config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%ghost %_sysconfdir/%name/isusable
%_controldir/%name
%_datadir/%name/*
%dir %_localstatedir/%name
%perl_vendor_privlib/Shorewall
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

* Sat Jul 14 2018 Alexey Shabalin <shaba@altlinux.ru> 5.2.1-alt0.Beta2
- 5.2.1-Beta2

* Fri Apr 27 2018 Grigory Ustinov <grenka@altlinux.org> 4.4.23.3-alt3.1
- Rebuilt for e2k.

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
