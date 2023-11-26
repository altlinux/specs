Name: xl2tpd
Version: 1.3.18
Release: alt1

Summary: Layer 2 Tunnelling Protocol Daemon (RFC 2661)
License: GPLv2
Group: Accessibility

Url: https://github.com/xelerance/xl2tpd 
Source0: %name-%version.tar

Provides: l2tpd = %EVR
Obsoletes: l2tpd =< 0.69-alt2
BuildRequires: libpcap-devel

%description
xl2tpd is an implementation of the Layer 2 Tunnelling Protocol (RFC 2661).
L2TP allows you to tunnel PPP over UDP. Some ISPs use L2TP to tunnel user
sessions from dial-in servers (modem banks, ADSL DSLAMs) to back-end PPP
servers. Another important application is Virtual Private Networks where
the IPsec protocol is used to secure the L2TP connection (L2TP/IPsec,
RFC 3193). The L2TP/IPsec protocol is mainly used by Windows and
Mac OS X clients. On Linux, xl2tpd can be used in combination with IPsec
implementations such as Openswan.
Example configuration files for such a setup are included in this RPM.

xl2tpd works by opening a pseudo-tty for communicating with pppd.
It runs completely in userspace but supports kernel mode L2TP.

xl2tpd supports IPsec SA Reference tracking to enable overlapping internak
NAT'ed IP's by different clients (eg all clients connecting from their
linksys internal IP 192.168.1.101) as well as multiple clients behind
the same NAT router.

xl2tpd supports the pppol2tp kernel mode operations on 2.6.23 or higher,
or via a patch in contrib for 2.4.x kernels. Note that kernel mode and
IPsec SA Reference tracking do not yet work together.

Xl2tpd is based on the 0.69 L2TP by Jeff McAdams <jeffm@iglou.com>
It was de-facto maintained by Jacco de Leeuw <jacco2@dds.nl> in 2002 and 2003.

%prep
%setup

%build
%make

%install
%makeinstall
install -pDm0755 %name.init %buildroot%_initdir/%name
install -pDm0644 %name.service %buildroot%_unitdir/%name.service
install -Dm 664 doc/l2tp-secrets.sample %buildroot%_sysconfdir/%name/l2tp-secrets
install -Dm 664 doc/l2tpd.conf.sample %buildroot%_sysconfdir/%name/%name.conf

%post
%post_service %name

%preun
%preun_service %name

%triggerun -- l2tpd =< 0.69-alt2
if [ "$2" -eq 0 ]; then
	mv -f /etc/l2tpd/l2tpd.conf /etc/%name/%name.conf
	mv -f /etc/l2tpd/l2tp-secrets /etc/%name/
fi

%files
%doc BUGS CHANGES CREDITS README* TODO
%config %_initdir/%name
%_unitdir/%name.service
%_sbindir/%name
%_sbindir/%name-control
%_bindir/pfc
%_mandir/man?/*
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/l2tp-secrets

%changelog
* Sun Nov 26 2023 Anton Farygin <rider@altlinux.ru> 1.3.18-alt1
- 1.3.18

* Sun Jun 04 2023 Anton Farygin <rider@altlinux.ru> 1.3.17-alt1
- 1.3.17

* Tue Apr 20 2021 Anton Farygin <rider@altlinux.ru> 1.3.16-alt1
- 1.3.16

* Wed Oct 23 2019 Anton Farygin <rider@altlinux.ru> 1.3.15-alt1
- 1.3.15

* Fri Apr 26 2019 Anton Farygin <rider@altlinux.ru> 1.3.14-alt1
- 1.3.14

* Sat Oct 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.10-alt1
- 1.3.10 released

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 1.3.9-alt1
- new version

* Fri Jan 30 2015 Anton Farygin <rider@altlinux.ru> 1.3.6-alt1
- new version

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.0-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Wed Sep 28 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.0-alt1
- 1.3.0 (Closes: #26377).

* Tue Aug 10 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.7-alt1
- 1.2.7
- Rename package from l2tpd to xl2tpd
- Continue redialing even if gethostbyname() failed (patch from corbina
  user)
- Default confiruration directory is now /etc/xl2tpd/
- Fix configs packaging

* Tue May 16 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.69-alt2
- Added patch for gcc4.1

* Fri Mar 24 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.69-alt1
- Inital build for sisyphus (may be rough)

