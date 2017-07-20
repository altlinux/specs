%define sname novnc
%define pname %sname-pve

Name: pve-%sname
Summary: HTML5 VNC client
Version: 0.6.4
Release: alt1
License: MPL 2.0
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: %pname.tar.xz
Source1: %sname.tar.xz

BuildArch: noarch

%description
VNC client using HTML5 (WebSockets, Canvas). This packet is use by
Proxmox VE to provide HTML VM console

%prep
%setup -q -n %pname -a1

cd %sname
ls ../debian/patches/*.patch | while read p; do patch -p1 < $p; done

%install
mkdir -p %buildroot%_datadir/%pname/app
cp -a %sname/app/images %buildroot%_datadir/%pname/app/
cp -a %sname/app/locale %buildroot%_datadir/%pname/app/
cp -a %sname/app/sounds %buildroot%_datadir/%pname/app/
cp -a %sname/app/styles %buildroot%_datadir/%pname/app/
install -m0644 %sname/app/error-handler.js %buildroot%_datadir/%pname/app/
install -m0644 %sname/app/ui.js %buildroot%_datadir/%pname/app.js
install -m0644 %sname/vnc.html %buildroot%_datadir/%pname/index.html.tpl

%files
%_datadir/%pname

%changelog
* Tue Jul 18 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.4-alt1
- 0.6-4

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.5.8-alt1
- 0.5-8

* Tue Dec 15 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.5.5-alt1
- initial release

