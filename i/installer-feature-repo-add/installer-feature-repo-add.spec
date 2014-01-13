Name: installer-feature-repo-add
Version: 0.1
Release: alt1

Summary: Add the installation media to APT configuration
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Conflicts: alterator-pkg < 2.6.18-alt1

%description
%summary

%package stage2
Summary: Add the installation media to APT configuration
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2

%description stage2
%summary

%prep
%setup

%install
%makeinstall

%files stage2
%_datadir/install2/postinstall.d/*

%changelog
* Mon Jan 13 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk

