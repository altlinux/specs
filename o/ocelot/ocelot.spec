Name:     ocelot
Version:  1.0
Release:  alt1

Summary:  Alternative compiled announcer (ocelot)
License:  Noncommercial public
Group:    Other

Url:      https://github.com/torrentpier/ocelot

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/torrentpier/ocelot.git
Source:   %name-%version.tar
Source1:  %name.service

BuildRequires: gcc-c++ boost-asio-devel boost-coroutine-devel boost-devel boost-serialization libev-devel libgperftools-devel libmysql++-devel libmysqlclient-devel

%description
Ocelot is a BitTorrent tracker written in C++ for the Gazelle project.
It supports requests over TCP and can only track IPv4 peers.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
install -m0644 -D ocelot.conf.dist %buildroot%_sysconfdir/%name/ocelot.conf
install -m0644 -D %SOURCE1 %buildroot%_unitdir/%name.service

%check
%make_build check

%pre
/usr/sbin/groupadd -r -f _ocelot
/usr/sbin/useradd -r -g _ocelot -d /var/empty -s /dev/null -c 'Ocelot announcer' _ocelot >/dev/null 2>&1 ||:

%files
%_bindir/*
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/ocelot.conf
%_unitdir/%name.service
%doc LICENSE CHANGES README.md

%changelog
* Sun Jan 28 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
