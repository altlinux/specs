Name: ve-ntp-server
Version: 0.1
Release: alt8

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: NTP server
License: GPL
Group: System/Base
BuildArch: noarch

#basic packages
Requires: apt
Requires: basesystem
Requires: sysklogd
Requires: etcnet
Requires: glibc-nss
Requires: glibc-locales
Requires: netlist

#configurator packages
Requires: alterator-fbi 
Requires: alterator-openntpd

#debug packages (?)
Requires: openssh-server
Requires: passwd
Requires: less
Requires: strace

%description
virtual package for ntp server appliance

%files


%changelog
* Thu Mar 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt8
- remove elinks

* Thu Mar 22 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- add apt/remove webserver

* Wed Mar 21 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- remove separate web interface

* Fri Mar 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- change description
- add elinks, strace,glibc-locales

* Thu Mar 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- improve requires

* Tue Feb 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- go to sisyphus

* Tue Feb 27 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 0.1-alt2.1
- add netlist to base packages.

* Wed Feb 21 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- little spec improvements

* Fri Feb 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
