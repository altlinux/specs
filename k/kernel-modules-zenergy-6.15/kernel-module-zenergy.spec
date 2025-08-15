%define module_name	zenergy
%define git f77293f
%define module_version	1.0
%define module_release	alt1.g%{git}

%define flavour		6.15

BuildRequires(pre): kernel-headers-modules-6.15
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: %module_name kernel module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: https://github.com/BoukeHaarsma23/zenergy
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

%requires_kimage

# x86/64 only
ExclusiveArch: %ix86 x86_64

%description
Based on AMD_ENERGY driver, but with some jiffies added so non-root users can
read it safely.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour M=`pwd` V=1 modules

%install
install -d %buildroot%module_dir
install *.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Fri Aug 15 2025 L.A. Kostis <lakostis@altlinux.org> 1.0.0-alt1.gf77293f
- Initial build for Sisyphus.
