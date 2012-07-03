Name: xfce-settings-lite-school
Version: 0.6
Release: alt2
BuildArch: noarch

Source:%name-%version.tar


Summary: Xfce4 settings for School version
License: GPL
Group: System/Configuration/Other
Packager: Anton V. Boyarshiniv <boyarsh@altlinux.org>

Requires: etcskel
Conflicts: xfce-settings-desktop

%description
Xfce4 settings  for School version

%package office-lite
Group: System/Configuration/Other
Summary: Xfce4 panel buttons to start OpenOffice.org
Requires: %name = %version
%description office-lite
Xfce4 panel buttons to start OpenOffice.org

%package office-superlite
Group: System/Configuration/Other
Summary: Xfce4 panel buttons to start abiword and gnumeric
Requires: %name = %version
%description office-superlite
Xfce4 panel buttons to start abiword and gnumeric

%package network
Group: System/Configuration/Other
Summary: Xfce4 panel buttons to start browser
Requires: %name = %version
%description network
Xfce4 panel buttons to start browser




%prep
%setup -q


%install
mkdir -p %buildroot/etc/skel/.config/xfce4/desktop
mkdir -p %buildroot/etc/skel/.config/xfce4/mcs_settings
mkdir -p %buildroot/etc/skel/.config/xfce4/panel
mkdir -p %buildroot/etc/skel/.config/xfce4-session
mkdir -p %buildroot/etc/skel/.config/autostart
mkdir -p %buildroot/etc/skel/.local/share/applications
install -m 644 etcskel/.config/xfce4/helpers.rc %buildroot/etc/skel/.config/xfce4/
install -m 644 etcskel/.config/xfce4/desktop/* %buildroot/etc/skel/.config/xfce4/desktop
install -m 644 etcskel/.config/xfce4/mcs_settings/* %buildroot/etc/skel/.config/xfce4/mcs_settings
install -m 644 etcskel/.config/xfce4/panel/* %buildroot/etc/skel/.config/xfce4/panel
install -m 644 etcskel/.config/xfce4-session/* %buildroot/etc/skel/.config/xfce4-session/
install -m 644 etcskel/.config/autostart/*  %buildroot/etc/skel/.config/autostart
install -m 644 etcskel/.local/share/applications/*  %buildroot/etc/skel/.local/share/applications
install -m 644 etcskel/.wm-select %buildroot/etc/skel/
install -m 644 etcskel/.Xdefaults %buildroot/etc/skel/

mkdir -p  %buildroot/usr/share/xfce4/backdrops
install -m 644 backgrounds/* %buildroot/usr/share/xfce4/backdrops
mkdir -p  %buildroot/usr/share/themes/ALTLinux-Lite/gtk-2.0
install -m 644 themes/ALTLinux-Lite/gtk-2.0/* %buildroot/usr/share/themes/ALTLinux-Lite/gtk-2.0/
install -m 644 themes/ALTLinux-Lite/*.png %buildroot/usr/share/themes/ALTLinux-Lite/


%files
/etc/skel/.wm-select
/etc/skel/.Xdefaults
/etc/skel/.config
/etc/skel/.config
/etc/skel/.local
%exclude /etc/skel/.config/xfce4/panel/launcher-11888137035.rc
%exclude /etc/skel/.config/xfce4/panel/launcher-12888137035.rc
%exclude /etc/skel/.config/xfce4/panel/launcher-10.rc
/usr/share/themes/ALTLinux-Lite
/usr/share/xfce4/backdrops

%post office-lite
subst 's/<!-- xfce-settings-desktop-office-lite\(.*\)-->/\1/' /etc/skel/.config/xfce4/panel/panels.xml

%post office-superlite
subst 's/<!-- xfce-settings-desktop-office-superlite\(.*\)-->/\1/' /etc/skel/.config/xfce4/panel/panels.xml

%post network
subst 's/<!-- xfce-settings-desktop-network\(.*\)-->/\1/' /etc/skel/.config/xfce4/panel/panels.xml

%files office-lite
/etc/skel/.config/xfce4/panel/launcher-11888137035.rc

%files office-superlite
/etc/skel/.config/xfce4/panel/launcher-12888137035.rc

%files network
/etc/skel/.config/xfce4/panel/launcher-10.rc



%changelog
* Wed Dec 12 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt2
- School version 

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



