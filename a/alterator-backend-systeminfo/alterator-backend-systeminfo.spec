%define _unpackaged_files_terminate_build 1

Name: alterator-backend-systeminfo
Version: 0.1.0
Release: alt1

Summary: Alterator backends for getting system information
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-backend-systeminfo

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14

%description
Alterator backends for getting system information.

%prep
%setup

%install
install -pD -m644 logger/last-dist-upgrade.lua %buildroot%_datadir/apt/scripts/last-dist-upgrade.lua
install -pD -m644 logger/last-dist-upgrade.conf %buildroot%_sysconfdir/apt/apt.conf.d/last-dist-upgrade.conf

mkdir -p %buildroot%_logdir/alterator
touch %buildroot%_logdir/alterator/last-dist-upgrade.log
chmod 644 %buildroot%_logdir/alterator/last-dist-upgrade.log

mkdir -p %buildroot%_alterator_datadir/backends
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions

install -v -p -m 755 -D systeminfo %buildroot%_libexecdir/%name/systeminfo
install -v -p -m 644 -D systeminfo.backend %buildroot%_alterator_datadir/backends/systeminfo.backend
install -v -p -m 644 -D org.altlinux.alterator.systeminfo1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D org.altlinux.alterator.systeminfo1.policy %buildroot%_datadir/polkit-1/actions

%files
%dir %_logdir/alterator
%_logdir/alterator/last-dist-upgrade.log
%_datadir/apt/scripts/*.lua
%config %_sysconfdir/apt/apt.conf.d/*.conf

%dir %_libexecdir/%name
%dir %_alterator_datadir/backends
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%_libexecdir/%name/systeminfo
%_alterator_datadir/backends/*.backend
%_datadir/dbus-1/interfaces/*.xml
%_datadir/polkit-1/actions/*.policy

%changelog
* Wed Sep 25 2024 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.0-alt1
- Initial build.
