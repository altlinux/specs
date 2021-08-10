Name: liri-platformtheme
Version: 1.0.0
Release: alt2

Summary: Qt platform theme plugin for apps integration
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/lirios/platformtheme

Source: %name-%version-%release.tar

BuildRequires: cmake cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5GSettings)
BuildRequires: pkgconfig(Qt5WaylandClient)
BuildRequires: pkgconfig(Liri1WaylandClient)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: qt5-base-devel-static

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_qt5_plugindir/platformthemes/libliritheme.so
%_qt5_plugindir/wayland-shell-integration/libliri-layer-shell.so

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt2
- updated from git.267a874

* Mon Oct 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial
