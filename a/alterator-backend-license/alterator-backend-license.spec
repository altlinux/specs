%define _unpackaged_files_terminate_build 1

Name: alterator-backend-license
Version: 0.1.0
Release: alt1

Summary: Alterator backend, replacing old license module
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-backend-license

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14
Requires: alterator-backend-edition

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_alterator_datadir/backends
mkdir -p %buildroot%_alterator_datadir/objects

install -v -p -m 644 -D org.altlinux.alterator.license.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D org.altlinux.alterator.license.policy %buildroot%_datadir/polkit-1/actions

install -v -p -m 644 -D license.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D license.object %buildroot%_alterator_datadir/objects


%files
%_datadir/dbus-1/interfaces/org.altlinux.alterator.license.xml
%_datadir/polkit-1/actions/org.altlinux.alterator.license.policy
%_alterator_datadir/backends/license.backend
%_alterator_datadir/objects/license.object


%changelog
* Fri Feb 21 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build

