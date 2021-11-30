Name: icewm-icon-regular
Version: 0.0.1
Release: alt4

Summary: Script create icon for IceWM
Group: Graphical desktop/Icewm
License: GPLv2+

Url: http://git.altlinux.org/people/balbes150/packages/icewm-icon-regular.git
Packager: Oleg Ivanov <balbes150@altlinux.org>

Requires: icewm >= 2.0.0-alt1

Source0: %name

BuildArch: noarch

%description
%summary

%install
install -pD -m 0755 %SOURCE0 %buildroot%_sysconfdir/skel/.xsession.d/%name

%files
%config %_sysconfdir/skel/.xsession.d/*

%changelog
* Sun Nov 14 2021 Oleg Ivanov <balbes150@altlinux.org> 0.0.1-alt4
- refactoring new version

* Fri Nov 12 2021 Oleg Ivanov <balbes150@altlinux.org> 0.0.1-alt3
- new version use script add-icon-desktop.sh

* Sun Nov 07 2021 Oleg Ivanov <balbes150@altlinux.org> 0.0.1-alt2
- replacing files with links

* Sat Nov 06 2021 Oleg Ivanov <balbes150@altlinux.org> 0.0.1-alt1
- init 

