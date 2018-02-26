Name: firefox-settings-desktop
Version: 5.0 
Release: alt3
BuildArch: noarch

Source:%name-%version.tar


Summary:  Firefox settings for 5.0 Desktop
License: GPL
Group: System/Configuration/Other
Packager: Anton V. Boyarshiniv <boyarsh@altlinux.org>

Provides: firefox-settings-lite
Requires: firefox => 3.6

%description
Firefox settings for 5.0 Desktop


%prep
%setup -q


%install
mkdir -p %buildroot/etc/mozilla/firefox/desktop

cp -r * %buildroot/etc/mozilla/firefox/desktop

mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name <<__EOF__
/etc/mozilla/firefox/current /etc/mozilla/firefox/desktop 2
__EOF__



%files
/etc/mozilla/firefox/desktop
%config %_altdir/%name


%changelog
* Wed Sep 15 2010 Andrey Cherepanov <cas@altlinux.org> 5.0-alt3
- adapt to Firefox 3.6

* Wed Jul 22 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- now conflicts to firefox <=3.6 

* Thu Jun 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- fixed to firefox 3.5 

* Mon Apr 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.1-alt2
- added conflict on firefox >=3.1 

* Fri Nov 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.1-alt0.M41.2
- mailto directly to thunderbird 

* Thu Nov 27 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.1-alt0.M41.1
- port to M41 

* Wed Nov 26 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.1-alt1
- mailto setting 

* Tue Oct 07 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.0-alt1
- build for sisyphus 

* Mon Sep 29 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.0-alt0.M41.2
- not check default browser 

* Thu Sep 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.0-alt0.M41.1
- initial version 


