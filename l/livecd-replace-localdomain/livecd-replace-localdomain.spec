Name: livecd-replace-localdomain
Version: 1.0
Release: alt3

Summary: Replace localdomain with reverse dig -x result
License: GPL-3.0-or-later
Group: System/Configuration/Other
URL: https://www.altlinux.org/LiveCD

BuildArch: noarch

Source: %name-%version.tar

Requires: avahi-daemon

%description
This package installs two files for systemd service.
It replaces localdomain with reverse dig -x results or
if no resolve replaces localdomain with last 2 bytes of IP.

%prep
%setup

%install
install -pD -m755 livecd-replace-localdomain \
	%buildroot%_bindir/livecd-replace-localdomain
install -pD -m755 \
	livecd-replace-localdomain.d/50-dig-x-hostname.sh \
	%buildroot%_libexecdir/livecd-replace-localdomain.d/50-dig-x-hostname.sh
install -pD -m755 \
	livecd-replace-localdomain.d/70-last-IP-bytes.sh \
	%buildroot%_libexecdir/livecd-replace-localdomain.d/70-last-IP-bytes.sh
install -pD -m644 livecd-replace-localdomain.service \
	%buildroot%systemd_unitdir/livecd-replace-localdomain.service

%files
%_bindir/livecd-replace-localdomain
%dir %_libexecdir/livecd-replace-localdomain.d/
%_libexecdir/livecd-replace-localdomain.d/50-dig-x-hostname.sh
%_libexecdir/livecd-replace-localdomain.d/70-last-IP-bytes.sh
%systemd_unitdir/livecd-replace-localdomain.service
%doc README.practicum.md

%preun
%preun_service %name 

%changelog
* Wed Aug 19 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt3
- Add addons.

* Fri Jul 31 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt2
- Add README.

* Thu Oct 23 2025 Artyom Osipchuk <artos@altlinux.org> 1.0-alt1
- Initial build.
