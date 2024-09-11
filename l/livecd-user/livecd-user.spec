Name: livecd-user
Version: 0.3.2
Release: alt1

Summary: Create LiveCD user
License: GPL-2.0-or-later
Group: System/Configuration/Other

Url: https://www.altlinux.org/LiveCD
Source0: %name-%version.tar

BuildArch: noarch

Requires: autologin-sh-functions

%description
%summary.

%prep
%setup

%build

%install
install -pDm755 %name.init %buildroot%_initdir/%name
install -pDm644 %name.service %buildroot%_unitdir/%name.service
install -pDm600 %name.conf %buildroot%_sysconfdir/sysconfig/%name.conf

%preun
if [ $1 -eq 0 ]; then
%preun_service %name
fi

%files
%_sysconfdir/sysconfig/%name.conf
%_initdir/%name
%_unitdir/%name.service

%changelog
* Wed Sep 11 2024 Anton Midyukov <antohami@altlinux.org> 0.3.2-alt1
- Add parameter LIVECD_SESSION (disable by default)

* Fri Jan 26 2024 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt1
- livecd-user.init: fix LIVECD_NO_ISSUE support

* Sat Jan 06 2024 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- Add parameter LIVECD_NO_ISSUE (disable by default)

* Wed Oct 26 2022 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- livecd-user.service: increase timeout to 120 seconds

* Sat Oct 15 2022 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
