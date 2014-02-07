Name: aceproxy
Version: 0.6
Release: alt1

Summary: AceProxy: Ace Stream HTTP Proxy

Group: Video
License: MIT
Url: https://github.com/ValdikSS/aceproxy

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/ValdikSS/aceproxy
Source: %name-%version.tar

BuildArch: noarch

%description
AceProxy allows you to watch Ace Stream live streams or BitTorrent files over HTTP.
It's written in Python + gevent.

Currently it supports Ace Stream Content-ID hashes (PIDs),
.acestream files and usual torrent files.

For installation, configuration and using info, visit Wiki:
https://github.com/ValdikSS/aceproxy/wiki/

Check config in /etc/aceproxy/aceconfig.py
Run $ aceproxy

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/%name/
ln -s %_datadir/%name/aceconfig.py %buildroot%_sysconfdir/%name/aceconfig.py

mkdir -p %buildroot%_bindir/
cat <<EOF >%buildroot%_bindir/%name
#!/bin/sh
cd %_datadir/%name/
python acehttp.py
EOF
chmod 0755 %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/%name/
cp -a * %buildroot/%_datadir/%name/

%files
%_bindir/aceproxy
%_datadir/%name/
%dir %_sysconfdir/%name/
%_sysconfdir/%name/aceconfig.py

%changelog
* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus
