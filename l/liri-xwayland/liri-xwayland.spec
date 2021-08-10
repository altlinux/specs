Name: liri-xwayland
Version: 0.10.0
Release: alt2

Summary: QML plugin with an XWayland implementation
License: LGPLv3
Group: Graphical desktop/Other
Url: https://github.com/lirios/qml-xwayland

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5WaylandClient)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)

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
%_libdir/qt5/qml/Liri/XWayland

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt2
- updated from git.5328dc1

* Mon Oct 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt1
- initial
