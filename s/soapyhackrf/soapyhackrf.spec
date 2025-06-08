%define _unpackaged_files_terminate_build 1

Name: soapyhackrf
Version: 0.3.4
Release: alt1

Summary: HackRF device support for SoapySDR
License: MIT
Group: Engineering
Url: https://github.com/pothosware/SoapyHackRF

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(SoapySDR)
BuildRequires: pkgconfig(libhackrf)

%description
The Soapy HackRF project provides a SoapySDR hardware support module.
Using this, any program using SoapySDR to interface to software
defined radio hardware can make use of the open source HackRF device
to transmit and receive.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc Changelog.txt LICENSE README.md
%_libdir/SoapySDR/modules0.8/*.so

%changelog
* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus
