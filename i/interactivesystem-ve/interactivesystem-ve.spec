Name: interactivesystem-ve
Summary: The skeleton package which defines an interactive %distribution system
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: basesystem-ve = %version-%release

Requires: console-common-scripts crontabs info less man
Requires: etcnet termutils passwd sash stat
Requires: time stmpclean syslogd-daemon

%description
This package defines the components of an interactive %distribution system
(for example, the package installation order to use during bootstrapping).

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

