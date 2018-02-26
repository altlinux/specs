Summary: Static Multicast Routing Daemon
Name: smcroute
Version: 0.94.1
Release: alt2
License: GPL
Group: System/Servers
Source: %name-%version.tar
Url: http://alioth.debian.org/projects/smcroute

Source1: %name.init

Patch0: %name-%version-alt-changes.patch

%description
SMCRoute is a daemon and command line tool to manipulate the multicast routes
of the Linux kernel. It can be used as an alternative to dynamic multicast
routers like 'mrouted' in situations where (only) static multicast routes
should be maintained and/or no proper IGMP signaling exists.

%prep
%setup
%patch -p1

%build
cd src
%autoreconf
%configure
%make_build all

%install
make -C src BINDIR=%buildroot%_sbindir install
install -pD doc/smcroute.8 %buildroot%_man8dir/smcroute.8
install -pD doc/mcsender.8 %buildroot%_man8dir/mcsender.8
install -m755 -D %SOURCE1 %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc ChangeLog AUTHORS COPYING
%_initdir/*
%_sbindir/*
%_man8dir/*

%changelog
* Mon Mar 01 2010 Afanasov Dmitry <ender@altlinux.org> 0.94.1-alt2
- build with ipv6 support but disable it by default

* Sat Feb 27 2010 Afanasov Dmitry <ender@altlinux.org> 0.94.1-alt1
- 0.94.1 release
- change Url
- add pidfile support
- add init script

* Tue Sep 02 2008 Afanasov Dmitry <ender@altlinux.org> 0.93d-alt1
- first build
