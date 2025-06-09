%define _unpackaged_files_terminate_build 1

Name: soapyosmo
Version: 0.2.5
Release: alt2

Summary: OsmoSDR device support for SoapySDR
License: MIT
Group: Engineering
Url: https://github.com/pothosware/SoapyOsmo

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(SoapySDR)
BuildRequires: boost-devel
BuildRequires: pkgconfig(libosmosdr)
BuildRequires: pkgconfig(libmirisdr)

%description
The SoapyOsmo project provides SoapySDR hardware support modules using
drivers in gr-osmosdr. Using this, any program using SoapySDR to
interface to software defined radio hardware can make use of OsmoSDR,
Mirics SDR, and RFSpace SDR devices.

This package contains the OsmoSDR hardware support module.

%package common
Group: Engineering
Summary: Common files for %name

%description common
The SoapyOsmo project provides SoapySDR hardware support modules using
drivers in gr-osmosdr. Using this, any program using SoapySDR to
interface to software defined radio hardware can make use of OsmoSDR,
Mirics SDR, and RFSpace SDR devices.

This package contains common files used by the individual driver
modules.

%package mirisdr
Group: Engineering
Summary: Mirics SDR device support for SoapySDR
Requires: %{name}-common = %{version}-%{release}

%description mirisdr
The SoapyOsmo project provides SoapySDR hardware support modules using
drivers in gr-osmosdr. Using this, any program using SoapySDR to
interface to software defined radio hardware can make use of OsmoSDR,
Mirics SDR, and RFSpace SDR devices.

This package contains the hardware support module for Mirics SDR
devices.

%package osmosdr
Group: Engineering
Summary: OsmoSDR device support for SoapySDR
Requires: %{name}-common = %{version}-%{release}

%description osmosdr
The SoapyOsmo project provides SoapySDR hardware support modules using
drivers in gr-osmosdr. Using this, any program using SoapySDR to
interface to software defined radio hardware can make use of OsmoSDR,
Mirics SDR, and RFSpace SDR devices.

This package contains the OsmoSDR hardware support module.

%package rfspace
Group: Engineering
Summary: RFSpace device support for SoapySDR
Requires: %{name}-common = %{version}-%{release}

%description rfspace
The SoapyOsmo project provides SoapySDR hardware support modules using
drivers in gr-osmosdr. Using this, any program using SoapySDR to
interface to software defined radio hardware can make use of OsmoSDR,
Mirics SDR, and RFSpace SDR devices.

This package contains the RFSpace hardware support module.

%prep
%setup
%patch -p1

%build
%cmake \
       -DENABLE_OSMOSDR=ON \
       -DENABLE_RTL=OFF \
       -DUSE_OSMO_RTLSDR=OFF \
       -DENABLE_MIRI=ON \
       -DENABLE_HACKRF=OFF \
       -DUSE_OSMO_HACKRF=OFF \
       -DENABLE_AIRSPY=OFF \
       -DENABLE_RFSPACE=ON \
       -DUSE_OSMO_AIRSPY=OFF \
       -DENABLE_BLADERF=OFF \
       -DUSE_OSMO_BLADERF=OFF \
       -DENABLE_REDPITAYA=OFF \
       -DENABLE_FREESRP=OFF \
       -Wno-dev

%cmake_build

%install
%cmake_install

%files common
%doc Changelog.txt COPYING README.md
%_libdir/libSoapyOsmoSDR.so*

%files mirisdr
%_libdir/SoapySDR/modules0.8/libmiriSupport.so

%files osmosdr
%_libdir/SoapySDR/modules0.8/libosmosdrSupport.so

%files rfspace
%_libdir/SoapySDR/modules0.8/librfspaceSupport.so

%changelog
* Mon Jun 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.5-alt2
- Rebuild with libosmosdr enabled

* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus
