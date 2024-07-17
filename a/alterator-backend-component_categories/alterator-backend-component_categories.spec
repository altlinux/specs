%define _unpackaged_files_terminate_build 1

Name: alterator-backend-component_categories
Version: 0.1.0
Release: alt1

Summary: Backend for components categories
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-backend-component_categories

BuildArch: noarch

Requires: alterator-interface-component_categories
Requires: alterator-entry
Requires: bash

Source0: %name-%version.tar

%package -n alterator-interface-component_categories
Summary: Interface for components categories
Group: System/Configuration/Other
Version: 0.1.0
Release: alt1

%description
Backend for components categories.

%description -n alterator-interface-component_categories
Interface for components categories.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_datadir/alterator/backends

install -v -p -m 644 -D ru.basealt.alterator.component-categories1.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 644 -D ru.basealt.alterator.component-categories1.xml %buildroot%_datadir/dbus-1/interfaces

install -v -p -m 644 -D component-categories.backend %buildroot%_datadir/alterator/backends

install -v -p -m 755 -D component-category-info %buildroot%_libexecdir/%name
install -v -p -m 755 -D list-component-categories %buildroot%_libexecdir/%name

%files
%dir %_libexecdir/%name
%dir %_datadir/alterator
%dir %_datadir/alterator/backends
%_libexecdir/%name/*
%_datadir/alterator/backends/*

%files -n alterator-interface-component_categories
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1/actions
%_datadir/dbus-1/interfaces/ru.basealt.alterator.component-categories1.xml
%_datadir/polkit-1/actions/ru.basealt.alterator.component-categories1.policy

%changelog
* Thu Jun 27 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
