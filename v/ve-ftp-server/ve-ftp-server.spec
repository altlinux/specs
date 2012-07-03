Name: ve-ftp-server
Version: 0.1
Release: alt4

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: FTP server
License: GPL
Group: System/Base
BuildArch: noarch

#base packages
Requires: apt
Requires: basesystem
Requires: sysklogd
Requires: etcnet
Requires: glibc-nss
Requires: glibc-locales
Requires: netlist

#configurator packages
Requires: anonftp
Requires: alterator-fbi
Requires: alterator-vsftpd
Requires: alterator-users

#debug packages (?)
Requires: openssh-server
Requires: passwd
Requires: less

%description
virtual package for ftp server appliance

%files


%changelog
* Thu Mar 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- remove elinks

* Thu Mar 22 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- add apt/remove webserver

* Wed Mar 21 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- remove separate web interface

* Wed Mar 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
