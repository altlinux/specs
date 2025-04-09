%define _unpackaged_files_terminate_build 1

%define files_alterator_interface() \
%dir %_datadir/dbus-1 \
%dir %_datadir/dbus-1/interfaces \
%dir %_datadir/polkit-1 \
%dir %_datadir/polkit-1/actions \
%_datadir/dbus-1/interfaces/*.%{1}.xml \
%_datadir/polkit-1/actions/*.%{1}.policy

%define files_alterator_backend() \
%dir %_alterator_datadir \
%dir %_alterator_datadir/objects \
%dir %_alterator_datadir/backends \
%_alterator_datadir/objects/%{1}.object \
%_alterator_datadir/backends/%{1}.backend

%define files_alterator_application() \
%dir %_alterator_datadir \
%dir %_alterator_datadir/backends \
%dir %_alterator_datadir/applications \
%_alterator_datadir/backends/%{1}-app.backend \
%_alterator_datadir/applications/%{1}.application

Name: alterator-application-systeminfo
Version: 0.4.4
Release: alt1

Summary: ALT Systeminfo - Alterator application that shows information about system
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-application-systeminfo

Source: %name-%version.tar

Requires: alterator-interface-application >= 0.1.1
Requires: alterator-backend-systeminfo >= 0.3.2
# Recommends: alterator-backend-edition >= 0.1.5
# Recommends: alterator-backend-packages >= 0.1.4

BuildRequires(pre): rpm-macros-alterator
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt6-base-common qt6-base-devel qt6-tools-devel
BuildRequires: libtomlplusplus-devel

%description
ALT Systeminfo - Alterator application that shows information about system.

%package -n alterator-interface-release_notes
Summary: Alterator interface for release notes
Group: System/Configuration/Other

%description -n alterator-interface-release_notes
%summary

%package -n alterator-backend-release_notes
Summary: Alterator backend for release notes
Group: System/Configuration/Other
Requires: alterator-interface-release_notes
Requires: alterator-module-executor >= 0.1.19

%description -n alterator-backend-release_notes
%summary

%package -n alterator-application-release_notes
Summary: Alterator application for release notes
Group: System/Configuration/Other
Requires: alterator-interface-application >= 0.1.1
Requires: alterator-backend-release_notes
Requires: alterator-application-systeminfo >= 0.4.3

%description -n alterator-application-release_notes
%summary

%package -n alterator-interface-license
Summary: Alterator interface for license
Group: System/Configuration/Other

%description -n alterator-interface-license
%summary

%package -n alterator-backend-license
Summary: Alterator backend for license
Group: System/Configuration/Other
Requires: alterator-interface-license
Requires: alterator-module-executor >= 0.1.19

%description -n alterator-backend-license
%summary

%package -n alterator-application-license
Summary: Alterator application for showing license
Group: System/Configuration/Other
Requires: alterator-interface-application >= 0.1.1
Requires: alterator-backend-license
Requires: alterator-application-systeminfo >= 0.4.4

%description -n alterator-application-license
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%files_alterator_application systeminfo
%_desktopdir/*
%_bindir/*
%doc LICENSE CHANGELOG.md

%files -n alterator-interface-release_notes
%files_alterator_interface release_notes1

%files -n alterator-backend-release_notes
%files_alterator_backend release-notes

%files -n alterator-application-release_notes
%files_alterator_application release-notes

%files -n alterator-interface-license
%files_alterator_interface license1

%files -n alterator-backend-license
%files_alterator_backend license

%files -n alterator-application-license
%files_alterator_application license

%changelog
* Wed Apr 09 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.4-alt1
- Changed an incorrect display names of branches (closes: #53758).
- Added support Cinnamon DE settings.
- Added License application for Alterator Explorer.
  Binary packages of this SRPM replaces binary packages which built
  from alterator-backend-license, alterator-application-license SRPMs.
- Renamed Alterator Explorer application from Properties to About System.
- Fixed wrong DE settings running.
- Fixed small size of License dialog.

* Sat Apr 05 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.3-alt1
- New version.

* Fri Mar 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.2-alt1
- New version.

* Wed Mar 19 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.1-alt2
- Change summary and description.

* Tue Mar 18 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.1-alt1
- New version.

* Mon Mar 17 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.0-alt1
- New version.

* Sun Mar 16 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.0-alt1
- New version.

* Sun Mar 09 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.1-alt1
- New version.

* Tue Mar 07 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.0-alt1
- New version.

* Tue Mar 04 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.3-alt1
- New version.

* Tue Feb 25 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.2-alt1
- New version.

* Thu Feb 20 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.1-alt1
- New version.

* Thu Oct 18 2024 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.0-alt1
- Initial build.
