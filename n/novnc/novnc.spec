Name: novnc
Version: 1.4.0
Release: alt1
Summary: VNC client using HTML5 (Web Sockets, Canvas) with encryption support

Group: Networking/Remote access
License: LGPL-3.0-only AND MPL-2.0
Url: https://github.com/novnc/noVNC
Source: %name-%version.tar

BuildArch: noarch

Provides: noVNC = %EVR
Requires: websockify

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%description
Websocket implementation of VNC client.

%prep
%setup
# hide requires git
sed -i 's|git clone|hide_me = git clone|' utils/novnc_proxy
# fix shebang
sed -i 's|/usr/bin/env bash|/bin/bash|' utils/novnc_proxy

%build
%install
mkdir -p %buildroot%_datadir/%name/utils
install -m 644 *html %buildroot%_datadir/%name
#provide an index file to prevent default directory browsing
install -m 644 vnc.html %buildroot%_datadir/%name/index.html
install -m 644 vnc_lite.html %buildroot%_datadir/%name/vnc_auto.html

cp -rp app  %buildroot%_datadir/%name
cp -rp core  %buildroot%_datadir/%name
cp -rp vendor  %buildroot%_datadir/%name

mkdir -p %buildroot%_bindir
install -m 755 utils/novnc_proxy %buildroot%_bindir/novnc_proxy
ln -r -s %buildroot%_bindir/novnc_proxy %buildroot%_bindir/novnc_server

mkdir -p %buildroot%_man1dir
install -m 644 docs/novnc_proxy.1 %buildroot%_man1dir/

%files
%doc README.md LICENSE.txt docs/API.md
%_datadir/%name
%_bindir/*
%_man1dir/*.1*

%changelog
* Fri Sep 15 2023 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Feb 11 2019 Lenar Shakirov <snejok@altlinux.ru> 0.6.2-alt2
- novnc-0.6.2-hide-git-require.patch added

* Wed Nov 01 2017 Lenar Shakirov <snejok@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.1-alt1
- 0.5.1
- cleanup spec

* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4-alt1
- First build for ALT (based on Fedora 0.4-9.fc21.src)

