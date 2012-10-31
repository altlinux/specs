Name: opennhrp
Version: 0.13.1
Release: alt1
Summary: NBMA Next Hop Resolution Protocol
Source: %name-%version.tar
Group: Networking/Other
License: GPL

Source1: opennhrp.init

BuildRequires: libcares-devel

%description
OpenNHRP implements NBMA Next Hop Resolution Protocol (as defined in
RFC 2332). It makes it possible to create dynamic multipoint VPN Linux
router using NHRP, GRE and IPsec. It aims to be Cisco DMVPN
compatible.

%prep
%setup

%build
%make \
	DOCDIR=%_defaultdocdir/%name-%version \
	MANDIR=%_mandir \
	CONFDIR=%_sysconfdir/%name \
	SBINDIR=%_sbindir \
	STATEDIR=%_runtimedir

%install
%make_install \
	DESTDIR=%buildroot \
	DOCDIR=%_defaultdocdir/%name-%version \
	MANDIR=%_mandir \
	CONFDIR=%_sysconfdir/%name \
	SBINDIR=%_sbindir \
	STATEDIR=%_runtimedir \
	install

install -m755 -D %SOURCE1 %buildroot%_initdir/opennhrp

%post
%post_service %name

%preun
%preun_service %name

%files
%config(noreplace) %attr(644,root,root) %_sysconfdir/%name/opennhrp.conf
%config %_initdir/opennhrp
%_sysconfdir/%name/opennhrp-script
%_sysconfdir/%name/*.sh
%_sbindir/*
%_defaultdocdir/%name-%version
%_man5dir/*
%_man8dir/*

%changelog
* Fri Aug 10 2012 Afanasov Dmitry <ender@altlinux.org> 0.13.1-alt1
- first build

