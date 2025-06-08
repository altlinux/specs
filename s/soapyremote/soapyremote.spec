%define _unpackaged_files_terminate_build 1

Name: soapyremote
Version: 0.5.2
Release: alt1

Summary: Use SoapySDR devices over network
License: BSL-1.0
Group: Engineering
Url: https://github.com/pothosware/SoapyRemote

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(SoapySDR)

%description
The SoapyRemote project provides a client module and a server that make it
possible on the client side to list and access hardware supported by SoapySDR
modules on the server as if they were local module

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc Changelog.txt LICENSE_1_0.txt README.md
%_libdir/SoapySDR/modules0.8/*.so
%_bindir/SoapySDRServer
%_man1dir/SoapySDRServer.1.*
%_unitdir/SoapySDRServer.service
%_sysctldir/SoapySDRServer.conf

%changelog
* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus
