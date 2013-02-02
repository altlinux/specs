Name: appliance-hn
Summary: Virtual package for packages useful on ovz HN
BuildArch: noarch
Version: 4.0.2
Release: alt1
License: GPL
Group: System/Base

# System
Requires: appliance-rescue-static
# This is minimal utilites not only for VEs
Requires: appliance-ve-std

Requires: syskeeper-hn

# For building VE's
Requires: mkimage-profiles

%description
%summary

%files

%changelog
* Sat Feb 02 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.2-alt1
- remove requires to kernelbootlog
- add requires to mkimage-profiles

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

