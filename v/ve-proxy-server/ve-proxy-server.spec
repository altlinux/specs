Name: ve-proxy-server
Version: 0.1
Release: alt2

Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Proxy server
License: GPL
Group: System/Base
BuildArch: noarch

#basic packages
Requires: basesystem
Requires: sysklogd
Requires: etcnet
Requires: glibc-nss
Requires: glibc-locales
Requires: netlist

#configurator packages
Requires: alterator-fbi 
Requires: alterator-squid

#debug packages (?)
Requires: openssh-server
Requires: passwd
Requires: less
Requires: elinks
Requires: strace

%description
virtual package for Proxy server appliance

%files


%changelog
* Thu Apr 05 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt2
- httpd-alterator removed from Requires.

* Fri Mar 16 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial release
