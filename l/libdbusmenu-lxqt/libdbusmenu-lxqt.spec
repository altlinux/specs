# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 0

Name: libdbusmenu-lxqt
Version: 0.5.0
Release: alt1

Summary: This library provides a Qt implementation of the DBusMenu protocol
License: LGPL-2.1
Group: Graphical desktop/Other

URL: https://lxqt-project.org/
VCS: https://github.com/lxqt/libdbusmenu-lxqt

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: lxqt2-build-tools
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
* Fri Nov 06 2026 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1
- New version 0.5.0.

* Mon Apr 20 2026 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Thu Apr 17 2025 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Tue Nov 05 2024 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- new version

* Wed Jun 12 2024 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1.20240531
- initial build
