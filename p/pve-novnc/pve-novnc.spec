%define sname novnc
%define pname %sname-pve

Name: pve-%sname
Summary: HTML5 VNC client
Version: 0.5.5
Release: alt1
License: MPL 2.0
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: %sname.tgz

Patch1: novnc-pveui.patch
Patch2: novnc-fix-base-css.patch

BuildArch: noarch

%description
VNC client using HTML5 (WebSockets, Canvas). This packet is use by
Proxmox VE to provide HTML VM console

%prep
%setup -q -n %sname
cp include/ui.js pveui.js
%patch1 -p1
%patch2 -p1

%install
mkdir -p %buildroot%_datadir/%pname
cp -a images %buildroot%_datadir/%pname/
cp -a include %buildroot%_datadir/%pname/
install -m0644 pveui.js %buildroot%_datadir/%pname/include/pveui.js

%files
%dir %_datadir/%pname
%dir %_datadir/%pname/include
%_datadir/%pname/include/playback.js
%_datadir/%pname/include/keyboard.js
%_datadir/%pname/include/blue.css
%_datadir/%pname/include/jsunzip.js
%_datadir/%pname/include/keysym.js
%_datadir/%pname/include/Orbitron700.woff
%_datadir/%pname/include/pveui.js
%_datadir/%pname/include/webutil.js
%_datadir/%pname/include/black.css
%_datadir/%pname/include/keysymdef.js
%_datadir/%pname/include/logo.js
%_datadir/%pname/include/websock.js
%_datadir/%pname/include/des.js
%_datadir/%pname/include/display.js
%_datadir/%pname/include/inflator.js
%_datadir/%pname/include/base.css
%_datadir/%pname/include/base64.js
%_datadir/%pname/include/rfb.js
%_datadir/%pname/include/Orbitron700.ttf
%_datadir/%pname/include/input.js
%_datadir/%pname/include/util.js
%_datadir/%pname/images

%changelog
* Tue Dec 15 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.5.5-alt1
- initial release

