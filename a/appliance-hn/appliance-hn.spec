Name: appliance-hn
Summary: Virtual package for packages useful on ovz HN
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

# System
Requires: appliance-rescue-static
# This is minimal utilites not only for VEs
Requires: appliance-ve-std

Requires: syskeeper-hn
Requires: kernelbootlog

# For building VE's
Requires: spt

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

