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

Name: alt-systeminfo
Version: 0.4.5
Release: alt3

Summary: ALT Systeminfo - Alterator application that shows information about system
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alt-systeminfo

Source: %name-%version.tar

Requires: alterator-interface-application >= 0.1.1
Requires: alterator-backend-systeminfo >= 0.3.2
Requires: alterator-module-executor >= 0.1.19
# Recommends: alterator-backend-edition >= 0.1.5
# Recommends: alterator-backend-packages >= 0.1.4

BuildRequires(pre): rpm-macros-alterator
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt6-base-common qt6-base-devel qt6-tools-devel
BuildRequires: libtomlplusplus-devel

Provides: alterator-interface-release_notes = %version-%release
Provides: alterator-backend-release_notes = %version-%release
Provides: alterator-application-release_notes = %version-%release
Provides: alterator-interface-license = %version-%release
Provides: alterator-backend-license = %version-%release
Provides: alterator-application-license = %version-%release
Provides: alterator-application-systeminfo = %version-%release

Obsoletes: alterator-interface-release_notes < 0.4.4-alt2
Obsoletes: alterator-backend-release_notes < 0.4.4-alt2
Obsoletes: alterator-application-release_notes < 0.4.4-alt2
Obsoletes: alterator-interface-license < 0.4.4-alt2
Obsoletes: alterator-backend-license < 0.4.4-alt2
Obsoletes: alterator-application-license < 0.4.4-alt2
Obsoletes: alterator-application-systeminfo < 0.4.5-alt3

%description
ALT Systeminfo - Alterator application that shows information about system.

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

%files_alterator_interface release_notes1
%files_alterator_backend release-notes
%files_alterator_application release-notes
%files_alterator_interface license1
%files_alterator_backend license
%files_alterator_application license

%changelog
* Fri Jul 11 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.5-alt3
- Rename package to alt-systeminfo with providing.

* Wed May 14 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.5-alt2
- Actualize upstream URL.

* Sat Apr 19 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.4.5-alt1
- Changed:
  + Size of edition wizard window.
- Fixed:
  + Missing names of editions if locale is not en or ru.
- Removed:
  + Extra text about components from edition wizard.

* Wed Apr 16 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.4.4-alt2
- Split unused subpackages with internal applications, interfaces and backends.

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

* Fri Mar 07 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.0-alt1
- New version.

* Tue Mar 04 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.3-alt1
- New version.

* Tue Feb 25 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.2-alt1
- New version.

* Thu Feb 20 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.1-alt1
- New version.

* Fri Oct 18 2024 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.0-alt1
- Initial build.
