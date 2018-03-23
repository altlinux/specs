Name: lxde
Version: 1.0
Release: alt15
Summary: Virtual package for install all parts of LXDE
Group: Graphical desktop/Other
License: GPL
BuildArch: noarch
Requires: lxde-lite = %EVR
Requires: lxde-lxrandr lxde-lxshortcut lxde-lxinput lxde-lxtask lxde-lxhotkey lxde-lxterminal
Requires: gpicview leafpad
Requires: lxde-lxpolkit
Conflicts: lxde-sysvinit
Packager: LXDE Packaging Team <lxde@packages.altlinux.org>

%description
%summary

%package lite
Summary: Virtual package for install minumal set of LXDE packages
Group: Graphical desktop/Other
License: GPL
BuildArch: noarch
Requires: lxde-common lxde-lxpanel lxde-lxsession lxde-freedesktop-menu lxde-lxsession-edit
Requires: pcmanfm2 menu-cache lxde-lxappearance lxde-lxappearance-obconf
Requires: openbox

%description lite
%summary

%package sysvinit
Summary: Virtual package for install LXDE packages for SysVinit
Group: Graphical desktop/Other
License: GPL
BuildArch: noarch
Requires: lxde-lite = %EVR
Requires: lxde-lxrandr lxde-lxshortcut lxde-lxinput lxde-lxtask lxde-lxhotkey lxde-lxterminal
Requires: gpicview leafpad
Requires: ConsoleKit2 polkit-sysvinit nm-sysvinit
Conflicts: lxde lxde-lxpolkit

%description sysvinit
%summary

%files
%files lite
%files sysvinit

%changelog
* Fri Mar 23 2018 Anton Midyukov <antohami@altlinux.org> 1.0-alt15
- Optimization of dependencies

* Thu Sep 07 2017 Anton Midyukov <antohami@altlinux.org> 1.0-alt14
- Added requires nm-sysvinit for lxde-sysvinit

* Thu Feb 16 2017 Anton Midyukov <antohami@altlinux.org> 1.0-alt13
- Added subpackage lxde-sysvinit
- Added requires lxde-lxhotkey

* Wed Feb 08 2017 Anton Midyukov <antohami@altlinux.org> 1.0-alt12
- Added requires lxde-lxpolkit

* Sun May 22 2016 Anton Midyukov <antohami@altlinux.org> 1.0-alt11
- Added requires lxde-session-edit

* Fri May 20 2016 Anton Midyukov <antohami@altlinux.org> 1.0-alt10
- Remove requires lxde-session-edit
- Added requires lxde-lxsession lxde-lxinput lxde-icon-theme.

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

