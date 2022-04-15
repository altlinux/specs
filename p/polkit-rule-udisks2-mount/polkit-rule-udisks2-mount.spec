Name: polkit-rule-udisks2-mount
Version: 1.2
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
install -Dpm 0644 10-udisks2-mount.rules %buildroot%_datadir/polkit-1/rules.d/10-udisks2-mount.rules

%files
%_datadir/polkit-1/rules.d/10-udisks2-mount.rules

%changelog
* Wed Apr 13 2022 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Add org.freedesktop.udisks2.filesystem-mount-system to rule.

* Mon Feb 14 2022 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Fix extension of rule file (ALT #41936).

* Tue Jan 25 2022 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus (ALT #40811).
