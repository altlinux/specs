Name: liri-shell
Version: 0.9.0
Release: alt3

Summary: Responsive shell for the Liri desktop.
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/lirios/shell

Source: %name-%version-%release.tar

BuildRequires: cmake cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5WaylandClient)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5AccountsService)
BuildRequires: pkgconfig(Qt5GSettings)
BuildRequires: pkgconfig(Liri1Core)
BuildRequires: pkgconfig(Liri1WaylandClient)
BuildRequires: pkgconfig(Liri1WaylandServer)
BuildRequires: pkgconfig(Liri1PlatformHeaders)
BuildRequires: pkgconfig(polkit-qt5-1)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libpipewire-0.2)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: qml(QtGraphicalEffects)
BuildRequires: qml(Fluid.Core)
BuildRequires: kf5-solid-devel
BuildRequires: libpam-devel
BuildRequires: qt5-tools-devel

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
%_prefix/lib/systemd/user/liri-shell*
%_prefix/libexec/liri-shell
%_prefix/libexec/liri-shell-helper
%_libdir/qt5/qml/Liri/*
%_datadir/liri-shell
%_datadir/glib-2.0/schemas/*.xml

%changelog
* Tue Nov 26 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt3
- update from upstream git.ec8c2372

* Fri Nov 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt2
- v0.9.0-445-g8d979d8f

* Wed Oct 09 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt1
- initial
