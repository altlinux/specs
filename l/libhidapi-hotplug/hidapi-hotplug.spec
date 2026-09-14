%define _name hidapi-hotplug
%define git 921fd57

Name: libhidapi-hotplug
Version: 0.15.0
Release: alt1.g%{git}

Summary: Library for communicating with USB and Bluetooth HID devices
License: GPLv3 or BSD
Group: Development/Other
Url: https://codeberg.org/OpenRGB/hidapi-hotplug
Vcs: https://codeberg.org/OpenRGB/hidapi-hotplug

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ctest
BuildRequires: /usr/bin/fox-config
BuildRequires: libudev-devel
BuildRequires: libusb-devel

Provides: %_name = %EVR

%description
This a fork of https://github.com/libusb/hidapi with hotplug support:

HIDAPI is a multi-platform library which allows an application to interface
with USB and Bluetooth HID-class devices on Windows, Linux, FreeBSD and Mac OS
X. On Linux, either the hidraw or the libusb back-end can be used. There are
trade-offs and the functionality supported is slightly different.

%package devel
Group: Development/C
Summary: Development files for hidapi
Requires: %_name = %EVR
Provides: %_name-devel = %EVR

%description devel
This package contains development files for hidapi which provides access to
USB and Bluetooth HID-class devices.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%_libdir/lib%_name-*.so.*
%doc AUTHORS.txt README.md LICENSE*.txt

%files devel
%_includedir/%_name/
%_libdir/cmake/%_name
%_libdir/lib%_name-hidraw.so
%_libdir/lib%_name-libusb.so
%_pkgconfigdir/%_name-hidraw.pc
%_pkgconfigdir/%_name-libusb.pc

%changelog
* Mon Sep 14 2026 L.A. Kostis <lakostis@altlinux.ru> 0.15.0-alt1.g921fd57
- Initial build for ALTLinux.
- .spec based on libhidapi package.
