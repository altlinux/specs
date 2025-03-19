%define _unpackaged_files_terminate_build 1

Name: alterator-application-systeminfo
Version: 0.4.1
Release: alt2

Summary: ALT Systeminfo - Alterator application that shows information about system
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-application-systeminfo

Source: %name-%version.tar

Requires: alterator-backend-systeminfo >= 0.2.2

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
%_alterator_datadir/applications/*
%_alterator_datadir/backends/*
%_desktopdir/*
%_bindir/*
%doc LICENSE CHANGELOG.md

%changelog
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
