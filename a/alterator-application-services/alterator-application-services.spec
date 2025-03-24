%define _unpackaged_files_terminate_build 1

Name: alterator-application-services
Version: 0.1.2
Release: alt1

Summary: Alterator application for managing services
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-application-services

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-alterator
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-base-common
BuildRequires: libtomlplusplus-devel

Requires: alterator-interface-service
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name
%doc *.md

%changelog
* Mon Mar 24 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- update interface by Andrey Alekseev <parovoz@altlinux.org>
- add search bar by Andrey Alekseev <parovoz@altlinux.org>

* Tue Mar 11 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt1
- fix missing icon on some environments by Andrey Alekseev <parovoz@altlinux.org>
- small ui improvements by Andrey Alekseev <parovoz@altlinux.org>

* Sun Mar 09 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt2
- fix main window title
- add .gitingnore

* Fri Mar 7 2025 Andrey Alekseev <parovoz@altlinux.org> 0.1.0-alt1
- initial build
