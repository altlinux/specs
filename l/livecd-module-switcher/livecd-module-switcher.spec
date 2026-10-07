Name: livecd-module-switcher
Version: 1.0
Release: alt3

Summary: Provides desktop icon to switch vbox modules to kvm or vice versa
License: GPL-3.0-or-later
Group: System/Configuration/Other
URL: https://www.altlinux.org/LiveCD/practicum?

BuildArch: noarch

Source: %name-%version.tar

Requires: polkit
Requires: shared-desktop-icons

%description
Provides desktop what starts systemd virtualbox.service or stops it.
Systemd virtualbox.service loads and unloads modules.
You must be in vboxusers group to use provided desktop icon.

%prep
%setup

%install
install -pD -m755 livecd-module-switcher.desktop \
	%buildroot%_datadir/applications/switcher.desktop
install -pD -m644 10-polkit-modules-load.rules \
	%buildroot%_datadir/polkit-1/rules.d/10-polkit-modules-load.rules

%files
%_datadir/applications/switcher.desktop
%_datadir/polkit-1/rules.d/10-polkit-modules-load.rules
%doc README.practicum.md

%changelog
* Thu Aug 20 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt3
- Add README.

* Mon Aug 10 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt2
- Add polkit rule to load modules for vboxusers group.

* Sun Aug 09 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt1
- Initial build.
