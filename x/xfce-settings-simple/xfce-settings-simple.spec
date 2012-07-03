Name: xfce-settings-simple
Version: 1.0
Release: alt4
BuildArch: noarch

Source:%name-%version.tar


Summary: Xfce4 simple settings
License: GPL
Group: System/Configuration/Other
Packager: Eugene Prokopiev <enp@altlinux.ru>

Requires: etcskel gtk2-theme-mist icon-theme-mist-simple xfwm4-theme-simple xfce4-session-engines menu-icons-default xfce4-settings xfce4-icon-theme xfce4-minimal
Requires: design-graphics-desktop
Obsoletes: xfce-settings-desktop
Conflicts: xfce-settings-lite xfce-settings-lite-office-superlite  xfce-settings-lite-office-lite xfce-settings-lite-network xfce-settings-lite-school xfce-settings-lite-school-office-superlite  xfce-settings-lite-school-xfce-office-lite xfce-settings-lite-school-xfce-network-lite

%description
Xfce4 simple settings

%prep
%setup -q

%install
mkdir -p %buildroot/etc
cp -a etcskel %buildroot/etc/skel

%files
/etc/skel

%changelog
* Wed May 18 2011 Eugene Prokopiev <enp@altlinux.ru> 1.0-alt4
- ported to XFCE 4.8

* Thu Apr 22 2010 Eugene Prokopiev <enp@altlinux.ru> 1.0-alt3
- use mist-simple icon theme

* Mon Dec 07 2009 Eugene Prokopiev <enp@altlinux.ru> 1.0-alt2
- ported to XFCE 4.6
- add dependencies

* Thu Oct 09 2008 Eugene Prokopiev <enp@altlinux.ru> 1.0-alt1
- fork from xfce-settings-lite

* Tue Sep 09 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt7
- fixed templates placenent in subpackages
- smarter defaults for mimetypes

* Tue Sep 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt6
- templates for office documents added 

* Wed Aug 06 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt5
- added xkb plugin 

* Mon Aug 04 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt4
- fixed desktop menu 

* Thu Jun 05 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt3
- drop TangoKDE usag 

* Thu Mar 06 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt2
- ported to sysiphus 

* Tue Dec 18 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt1
- renamed from xfce-settings-desktop to xfce-settings-lite 

* Tue Dec 04 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- changed design, added theme, backgrounds 

* Mon Oct 22 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- Terminal chamged to urxvt 

* Thu Oct 11 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- some panel buttons moved to subpackages
- added customized menu

* Wed Sep 26 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- settings for xarchiver added 

* Tue Sep 18 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- .wm-select added 

* Mon Sep 03 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build



