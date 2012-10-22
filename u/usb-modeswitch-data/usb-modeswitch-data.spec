Summary: Data and udev-rules for usb-modeswitch
Name: usb-modeswitch-data
Version: 20120815
Release: alt1
License: GPL

Group: System/Configuration/Hardware
Url: http://www.draisberghof.de/usb_modeswitch/

Source: %name-%version.tar
Patch: huawei-E171.patch

BuildArch: noarch
Requires: usb-modeswitch >= 1.2.2

%description
Data and udev-rules for usb-modeswitch

%define modeswitch_rulesdir %_datadir/usb_modeswitch

%prep
%setup
%patch

%install
DESTDIR=%buildroot make install

%files
%doc ChangeLog README
%modeswitch_rulesdir
/lib/udev/rules.d/*

%changelog
* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 20120815-alt1
- 20120815

* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 20120531-alt3
- huawei-E171 added

* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 20120531-alt2
- minimum required version changed to 1.2.2 by upstream

* Thu Aug 09 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20120531-alt1
- 2012-05-31

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

