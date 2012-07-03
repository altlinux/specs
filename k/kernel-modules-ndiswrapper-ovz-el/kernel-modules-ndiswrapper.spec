%define module_name	ndiswrapper
%define module_version	1.57
%define module_release	alt1

%define kversion	2.6.32
%define krelease	alt71
%define flavour		ovz-el

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name


Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.71

Group: System/Kernel and hardware
Summary: %module_name kernel module allows you to use Windows WLAN card drivers

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>


Url: http://ndiswrapper.sourceforge.net
License: GPL

ExclusiveOS:	Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires:	kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires:	kernel-source-%module_name-%module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq:		coreutils
Prereq:         kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch:	%ix86 x86_64
Patch1: ndiswrapper_kernel_2.6.27.patch
Patch2: ndiswrapper-2.6.29.patch
Patch3: 2.6.35.patch
Patch4: 2.6.37.patch
Patch5: 2.6.38.patch

%if "%kversion" >= "3.1.1"
Patch6: 3.1.1.patch
%endif

%description
Some vendors do not release specifications of the hardware 
or provide a linux driver for their wireless network cards. 
The NdisWrapper project provides a linux kernel module that 
loads and runs Ndis (Windows network driver API) drivers 
supplied by the vendors.

This package contains only kernel module.

The userspace tools from NdisWrapper comes in a separate package 
(ndiswrapper...).


%prep

%__rm -rf kernel-source-%module_name-%module_version
tar -xvf %kernel_src/kernel-source-%module_name-%module_version.tar.gz
%setup -D -T -n %module_name-%module_version/driver

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc


%make_build KPSUB=26 KBUILD=%_usrsrc/linux-%kversion-%flavour KSRC=%_usrsrc/linux-%kversion-%flavour \
%ifarch %ix86
CC="gcc-$GCC_VERSION -m32"
%endif

%install
%__mkdir -p \
    %buildroot/%module_dir
    %__cp -a %module_name.ko %buildroot//%module_dir

%post
%post_kernel_modules %kversion-%flavour-%krelease
%postun
%postun_kernel_modules %kversion-%flavour-%krelease


%files
%dir %module_dir/
%module_dir/*

%changelog
* Wed Jun 27 2012 Anton Protopopov <aspsk@altlinux.org> 1.57-alt1.132640.71
- Build for kernel-image-ovz-el-2.6.32-alt71.

* Mon Jan 16 2012 Anton Protopopov <aspsk@altlinux.org> 1.57-alt1
- 1.57

* Mon Nov 14 2011 Anton Protopopov <aspsk@altlinux.org> 1.56-alt7
- Fix build with 3.1.1 kernel

* Thu May 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.56-alt6
- More fix by (GalaxyMaster) galaxy@openwall.com

* Wed May 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.56-alt5.1
- Thanks (GalaxyMaster) galaxy@openwall.com for previous fix

* Fri May 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.56-alt5
- Fixed for 2.6.37

* Thu Mar 24 2011 Anton Protopopov <aspsk@altlinux.org> 1.56-alt4
- Merge with boyarsh@

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 1.56-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 1.56-alt2
- technical

* Wed Mar 03 2010 Anton Protopopov <aspsk@altlinux.org> 1.56-alt1
- 1.56

* Thu Aug 06 2009 Michail Yakushin <silicium@altlinux.ru> 1.55-alt2
- alt2 

* Mon Jul 20 2009 Anton Protopopov <aspsk@altlinux.org> 1.55-alt1
- 1.55

* Thu Jan 29 2009 Michail Yakushin <silicium@altlinux.ru> 1.54-alt1
- 1.54 

* Thu Jul 03 2008 Michail Yakushin <silicium@altlinux.ru> 1.53-alt1
- 1.53 

* Mon Feb 11 2008 Michail Yakushin <silicium@altlinux.ru> 1.52-alt1
- 1.52

* Thu Dec 13 2007 Sergey Vlasov <vsu@altlinux.ru> 1.50-alt1
- Version 1.50.

* Wed Aug 08 2007 L.A. Kostis <lakostis@altlinux.ru> 1.47-alt1
- Version 1.47.

* Sun Jun 10 2007 L.A. Kostis <lakostis@altlinux.ru> 1.46-alt1
- Version 1.46.

* Sun Apr 22 2007 L.A. Kostis <lakostis@altlinux.ru> 1.42-alt1
- Version 1.42.

* Sat Feb 17 2007 L.A. Kostis <lakostis@altlinux.ru> 1.37-alt1
- Version 1.37.

* Mon Jan 29 2007 Sergey Vlasov <vsu@altlinux.ru> 1.31-alt2
- Removed unneeded "Prereq: modutils".

* Sat Dec 09 2006 L.A. Kostis <lakostis@altlinux.ru> 1.31-alt1
- Version 1.31.

* Fri Dec 01 2006 L.A. Kostis <lakostis@altlinux.org> 1.30-alt1
- Version 1.30.

* Wed Nov 29 2006 L.A. Kostis <lakostis@altlinux.org> 1.29-alt1
- Version 1.29.

* Sun Nov 19 2006 L.A. Kostis <lakostis@altlinux.org> 1.28-alt1
- Version 1.28.

* Mon Oct 23 2006 L.A. Kostis <lakostis@altlinux.org> 1.27-alt1
- Version 1.27.

* Sun Oct 22 2006 L.A. Kostis <lakostis@altlinux.org> 1.26-alt1
- Version 1.26.

* Wed Oct 11 2006 L.A. Kostis <lakostis@altlinux.org> 1.24-alt1
- Version 1.24.

* Fri Sep 22 2006 L.A. Kostis <lakostis@altlinux.org> 1.22-alt2
- add hack for %%ix86 cross-build on x86_64 host.

* Fri Aug 11 2006 L.A. Kostis <lakostis@altlinux.ru> 1.22-alt1
- Version 1.22.

* Sun Jul 09 2006 L.A. Kostis <lakostis@altlinux.ru> 1.16-alt1
- Imported Sisyphus .spec (from oddity@) to kernel cvs.
- Fix build process for 2.6 kernel (remove uname autoguessing).
- Remove ifdef's for 2.4 - it's not build here anymore due gcc-3.4 dependency.

* Mon Jul 18 2005 Ivan Zakharyaschev <imz@altlinux.ru> 1.1-alt1
- Initial revision.

