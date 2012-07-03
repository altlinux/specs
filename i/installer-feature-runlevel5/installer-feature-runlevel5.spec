Name: installer-feature-runlevel5
Version: 0.1
Release: alt2

Summary: system with graphical boot
License: GPL
Group: System/Configuration/Other

Source: %name-%version.tar

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

%description
%summary

%package stage2
Summary: system with graphical boot
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2
Conflicts: installer-hpc-stage2 <= 0.3-alt2
Conflicts: installer-ltsp-school-stage2 <= 0.4-alt4.4
Conflicts: installer-ltsp-stage2 <= 0.1-alt2.5.7
Conflicts: installer-junior-school-stage2 <= 0.4-alt5
Conflicts: installer-junior-stage2 <= 0.4-alt4

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/postinstall.d/*

%changelog
* Thu Sep 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt2
- remove Requires: portmap > 1:4.0-alt2

* Wed Apr 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
