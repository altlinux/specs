%define _unpackaged_files_terminate_build 1

Name: soapybladerf
Version: 0.4.2
Release: alt1

Summary: bladeRF device support for SoapySDR
License: LGPL-2.1
Group: Engineering
Url: https://github.com/pothosware/SoapyBladeRF

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(SoapySDR)
BuildRequires: pkgconfig(libbladeRF)

%description
The Soapy bladeRF project provides a SoapySDR hardware support module.
Using this, any program using SoapySDR to interface to software
defined radio hardware can make use of the nuand bladeRF device to
transmit and receive.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc Changelog.txt LICENSE.LGPLv2.1 README.md
%_libdir/SoapySDR/modules0.8/libbladeRFSupport.so

%changelog
* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus
