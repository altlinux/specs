Name: livecd-network-style
Version: 1.2
Release: alt1

Summary: Provides configurations for "Networks in Linux" prac
License: GPL-3.0-or-later
Group: System/Configuration/Other
URL: https://www.altlinux.org/LiveCD/regular-protocols

BuildArch: noarch

Source: %name-%version.tar

%description
This package provides prac configurations.
1. domain name service
2. avahi tmpfiles link for root usage
3. scripts for reporting homework
live-autonet - configure net by NVRAM vars
live-report - save record of terminal
live-sethostname - hostname by NVRAM vars
live-zeroing - clean user cache

%prep
%setup

%install
install -pD -m644 tmpfiles.d/avahi-daemon.conf %buildroot%_tmpfilesdir/avahi-daemon.conf
install -pD -m644 systemd/live-sethostname.service %buildroot/usr/lib/systemd/system/live-sethostname.service
for file in bin/*; do
	filename=$(basename "$file")
	install -pD -m700 $file %buildroot%_bindir/$filename
done

%files
%systemd_unitdir/live-sethostname.service
%_tmpfilesdir/avahi-daemon.conf
%_bindir/live-autonet
%_bindir/live-report
%_bindir/live-sethostname
%_bindir/live-zeroing

%changelog
* Fri Jun 19 2026 Artyom Osipchuk <artos@altlinux.org> 1.2-alt1
- Add scripts for reporting homework.

* Fri Jun 19 2026 Artyom Osipchuk <artos@altlinux.org> 1.1-alt1
- Add avahi tmpfiles link for root usage.

* Mon Jun 08 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt1
- Initial build.
