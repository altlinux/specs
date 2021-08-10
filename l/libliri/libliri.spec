Name: libliri
Version: 0.0.20210809
Release: alt1

Summary: Libraries for Liri apps
License: LGPLv3
Group: System/Libraries
Url: https://github.com/lirios/libliri

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)

%package devel
Summary: Libraries for Liri apps
Group: Development/C++

%description
%summary

%description devel
%summary
this package contains development part of %name

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/liri-notify
%_libdir/libLiri1Core.so.*
%_libdir/libLiri1DBusService.so.*
%_libdir/libLiri1LocalDevice.so.*
%_libdir/libLiri1Logind.so.*
%_libdir/libLiri1Models.so.*
%_libdir/libLiri1Notifications.so.*
%_libdir/libLiri1Xdg.so.*

%dir %_libdir/qt5/qml/Liri
%_libdir/qt5/qml/Liri/Core
%_libdir/qt5/qml/Liri/Device
%_libdir/qt5/qml/Liri/DBusService
%_libdir/qt5/qml/Liri/Notifications

%files devel
%_includedir/Liri*
%_libdir/libLiri*.so
%_libdir/cmake/Liri*
%_pkgconfigdir/Liri*.pc

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20210809-alt1
- updated from git.c7cac0c

* Fri Dec 11 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20201130-alt1
- updated from git.6e47eb9

* Fri Aug 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20200312-alt1
- updated from git.0943d3b

* Mon Oct 07 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20190924-alt1
- initial
