Name: appliance-base-minimal
Summary: Virtual package that require some essential packages
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

# System
Requires: appliance-base-interactivesystem

Requires: hostinfo
Requires: netlist
Requires: rsync
Requires: shadow-edit
Requires: sysklogd
Requires: vim-console

%description
%summary
This appliance need to be required from every other appliance

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

