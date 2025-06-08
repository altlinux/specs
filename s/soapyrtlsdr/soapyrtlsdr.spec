%define _unpackaged_files_terminate_build 1

Name: soapyrtlsdr
Version: 0.3.3
Release: alt1

Summary: RTL-SDR device support for SoapySDR
License: MIT
Group: Engineering
Url: https://github.com/pothosware/SoapyRTLSDR

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(librtlsdr)
BuildRequires: pkgconfig(SoapySDR)

%description
The Soapy RTL-SDR project provides a SoapySDR hardware support module.
Using this, any program using SoapySDR to interface to software
defined radio hardware can make use of low cost DVB-T/DAB+ USB dongles
based on the Realtek RTL2832U chip as receivers.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc Changelog.txt LICENSE.txt README.md
%_libdir/SoapySDR/modules0.8/librtlsdrSupport.so

%changelog
* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus
