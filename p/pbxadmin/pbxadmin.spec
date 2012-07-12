Name: pbxadmin
Summary: Console utilites for PBX administration
Version: 0.0.5
Release: alt1
License: GPL
Group: System/Servers
BuildArch: noarch
Url: http://sisyphus.ru/ru/srpm/Sisyphus/pbxadmin
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Requires: %name-common	= %version-%release
Requires: %name-core 	= %version-%release
Requires: %name-monitor = %version-%release

%package common
Summary: Console utilites for PBX administration
Group: System/Servers
BuildArch: noarch

%description common
Console utilites for PBX administration

%package core
Summary: Console utilites for PBX administration
Group: System/Servers
Requires(pre): asterisk-user
Requires: sudo >= 1:1.6.8p12-alt11
Requires: %name-common = %version-%release

%description core
Console utilites for PBX administration

%package monitor
Summary: Console utilites for PBX administration
Group: System/Servers
Requires: %name-common = %version-%release

%description monitor
Console utilites for PBX administration

%description
Console utilites for PBX administration


%prep
%setup

%install
mkdir -p %buildroot/usr/libexec/pbx
install -D -m755 pbx %buildroot%_bindir/pbx
install -D -m755 utilites/* %buildroot/usr/libexec/pbx/
install -D -m500 sudoers %buildroot/etc/sudoers.d/pbxadmin

%files
%attr(0755,root,root) /usr/libexec/pbx/console.sh
%attr(0755,root,root) /usr/libexec/pbx/restart.sh
%attr(0755,root,root) /usr/libexec/pbx/reconfig.sh

%files common
%dir /usr/libexec/pbx

%files core
%attr(0550,_asterisk,pbxadmin) %_bindir/pbx
%attr(0400,root,root) /etc/sudoers.d/pbxadmin

%files monitor
%attr(0755,root,root) /usr/libexec/pbx/monitormix.sh

%changelog
* Thu Jul 12 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt1
- move sudo config from /etc/sudo.d to /etc/sudoers.d (Closes: 27537)

* Wed May 25 2011 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1
- run pbxadmin utilites as root
- rename 'pbx reload' to 'pbx reconfig' and update

* Mon Oct 26 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt2
- add Url tag

* Sat Oct 24 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt1
- add start from pbxadmin group (change uid to _asterisk)

* Tue Feb 10 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- move /usr/libexec/pbx to %name-common

* Tue Feb 10 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- initial build for Sisyphus

