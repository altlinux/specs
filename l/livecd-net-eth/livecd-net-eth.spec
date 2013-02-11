Name: livecd-net-eth
Version: 0.2
Release: alt1

Summary: Try to autoconfigure ethernet interfaces
License: GPL
Group: System/Configuration/Networking

Url: http://www.altlinux.org/etcnet
Source0: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
This package might be useful for livecd images or virtual machines
when it's required to autoconfigure ethernet interfaces via DHCP.

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
* Mon Feb 11 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- resolv.conf (aufs) related workaround

* Fri Feb 08 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on livecd-online-repo, livecd-setlocale)

