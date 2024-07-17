%define _unpackaged_files_terminate_build 1

Name: alterator-application-packages
Version: 0.1.1
Release: alt1

Summary: Alterator application for managing system packages and package repositories
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-application-packages

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-common qt5-base-devel qt5-declarative-devel qt5-tools-devel
BuildRequires: libqbase-devel
BuildRequires: desktop-file-utils ImageMagick-tools
BuildRequires: xorg-xvfb xvfb-run

Requires: alterator-backend-packages alterator-manager alterator-module-executor

%description
Alterator application for managing system packages and package repositories
through apt and rpm.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_alterator_datadir/backends
mkdir -p %buildroot%_alterator_datadir/applications

install -v -p -m 644 -D alterator/amp-apt.backend %buildroot%_alterator_datadir/backends
install -v -p -m 644 -D alterator/amp-apt.application %buildroot%_alterator_datadir/applications

install -v -p -m 644 -D alterator/amp-rpm.backend %buildroot%_datadir/alterator/backends
install -v -p -m 644 -D alterator/amp-rpm.application %buildroot%_alterator_datadir/applications

install -v -p -m 644 -D alterator/amp-repo.backend %buildroot%_datadir/alterator/backends
install -v -p -m 644 -D alterator/amp-repo.application %buildroot%_alterator_datadir/applications

%files
%doc LICENSE
%_bindir/%name
%dir %_alterator_datadir/backends
%dir %_alterator_datadir/applications
%_alterator_datadir/backends/*.backend
%_alterator_datadir/applications/*.application

%changelog
* Thu Jul 11 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Cache apt page, so it takes less time to load after first try.
- Show package info as a table instead of plain text.

* Mon Feb 26 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
