%define module_name	rts5139
%define git 8093764
%define module_version	1.05
%define module_release	alt3.g%{git}

%define flavour		6.16
%define karch %ix86 x86_64 aarch64
BuildRequires(pre): kernel-headers-modules-6.16
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: rts5139 kernel module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL-3
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: https://github.com/asymingt/rts5139.git
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version-alt2.g%{git}

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

%requires_kimage

Requires: %{module_name}-blacklist

ExclusiveArch: %karch

# due kernel upstream change 0ea163a18b17f9e0f8350bb348ae69c4a376be66
Patch: 6.15.patch

%description
This is a temporary fix for RTS5129/RTS5139 USB MMC card reader on Linux 3.16+
kernels.

PLEASE USE THIS DRIVER ONLY IF YOU SEE ERRORS IN LOGS! Upstream rtsx_ should
work just fine.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%patch -p1

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour M=`pwd` V=1 modules

%install
install -d %buildroot%module_dir
install %{module_name}.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Fri Aug 15 2025 L.A. Kostis <lakostis@altlinux.org> 1.05-alt3.g8093764
- GIT 8093764.
- Added patch for 6.15+ kernels.

* Mon Aug 19 2024 L.A. Kostis <lakostis@altlinux.org> 1.05-alt2.gfde2d2b
- Fix build with 6.10+ kernels.

* Mon Jun 17 2024 L.A. Kostis <lakostis@altlinux.org> 1.05-alt1.gfde2d2b
- Initial build for Sisyphus.
