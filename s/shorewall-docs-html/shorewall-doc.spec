
Name: shorewall-docs-html
Version: 4.4.23.3
Release: alt1
Summary: Shoreline Firewall is an iptables-based firewall for Linux systems.
License: GPL
Group: Security/Networking
Url: http://www.shorewall.net/
Source0: %name-%version.tar.bz2

Packager: Alexey Shabalin <shaba@altlinux.ru>

BuildArch: noarch

%description
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

%prep
%build

%install
mkdir -p %buildroot%_docdir
%__tar -xjf %SOURCE0 -C %buildroot%_docdir/

%files
%_docdir/*

%changelog
* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 4.4.23.3-alt1
- 4.4.23.3

* Fri Dec 17 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.15.1-alt1
- 4.4.15.1

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.13.1-alt1
- 4.4.13.1

* Thu Feb 11 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.6-alt1
- 4.4.6

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.4-alt1
- 4.4.4

* Fri Nov 06 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt1
- 4.4.3

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.2-alt1
- 4.4.2

* Fri Oct 02 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- 4.4.1
- current stable release 4.4

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
