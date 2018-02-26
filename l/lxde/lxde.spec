Name: lxde
Version: 1.0
Release: alt9
Summary: Virtual package for install all parts of LXDE
Group: Graphical desktop/Other
License: GPL
BuildArch: noarch
Requires: lxde-common lxde-lxpanel lxde-lxsession pcmanfm2 lxde-freedesktop-menu menu-cache lxde-lxappearance lxde-lxsession-edit
Requires: lxde-lxrandr lxde-lxshortcut lxde-lxtask gpicview leafpad
Packager: LXDE Packaging Team <lxde@packages.altlinux.org>

%description
%summary

%package lite
Summary: Virtual package for install minumal set of LXDE packages
Group: Graphical desktop/Other
License: GPL
Requires: lxde-common lxde-lxpanel lxde-lxsession pcmanfm2 lxde-freedesktop-menu menu-cache lxde-lxappearance lxde-lxsession-edit

%description lite
%summary

%files
%files lite

%changelog
* Fri Mar 11 2011 Radik Usupov <radik@altlinux.org> 1.0-alt9
- changed requires for further transition to global freedesktop menu

* Mon Mar 07 2011 Mykola Grechukh <gns@altlinux.ru> 1.0-alt8
- dependencies updated

* Wed May 26 2010 Mykola Grechukh <gns@altlinux.ru> 1.0-alt7
- packager updated to team

* Tue May 25 2010 Radik Usupov <radik@altlinux.org> 1.0-alt3.M51.5
- pcmanfm -> pcmanfm2

* Tue May 04 2010 Mykola Grechukh <gns@altlinux.ru> 1.0-alt5
- qtrayvolman added

* Mon May 03 2010 Mykola Grechukh <gns@altlinux.ru> 1.0-alt4
- new version

* Sun Dec 13 2009 Mykola Grechukh <gns@altlinux.ru> 1.0-alt3
- requirements updated for new upstream state

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 1.0-alt2
- add requires lxde-lxmenu-data for new version of lxde-lxpanel

* Fri Jul 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.0-alt1
- First build for ALTLinux

