Name: installer-feature-gdm-abstraction
Version: 0.1
Release: alt1

Summary: Setup gdm-theme-abstraction as default
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
Packager: Radik Usupov <radik@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: Setup gdm-theme-abstraction as default
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
%_datadir/install2/preinstall.d/*

%changelog
* Thu Jan 06 2011 Radik Usupov <radik@altlinux.org> 0.1-alt1
- Initial build


