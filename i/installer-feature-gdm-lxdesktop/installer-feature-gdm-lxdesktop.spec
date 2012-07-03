Name: installer-feature-gdm-lxdesktop
Version: 0.2
Release: alt1

Summary: Setup gdm-theme-lxdesktop as default
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
Packager: Radik Usupov <radik@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: Setup gdm-theme-lxdesktop as default
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
* Wed Sep 07 2011 Radik Usupov <radik@altlinux.org> 0.2-alt1
- Fixed script

* Sun Apr 10 2011 Radik Usupov <radik@altlinux.org> 0.1-alt1
- Initial build



