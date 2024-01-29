%define _unpackaged_files_terminate_build 1

Name: alterator-module-categories
Version: 0.1.1
Release: alt1

Summary: Categories interface for alterator browser.
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-module-categories

BuildArch: noarch

Source0: %name-%version.tar

Requires: alterator-module-executor

%description
Object categories interface for alterator browser operating via D-Bus.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
#mkdir -p %buildroot%_sysconfdir/polkit-1/rules.d
mkdir -p %buildroot%_datadir/polkit-1/actions

# for alterator-manager autorestart
mkdir -p %buildroot%_datadir/alterator/backends

mkdir -p %buildroot%_datadir/alterator/categories
mkdir -p %buildroot%_libexecdir/%name

install -v -p -m 644 -D ru.basealt.alterator.categories.xml %buildroot%_datadir/dbus-1/interfaces
#install -v -p -m 644 -D 49-alterator-module-categories.rules %buildroot%_sysconfdir/polkit-1/rules.d
install -v -p -m 644 -D ru.basealt.alterator.categories.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 644 -D categories.backend %buildroot%_datadir/alterator/backends
install -v -p -m 755 -D category-info %buildroot%_libexecdir/%name
install -v -p -m 755 -D list-categories %buildroot%_libexecdir/%name

%files
%dir %_datadir/alterator/backends
%dir %_datadir/alterator/categories
%dir %_libexecdir/%name
%_datadir/alterator/backends/categories.backend
%_datadir/polkit-1/actions/ru.basealt.alterator.categories.policy
%_libexecdir/%name/category-info
%_libexecdir/%name/list-categories
%_datadir/dbus-1/interfaces/ru.basealt.alterator.categories.xml
#%_sysconfdir/polkit-1/rules.d/49-alterator-module-categories.rules

%changelog
* Mon Jan 29 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

* Tue Nov 14 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
