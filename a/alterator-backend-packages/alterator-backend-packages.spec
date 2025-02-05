%define _unpackaged_files_terminate_build 1

Name: alterator-backend-packages
Version: 0.1.4
Release: alt1

Summary: Alterator backends for managing system packages
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-backend-packages

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

Requires: alterator-interface-packages
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14

%package -n alterator-interface-packages
Summary: Alterator interfaces for managing system packages
Group: System/Configuration/Other
Version: 0.1.1
Release: alt1

%description
Alterator backends for managing system packages and package repositories
through apt and rpm.

%description -n alterator-interface-packages
Alterator interfaces for managing system packages and package repositories
through apt and rpm.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_alterator_datadir/backends
mkdir -p %buildroot%_alterator_datadir/objects

install -v -p -m 644 -D apt/org.altlinux.alterator.apt1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D apt/org.altlinux.alterator.apt1.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 755 -D apt/apt-wrapper %buildroot%_libexecdir/%name/apt-wrapper
install -v -p -m 644 -D apt/apt.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D apt/apt.object %buildroot%_alterator_datadir/objects

install -v -p -m 644 -D apt/logger/alterator-logger.lua %buildroot%_datadir/apt/scripts/alterator-logger.lua
install -v -p -m 644 -D apt/logger/alterator-logger.conf %buildroot%_sysconfdir/apt/apt.conf.d/alterator-logger.conf

install -v -p -m 644 -D rpm/org.altlinux.alterator.rpm1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D rpm/org.altlinux.alterator.rpm1.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 644 -D rpm/rpm.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D rpm/rpm.object %buildroot%_alterator_datadir/objects

install -v -p -m 644 -D repo/org.altlinux.alterator.repo1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D repo/org.altlinux.alterator.repo1.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 644 -D repo/repo.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D repo/repo.object %buildroot%_alterator_datadir/objects

mkdir -p %buildroot%_logdir/alterator/apt
touch %buildroot%_logdir/alterator/apt/dist-upgrades.log
chmod 644 %buildroot%_logdir/alterator/apt/dist-upgrades.log
touch %buildroot%_logdir/alterator/apt/updates.log
chmod 644 %buildroot%_logdir/alterator/apt/updates.log

%files
%dir %_logdir/alterator/
%dir %_logdir/alterator/apt
%ghost %_logdir/alterator/apt/*.log
%_datadir/apt/scripts/*.lua
%config %_sysconfdir/apt/apt.conf.d/*.conf
%_libexecdir/%name/apt-wrapper
%dir %_alterator_datadir/backends
%_alterator_datadir/backends/*.backend
%dir %_alterator_datadir/objects
%_alterator_datadir/objects/*.object

%files -n alterator-interface-packages
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%_datadir/dbus-1/interfaces/*.xml
%_datadir/polkit-1/actions/*.policy

%changelog
* Wed Feb 05 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.4-alt1
- Fix timeouts for install and remove (thx Kozyrev Yuri).
- Turn lastUpdate tracker into loggers for apt updates and dist-upgrades
  (thx Kirill Sharov).
- Add lastDistUpgrade method to apt interface (thx Kozyrev Yuri).

* Mon Dec 09 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- Fix incorrect names of packages from ListAllPackages method.
- Change alterator entries format from ini to toml.

* Tue Oct 22 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.2-alt1
- Change prefix from ru.basealt to org.altlinux.
- Remove error output from Info methods.

* Wed Sep 25 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Fix some incorrect package names in List method of apt backend.
- Add lastUpdate method to apt backend.
- Add error output to all methods.

* Wed May 29 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
