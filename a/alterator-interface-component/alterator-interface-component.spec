%define _unpackaged_files_terminate_build 1

Name: alterator-interface-component
Version: 0.1.1
Release: alt1

Summary: Components interface for alterator browser
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-interface-component

BuildArch: noarch

Requires: alterator-entry

Source0: %name-%version.tar

%description
Components interface for alterator browser.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_libexecdir/%name

install -v -p -m 644 -D ru.basealt.alterator.component1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D ru.basealt.alterator.component1.policy %buildroot%_datadir/polkit-1/actions

sed -i 's/@VERSION@/%version/' basic_check_component_installed
install -v -p -m 755 -D basic_check_component_installed %buildroot%_libexecdir/%name/basic_check_component_installed

sed -i 's/@VERSION@/%version/' basic_get_component_description
install -v -p -m 755 -D basic_get_component_description %buildroot%_libexecdir/%name/basic_get_component_description

%files
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1/actions
%dir %_libexecdir/%name
%_libexecdir/%name/basic_check_component_installed
%_libexecdir/%name/basic_get_component_description
%_libexecdir/%name/*
%_datadir/polkit-1/actions/ru.basealt.alterator.component1.policy
%_datadir/dbus-1/interfaces/ru.basealt.alterator.component1.xml

%changelog
* Thu Jun 27 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Improve performance of basic check for component installed.

* Thu Jun 27 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
