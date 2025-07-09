%define _unpackaged_files_terminate_build 1

Name: alterator-backend-batch-component_categories
Version: 0.3
Release: alt2

Summary: Alterator backends for getting information about all categories
License: GPLv3
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-backend-batch_component_categories.git

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

Requires: alterator-backend-component_categories
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

install -v -p -m 755 -D batch_component_categories %buildroot%_libexecdir/%name/batch_component_categories
install -v -p -m 644 -D batch_component_categories.backend %buildroot%_alterator_datadir/backends/batch_component_categories.backend
install -v -p -m 644 -D org.altlinux.alterator.batch_component_categories1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D org.altlinux.alterator.batch_component_categories1.policy %buildroot%_datadir/polkit-1/actions

%files
%dir %_libexecdir/%name
%_libexecdir/%name/batch_component_categories
%_alterator_datadir/backends/*.backend
%_datadir/dbus-1/interfaces/*.xml
%_datadir/polkit-1/actions/*.policy

%changelog
* Mon Jul 07 2025 Pavel Khromov <hromovpi@altlinux.org> 0.3-alt2
- Change URL

* Thu May 22 2025 Michael Chernigin <chernigin@altlinux.org> 0.3-alt1
- Support category dirs

* Thu May 15 2025 Andrey Limachko <liannnix@altlinux.org> 0.2-alt1
- Remove %_alterator_datadir macro and hardcode path

* Mon Mar 03 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1-alt1
- Initial build
