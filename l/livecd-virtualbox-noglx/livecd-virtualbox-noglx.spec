Name: livecd-virtualbox-noglx
Version: 0.2
Release: alt1

Summary: A kludge for vboxdrv problems with GLX
License: public domainL
Group: System/Configuration/Other

Url: https://bugzilla.altlinux.org/28782
Source: %name-%version.tar
BuildArch: noarch

%description
This package works around a weird problem by gracefully reducing
vboxdrv functionality being used thus avoiding the freeze.

Thanks Alexey Borisenkov and Mikhail Efremov for the hints.

%prep
%setup

%build

%install
install -pDm755 %name.init %buildroot%_initdir/%name
install -pDm644 %name.service %buildroot%_unitdir/%name.service
install -pDm755 livecd-postinstall.d/50-cp-xorg.conf.sh \
  %buildroot%_libexecdir/alterator/hooks/livecd-postinstall.d/50-cp-xorg.conf.sh

%files
%_initdir/%name
%_unitdir/%name.service
%_libexecdir/alterator/hooks/livecd-postinstall.d/50-cp-xorg.conf.sh

%changelog
* Wed Apr 24 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- added postinstall script to carry over the dynamic configuration
  into the installed system (in case it was); thanks sem@

* Mon Apr 22 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

