Name: installer-feature-set-tz-stage3
Version: 0.1
Release: alt1

Summary: Set TZ in stage3 from kernel command line
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch

%description
This package sets destination system's timezone
from kernel command line (stage3 version).

%prep

%post
. shell-config
ZONE=$(cat /proc/cmdline | sed -n 's/^.* tz=\([^ ]*\).*/\1/gp')
if [ -n "$ZONE" ]; then
	shell_config_set /etc/sysconfig/clock ZONE "'$ZONE'"
	service clock tzset
fi

%files

%changelog
* Tue Mar 21 2017 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- remade from installer-feature-set-tz 0.2-alt1 to simplify it
