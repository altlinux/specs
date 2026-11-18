%define _unpackaged_files_terminate_build 1

Name: soapyaudio
Version: 0.2.0
Release: alt1

Summary: Audio device support for SoapySDR
License: MIT
Group: Engineering
Url: https://github.com/pothosware/SoapyAudio

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(SoapySDR)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(rtaudio)

%description
The SoapyAudio project provides a SoapySDR module for using Software
Defined Radio devices that are connected through audio interfaces.
It uses hamlib to provide control of tuning and other functions where
available.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc Changelog.txt LICENSE.txt README.md
%_libdir/SoapySDR/modules0.8/libaudioSupport.so

%changelog
* Wed Nov 18 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.0-alt1
- new version 0.2.0 (with rpmrb script)

* Sat Nov 14 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.2-alt1
- new version 0.1.2 (with rpmrb script)

* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus
