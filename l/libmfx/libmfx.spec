%def_without tools

%define sover 1
Name: libmfx
Version: 22.5.4
Release: alt1

Summary: The Intel Media SDK

License: MIT
Group: System/Libraries
Url: https://github.com/Intel-Media-SDK/MediaSDK

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Intel-Media-SDK/MediaSDK/archive/intel-mediasdk-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(wayland-client)

ExclusiveArch: x86_64

%description
The Intel Media SDK provides a plain C API to access hardware-accelerated
video decode, encode and filtering on Intel Gen graphics hardware
platforms. The implementation is written in C++11, with parts in C-for-Media
(CM).

%package devel
Summary: Development files Intel Media SDK
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the development headers and pkgconfig files for
the Intel Media SDK.

%prep
%setup

%build
%cmake_insource \
    -DENABLE_X11_DRI3:BOOL=ON \
    -DENABLE_WAYLAND:BOOL=ON \
    -DENABLE_TEXTLOG:BOOL=ON \
    -DENABLE_STAT:BOOL=ON \
    -DBUILD_TESTS:BOOL=OFF \
%if_with tools
    -DBUILD_TOOLS:BOOL=ON \
%else
    -DBUILD_SAMPLES:BOOL=OFF \
    -DBUILD_TOOLS:BOOL=OFF \
%endif
    -DENABLE_ITT:BOOL=OFF \
    -DBUILD_KERNELS:BOOL=OFF \
    %nil
%make_build

%install
%makeinstall_std

%files
%doc CHANGELOG.md CODEOWNERS README.rst
%if_with tools
%_bindir/asg-hevc
%_bindir/hevc_fei_extracto
%_bindir/mfx-tracer-config
%endif
%_libdir/libmfx.so.*
%_libdir/libmfxhw64.so.*
%if_with tools
%_libdir/libmfx-tracer.so.*
%endif
%dir %_libdir/mfx/
%_libdir/mfx/libmfx_*_hw64.so
%dir %_datadir/mfx/
%_datadir/mfx/plugins.cfg

%files devel
%_includedir/mfx/
%_libdir/libmfx.so
%_libdir/libmfxhw64.so
%if_with tools
%_libdir/libmfx-tracer.so
%endif
%_pkgconfigdir/*.pc

%changelog
* Fri Mar 03 2023 Vitaly Lipatov <lav@altlinux.ru> 22.5.4-alt1
- initial build for ALT Sisyphus
