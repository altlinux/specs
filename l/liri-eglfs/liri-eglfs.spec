Name: liri-eglfs
Version: 0.0.20191126
Release: alt1

Summary: Qt platform plugin with DRM/KMS support.
License: GPLv3
Group: System/Libraries
Url: https://github.com/lirios/eglfs

Source: %name-%version-%release.tar

BuildRequires: cmake cmake-modules-liri qt5-base-devel-static
BuildRequires: pkgconfig(Qt5Udev)
BuildRequires: pkgconfig(Liri1Core)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(fontconfig)

%package devel
Summary: Qt platform plugin with DRM/KMS support.
Group: Development/C++

%description
%summary
It's a fork of Qt's eglfs plugin with more feature such as:
 * Get permission to access devices to unprivileged users using logind.
 * Screen configuration.
 * Real-time screen recording.

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
%doc README.md
%_libdir/libLiri1*.so.*
%_libdir/qt5/plugins/liri/egldeviceintegrations
%_libdir/qt5/plugins/platforms/liblirieglfs.so

%files devel
%_includedir/Liri*
%_libdir/libLiri1*.so
%_libdir/cmake/Liri1PlatformHeaders
%_pkgconfigdir/Liri1PlatformHeaders.pc

%changelog
* Tue Nov 26 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191126-alt1
- updated from git.127e9b5c

* Fri Oct 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20190930-alt1
- initial
