# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 0

Name: libdbusmenu-lxqt
Version: 0.1.0
Release: alt1.20240531

Summary: This library provides a Qt implementation of the DBusMenu protocol
License: LGPL-2.1
Group: Graphical desktop/Other

Url: https://github.com/lxqt/libdbusmenu-lxqt
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: qt6-base-devel

%description
%summary.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Development files for %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG NEWS README.md
%_libdir/libdbusmenu-lxqt.so.%sover
%_libdir/libdbusmenu-lxqt.so.%sover.*

%files devel
%_libdir/libdbusmenu-lxqt.so
%_libdir/cmake/dbusmenu-lxqt/
%_includedir/dbusmenu-lxqt/
%_pkgconfigdir/dbusmenu-lxqt.pc

%changelog
* Wed Jun 12 2024 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1.20240531
- initial build
