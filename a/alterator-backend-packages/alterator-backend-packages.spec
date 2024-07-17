%define _unpackaged_files_terminate_build 1

Name: alterator-backend-packages
Version: 0.1.0
Release: alt1

Summary: Alterator backends for managing system packages
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-backend-packages

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

Requires: alterator-interface-packages
Requires: alterator-manager
Requires: alterator-module-executor

%package -n alterator-interface-packages
Summary: Alterator interfaces for managing system packages
Group: System/Configuration/Other
Version: 0.1.0
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

install -v -p -m 644 -D apt/ru.basealt.alterator.apt1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D apt/ru.basealt.alterator.apt1.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 755 -D apt/apt-wrapper %buildroot%_libexecdir/%name/apt-wrapper
install -v -p -m 644 -D apt/apt.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D apt/apt.object %buildroot%_alterator_datadir/objects

install -v -p -m 644 -D rpm/ru.basealt.alterator.rpm1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D rpm/ru.basealt.alterator.rpm1.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 644 -D rpm/rpm.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D rpm/rpm.object %buildroot%_alterator_datadir/objects

install -v -p -m 644 -D repo/ru.basealt.alterator.repo1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D repo/ru.basealt.alterator.repo1.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 644 -D repo/repo.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D repo/repo.object %buildroot%_alterator_datadir/objects

%files
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
* Wed May 29 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
