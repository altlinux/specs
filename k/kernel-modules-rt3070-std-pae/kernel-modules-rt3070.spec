%define module_name	rt3070
%define module_release alt4
%define module_version	2.5.0.2

%define flavour		std-pae
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-pae

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Kernel module for Ralink rt3070 chipset

License: Distributable
Group: System/Kernel and hardware
Url: http://www.ralinktech.com/ralink/Home/Support/Linux.html

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

Patch1: fix-build-with-modern-kernels.patch

%description
This is a driver for the Ralink RT3070 802.11 b/g/n chip.

These are modules for ALT Linux system.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2

%setup -D -T -n kernel-source-%module_name-%module_version

%patch1 -p1

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
make CC=gcc-$GCC_VERSION LINUX_SRC=%_usrsrc/linux-%kversion-%flavour

%install
install -m644 -D os/linux/%{module_name}sta.ko %buildroot/%module_dir/%{module_name}sta.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.5.0.2-alt4
- new template

* Mon Feb 06 2012 Anton Protopopov <aspsk@altlinux.org> 2.5.0.2-alt3
- Fix build with 3+ kernels

* Tue Sep 06 2011 Andriy Stepanov <stanv@altlinux.ru> 2.5.0.2-alt2
- Fix module location.

* Fri Jul 22 2011 Timur Aitov <timonbl4@altlinux.org> 2.5.0.2-alt1
- Initial build for ALT Linux

