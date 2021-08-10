Name: qt5-accountsservice
Version: 1.3.0
Release: alt2

Summary: Qt-style API for AccountsService DBus service
License: LGPLv3
Group: System/Libraries
Url: https://github.com/lirios/qtaccountsservice

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)

%package -n libqt5-accountsservice
Summary: Qt-style API for AccountsService DBus service
Group: System/Libraries

%package devel
Summary: Qt-style API for AccountsService DBus service
Group: Development/C++

%description
%summary

%description -n libqt5-accountsservice
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

%files -n libqt5-accountsservice
%_libdir/libQt5AccountsService.so.*
%_libdir/qt5/qml/QtAccountsService

%files devel
%_includedir/Qt5AccountsService
%_libdir/libQt5AccountsService.so
%_libdir/cmake/Qt5AccountsService
%_pkgconfigdir/Qt5AccountsService.pc

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt2
- v1.3.0-21-gcc8bbdc

* Mon Oct 07 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- initial
