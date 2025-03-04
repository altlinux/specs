%define _unpackaged_files_terminate_build 1

Name: alterator-backend-systeminfo
Version: 0.1.2
Release: alt1

Summary: Alterator backends for getting system information
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-backend-systeminfo

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14

%description
Alterator backends for getting system information.

%prep
%setup

%install
mkdir -p %buildroot%_alterator_datadir/backends
mkdir -p %buildroot%_alterator_datadir/objects
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions

install -v -p -m 755 -D systeminfo %buildroot%_libexecdir/%name
install -v -p -m 644 -D systeminfo.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D org.altlinux.alterator.systeminfo1.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D org.altlinux.alterator.systeminfo1.policy %buildroot%_datadir/polkit-1/actions

%files
%dir %_libexecdir/%name
%dir %_alterator_datadir/backends
%dir %_alterator_datadir/objects
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%_libexecdir/*
%_alterator_datadir/backends/*
%_datadir/dbus-1/interfaces/*
%_datadir/polkit-1/actions/*

%changelog
* Tue Mar 04 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.2-alt1
- New version.

* Thu Feb 20 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.1-alt1
- New version.

* Wed Sep 25 2024 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.0-alt1
- Initial build.

