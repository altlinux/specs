%define _unpackaged_files_terminate_build 1

Name: gnome-pie
Version: 0.7.3
Release: alt2
Summary: A pie menu launcher for linux
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://github.com/Schneegans/Gnome-Pie
Source0: %name-%version.tar
BuildRequires(pre): rpm-macros-cmake cmake
BuildRequires: libgnome-menus-devel libgtk+3-devel libwnck3-devel
BuildRequires: vala glib2-devel
BuildRequires: libpcre2-devel libffi-devel bzlib-devel libarchive-devel
BuildRequires: libxml2-devel libXtst-devel libgee0.8-devel

%description
Gnome-Pie is a circular application launcher for Linux. It is made of several pies, each consisting of multiple slices.
The user presses a key stroke which opens the desired pie. By activating one of its slices, applications may be launched, key presses may be simulated or files can be opened.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/scalable/apps/%name-symbolic.svg
%exclude %_datadir/locale/zanata.xml
%_man1dir/%name.1.xz
%_defaultdocdir/%name/README.md
%_datadir/%name

%changelog
* Mon Feb 17 2025 Obidin Oleg <nofex@altlinux.org> 0.7.3-alt2
- Remove unnecessary libappindicator-gtk3 BR
- Changed the wrong description

* Tue Aug 21 2024 Obidin Oleg <nofex@altlinux.org> 0.7.3-alt1
- First build for ALT
