Name: prosody
Version: 0.11.2
Release: alt1

Summary: Modern XMPP communication server

Group: System/Servers
License: GPL
Url: https://prosody.im/

BuildRequires: openssl lua5 liblua5-devel libidn-devel libssl-devel

Requires: openssl lua-module-luaexpat lua-module-luasocket lua-module-luafilesystem lua-module-luasec

Source0: %name-%version.tar
Source1: %name.cfg.lua
Source2: %name.service

%description
%summary

%prep
%setup

%build
./configure --prefix=/usr
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%systemd_unitdir
mkdir -p %buildroot/%_localstatedir/%name
mv %buildroot/%_sysconfdir/%name/%name.cfg.lua %buildroot/%_sysconfdir/%name/%name.cfg.example.lua
cp %SOURCE1 %buildroot/%_sysconfdir/%name
cp %SOURCE2 %buildroot/%systemd_unitdir

%pre
/usr/sbin/groupadd -r -f _%name
/usr/sbin/useradd -r -g _%name -d /var/empty -s /sbin/nologin -n -c "%summary" _%name >/dev/null 2>&1 ||:

%preun
%preun_service %name

%post
%post_service %name

%files
%_bindir/*
%_libexecdir/%name
%config(noreplace) %_sysconfdir/%name
%systemd_unitdir/%name.service
%attr(0755,_%name,_%name) %dir %_localstatedir/%name
%_man1dir/*

%changelog
* Fri Jan 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.11.2-alt1
- Build new version.

* Fri Dec 14 2018 Grigory Ustinov <grenka@altlinux.org> 0.11.1-alt1
- Build new version (Closes: #33835).

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.10-alt3.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Aug 31 2017 Eugene Prokopiev <enp@altlinux.ru> 0.9.10-alt3
- rebuild with lua5.3 fir sisyphus

* Sat Nov 05 2016 Eugene Prokopiev <enp@altlinux.ru> 0.9.10-alt2
- remove lua-posix dependency

* Tue Nov 01 2016 Eugene Prokopiev <enp@altlinux.ru> 0.9.10-alt1
- new version
- add unit and minimal config

* Tue Jul 05 2016 Eugene Prokopiev <enp@altlinux.ru> 0.9.8-alt1
- inital build

