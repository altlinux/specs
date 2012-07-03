Name: installer-feature-add-memtest
Version: 0.6
Release: alt1

Summary: Ensure that memtest* is added to bootloader config
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
Installer stage2 hook: %summary

%package stage2
Summary: Ensure that memtest* is added to bootloader config
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage2

%description stage2
Installer stage2 hook: %summary

%prep
%setup

%install
%makeinstall

%files stage2
%_datadir/install2/postinstall.d/*

%changelog
* Fri Sep 25 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt1
- Clear DURING_INSTALL variable

* Thu Sep 24 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt1
- fix fatal typo (closes: #21697)

* Mon Sep 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Use installkernel --label (Vladislav Zavjalov; closes: #18679).

* Fri Mar 20 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Fixed fatal typo in postinstall hook.

* Tue Mar 17 2009 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Clear $DURING_INSTALL variable.
- Unitize lilo boot menu entry.

* Mon Sep 22 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk
