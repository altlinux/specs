%define module_name             e1000e
%define module_version          1.6.3
%define module_release          alt1

%define kversion	2.6.32
%define krelease	alt71
%define flavour		ovz-el

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.71

Summary: E1000E Driver
License: GPL
Group: System/Kernel and hardware
URL: https://sourceforge.net/projects/e1000

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86 x86_64

%description
E1000E Linux kernel driver

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build -C src CFLAGS_EXTRA=-DCONFIG_E1000E_SEPARATE_TX_HANDLER \
                KSRC=%_usrsrc/linux-%kversion-%flavour KBUILD=%_usrsrc/linux-%kversion-%flavour

%install
%__install -d %buildroot/%module_dir
%__cp -a src/%module_name.ko %buildroot/%module_dir/

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir

%changelog
* Wed Jun 27 2012 Anton Protopopov <aspsk@altlinux.org> 1.6.3-alt1.132640.71
- Build for kernel-image-ovz-el-2.6.32-alt71.

* Tue Nov 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.3-alt1
- New version

* Mon Feb 21 2011 Anton Protopopov <aspsk@altlinux.org> 1.2.20-alt1
- Build for Sisyphus
