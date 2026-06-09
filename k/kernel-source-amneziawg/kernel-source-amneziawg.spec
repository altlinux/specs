%define _unpackaged_files_terminate_build 1

Name: kernel-source-amneziawg

Version: 1.0.20260329
Release: alt2

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

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 .

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Tue Jun 09 2026 Anton Farygin <rider@altlinux.org> 1.0.20260329-alt2
- 1.0.20260329 -> 1.0.20260329-2

* Tue Jun 09 2026 Anton Farygin <rider@altlinux.org> 1.0.20260329-alt1
- 1.0.20251104 -> 1.0.20260329

* Wed Jan 21 2026 Anton Farygin <rider@altlinux.org> 1.0.20251104-alt1
- 1.0.20251004 -> 1.0.20251104

* Tue Oct 07 2025 Anton Farygin <rider@altlinux.com> 1.0.20251004-alt1
- 1.0.20241112 - 1.0.20251004

* Sat Mar 22 2025 Anton Farygin <rider@altlinux.com> 1.0.20241112-alt1
- initial build for ALT Linux

