%define _unpackaged_files_terminate_build 1
%define abiversion 2

Name: zxc
Version: 0.11.0
Release: alt1

Summary: High-performance asymmetric lossless compression
License: BSD-3-Clause
Group: Archiving/Compression
Vcs: https://github.com/hellobertrand/zxc
Url: https://github.com/hellobertrand/zxc

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%description
ZXC is a high-performance, lossless, asymmetric compression library optimized
for Content Delivery and Embedded Systems (Game Assets, Firmware, App Bundles).
It is designed to be "Write Once, Read Many" (WORM). Unlike codecs like LZ4, ZXC
trades compression speed (build-time) for maximum decompression throughput (run-time).

%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%package -n lib%name%abiversion
Summary: ZXC shared lib
Group: System/Libraries
%description -n lib%name%abiversion
ZXC shared lib

%package -n lib%name-devel
Summary: ZXC header, pkg-config and cmake files
Group: Development/C
%description -n lib%name-devel
ZXC header, pkg-config and cmake files

%files
%doc LICENSE README.md
%_bindir/%name

%files -n lib%name%abiversion
%_libdir/lib*

%files -n lib%name-devel
%_includedir/*
%_cmakedir/%name
%_pkgconfigdir/*

%changelog
* Fri Jun 05 2026 Vladislav Glinkin <smasher@altlinux.org> 0.11.0-alt1
- New version

* Fri Mar 27 2026 Vladislav Glinkin <smasher@altlinux.org> 0.9.1-alt1
- Initial build for ALT

