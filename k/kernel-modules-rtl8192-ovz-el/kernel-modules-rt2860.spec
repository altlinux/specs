%define module_name	rtl8192
%define module_release	alt6
%define module_version  0018.1025

%define kversion	2.6.32
%define krelease	alt71
%define flavour		ovz-el

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.71

Summary: Kernel module for Realtek rtl8192 chipsets

License: GPLv2
Group: System/Kernel and hardware

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
Requires: firmware-rtl8192 
ExclusiveArch: %ix86 x86_64

Patch0: build-on-3.x.patch

%if "%kversion" >= "3.1.1"
Patch1: 3.1.1.patch
%endif

%description
This is a driver for the Realtek 819x 802.11 b/g/n chips.

These are modules for ALT Linux system.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2

%setup -D -T -n kernel-source-%module_name-%module_version

%patch0 -p1
%if "%kversion" >= "3.1.1"
%patch1 -p1
%endif

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%__make CC=gcc-$GCC_VERSION KSRC=%_usrsrc/linux-%kversion-%flavour

%install
mkdir -p %buildroot/%module_dir/extra/
install -m644 -D HAL/rtl8192/*.ko %buildroot/%module_dir/extra/

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir

%changelog
* Wed Jun 27 2012 Anton Protopopov <aspsk@altlinux.org> 0018.1025-alt6.132640.71
- Build for kernel-image-ovz-el-2.6.32-alt71.

* Tue Dec 20 2011 Anton Protopopov <aspsk@altlinux.org> 0018.1025-alt6
- Fix build on 3.x kernels, again

* Fri Dec 16 2011 Anton Protopopov <aspsk@altlinux.org> 0018.1025-alt5
- Fix build on 3.x kernels

* Tue Nov 15 2011 Anton Protopopov <aspsk@altlinux.org> 0018.1025-alt4
- Fix build with 3.1.1

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 0018.1025-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 0018.1025-alt2
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 0018.1025-alt1
- 0018.1025

* Tue Sep 14 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0017.0705-alt1
- 0017.0705 

* Fri May 28 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0015.0127-alt1
- initial build


