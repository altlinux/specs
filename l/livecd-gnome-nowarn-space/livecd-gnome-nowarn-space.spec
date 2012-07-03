Name: livecd-gnome-nowarn-space
Version: 0.3
Release: alt1

Summary: Disable gnome warning about free space on livecd
License: GPL
Group: System/Configuration/Other

Source0: %name-%version.tar 


BuildArch: noarch

%description
Disables gnome warning about free space on livecd

%prep
%setup

%install
umask 0066
mkdir -p %buildroot/etc/skel/.gconf/apps/gnome_settings_daemon/plugins/housekeeping
touch %buildroot/etc/skel/.gconf/apps/%%gconf.xml
touch %buildroot/etc/skel/.gconf/apps/gnome_settings_daemon/%%gconf.xml
touch %buildroot/etc/skel/.gconf/apps/gnome_settings_daemon/plugins/%%gconf.xml
install -pD -m0644 gconf.xml  %buildroot/etc/skel/.gconf/apps/gnome_settings_daemon/plugins/housekeeping/%%gconf.xml 


%files 
/etc/skel/.gconf/apps/*


%changelog
* Tue Apr 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- one more empty %%gconf.xml file added

* Fri Nov 26 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- empty %%gconf.xml files added

* Thu Nov 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build


