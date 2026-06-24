%define _unpackaged_files_terminate_build 1

Name: soapyuhd
Version: 0.4.1
Release: alt2

Summary: SoapySDR device support for libuhd
License: GPL-3.0
Group: Engineering
Url: https://github.com/pothosware/SoapyUHD

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(SoapySDR)
BuildRequires: uhd-devel

ExcludeArch: i586

%description
Both SoapySDR and the Universal Hardware Driver by Ettus Research
projects provide libraries to access various software defined radio
hardware through a common interface.

This UHD module makes all SoapySDR devices available to applications
using libuhd. An interface in the other direction is available in the
soapysdr-module-uhd package.

%prep
%setup
%patch -p1

%build
%cmake \
	   -Wno-dev
%cmake_build

%install
%cmake_install

%files
%doc Changelog.txt COPYING README.md
%_libdir/SoapySDR/modules0.8/*.so
%_libdir/uhd/modules/libsoapySupport.so

%changelog
* Mon Jun 15 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.1-alt2
- Fix build with uhd-4.10.

* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
