%define _unpackaged_files_terminate_build 1

Name: soapyredpitaya
Version: 0.1.1
Release: alt1

Summary: RedPitaya device support for SoapySDR
License: GPL-3.0
Group: Engineering
Url: https://github.com/pothosware/SoapyRedPitaya

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(SoapySDR)

%description
The Soapy Red Pitaya project provides a SoapySDR hardware support module.
Using this, any program using SoapySDR to interface to software
defined radio hardware can make use of the Red Pitaya HF channels to
transmit and receive.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc Changelog.txt COPYING README.md
%_libdir/SoapySDR/modules0.8/libRedPitaya.so

%changelog
* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus
