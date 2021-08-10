Name: liri-wayland
Version: 0.0.20210808
Release: alt1

Summary: Wayland client and server extensions
License: LGPLv3
Group: System/Libraries
Url: https://github.com/lirios/wayland

Source: %name-%version-%release.tar

BuildRequires: cmake cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5WaylandClient)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)

%package -n libliri-wayland-client
Summary: Liri wayland client extensions
Group: System/Libraries

%package -n libliri-wayland-client-devel
Summary: Liri wayland client extensions
Group: Development/C++

%package -n libliri-wayland-server
Summary: Liri wayland server extensions
Group: System/Libraries

%package -n libliri-wayland-server-devel
Summary: Liri wayland server extensions
Group: Development/C++

%description
%summary

%description -n libliri-wayland-client
%summary

%description -n libliri-wayland-client-devel
%summary

%description -n libliri-wayland-server
%summary

%description -n libliri-wayland-server-devel
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files -n libliri-wayland-client
%_libdir/libLiri1WaylandClient.so.*
%_libdir/qt5/qml/Liri/WaylandClient

%files -n  libliri-wayland-server
%_libdir/libLiri1WaylandServer.so.*
%_libdir/qt5/qml/Liri/WaylandServer

%files -n libliri-wayland-client-devel
%_includedir/LiriWaylandClient
%_libdir/libLiri1WaylandClient.so
%_pkgconfigdir/Liri1WaylandClient.pc
%_libdir/cmake/Liri1WaylandClient

%files -n libliri-wayland-server-devel
%_includedir/LiriWaylandServer
%_libdir/libLiri1WaylandServer.so
%_pkgconfigdir/Liri1WaylandServer.pc
%_libdir/cmake/Liri1WaylandServer

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20210808-alt1
- update from git.da74133

* Thu Aug 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20200726-alt1
- update from upstream git.5b1e3bf

* Thu Apr 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20200401-alt1
- update from upstream git.00a598b

* Tue Nov 26 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191126-alt1
- update from upstream git.3ec6248

* Fri Nov 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191026-alt1
- update from upstream git.89303e9

* Mon Oct 07 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191002-alt1
- initial
