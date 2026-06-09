%define module_name	amneziawg
%define module_version	1.0.20260329
%define module_release	alt1

%define flavour		6.18
%define karch %ix86 x86_64 aarch64
BuildRequires(pre): kernel-headers-modules-6.18
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: AmneziaWG is a fast, modern, secure VPN tunnel module for Linux kernel
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

URL: https://amnezia.org
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %karch 

%description
AmneziaWG Kernel Module.

AmneziaWG is a streamlined, high-performance kernel module providing VPN
functionality based on WireGuard technology. Leveraging cutting-edge
cryptographic techniques, it offers exceptional speed, security, and simplicity,
making it suitable for various use cases-from embedded systems to large-scale
server deployments. Designed specifically as a robust kernel-level integration
for AmneziaVPN, it simplifies deployment and enhances reliability compared to
traditional VPN implementations like IPSec or OpenVPN. Although actively
evolving, AmneziaWG already stands out as a secure, user-friendly,
and efficient solution within modern VPN infrastructures.

%prep
rm -rf kernel-source-%module_name-%module_version
mkdir kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2 -C kernel-source-%module_name-%module_version
%setup -D -T -n kernel-source-%module_name-%module_version/src

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules M=`pwd`

%install
install -d %buildroot%module_dir
install amneziawg.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Jun 09 2026 Anton Farygin <rider@altlinux.org> 1.0.20260329-alt1
- 1.0.20251104 -> 1.0.20260329

* Wed Jan 21 2026 Anton Farygin <rider@altlinux.org> 1.0.20251104-alt1
- 1.0.20251004 -> 1.0.20251104

* Tue Oct 07 2025 Anton Farygin <rider@altlinux.com> 1.0.20251004-alt1
- 1.0.20241112 -> 1.0.20251004

* Sat Mar 22 2025 Anton Farygin <rider@altlinux.com> 1.0.20241112-alt1.%kcode.%kbuildrelease
- Initial build for ALT Linux.
