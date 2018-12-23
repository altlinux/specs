Name: vpn-ws
Version: 0.2
Release: alt2

Summary: A VPN system over websockets

License: MIT
Group: System/Servers
Url: https://github.com/unbit/vpn-ws

Source: %name-%version.tar

BuildRequires: openssl-devel

%description
This is the client/server implementation of a layer-2 software switch able to route packets over websockets connections.
The daemon is meant to be run behind nginx, apache, the uWSGI http router or a HTTP/HTTPS proxy able to speak the uwsgi
protocol and to manage websockets connections.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot/%_sbindir/
cp vpn-ws* %buildroot/%_sbindir/
mkdir -p %buildroot/%_sysconfdir
echo URL= > %buildroot/%_sysconfdir/vpn-ws-client.conf
mkdir -p %buildroot/%systemd_unitdir
cp altlinux/vpn-ws*.service %buildroot/%systemd_unitdir/

%files
%doc README.md
%_sbindir/*
%_sysconfdir/vpn-ws-client.conf
%systemd_unitdir/vpn-ws*.service

%changelog
* Sun Dec 23 2018 Eugene Prokopiev <enp@altlinux.ru> 0.2-alt2
- vpn-ws is ready to use

* Sat Dec 22 2018 Eugene Prokopiev <enp@altlinux.ru> 0.2-alt1
- initial build

