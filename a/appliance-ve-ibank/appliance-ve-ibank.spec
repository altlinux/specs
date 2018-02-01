Url: http://www.altlinux.org/Appliances
Name: appliance-ve-ibank
Summary: Simple VE for iBank
BuildArch: noarch
Version: 4.0.1
Release: alt3
License: GPL
Group: System/Base

Requires: appliance-base-sshd-x11
Requires: appliance-base-basesystem
Requires: catdoc
Requires: cpio
Requires: dev
Requires: fuse-encfs
Requires: iptables
Requires: java-devel-default
Requires: mc
Requires: perl-Git
Requires: syskeeper-ve

%description
%summary

%files

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt3
- NMU: java 1.5 no more, using default java sdk.

* Sun Jun 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- add Url tag

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

