Name: basesystem-ve
Summary: The skeleton package which defines a basic %distribution system
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: appliance-base-compress-minimal

Requires: altlinux-release bash chkconfig common-licenses su
Requires: diffutils etcskel filesystem findutils gawk getopt
Requires: grep rootfiles rpm-build sed
Requires: service setup shadow-utils startup sysvinit-utils login
Requires: vitmp /bin/hostname
Requires: mktemp >= 1:1.3.1
Requires: which

%description
This package defines the components of a basic %distribution system
(for example, the package installation order to use during bootstrapping).

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

