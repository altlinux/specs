Name: card-actions
Version: 1.7
Release: alt1

Summary: Smart card action handler scripts
License: GPLv2
Group: Monitoring

Source0: card_inserted
Source1: card_removed
Source2: pkcs11_eventmgr.sh
Source3: pkcs11_eventmgr.init

BuildArch: noarch

%description
%summary

%install
install -pDm755 %SOURCE0 %buildroot%_bindir/card_inserted
install -pDm755 %SOURCE1 %buildroot%_bindir/card_removed
install -pDm755 %SOURCE2 %buildroot%_x11sysconfdir/profile.d/pkcs11_eventmgr.sh
install -pDm755 %SOURCE3 %buildroot%_initdir/pkcs11_eventmgr
mkdir -p %buildroot%_localstatedir/smartcard

%post
%post_service pkcs11_eventmgr

%preun
%preun_service pkcs11_eventmgr

%files
%_bindir/*
%_initdir/pkcs11_eventmgr
%_x11sysconfdir/profile.d/*.sh
%dir %_localstatedir/smartcard/

%changelog
* Fri Feb 10 2017 Andrey Cherepanov <cas@altlinux.org> 1.7-alt1
- Initial build in Sisyphus

* Mon Nov 14 2016 Andrey Cherepanov <cas@altlinux.org> 1.7-alt0.M70C.1
- rewrite to use loginctl and dm-tool

* Fri Oct 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6-alt1
- add homedir removing on different user login

* Wed Oct 03 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5-alt1
- remove /var/lib/smartcard/user on shutdown and startup

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 1.4-alt1
- card_*: minor tweaks/fixups

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- card_*: slightly better logging

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 1.2-alt1
- essentially rewrote scripts
  + card_insert:
    - get rid of extra gnome-panel dependency
    - a few hundred microsecond sleeps were clearly a thinko here
- added initscript instead of rc.local hack (no migration though)
- spec cleanup

* Tue Jan 31 2012 Michail Yakushin <silicium@altlinux.ru> 1.1-alt1
- fix card_insert script. kill all user process after session termination

* Thu Nov 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1
- initial
