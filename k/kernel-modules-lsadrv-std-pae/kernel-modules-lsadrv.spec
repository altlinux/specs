%define module_name             lsadrv
%define module_version          2.0.1
%define module_release          alt1

%define kversion	3.4.4
%define krelease	alt1
%define flavour		std-pae

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.197636.1

Summary: Linux Kernel drivers supporting Hitachi StarBoard interactive whiteboard.
License: GPL
Group: System/Kernel and hardware
URL: http://nixtech.ru/

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Patch1: ioctl_and_mutex.patch

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name-%module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86

%description
%module_name kernel driver for Linux.
This is usable for Hitachi StarBoard interactive whiteboard.
    FX-63/77(G)/82(WG) Wired
    FX-DUO-63/77/88W Wired
    FX-TRIO-77/77(S)/88W

This is module for your ALT Linux system.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%patch1 -p1

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make KERNEL_SRC=%_usrsrc/linux-%kversion-%flavour-%krelease \
    KERNELRELEASE=%kversion-%flavour-%krelease \
    %kversion-%flavour-%krelease/%module_name.ko

%install
%__install -d %buildroot/%module_dir
%__cp -a %kversion-%flavour-%krelease/%module_name.ko %buildroot/%module_dir/

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir

%changelog
* Mon Jun 25 2012 Anton Protopopov <aspsk@altlinux.org> 2.0.1-alt1.197636.1
- Build for kernel-image-std-pae-3.4.4-alt1.

* Fri Feb 4 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt1
- intial build for altlinux 
