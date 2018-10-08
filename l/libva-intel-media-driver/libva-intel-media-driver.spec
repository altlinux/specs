Name: libva-intel-media-driver
Version: 18.3.0
Release: alt1

Summary: Intel(R) Media Driver for VAAPI
License: MIT
Group: System/Libraries
Url: https://github.com/intel/media-driver/

Source: %name-%version.tar

BuildRequires: libdrm-devel libX11-devel libGL-devel libEGL-devel gcc-c++ libpciaccess-devel
BuildRequires: libva-devel >= 2.3.0
BuildRequires: cmake rpm-macros-cmake
BuildRequires: intel-gmmlib-devel >= 18.3.0
BuildRequires(pre): rpm-build-ubt
ExclusiveArch: x86_64

%description
The Intel(R) Media Driver for VAAPI is a new VA-API (Video Acceleration API) user mode driver
supporting hardware accelerated decoding, encoding, and video post processing for GEN based graphics hardware.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE.md README.md
%_libdir/dri/*.so
%_libdir/igfxcmrt64.so

%changelog
* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 18.3.0-alt1
- first build for ALT

