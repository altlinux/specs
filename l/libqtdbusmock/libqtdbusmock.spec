%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: libqtdbusmock
Version: 0.9.1
Release: alt1

Summary: Library for mocking DBus interactions using Qt
License: LGPL-3.0-only
Group: Development/C++
Url: https://gitlab.com/ubports/development/core/libqtdbusmock

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(gtest)
BuildRequires: ayatana-cmake-modules

%if_with check
BuildRequires: ctest
BuildRequires: /proc
BuildRequires: dbus
BuildRequires: python3(dbusmock)
%endif

%description
A simple library for mocking DBus services with a Qt API. The software
is relevant for unit testing DBus services based on Qt API.

This package contains the shared library.

%package devel
Group: Development/C++
Summary: Library for mocking DBus interactions using Qt (development files)
Requires: %{name} = %{version}-%{release}

%description devel
A simple library for mocking DBus services with a Qt API. The software
is relevant for unit testing DBus services based on Qt API.

This package contains header files needed for development.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV

%files
%doc AUTHORS ChangeLog COPYING COPYING.LGPL README.md
%_libdir/libqtdbusmock.so.1*
%dir %_datadir/libqtdbusmock
%dir %_datadir/libqtdbusmock/templates
%_datadir/libqtdbusmock/templates/org.freedesktop.hostname1.py
%_datadir/libqtdbusmock/templates/org.freedesktop.login1.py

%files devel
%_libdir/libqtdbusmock.so
%dir %_includedir/libqtdbusmock-1
%dir %_includedir/libqtdbusmock-1/libqtdbusmock
%_includedir/libqtdbusmock-1/libqtdbusmock/DBusMock.h
%_includedir/libqtdbusmock-1/libqtdbusmock/DeclareMetatypes.h
%_includedir/libqtdbusmock-1/libqtdbusmock/ExportInterfaces.h
%_includedir/libqtdbusmock-1/libqtdbusmock/Method.h
%_includedir/libqtdbusmock-1/libqtdbusmock/MethodCall.h
%_includedir/libqtdbusmock-1/libqtdbusmock/MockInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/MockInterfaceClasses.h
%_includedir/libqtdbusmock-1/libqtdbusmock/NamedMethodCall.h
%_includedir/libqtdbusmock-1/libqtdbusmock/NetworkManagerMockInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/NotificationDaemonMockInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/OfonoConnectionManagerInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/OfonoMockInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/OfonoModemInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/OfonoNetworkRegistrationInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/OfonoSimManagerInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/PropertiesInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/URfkillDeviceInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/URfkillInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/URfkillKillswitchInterface.h
%_includedir/libqtdbusmock-1/libqtdbusmock/config.h
%_pkgconfigdir/libqtdbusmock-1.pc

%changelog
* Fri Jul 18 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus
