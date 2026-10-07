Name: livecd-cmdline-password
Version: 1.0
Release: alt2

Summary: Change password hash from /proc/cmdline
License: GPL-3.0-or-later
Group: System/Configuration/Other
URL: https://www.altlinux.org/LiveCD

BuildArch: noarch

Source: %name-%version.tar

%description
This package installs two files for systemd service.
Changing password from /proc/cmdline is useful for net boot.
You can give password hash in "password_hash=" var.
Check README for examples.

%prep
%setup

%install
install -pD -m755 livecd-cmdline-password \
	%buildroot%_bindir/livecd-cmdline-password
install -pD -m644 livecd-cmdline-password.service \
	%buildroot%systemd_unitdir/livecd-cmdline-password.service

%files
%_bindir/livecd-cmdline-password
%systemd_unitdir/livecd-cmdline-password.service
%doc README.practicum.md

%preun
%preun_service %name

%changelog
* Thu Aug 20 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt2
- Add README.

* Thu Aug 13 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt1
- Initial build.
