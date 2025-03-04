%define _unpackaged_files_terminate_build 1

Name: alterator-application-systeminfo
Version: 0.1.3
Release: alt1

Summary: Alterator application for getting information about system
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-application-systeminfo

Source: %name-%version.tar

Requires: alterator-backend-systeminfo >= 0.1.2
Requires: alterator-backend-packages   >= 0.1.4
Requires: alterator-backend-edition

BuildRequires(pre): rpm-macros-alterator
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt6-base-common qt6-base-devel qt6-tools-devel
BuildRequires: libtomlplusplus-devel

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
mkdir -p %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D alterator/systeminfo-app.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D alterator/systeminfo.application %buildroot%_alterator_datadir/applications

%files
%dir %_alterator_datadir
%dir %_alterator_datadir/applications
%dir %_alterator_datadir/backends
%_alterator_datadir/applications/*
%_alterator_datadir/backends/*
%_bindir/%name
%doc LICENSE CHANGELOG.md

%changelog
* Tue Mar 04 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.3-alt1
- New version.

* Tue Feb 25 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.2-alt1
- New version.

* Thu Feb 20 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.1-alt1
- New version.

* Thu Oct 18 2024 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.0-alt1
- Initial build.
