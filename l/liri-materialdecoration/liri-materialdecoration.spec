Name: liri-materialdecoration
Version: 1.1.0
Release: alt1

Summary: Client-side decoration for Qt applications on Wayland
License: LGPL
Group: Graphical desktop/Other
Url: https://github.com/lirios/materialdecoration

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5WaylandClient)

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
%doc README.md
%_libdir/qt5/plugins/wayland-decoration-client/libmaterialdecoration.so

%changelog
* Thu Oct 31 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- initial
