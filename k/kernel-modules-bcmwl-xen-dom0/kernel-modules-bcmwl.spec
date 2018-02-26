%define module_name	bcmwl
%define module_version	5.100.82.112
%define module_release	alt2

%define kversion	2.6.32
%define krelease	alt55
%define flavour		xen-dom0

%define norm_version	%kversion

%define module_dir /lib/modules/%kversion-%flavour-%krelease/net

Summary: Modules for Broadcom-based WiFi .11a/b/g adapters
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.55
License: Proprietary
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://www.broadcom.com/support/802.11/linux_sta.php
Patch1: bcmwl-build-kernel3.2.patch
BuildRequires: perl sharutils
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86 x86_64

%description
These packages contain Broadcom's IEEE 802.11a/b/g/n hybrid Linux device
driver for use with Broadcom's BCM4311-, BCM431i2-,
BCM4321-, and BCM4322-based hardware.

NOTE: You must read the LICENSE.TXT file in the lib directory before
using this software.
%prep
rm -rf kernel-source-%module_name-%module_version

tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2

%setup -D -T -n kernel-source-%module_name-%module_version
%if "%kversion" >= "3.2"
%patch1 -p2
%endif

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
make -C %_usrsrc/linux-%kversion-%flavour SUBDIRS=`pwd` modules

%install
mkdir -p $RPM_BUILD_ROOT%module_dir/

. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
make -C %_usrsrc/linux-%kversion-%flavour INSTALL_MOD_PATH=%buildroot INSTALL_MOD_DIR=net SUBDIRS=`pwd`  modules_install 

# blacklist several modules (see ALT bugs #26265, #26250)
mkdir -p %buildroot/%_sysconfdir/modprobe.d
cat > %buildroot/%_sysconfdir/modprobe.d/blacklist-bcm.conf << __EOF__
blacklist bcm43xx
blacklist ssb
blacklist b43
__EOF__

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir
%config(noreplace) %_sysconfdir/modprobe.d/blacklist-bcm.conf

%changelog
* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.100.82.112-alt2.132640.55
- Build for kernel-image-xen-dom0-2.6.32-alt55.

* Thu Jan 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.100.82.112-alt2
- fix to build with kernel 3.2

* Thu Jan 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.100.82.112-alt1
- 5.100.82.112

* Thu Sep 15 2011 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt6
- Add 'conf' extension to modprobe configuration file

* Wed Sep 14 2011 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt5
- Blacklist several modules (ALT 26265)

* Thu Feb 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.60.48.36-alt4
- 2.6.35 patch extended to infinity

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt2
- technical

* Wed Nov 10 2010 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt1
- 5.60.48.36

* Wed Jan 13 2010 Anton Protopopov <aspsk@altlinux.org> 5.10.91.9.3-alt1
- 5.10.91.9.3

* Tue May 26 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.91.9-alt1
- 5.10.91.9 

* Tue Apr 21 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt2
- Fix module position (closes: 19603) 

* Wed Mar 25 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt1
- initial build 

