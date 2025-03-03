%define _unpackaged_files_terminate_build 1

Name: alterator-backend-batch-components
Version: 0.0.1
Release: alt1

Summary: Alterator backends for getting information about all components
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-backend-batch_components

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

Requires: alterator-backend-component
Requires: alt-components-base
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_alterator_datadir/backends
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions

install -v -p -m 755 -D batch_components %buildroot%_libexecdir/%name/batch_components
install -v -p -m 644 -D batch_components.backend %buildroot%_alterator_datadir/backends/batch_components.backend
install -v -p -m 644 -D org.altlinux.alterator.batch_components1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D org.altlinux.alterator.batch_components1.policy %buildroot%_datadir/polkit-1/actions

%files
%dir %_libexecdir/%name
%dir %_alterator_datadir/backends
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%_libexecdir/%name/batch_components
%_alterator_datadir/backends/*.backend
%_datadir/dbus-1/interfaces/*.xml
%_datadir/polkit-1/actions/*.policy

%changelog
* Fri Feb 28 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.1-alt1
- Initial build.
