Name: livecd-install-wmaker
Version: 0.4
Release: alt1

Summary: WindowMaker configuration for livecd-install
License: Public domain
Group: System/X11

Url: http://altlinux.org/m-p
Source0: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
Runtime %summary.

%prep
%setup

%build

%install
install -pDm755 %name.init %buildroot%_initdir/%name
install -pDm644 %name.service %buildroot%_unitdir/%name.service

%files
%_initdir/%name
%_unitdir/%name.service

%changelog
* Tue Mar 19 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- drop the workaround introduced in previous version, hooray!

* Tue Mar 12 2013 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- drop fbdev_drv (see also #28669)

* Tue Mar 12 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- added setstyle script

* Mon Mar 11 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (thx aen@ for the exact contents)

