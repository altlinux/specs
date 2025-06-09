%define _unpackaged_files_terminate_build 1

Name: soapyairspy
Version: 0.2.0
Release: alt1

Summary: Airspy device support for SoapySDR
License: MIT
Group: Engineering
Url: https://github.com/pothosware/SoapyAirspy

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(SoapySDR)
BuildRequires: pkgconfig(libairspy)

%description
The Soapy Airspy project provides a SoapySDR hardware support module.
Using this, any program using SoapySDR to interface to software
defined radio hardware can make use of Airspy receivers.

%prep
%setup

%build
%cmake \
       -Wno-dev
%cmake_build

%install
%cmake_install

%files
%doc Changelog.txt LICENSE.txt README.md
%_libdir/SoapySDR/modules0.8/libairspySupport.so

%changelog
* Mon Jun 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
