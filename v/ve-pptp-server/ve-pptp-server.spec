Name: ve-pptp-server
Version: 0.1
Release: alt2

Packager: L.A. Kostis <lakostis@altlinux.org>

Summary: virtual package for pptp server appliance
License: GPL
Group: System/Base
BuildArch: noarch

#basic packages
Requires: apt
Requires: basesystem
Requires: sysklogd
Requires: etcnet
Requires: glibc-nss
Requires: pptpd
Requires: netlist

#configurator packages
Requires: alterator-fbi 
#Requires: alterator-pptpd

#debug packages (?)
Requires: openssh-server
Requires: passwd
Requires: less

%description
virtual package for pptp server appliance

%files


%changelog
* Fri Apr 13 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 0.1-alt2
- add apt to requires.

* Wed Mar 28 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 0.1-alt1
- use alterator-pptpd as stub (FIXME!)
- initial release.
