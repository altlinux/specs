Name: installer-feature-vm-simple
Version: 0.1
Release: alt1

Summary: Partitioning with swap, / and /home
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
Packager: Eugene Prokopiev <enp@altlinux.ru>
BuildArch: noarch

%description
%summary

%package stage2
Summary: Partitioning with swap, / and /home
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/initinstall.d/*

%changelog
* Tue Aug 12 2008 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- init with installer-sdk

