Name: ve-print-server
Version: 0.1
Release: alt4

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: Print server
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

#ve specific packages
Requires: cups
Requires: foomatic
Requires: printer-drivers-base
Requires: openssl


#debug packages (?)
Requires: openssh-server
Requires: passwd
Requires: less
Requires: elinks
Requires: strace

%description
virtual package for printing server appliance

%files


%changelog
* Thu Mar 22 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add apt/remove webserver

* Fri Mar 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- change description
- add elinks, strace, glibc-locales

* Thu Mar 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- remove ntpd from requires

* Wed Feb 28 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
