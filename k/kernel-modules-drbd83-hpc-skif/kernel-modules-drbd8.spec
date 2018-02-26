# $Id: kernel-modules-drbd.spec,v 1.14 2007/11/13 11:12:49 vsu Exp $

%define module_name	drbd83
%define module_release	alt1
%define module_version	8.3.8

%define kversion	2.6.32
%define krelease	alt24
%define flavour		hpc-skif

%define base_arch %(echo %_target_cpu | sed 's/i.86/i386/;s/athlon/i386/')

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary:	Linux %{module_name} kernel modules for DRBD.
Name:		kernel-modules-%module_name-%flavour
Version:	%module_version
Release:	%module_release.132640.24
License:	GPL
Group:		System/Kernel and hardware

Packager:       Kernel Maintainer Team <kernel@packages.altlinux.org>

URL:		http://www.drbd.org
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name-%module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq:         kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch:	%ix86 x86_64

Patch1: kernel-image-el-smp-compliance.patch

%description
This module is the kernel-dependant driver for DRBD.  This is split out so
that multiple kernel driver versions can be installed, one for each
installed kernel.

%prep

%__rm -rf kernel-source-%module_name-%module_version

%__tar -jxvf %_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2

%setup -D -T -n kernel-source-%module_name-%module_version

%if "%kversion" >= "2.6.26"
%__subst 's,\&proc_root,NULL,g' *.c
%endif

%if "%flavour" == "el-smp"
%patch1 -p2
%endif

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make \
%ifarch %ix86
CC="gcc-$GCC_VERSION -m32" \
%else
CC=gcc-$GCC_VERSION \
%endif
KDIR=%_usrsrc/linux-%kversion-%flavour/

%install
%__mkdir -p \
    $RPM_BUILD_ROOT/%module_dir
%if "%kversion" <= "2.6.0"
%__cp -a drbd.o $RPM_BUILD_ROOT/%module_dir
%else
%__cp -a *.ko $RPM_BUILD_ROOT/%module_dir
%endif

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Wed Oct 20 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.8-alt1.132640.24
- Build for kernel-image-hpc-skif-2.6.32-alt24.

* Wed Aug 25 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 8.3.8-alt1
- 8.3.8

* Sat Feb 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 8.3.7-alt1
- 8.3.7

* Tue Oct 21 2008 L.A. Kostis <lakostis@altlinux.ru> 8.2.6-alt2
- Remove obsoleted &proc_root (only for kernel >= 2.6.26).

* Sun Sep 07 2008 Eugene Prokopiev <enp@altlinux.ru> 8.2.6-alt1
- build for 8.2.6

* Fri Feb 15 2008 Michail Yakushin <silicium@altlinux.ru> 8.0.10-alt1
- build for 8.0.10 
 
* Mon Jan 29 2007 Sergey Vlasov <vsu@altlinux.ru> 0.7.22-alt3
- Removed unneeded "Prereq: modutils".

* Tue Dec 05 2006 L.A. Kostis <lakostis@altlinux.org> 0.7.22-alt2
- Disable devfs support for 2.6 kernels.

* Sun Nov 19 2006 L.A. Kostis <lakostis@altlinux.org> 0.7.22-alt1
- 0.7.22.

* Fri Oct 27 2006 L.A. Kostis <lakostis@altlinux.org> 0.7.21-alt2
- add hack for %%ix86 cross-build on x86_64 host.

* Sun Sep 17 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.21-alt1
- 0.7.21.

* Sun Jul 09 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.20-alt1
- 0.7.20.

* Mon Jun 05 2006 LAKostis <lakostis at altlinux.ru> 0.7.19-alt1
- 0.7.19.

* Mon May 01 2006 LAKostis <lakostis at altlinux.ru> 0.7.18-alt1
- 0.7.18.

* Sun Apr 16 2006 LAKostis <lakostis at altlinux.ru> 0.7.17-alt1
- 0.7.17.

* Fri Feb 24 2006 LAKostis <lakostis at altlinux.ru> 0.7.16-alt1
- 0.7.16.

* Fri Jan 06 2006 LAKostis <lakostis at altlinux.ru> 0.7.15-alt1
- 0.7.15.

* Sun Dec 25 2005 Sergey Vlasov <vsu@altlinux.ru> 0.7.14-alt2
- Fix build for 2.4.x kernels.

* Sun Oct 30 2005 LAKostis <lakostis at altlinux.ru> 0.7.14-alt1
- initial build for Sisyphus

