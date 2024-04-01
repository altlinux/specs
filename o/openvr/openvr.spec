%define _unpackaged_files_terminate_build 1

%define soname 2
%define libname lib%name%soname
%define devname lib%name-devel

Name: openvr
Version: 2.5.1
Release: alt1

Summary: Virtual reality SDK

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/ValveSoftware/openvr

Source: %name-%version.tar

Patch0: openvr-2.3.3-alt-install-library.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

%description
OpenVR is an API and runtime that allows access to VR hardware from multiple vendors
without requiring that applications have specific knowledge of the hardware they are
targeting.

%package -n %libname
Summary: SDK openvr API library
Group: System/Libraries

%description -n %libname
OpenVR is an API and runtime that allows access to VR hardware from multiple vendors
without requiring that applications have specific knowledge of the hardware they are
targeting.

%package -n %devname
Summary: Development files for openvr API
Group: Development/Other
Requires: %libname = %EVR

%description -n %devname
OpenVR is an API and runtime that allows access to VR hardware from multiple vendors
without requiring that applications have specific knowledge of the hardware they are
targeting.

%prep
%setup
%patch0 -p1

# drop prebuild binary
rm -rv lib bin

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_SHARED=ON \
    -DBUILD_UNIVERSAL=OFF \
    -DUSE_LIBCXX=OFF \
    %nil

%cmake_build

%install
%cmake_install

%files -n %libname
%_libdir/libopenvr_api.so.*

%files -n %devname
%doc LICENSE README.md
%_includedir/%name
%_libdir/libopenvr_api.so
%_datadir/pkgconfig/%name.pc

%changelog
* Mon Apr 01 2024 Mikhail Tergoev <fidel@altlinux.org> 2.5.1-alt1
- 2.5.1

* Mon Mar 18 2024 Mikhail Tergoev <fidel@altlinux.org> 2.2.3-alt1
- initial build for ALT Sisyphus

