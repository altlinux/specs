Name: livecd-virtualbox-noglx
Version: 0.1
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

Thanks Alexey Borisenkov for the hint.

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
* Mon Apr 22 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

