%define module_name	emlog
%define module_release	alt2
%define module_version	0.51

%define kversion	3.4.4
%define krelease	alt1
%define flavour		std-def

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.197636.1

Summary: emlog is a kernel module used in Embedded Linux for logging purposes

License: Distributable
Group: System/Kernel and hardware
Url: http://www.linuxconsulting.ro/emlog/

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
ExclusiveArch: %ix86 x86_64

%description
emlog implements a circular buffer on a character device and can be used
instead of normal log files to keep loggin to 0 disk space. Buffer size can be
adjusted when creating the character device. Multiple log files (character
devices) can be created and used.

These are modules for ALT Linux system.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2

%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%__make CC=gcc-$GCC_VERSION KDIR=%_usrsrc/linux-%kversion-%flavour

%install
install -m644 -D %{module_name}.ko %buildroot/%module_dir/%{module_name}.ko

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir

%changelog
* Mon Jun 25 2012 Anton Protopopov <aspsk@altlinux.org> 0.51-alt2.197636.1
- Build for kernel-image-std-def-3.4.4-alt1.

* Mon Sep 06 2011 Andriy Stepanov <stanv@altlinux.ru> 0.51-alt2
- Fix summary.

* Mon Sep 05 2011 Timur Aitov <timonbl4@altlinux.org> 0.51-alt1
- Initial build for ALT Linux

