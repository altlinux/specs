Name: liri-materialdecoration
Version: 1.1.0
Release: alt4

Summary: Client-side decoration for Qt applications on Wayland
License: LGPLv3
Group: Graphical desktop/Other
Url: https://github.com/lirios/materialdecoration

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri qt5-base-devel-static
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5WaylandClient)
BuildRequires: pkgconfig(xkbcommon)

%description
%summary

%prep
%setup
%add_optflags -I%_includedir/qt5/QtXkbCommonSupport/5.15.2

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_libdir/qt5/plugins/wayland-decoration-client/libmaterialdecoration.so

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt4
- update from git.1d9f0fd

* Mon Mar 01 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt3
- fixed build with Qt >= 5.15.2

* Mon Aug 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt2
- fixed build witjh Qt >= 5.15

* Thu Oct 31 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- initial
