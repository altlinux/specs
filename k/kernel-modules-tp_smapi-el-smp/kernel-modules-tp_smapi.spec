%define module_name             tp_smapi
%define module_version          0.40
%define module_release          alt2

%define kversion	2.6.32
%define krelease	alt38
%define flavour		el-smp

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.38

Summary: IBM ThinkPad SMAPI Driver
License: GPL
Group: System/Kernel and hardware
URL: http://tpctl.sourceforge.net

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Patch: tp_smapi-0.40-patch_for_2.6.37.patch 
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
ExclusiveArch: %ix86 x86_64

%description
ThinkPad laptops include a proprietary interface called SMAPI BIOS
(System Management Application Program Interface) which provides some
hardware control functionality that is not accessible by other means.

This driver exposes some features of the SMAPI BIOS through a sysfs
interface. It is suitable for newer models, on which SMAPI is invoked
through IO port writes. Older models use a different SMAPI interface;
for those, try the "thinkpad" module.

These are modules for your ALT Linux system.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%if "%kversion" >= "2.6.37"
%patch -p1 
%endif

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build KSRC=%_usrsrc/linux-%kversion-%flavour \
	KBUILD=%_usrsrc/linux-%kversion-%flavour \
	HDAPS=1

%install
%__install -d %buildroot/%module_dir
%__cp -a {thinkpad_ec,tp_smapi,hdaps}.ko %buildroot/%module_dir/

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir
%exclude %module_dir/hdaps.ko
%doc README CHANGES

%changelog
* Wed Jul 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.40-alt2.132640.38
- Build for kernel-image-el-smp-2.6.32-alt38.

* Thu Feb 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.40-alt2
- don't pack hdaps.ko

* Fri Feb 18 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.40-alt1
- new version (0.40), fix build with 2.6.37

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 0.37-alt4
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 0.37-alt3
- technical

* Sat Nov 01 2008 Michail Yakushin <silicium@altlinux.ru> 0.37-alt2
- fix build for 2.6.27

* Mon Jun 02 2008 Michail Yakushin <silicium@altlinux.ru> 0.37-alt1
- new version (0.37)

* Tue Feb 12 2008 Michail Yakushin <silicium@altlinux.ru> 0.36-alt1
- new version (0.36)

* Sun Jan 20 2008 L.A. Kostis <lakostis@altlinux.org> 0.33-alt1
- new version (0.33).

* Tue Aug 07 2007 Dmitry V. Levin <ldv@altlinux.org> 0.30-alt4
- Raised module release number to fix package update.

* Sun Jul 08 2007 L.A. Kostis <lakostis@altlinux.ru> 0.30-alt3.1
- fix whitespaces.

* Mon Feb 19 2007 Grigory Batalov <bga@altlinux.ru> 0.30-alt3
- Build with HDAPS (bug #10738, raorn@).

* Mon Jan 29 2007 Sergey Vlasov <vsu@altlinux.ru> 0.30-alt2
- Removed unneeded "Prereq: modutils".

* Sat Jan 27 2007 Grigory Batalov <bga@altlinux.ru> 0.30-alt1
- New upstream release.

* Fri Apr 28 2006 Grigory Batalov <bga@altlinux.ru> 0.19-alt1
- Initial ALTLinux release.
