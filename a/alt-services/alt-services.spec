%define _unpackaged_files_terminate_build 1

Name: alt-services
Version: 0.1.4
Release: alt1
Provides: alterator-application-services
Obsoletes: alterator-application-services

Summary: Alterator application for managing services
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alt-services

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-alterator
BuildRequires: cmake extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-base-common
BuildRequires: libtoml11-devel
BuildRequires: boost-devel-headers
BuildRequires: kf6-kwidgetsaddons-devel

Requires: alterator-interface-service >= 0.2.1
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14

%description
GUI utility for alterator service management.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
install -v -p -m 644 -D %name.desktop %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_datadir/alterator/applications
install -v -p -m 644 -D alterator/alt-services.application %buildroot%_datadir/alterator/applications

mkdir -p %buildroot%_datadir/alterator/backends
install -v -p -m 644 -D alterator/alt-services.backend %buildroot%_datadir/alterator/backends

%files
%_bindir/alt-services
%_desktopdir/alt-services.desktop
%_datadir/alterator/applications/alt-services.application
%_datadir/alterator/backends/alt-services.backend
%doc *.md

%changelog
* Tue Jul 22 2025 Andrey Limachko <liannnix@altlinux.org> 0.1.4-alt1
- new version (thx Andrey Alekseev)

* Wed May 14 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- add tooltip in service table header
- service will not be displayed if any errors were encountered during parsing
- add role icons
- implement composite parameters and arrays
- implement deployment/configuration dialog
- implement start/stop methods
- add desktop file
- add force_deploy parameter
- changed parameter icon
- improved properties table
- resources are now displayed in groups
- various UI improvements

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
