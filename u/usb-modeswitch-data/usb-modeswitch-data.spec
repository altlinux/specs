Summary: Data and udev-rules for usb-modeswitch
Name: usb-modeswitch-data 
Version: 20110619
Release: alt2
License: GPL

Group:  System/Configuration/Hardware
URL: http://www.draisberghof.de/usb_modeswitch/
Source0: %name-%version.tar

BuildArch: noarch
Requires: usb-modeswitch >= 1.1.6


%description
Data and udev-rules for usb-modeswitch

%define modeswitch_rulesdir %_datadir/usb_modeswitch

%prep

%setup -q

%install
DESTDIR=%buildroot make install

%files
%doc ChangeLog README 
%modeswitch_rulesdir
/lib/udev/rules.d/*

%changelog
* Tue Jul 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110619-alt2
- added "change" event processing (manowar@)

* Fri Jul 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110619-alt1
- Upstream 2011-06-19 by manowar@

* Mon Feb 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101222-alt1
- updated from upstream

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101202-alt1
- updated from upstream
- versioned requires

* Fri Sep 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100826-alt1
- first build

