Url: http://www.altlinux.org/Appliances
Name: appliance-asterisk-test
Summary: Asterisk testing packages
BuildArch: noarch
Version: 4.0.1
Release: alt2
License: GPL
Group: System/Base

Requires: appliance-network-debug

# SIP test
Requires: sipsak
Requires: sipp

Requires: tcpdump
Requires: tshark

%description
%summary

%files

%changelog
* Sun Jun 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- add Url tag

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

