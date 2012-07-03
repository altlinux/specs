Name: appliance-build-pbx
Summary: Packages required for build PBX components
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: appliance-devel-base

# Asterisk 1.6.*
Requires: libspandsp6-devel

Requires: appliance-build-asterisk
Requires: appliance-build-dahdi

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

