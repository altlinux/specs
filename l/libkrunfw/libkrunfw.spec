%define kernel linux-6.12.91
%define so_version 5

Name:    libkrunfw
Version: 5.5.0
Release: alt1

Summary: A dynamic library bundling the guest payload consumed by libkrun
License: LGPL-2.1-only AND GPL-2.0-only
Group:   System/Libraries
Url:     https://github.com/libkrun/libkrunfw
Vcs:     https://github.com/libkrun/libkrunfw.git

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: %kernel.tar.xz
	
BuildRequires:  git-core
BuildRequires:  python3-module-elftools
BuildRequires:  libssl-devel

BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  elfutils-devel
BuildRequires:  flex

%description
%summary.
	
%package devel
Summary: Development files for libkrunfw
Group: Development/Other
Requires: %name = %EVR
 
%description devel
%summary.

%prep
%setup
mkdir -p tarballs
cp %SOURCE1 tarballs

%build
%make_build --no-print-directory

%install
%makeinstall_std PREFIX=%_prefix

%files
%_libdir/libkrunfw.so.%so_version
%_libdir/libkrunfw.so.%so_version.*

%files devel
%_libdir/libkrunfw.so

%changelog
* Mon Sep 07 2026 Maxim Slipenko <maks1ms@altlinux.org> 5.5.0-alt1
- Initial build for Sisyphus
