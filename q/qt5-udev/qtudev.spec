Name: qt5-udev
Version: 0.0.20201001
Release: alt1

Summary: Qt-style API to use udev
License: LGPLv3
Group: System/Libraries
Url: https://github.com/lirios/qtudev

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(umockdev-1.0)

%package -n libqt5-udev
Summary: Qt-style API to use udev
Group: System/Libraries

%package devel
Summary: Qt-style API to use udev
Group: Development/C++

%description
%summary

%description -n libqt5-udev
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

%files -n libqt5-udev
%_libdir/libQt5Udev.so.*

%files devel
%_includedir/Qt5Udev
%_libdir/libQt5Udev.so
%_libdir/cmake/Qt5Udev
%_pkgconfigdir/Qt5Udev.pc

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20201001-alt1
- updated form git.f80ba68

* Fri Oct 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191001-alt1
- initial
