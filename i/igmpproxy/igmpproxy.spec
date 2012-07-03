Name: igmpproxy
Version: 0.1
Release: alt1

Summary: Dynamic Multicast Routing Daemon
License: GPLv2
Group: System/Configuration/Networking
Url: http://sourceforge.net/projects/igmpproxy/

Packager: Vitaly Kuznetsovr <vitty@altlinux.ru>
Source0: %name-%version.tar

%description
IGMPproxy is a simple dynamic Multicast Routing Daemon using only IGMP
signalling. It's intended for simple forwarding of Multicast traffic 
between networks.

%prep
%setup
%autoreconf

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc NEWS README COPYING
%config(noreplace) %_sysconfdir/*.conf
%_sbindir/*
%_man5dir/*
%_man8dir/*

%changelog
* Fri May 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- Initial
