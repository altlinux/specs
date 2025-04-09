%define _unpackaged_files_terminate_build 1

Name: alterator-backend-systeminfo
Version: 0.3.2
Release: alt1

Summary: Alterator backend for getting system information
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-backend-systeminfo

BuildArch: noarch
Source: %name-%version.tar

Requires: alterator-interface-systeminfo >= 0.3.0
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14

BuildRequires(pre): rpm-macros-alterator

%description
%summary

%package -n alterator-interface-systeminfo
Summary: Alterator interface for getting system information
Group: System/Configuration/Other
Version: 0.3.0

%description -n alterator-interface-systeminfo
%summary

%prep
%setup

%install
%makeinstall_std

%files
%dir %_libexecdir/%name
%dir %_alterator_datadir/backends
%dir %_alterator_datadir/objects
%_libexecdir/*
%_alterator_datadir/backends/*
%_alterator_datadir/objects/*

%files -n alterator-interface-systeminfo
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%_datadir/dbus-1/interfaces/*
%_datadir/polkit-1/actions/*

%changelog
* Wed Apr 09 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.2-alt1
- New version.

* Sat Apr 05 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.1-alt1
- New version.

* Fri Mar 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.0-alt1
- New version.

* Mon Mar 17 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.2-alt1
- New version.

* Fri Mar 14 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.1-alt1
- New version.

* Wed Mar 12 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.0-alt1
- New version.

* Fri Mar 07 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.2-alt2
- Put object file for Alterator Explorer.

* Tue Mar 04 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.2-alt1
- New version.

* Thu Feb 20 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.1-alt1
- New version.

* Wed Sep 25 2024 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.0-alt1
- Initial build.

