BuildArch: noarch
Name: appliance-fake-vzmc
Summary: Make Virtuozzo Management Console installable to ALT Linux
Version: 1.0
Release: alt1
Packager: Pavlov Konstantin <thresh@altlinux.ru>
License: GPL
Group: System/Base

ExclusiveArch: %ix86

Provides: qt = 3.3.8
Requires: libqt3 >= 3.3.8-alt1
Requires: expect

%description
%summary

%files

%changelog
* Mon Jul 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux.

