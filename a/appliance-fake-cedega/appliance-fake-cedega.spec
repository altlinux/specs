BuildArch: noarch
Name: appliance-fake-cedega
Summary: Make Cedega rpms installable to ALT Linux
Version: 1.0
Release: alt1
Packager: Pavlov Konstantin <thresh@altlinux.ru>
License: GPL
Group: System/Base

ExclusiveArch: %ix86

Provides: dbus-python = 1.0
Requires: python-module-pygtk-libglade
Requires: python-module-dbus
Requires: wget

%description
%summary

%files

%changelog
* Mon Aug 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux.


