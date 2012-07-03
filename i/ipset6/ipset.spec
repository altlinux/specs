%define prefix /
%define exec_prefix /
%define _prefix /
%define origname ipset
Name: ipset6
Version: 6.8
Release: alt2

Summary: Tools for managing sets of IP or ports with iptables
License: GPLv2
Group: System/Kernel and hardware
Url: http://ipset.netfilter.org/

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: libmnl-devel

%description
IP sets are a framework inside the Linux 2.4.x and 2.6.x kernel,
which can be administered by the ipset utility.
Depending on the type, currently an IP set may store IP addresses,
(TCP/UDP) port numbers or IP addresses with MAC addresses in a way,
which ensures lightning speed when matching an entry against a set.

ipset may be the proper tool for you, if you want to
 * store multiple IP addresses or port numbers and match against the
   collection by iptables at one swoop;
 * dynamically update iptables rules against IP addresses or ports
   without performance penalty;
 * express complex IP address and ports based rulesets with one single
   iptables rule and benefit from the speed of IP sets

%prep
%setup -q
%patch0 -p1
autoreconf -fisv

%build
%configure --without-kbuild --without-ksource
%make_build LIBDIR=/%_lib/ BINDIR=/sbin/

%install
%makeinstall prefix=%buildroot/ exec_prefix=%buildroot/ sbindir=%buildroot/sbin libdir=%buildroot/%_lib

%files
%doc ChangeLog ChangeLog.ippool README
/sbin/*
%_man8dir/*

%changelog
* Thu Aug 04 2011 Mykola Grechukh <gns@altlinux.ru> 6.8-alt2
- name changed to ipset6

* Tue Aug 02 2011 Anton Farygin <rider@altlinux.ru> 6.8-alt1
- new version

* Mon Apr 18 2011 Anton Farygin <rider@altlinux.ru> 4.5-alt1
- new version

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 4.4-alt1
- new version

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 4.3-alt1
- new version
- build kernel-source from this package

* Fri Mar 12 2010 Igor Zubkov <icesik@altlinux.org> 4.1-alt2
- move binaries from /usr/sbin/ to /sbin/ and
  libraries from /usr/lib/ to /lib/

* Wed Dec 23 2009 Igor Zubkov <icesik@altlinux.org> 4.1-alt1
- 3.2 -> 4.1

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 3.2-alt1
- 2.4.5 -> 3.2

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 2.4.5-alt1
- 2.4.4 -> 2.4.5

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 2.4.4-alt1
- 2.4.3 -> 2.4.4

* Sun Oct 26 2008 Igor Zubkov <icesik@altlinux.org> 2.4.3-alt1
- 2.3.0 -> 2.4.3

* Wed Jul 09 2008 Igor Zubkov <icesik@altlinux.org> 2.3.0-alt1
- 2.2.9 -> 2.3.0
- update and cleanup kernel headers in package

* Thu Jun 28 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 2.2.9-alt1
- rebuild for ALTLinux.
- fix link problem (tnx to ldv@ for simular fix in iptables).

* Fri Aug  4 2006 Samir Bellabes <sbellabes@n4.mandriva.com> 2.2.9-1mdv2007.0
- new release.
- use mkrel tag
- include kernel headers in the package.

* Wed Aug 31 2005 Couriousous <couriousous@mandriva.org> 2.2.2-4mdk
- Fix plugin loading on x86_64

* Wed Aug 10 2005 Samir Bellabes <sbellabes@mandriva.com> 2.2.2-3mdk
- Fix missing PREFIX

* Tue Aug  2 2005 Olivier Blin <oblin@mandriva.com> 2.2.2-2mdk
- fix libdir on x86_64

* Fri Jul 29 2005 Samir Bellabes <sbellabes@mandriva.com> 2.2.2-1mdk
- first release
