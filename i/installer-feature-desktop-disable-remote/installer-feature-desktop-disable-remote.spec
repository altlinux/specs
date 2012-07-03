Name: installer-feature-desktop-disable-remote
Version: 0.1
Release: alt1

Summary: Disable remote access
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: Disable remote access
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2
Conflicts: installer-ltsp-school-stage2 < 0.4-alt4.11
#Conflicts: installer-junior-school-stage2
#Conflicts: installer-junior-stage2

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/preinstall.d/*

%changelog
* Tue Apr 08 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk

