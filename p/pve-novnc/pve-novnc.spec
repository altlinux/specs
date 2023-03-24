%define sname novnc
%define pname %sname-pve

Name: pve-%sname
Summary: HTML5 VNC client
Version: 1.4.0
Release: alt1
License: MPL-2.0
Group: Networking/WWW
Url: https://git.proxmox.com/

Source0: %name-%version.tar
Source1: %sname.tar
Source2: noVNC-ru.po
Source3: noVNC-ru.json

BuildRequires: esbuild

BuildArch: noarch

%description
VNC client using HTML5 (WebSockets, Canvas). This packet is use by
Proxmox VE to provide HTML VM console

%prep
%setup -q -n %pname -a1

cd %sname
cat ../debian/patches/series | while read p; do patch -p1 < ../debian/patches/$p; done
install -m0644 %SOURCE3 app/locale/ru.json
esbuild --bundle app/ui.js > app.js

%install
mkdir -p %buildroot%_datadir/%pname/app
cp -a %sname/app/images %buildroot%_datadir/%pname/app/
cp -a %sname/app/locale %buildroot%_datadir/%pname/app/
cp -a %sname/app/sounds %buildroot%_datadir/%pname/app/
cp -a %sname/app/styles %buildroot%_datadir/%pname/app/
install -m0644 %sname/app/error-handler.js %buildroot%_datadir/%pname/app/
install -m0644 %sname/app.js %buildroot%_datadir/%pname/
install -m0644 %sname/vnc.html %buildroot%_datadir/%pname/index.html.tpl

%files
%_datadir/%pname

%changelog
* Fri Mar 10 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.4.0-alt1
- 1.4.0-1

* Sat Nov 26 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.3.3-alt2
- add Russian locale

* Thu May 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.3.3-alt1
- 1.3.3
- build from gear

* Wed Sep 11 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0-1

* Fri Mar 01 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0-3

* Fri Jul 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.4-alt2
- added russian translation

* Tue Jul 18 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.4-alt1
- 0.6-4

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.5.8-alt1
- 0.5-8

* Tue Dec 15 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.5.5-alt1
- initial release

