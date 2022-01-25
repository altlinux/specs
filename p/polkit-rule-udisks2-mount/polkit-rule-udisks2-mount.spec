Name: polkit-rule-udisks2-mount
Version: 1.0
Release: alt1

Summary: Polkit rule to allow users in group xgrp mount removable storage devices
License: GPL-3.0
Group: Other
URL: http://altlinux.org

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
install -Dpm 0644 10-udisks2-mount.rule %buildroot%_datadir/polkit-1/rules.d/10-udisks2-mount.rule

%files
%_datadir/polkit-1/rules.d/10-udisks2-mount.rule

%changelog
* Tue Jan 25 2022 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus (ALT #40811).
