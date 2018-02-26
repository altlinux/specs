Name: xl2tpd
Version: 1.3.0
Release: alt1

Summary: Layer 2 Tunnelling Protocol Daemon (RFC 2661)
License: GPL
Group: Accessibility

# http://git.openswan.org/cgi-bin/gitweb.cgi?p=xl2tpd
# git://git.openswan.org/xl2tpd
Url: http://www.xelerance.com/software/xl2tpd/
Source0: %name-%version.tar

Provides: l2tpd = %version-%release
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
%_sbindir/%name
%_sbindir/%name-control
%_bindir/pfc
%_mandir/man?/*
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/l2tp-secrets

%changelog
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

