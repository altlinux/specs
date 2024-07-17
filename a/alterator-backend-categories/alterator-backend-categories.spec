%define _unpackaged_files_terminate_build 1

Name: alterator-backend-categories
Version: 0.1.0
Release: alt1

Summary: Backend for Alterator categories
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-backend-categories

BuildArch: noarch

Source0: %name-%version.tar

Requires: alterator-interface-categories
Requires: alterator-module-executor
Requires: alterator-entry
Requires: bash

%package -n alterator-interface-categories
Summary: Interface for Alterator categories
Group: System/Configuration/Other
Version: 0.1.0
Release: alt1

%description
Backend for Alterator categories.

%description -n alterator-interface-categories
Interface for Alterator categories.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/alterator/backends
mkdir -p %buildroot%_datadir/alterator/categories
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions

install -v -p -m 644 -D categories.backend %buildroot%_datadir/alterator/backends
install -v -p -m 755 -D category-info %buildroot%_libexecdir/%name
install -v -p -m 755 -D list-categories %buildroot%_libexecdir/%name
install -v -p -m 644 -D ru.basealt.alterator.categories.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D ru.basealt.alterator.categories.policy %buildroot%_datadir/polkit-1/actions

%files
%doc LICENSE
%dir %_datadir/alterator/backends
%dir %_libexecdir/%name
%_datadir/alterator/backends/categories.backend
%_libexecdir/%name/category-info
%_libexecdir/%name/list-categories

%files -n alterator-interface-categories
%_datadir/polkit-1/actions/ru.basealt.alterator.categories.policy
%_datadir/dbus-1/interfaces/ru.basealt.alterator.categories.xml

%changelog
* Tue Jun 25 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
