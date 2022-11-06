# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     xdg-desktop-portal-lxqt
Version:  0.3.0
Release:  alt1

Summary:  A backend implementation for xdg-desktop-portal
License:  LGPL-2.1
Group:    Graphical desktop/Other
Url:      https://github.com/lxqt/xdg-desktop-portal-lxqt

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libfm-qt-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libgio-devel

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc *.md
%_prefix/libexec/xdg-desktop-portal-lxqt
%_desktopdir/org.freedesktop.impl.portal.desktop.lxqt.desktop
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.lxqt.service
%_datadir/xdg-desktop-portal/portals/lxqt.portal

%changelog
* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- new version 0.3.0

* Mon Apr 18 2022 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
