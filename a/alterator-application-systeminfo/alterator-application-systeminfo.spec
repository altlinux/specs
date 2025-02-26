%define _unpackaged_files_terminate_build 1

Name: alterator-application-systeminfo
Version: 0.1.2
Release: alt1

Summary: Alterator application for getting information about system
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-application-systeminfo

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt6-base-common qt6-base-devel qt6-tools-devel
BuildRequires: libtomlplusplus-devel

Requires: alterator-backend-systeminfo >= 0.1.1
Requires: alterator-backend-packages   >= 0.1.4
Requires: alterator-backend-edition

%description
Alterator application for getting information about system.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%_alterator_datadir/applications
mkdir -p %buildroot%_alterator_datadir/objects
mkdir -p %buildroot%_alterator_datadir/backends
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_datadir/dbus-1/interfaces

install -v -p -m 644 -D alterator/systeminfo-app.object %buildroot%_alterator_datadir/objects/systeminfo.object
install -v -p -m 644 -D alterator/systeminfo-app.backend %buildroot%_alterator_datadir/backends/systeminfo-app.backend
install -v -p -m 644 -D alterator/systeminfo.application %buildroot%_alterator_datadir/applications/systeminfo.application

%files
%_alterator_datadir/applications/*.application
%_alterator_datadir/backends/*.backend
%_alterator_datadir/objects/*.object
%_bindir/%name

%changelog
* Tue Feb 25 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.2-alt1
- New version.

* Thu Feb 20 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.1-alt1
- New version.

* Thu Oct 18 2024 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.0-alt1
- Initial build.

