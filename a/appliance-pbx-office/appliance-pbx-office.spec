Url: http://www.altlinux.org/Appliances
Name: appliance-pbx-office
Summary: Asterisk for office virtual packege
BuildArch: noarch
Version: 4.0.1
Release: alt3
License: GPL
Group: System/Servers

Requires: appliance-pbx-hardware
Requires: asterisk-full
Requires: appliance-hn
Requires: appliance-base-server
Requires: appliance-caching-dns
Requires: appliance-network-debug
Requires: appliance-service-nagios
Requires: appliance-asterisk-test
Requires: tftp-server-xinetd
Requires: postgresql9.4

Requires: mithraen-pbx-systemtest

Requires: acpid
Requires: eject
Requires: elinks
Requires: gettext
Requires: gzip-utils
Requires: interactivesystem
Requires: lftp
Requires: lilo
Requires: luit
Requires: mdadm
Requires: nut-server
Requires: passwdqc-utils
Requires: perl-DBM
Requires: perl-Git
Requires: postfix-cyrus
Requires: python-modules-compiler
Requires: python-modules-email
Requires: python-modules-encodings
Requires: reiserfsprogs
Requires: shadow-suite
Requires: strace
Requires: sysfsutils
Requires: traceroute
Requires: update-kernel
Requires: xfsprogs

%description
%summary

%files

%changelog
* Wed Oct 07 2015 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt3
- postgresql 9.4

* Sun Jun 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- add Url tag

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

