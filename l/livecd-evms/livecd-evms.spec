Name: livecd-evms
Version: 0.2.2
Release: alt1

Summary: Tune EVMS config to run from LiveCD
License: GPLv2
Group: System/Configuration/Other

Url: http://www.altlinux.org/Alterator
Source0: %name
Source1: %name.service
Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch
PreReq: service chkconfig
Requires: libevms

Requires(post): chkconfig
Requires(preun): chkconfig

%description
%summary
(livecd-install won't work if this isn't done)

%install
install -pDm755 %SOURCE0 %buildroot%_initdir/%name
install -pDm644 %SOURCE1 %buildroot%_unitdir/livecd-evms.service

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name
%_unitdir/%name.service

%changelog
* Wed Jul 02 2014 Michael Shigorin <mike@altlinux.org> 0.2.2-alt1
- updated systemd unit file (thx shaba@)

* Tue Jul 01 2014 Michael Shigorin <mike@altlinux.org> 0.2.1-alt1
- added systemd unit file (214 broke sysv initscript compatibility)

* Thu May 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- exclude zram*

* Mon May 25 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- start service by default

* Thu May 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
