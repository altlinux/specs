%define _unpackaged_files_terminate_build 1

Name: alterator-module-categories
Version: 0.1.1
Release: alt2

Summary: Categories interface for alterator browser.
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-module-categories

BuildArch: noarch

Source0: %name-%version.tar

Requires: alterator-module-executor alterator-entry bash

%description
Scripts and D-Bus inteface to work with categories in Alterator.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_datadir/alterator/backends
mkdir -p %buildroot%_datadir/alterator/categories
mkdir -p %buildroot%_libexecdir/%name

install -v -p -m 644 -D ru.basealt.alterator.categories1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D ru.basealt.alterator.categories1.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 644 -D categories.backend %buildroot%_datadir/alterator/backends
install -v -p -m 755 -D category-info %buildroot%_libexecdir/%name
install -v -p -m 755 -D list-categories %buildroot%_libexecdir/%name

%files
%doc LICENSE
%dir %_datadir/alterator/backends
%dir %_datadir/alterator/categories
%dir %_libexecdir/%name
%_datadir/alterator/backends/categories.backend
%_datadir/polkit-1/actions/ru.basealt.alterator.categories1.policy
%_libexecdir/%name/category-info
%_libexecdir/%name/list-categories
%_datadir/dbus-1/interfaces/ru.basealt.alterator.categories1.xml

%changelog
* Tue Apr 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt2
- fix comply with spec
- fix shellcheck warning to use bash instead of sh
- remove rules

* Mon Jan 29 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

* Tue Nov 14 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
