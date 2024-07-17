%define _unpackaged_files_terminate_build 1

Name: alterator-application-components
Version: 0.1.1
Release: alt1

Summary: Alterator application for managing system components
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-application-components

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-common qt5-base-devel qt5-declarative-devel qt5-tools-devel
BuildRequires: boost-devel-headers
BuildRequires: libqbase-devel

Requires: alterator-backend-packages alterator-entry libqbase alterator-interface-component alterator-backend-component_categories

%description
Alterator application for managing system components.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%_datadir/alterator/applications
mkdir -p %buildroot%_datadir/alterator/objects
mkdir -p %buildroot%_datadir/alterator/backends
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_datadir/dbus-1/interfaces

install -v -p -m 644 -D alterator/components.object %buildroot%_datadir/alterator/objects
install -v -p -m 644 -D alterator/components-app.application %buildroot%_datadir/alterator/applications
install -v -p -m 644 -D alterator/components.backend %buildroot%_datadir/alterator/backends
install -v -p -m 644 -D alterator/components-app.backend %buildroot%_datadir/alterator/backends
install -v -p -m 644 -D setup/ru.basealt.alterator.components1.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 644 -D setup/ru.basealt.alterator.components1.xml %buildroot%_datadir/dbus-1/interfaces

%files
%_datadir/alterator/applications/*.application
%_datadir/alterator/backends/*.backend
%_datadir/alterator/objects/*.object
%_datadir/polkit-1/actions/ru.basealt.alterator.components1.policy
%_datadir/dbus-1/interfaces/ru.basealt.alterator.components1.xml
%_bindir/%name

%changelog
* Thu Mar 21 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Add support for nested categories of components.
- Update logic to comply with new component status API.

* Thu Mar 21 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
