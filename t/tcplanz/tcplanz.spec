Name: tcplanz
Version: 0.1
Release: alt1

Summary: TCPDump latency analyzer

Url: https://github.com/yandex/tcplanz
License: Yandex public license
Group: Monitoring

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/yandex/tcplanz.git
Source: %name-%version.tar

BuildArch: noarch

%description
This project allows to get web server performance metric from traffic TCPDump.
This allows to measure up metric like html delivery time which are
usually not available in runtime and have second opinion about other metrics like server latency.

%prep
%setup
find -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env pypy|#!%__python|'

%build

%install
mkdir -p %buildroot%_datadir/%name/ %buildroot%_bindir/
cp -a refactoring *.py %buildroot%_datadir/%name/
mv %buildroot%_datadir/%name/decode-pcap.py %buildroot%_bindir/%name
# compat
ln -s %name %buildroot%_bindir/decode-pcap
ln -s %name %buildroot%_bindir/parse-pcap

%files
%doc broken/removed.txt AUTHORS LICENSE readme.md
%_bindir/%name
%_bindir/decode-pcap
%_bindir/parse-pcap
%_datadir/%name/

%changelog
* Mon Jan 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
