Name:    libsurvive
Version: 1.01
Release: alt1

Summary: Open Source Lighthouse Tracking System
License: MIT
Group:   System/Libraries
Url:     https://github.com/cntools/libsurvive

# Source-url: https://github.com/collabora/libsurvive/releases/download/v%version/libsurvive-v%version-source.zip
Source:  %name-%version.tar

BuildRequires: gcc-c++ cmake
BuildRequires: zlib-devel eigen3 libX11-devel libusb-devel libpcap-devel
BuildRequires: liblapack-devel libfreeglut-devel libudev-devel
BuildRequires: libhidapi-devel libopencv-devel
# Excluded as it currently breaks the build
# BuildRequires: sciplot-devel

%description
Libsurvive is a set of tools and libraries that enable 6 dof tracking
on lighthouse and vive based systems that is completely open source and
can run on any device. It currently supports both SteamVR 1.0 and SteamVR 2.0
generation of devices and should support any tracked object commercially available.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

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

%files
%doc LICENSE README.md
%_bindir/sensors-readout
%_bindir/survive-buttons
%_bindir/survive-cli
%_bindir/survive-solver
%_bindir/survive-websocketd
%_libdir/%name.so.0*
%_libdir/%name/plugins/*
%_udevrulesdir/81-vive.rules

%files devel
%doc docs/*.md
%_bindir/api_example
%_includedir/%name/*
%_includedir/cnkalman
%_includedir/cnmatrix
%_libdir/%name.so
%_libdir/pkgconfig/*.pc

%changelog
* Wed Jan 15 2025 Sergey Palcheh <minergenon@altlinux.org> 1.01-alt1
- initial build for ALT Sisyphus

