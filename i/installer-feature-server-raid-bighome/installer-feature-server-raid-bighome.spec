Name: installer-feature-server-raid-bighome
Version: 0.1
Release: alt3

Summary: RAID profile for server with large /home (e.g. LTSP)
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: RAID profile for server with large /home (e.g. LTSP)
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2
Requires: alterator-vm >= 0.3-alt24
Conflicts: installer-ltsp-school-stage2 < 0.4-alt4.11

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/initinstall.d/*

%changelog
* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- renamed to satisfy lazy girar
- no Provides:/Obsoletes: as old name wasn't used for an upload

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- added proper alterator-vm dependency

* Tue Apr 08 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk

