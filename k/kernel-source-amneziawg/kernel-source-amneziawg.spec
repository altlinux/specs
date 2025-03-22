%define _unpackaged_files_terminate_build 1

Name: kernel-source-amneziawg

Version: 1.0.20241112
Release: alt1

Summary: AmneziaWG kernel module source for Amnezia VPN based on WireGuard
License: GPLv2
Group: Development/Kernel
Url: https://amnezia.org
VCS: https://github.com/amnezia-vpn/amneziawg-linux-kernel-module
BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

%description
Kernel source package for AmneziaWG, a VPN kernel module based on WireGuard.

AmneziaWG provides secure, fast, and privacy-focused VPN connectivity as part
of the Amnezia VPN project.
This package includes the kernel module source code compatible with Linux
kernel version 6.12, provided as an out-of-tree module.

%prep
%setup

%build
mv %name %name-%version
%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Sat Mar 22 2025 Anton Farygin <rider@altlinux.com> 1.0.20241112-alt1
- initial build for ALT Linux

