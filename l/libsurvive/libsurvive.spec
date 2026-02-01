%define soname 0

Name: libsurvive
Version: 1.01
Release: alt2

Summary: Open Source Lighthouse Tracking System
License: MIT
Group: System/Libraries
Url: https://github.com/cntools/libsurvive
Vcs: https://github.com/cntools/libsurvive

Source:  %name-%version.tar

ExcludeArch: %ix86

BuildRequires: gcc-c++ cmake
BuildRequires: zlib-devel eigen3-compat-devel libX11-devel libusb-devel libpcap-devel
BuildRequires: liblapack-devel libfreeglut-devel libudev-devel
BuildRequires: libhidapi-devel libopencv-devel

%description
Libsurvive is a set of tools and libraries that enable 6 dof tracking
on lighthouse and vive based systems that is completely open source and
can run on any device. It currently supports both SteamVR 1.0 and SteamVR 2.0
generation of devices and should support any tracked object commercially available.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name%soname = %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %name%soname
Group: System/Libraries
Summary: %name library
Obsoletes: %name <= 1.01-alt1
%description -n %name%soname
%name library.

%package tools
Summary: Tools for %name
Group: Other
Requires: %name%soname = %EVR
%description tools
Tools for %name.

%package plugins
Summary: Plugins for %name
Group: Other
Requires: %name%soname = %EVR
%description plugins
Plugins for %name.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package.

%prep
%setup

# Drop bundled libraries for non-Linux platforms
rm redist/*.m redist/dirent.windows.h

%build
rm -rf build

%cmake \
  -DLIB_INSTALL_DIR="%_libdir/" \
  -DUSE_EIGEN=ON \
  -DUSE_OPENBLAS=ON \
  -DUSE_OPENCV=ON \
  -DUSE_HIDAPI=ON

%cmake_build

%install
%cmake_install
rm -r %buildroot%_libexecdir/*.a

# Install udev rules
install -Dpm0644 -t %buildroot%_udevrulesdir useful_files/81-vive.rules

%files common
%doc LICENSE README.md docs

%files -n %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%{soname}.*
%_udevrulesdir/81-vive.rules

%files tools
%_bindir/*

%files plugins
%_libdir/%name/plugins

%files devel
%_includedir/*
%_libdir/%name.so
%_libdir/pkgconfig/*.pc

%changelog
* Sun Feb 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.01-alt2
- FTBFS: rebuilded with eigen3-compat-devel.
- Added ExcludeArch: ix86.

* Wed Jan 15 2025 Sergey Palcheh <minergenon@altlinux.org> 1.01-alt1
- initial build for ALT Sisyphus

