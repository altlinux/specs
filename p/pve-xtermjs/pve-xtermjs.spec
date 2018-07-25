Name: pve-xtermjs
Summary: HTML/JS Shell client
Version: 1.0.5
Release: alt1
License: GPL
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: %name.tar.xz

BuildArch: noarch
BuildRequires: pve-common

%description
This is an xterm.js client for PVE Host, Container and Qemu Serial Terminal

%prep
%setup -q -n %name

tar -xf xterm-*.tgz
cp -ar package/dist/* src/www

sed -i 's|Proxmox|PVE|' src/www/index.html.tpl.in

%install
%make -C src DESTDIR=%buildroot install

%files
%_bindir/termproxy
%_datadir/%name
%perl_vendor_privlib/PVE

%changelog
* Fri Jul 20 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0-5

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- initial release

