Name: installer-feature-fstrim
Version: 0.1
Release: alt1

Summary: trim SSD upon installation
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: trim SSD upon installation
Group: System/Configuration/Other
Requires: installer-common-stage2

%description stage2
%summary

%prep
%setup

%install
%makeinstall

%files stage2
%_datadir/install2/postinstall.d/*

%changelog
* Wed Oct 17 2018 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk

