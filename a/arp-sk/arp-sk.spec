Name: arp-sk
Version: 0.0.16
Release: alt1
Summary: ARP traffic generation tools

License: GPL
Group: Communications
URL: http://sid.rstack.org/arp-sk

Packager: Pavlov Konstantin <thresh@altlinux.ru>
Source: http://sid.rstack.org/arp-sk/files/%name-%version.tgz
Source1: arp-sk.start
Source2: arp-sk.conf

Patch1: arp-sk-0.0.16-no-compat.patch

BuildRequires: libnet2-devel automake autoconf

%description
A tool designed to manipulate ARP tables of all kinds of equipment.

%package server
Summary: ARP traffic generation tools -- server init script.
Requires: %name = %version-%release
Group: System/Servers

%description server
A tool designed to manipulate ARP tables of all kinds of equipment.

This package contains startup script for arp-sk in daemon mode.

%prep
%setup

%patch1 -p1

rm -rf compat/

%build

%__autoreconf

%configure \
	--prefix=%_prefix 

%__make

%install

%make_install DESTDIR="%buildroot" install

mkdir -p %buildroot%_datadir/doc/%name-%version
install -pm644 AUTHORS ChangeLog NEWS README TODO ARP CONTRIB %buildroot%_datadir/doc/%name-%version

ln -sf /usr/share/license/GPL-2 %buildroot%_datadir/doc/%name-%version/COPYING

mkdir -p %buildroot%_initdir
install -p -m755 %SOURCE1 %buildroot%_initdir/arp-sk

mkdir -p %buildroot%_sysconfdir/sysconfig
install -pm644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/arp-sk

%post server
%post_service arp-sk

%preun server
%preun_service arp-sk

%files
%_sbindir/*
%_man1dir/*
%_datadir/doc/%name-%version

%files server
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Fri Sep 29 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.16-alt1
- initial version.

