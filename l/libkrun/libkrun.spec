%define _unpackaged_files_terminate_build 1
%define so_version 1

Name:    libkrun
Version: 1.19.4
Release: alt1
Summary: Dynamic library providing Virtualization-based process isolation capabilities
License: Apache-2.0
Group:   System/Libraries
Url:     https://github.com/libkrun/libkrun
Vcs:     https://github.com/libkrun/libkrun.git

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

BuildRequires: glibc-devel-static
BuildRequires: binutils
BuildRequires: libcap-ng-devel
BuildRequires: libepoxy-devel
BuildRequires: libdrm-devel
BuildRequires: libvirglrenderer-devel
BuildRequires: clang-devel
BuildRequires: libssl-devel
BuildRequires: pipewire-libs-devel
BuildRequires: libcurl-devel

Requires: libkrunfw

%description
%summary

%package devel
Summary: Development files for libkrun
Group: Development/Other
Requires: %name = %EVR
 
%description devel
%summary.

%prep
%setup -a1
echo "" >> .cargo/config.toml
%rust_prep

%build
%make_build BLK=1 NET=1 GPU=1 SND=1 PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%files
%_libdir/libkrun.so.%so_version
%_libdir/libkrun.so.%so_version.*

%files devel
%_libdir/libkrun.so
%_libdir/pkgconfig/libkrun.pc
%_includedir/libkrun.h
%_includedir/libkrun_display.h
%_includedir/libkrun_input.h

%changelog
* Mon Sep 07 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.19.4-alt1
- Initial build for Sisyphus
