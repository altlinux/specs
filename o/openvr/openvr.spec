%define _unpackaged_files_terminate_build 1

%define soname 2
%define libname lib%name%soname
%define devname lib%name-devel

Name: openvr
Version: 2.15.6
Release: alt1

Summary: Virtual reality SDK

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/ValveSoftware/openvr

Source: %name-%version.tar

# Use GNUInstallDirs to determine lib install path
Patch0: 1511.patch
# Add ability to build with system installed jsoncpp
Patch1: 1716.patch
# Add option to neuter the steamvr check
Patch2: openvr-skip-steamvr-check.patch
# Define soversion for the OpenVR API library
Patch3: openvr-api-soversion.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: jsoncpp-devel

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

This package provides the shared libraries for the OpenVR Application API.

%package -n %devname
Summary: Development files for openvr API
Group: Development/Other
Requires: %libname = %EVR

%description -n %devname
OpenVR is an API and runtime that allows access to VR hardware from multiple vendors
without requiring that applications have specific knowledge of the hardware they are
targeting.

This package provides the development headers for OpenVR.

%prep
%setup
%autopatch -p1

# Delete prebuilt binaries and libraries
rm -r bin lib

# Delete bundled library sources
rm -r thirdparty samples/thirdparty

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DBUILD_SHARED=ON \
    -DUSE_SYSTEM_JSONCPP=ON \
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
* Mon Jun 15 2026 Mikhail Tergoev <fidel@altlinux.org> 2.15.6-alt1
- 2.15.6

* Mon Jan 12 2026 Ilya Sorochan <k0tran@altlinux.org> 2.12.14-alt1
- 2.12.14

* Mon May 12 2025 Mikhail Tergoev <fidel@altlinux.org> 2.7.1-alt1
- 2.7.1

* Mon Apr 07 2025 Mikhail Tergoev <fidel@altlinux.org> 2.5.1-alt2
- fixed FTBFS

* Mon Apr 01 2024 Mikhail Tergoev <fidel@altlinux.org> 2.5.1-alt1
- 2.5.1

* Mon Mar 18 2024 Mikhail Tergoev <fidel@altlinux.org> 2.2.3-alt1
- initial build for ALT Sisyphus

