%define _unpackaged_files_terminate_build 1

Name: alterator-application-license
Version: 0.1.0
Release: alt1

Summary: Alterator application for viewing license
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-application-license

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-common qt5-base-devel qt5-tools-devel
BuildRequires: libqbase-devel

Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14
Requires: alterator-backend-license

%description
Alterator application for viewing license.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_alterator_datadir/backends
mkdir -p %buildroot%_alterator_datadir/applications

install -v -p -m 644 -D alterator-application-license.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D alterator-application-license.application %buildroot%_alterator_datadir/applications


%files
%_bindir/%name
%dir %_alterator_datadir/backends
%dir %_alterator_datadir/applications
%_alterator_datadir/backends/*.backend
%_alterator_datadir/applications/*.application

%changelog
* Fri Feb 21 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build for Sisyphus
