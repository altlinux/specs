%define _unpackaged_files_terminate_build 1

Name: alterator-application-systeminfo
Version: 0.4.3
Release: alt1

Summary: ALT Systeminfo - Alterator application that shows information about system
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-application-systeminfo

Source: %name-%version.tar

Requires: alterator-interface-application >= 0.1.1
Requires: alterator-backend-systeminfo >= 0.3.1
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

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%dir %_alterator_datadir
%dir %_alterator_datadir/applications
%dir %_alterator_datadir/backends
%_alterator_datadir/applications/systeminfo.application
%_alterator_datadir/backends/systeminfo-app.backend
%_desktopdir/*
%_bindir/*
%doc LICENSE CHANGELOG.md

%files -n alterator-interface-release_notes
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%_datadir/dbus-1/interfaces/*.release_notes1.xml
%_datadir/polkit-1/actions/*.release_notes1.policy

%files -n alterator-backend-release_notes
%dir %_alterator_datadir
%dir %_alterator_datadir/objects
%dir %_alterator_datadir/backends
%_alterator_datadir/objects/release-notes.object
%_alterator_datadir/backends/release-notes.backend

%files -n alterator-application-release_notes
%dir %_alterator_datadir
%dir %_alterator_datadir/backends
%dir %_alterator_datadir/applications
%_alterator_datadir/backends/release-notes-app.backend
%_alterator_datadir/applications/release-notes.application

%changelog
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
