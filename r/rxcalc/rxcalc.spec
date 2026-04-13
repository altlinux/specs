#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: rxcalc
Version: 20251015
Release: alt1
Summary: RxCalc is a calculator for the analysis of multi-stage receiver

Group: Engineering
License: GPL-3.0-or-later

URL: https://github.com/arhiv6/rxcalc
VCS: https://github.com/arhiv6/rxcalc

Source: %name-%version.tar

Buildrequires(pre): rpm-macros-cmake
Buildrequires: rpm-build-cmake
Buildrequires: gcc-c++
Buildrequires: qt6-base-devel
Buildrequires: qt6-svg-devel
Buildrequires: libcups-devel

%description
RxCalc is a calculator for the analysis of multi-stage receiver.
The software can calculate cascaded and system parameters: gain, noise,
sensitivity, input and output P1dB and IP3, noise floor,
spur-free dynamic range, MDS, SNR, and others.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Fri Apr 10 2026 Polina Poidenko <polipoki@altlinux.org> 20251015-alt1
- Initial build for Sisyphus.
