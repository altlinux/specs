%define _unpackaged_files_terminate_build 1

Name: alterator-interface-component
Version: 0.1.5
Release: alt1

Summary: Components interface for alterator browser
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-interface-component

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires(pre): rpm-macros-features
Requires: alterator-entry >= 0.1.1
Requires: python3

%if_feature python3 3.11
%filter_from_requires /python3(toml)/d
%else
%filter_from_requires /python3(tomllib)/d
Requires: python3-module-toml
%endif

Source0: %name-%version.tar

%description
Components interface for alterator browser.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_libexecdir/%name

install -v -p -m 644 -D org.altlinux.alterator.component1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D org.altlinux.alterator.component1.policy %buildroot%_datadir/polkit-1/actions

sed -i 's/@VERSION@/%version/' basic_check_component_installed
install -v -p -m 755 -D basic_check_component_installed %buildroot%_libexecdir/%name/basic_check_component_installed

sed -i 's/@VERSION@/%version/' basic_get_component_description
install -v -p -m 755 -D basic_get_component_description %buildroot%_libexecdir/%name/basic_get_component_description

install -v -p -m 755 -D extract_packages %buildroot%_libexecdir/%name/extract_packages

%files
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1/actions
%dir %_libexecdir/%name
%_libexecdir/%name/*
%_datadir/polkit-1/actions/org.altlinux.alterator.component1.policy
%_datadir/dbus-1/interfaces/org.altlinux.alterator.component1.xml

%changelog
* Thu Dec 19 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.5-alt1
- Add support for python3.9.

* Mon Dec 09 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.4-alt1
- Switch to Alterator Entry in toml.
- Change getDescription to return array of bytes instead of strings.

* Tue Oct 22 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.3-alt1
- Change prefix from ru.basealt to org.altlinux.

* Thu Sep 23 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.2-alt1
- Fix install status of virtual packages.

* Thu Jun 27 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Improve performance of basic check for component installed.

* Thu Jun 27 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
