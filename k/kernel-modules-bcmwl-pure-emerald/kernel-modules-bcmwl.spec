%define module_name	bcmwl
%define module_version	5.100.82.38
%define module_release	alt1

%define kversion	2.6.39
%define kextraversion	%nil

%define krelease	alt6
%define flavour		pure-emerald

%define norm_version	%kversion

%define module_dir /lib/modules/%kversion%kextraversion-%flavour-%krelease/net

Summary: Modules for Broadcom-based WiFi .11a/b/g adapters
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132647.6
License: Proprietary
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://www.broadcom.com/support/802.11/linux_sta.php
BuildRequires: perl sharutils
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-source-%{module_name}_%{module_version} = %module_version
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86 x86_64
Patch1: 02-license.patch
Patch2: hybrid_multicast.patch

Patch91: wl-2.6.37-autoconf.patch
Patch92: wl-2.6.37-init_mutex.patch
Patch93: wl-2.6.37-license.patch
Patch94: wl-2.6.37-rfkill.patch

%description
These packages contain Broadcom's IEEE 802.11a/b/g/n hybrid Linux device
driver for use with Broadcom's BCM4311-, BCM431i2-,
BCM4321-, and BCM4322-based hardware.

NOTE: You must read the LICENSE.TXT file in the lib directory before
using this software.
%prep
rm -rf kernel-source-%{module_name}_%module_version-%module_version

tar -jxvf %kernel_src/kernel-source-%{module_name}_%module_version-%module_version.tar.bz2

%setup -D -T -n kernel-source-%{module_name}_%module_version-%module_version

%if "%kversion" >= "2.6.38"
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%else
%patch1 -p1
%if "%kversion" == "2.6.35"
%patch2 -p0
%endif
%endif

%build
. %_usrsrc/linux-%kversion%kextraversion-%flavour/gcc_version.inc
make -C %_usrsrc/linux-%kversion%kextraversion-%flavour SUBDIRS=`pwd` modules

%install
mkdir -p $RPM_BUILD_ROOT%module_dir/

. %_usrsrc/linux-%kversion%kextraversion-%flavour/gcc_version.inc
make -C %_usrsrc/linux-%kversion%kextraversion-%flavour INSTALL_MOD_PATH=%buildroot INSTALL_MOD_DIR=net SUBDIRS=`pwd`  modules_install 
%post
%post_kernel_modules %kversion%kextraversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion%kextraversion-%flavour-%krelease

%files
%module_dir

%changelog
* Thu Aug 04 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.6
- built for new kernel release

* Tue Jul 12 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.5
- built for 2.6.39-alt5

* Fri Jun 24 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.4
- built for 2.6.39-alt4

* Wed May 25 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.4.g4a7df24
- built for 2.6.39-alt4.g4a7df24

* Mon May 23 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.3
- built for 2.6.39-alt3

* Thu May 19 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.2
- built for 2.6.39-alt2

* Tue May 10 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.1.rc7
- built for rc7

* Wed May 04 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.1.rc6
- built for rc6

* Tue May 03 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.1.rc5.git7
- built for rc5-git7

* Wed Apr 27 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.1.rc5
- built for .39-rc5

* Tue Apr 19 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.1.rc4
- rc4

* Tue Apr 12 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.1.rc3
- 39.rc3

* Fri Apr 08 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.1.rc2.1
- rc2.1

* Fri Apr 08 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.1.rc2
build for kernel-image-pure-emerald-2.6.39-alt1.rc2

* Wed Apr 06 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132647.1.rc1
- build for kernel-image-pure-emerald-2.6.39-alt1.rc1

* Tue Mar 15 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132646.9
- build for kernel-image-pure-emerald-2.6.38-alt9

* Thu Mar 10 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132646.8.rc8.1
- build for kernel-image-pure-emerald-2.6.38-alt8.rc8

* Mon Mar 07 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132646.7.rc7.1
- built for alt7.rc7.1

* Tue Feb 22 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132646.6.rc6.1
- pure-emerald alt6.rc6.1

* Mon Feb 21 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132646.5.rc5.2
- pure-emerald alt5.rc5.2

* Fri Feb 18 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.38rc5
- built for gns-test 38rc5

* Wed Jan 26 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1.132645.3
- built for std-ng 2.6.37

* Wed Dec 08 2010 Michail Yakushin <silicium@altlinux.ru> 5.60.48.36-alt2.132643.9
- Build for kernel-image-std-def-2.6.35-alt9.

* Thu Sep 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.60.48.36-alt2
- patch for 2.6.35 added

* Mon Jun 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.60.48.36-alt1
- 5.60.48.36

* Thu Dec 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.10.91.9.3-alt1
- 5.10.91.9.3

* Thu Jul 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 5.10.91.9-alt3
- merged patches from debian

* Sat Jul 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 5.10.91.9-alt2
- fixed build for kernel 2.6.30

* Tue May 26 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.91.9-alt1
- 5.10.91.9 

* Tue Apr 21 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt2
- Fix module position (closes: 19603) 

* Wed Mar 25 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt1
- initial build 

