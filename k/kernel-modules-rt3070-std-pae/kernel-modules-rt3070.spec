%define module_name	rt3070
%define module_release	alt3
%define module_version	2.5.0.2

%define kversion	3.4.4
%define krelease	alt1
%define flavour		std-pae

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.197636.1

Summary: Kernel module for Ralink rt3070 chipset

License: Distributable
Group: System/Kernel and hardware
Url: http://www.ralinktech.com/ralink/Home/Support/Linux.html

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86

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
%__make CC=gcc-$GCC_VERSION LINUX_SRC=%_usrsrc/linux-%kversion-%flavour

%install
install -m644 -D os/linux/%{module_name}sta.ko %buildroot/%module_dir/%{module_name}sta.ko

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir

%changelog
* Mon Jun 25 2012 Anton Protopopov <aspsk@altlinux.org> 2.5.0.2-alt3.197636.1
- Build for kernel-image-std-pae-3.4.4-alt1.

* Mon Feb 06 2012 Anton Protopopov <aspsk@altlinux.org> 2.5.0.2-alt3
- Fix build with 3+ kernels

* Tue Sep 06 2011 Andriy Stepanov <stanv@altlinux.ru> 2.5.0.2-alt2
- Fix module location.

* Fri Jul 22 2011 Timur Aitov <timonbl4@altlinux.org> 2.5.0.2-alt1
- Initial build for ALT Linux

