%define module_name     vhba
%define module_version  20110915
%define module_release  alt1

%define kversion        2.6.39
%define krelease        alt6
%define flavour         pure-emerald

%define module_dir /lib/modules/%kversion-%flavour-%krelease/extra

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132647.6

Summary: VHBA virtual host bus adapter module
License: GPLv2
Group: System/Kernel and hardware

URL: http://cdemu.sourceforge.net/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source1: 60-%module_name.rules

Patch1: vhba-makefile-werror.patch
Patch2: vhba-patch-scsi_qcmd.patch

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel

BuildRequires: module-init-tools
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
VHBA kernel module, a virtual SCSI host bus adapter used by CDEmu daemon from
userspace-cdemu suite.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build KDIR=%_usrsrc/linux-%kversion-%flavour

%install
install -d %buildroot/%module_dir
cp -a %module_name.ko %buildroot/%module_dir/
install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/udev/rules.d/60-%module_name.rules

%post
%post_kernel_modules %kversion-%flavour-%krelease
 
%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir
%config %_sysconfdir/udev/rules.d/60-%module_name.rules

%changelog
* Wed Sep 28 2011 Mykola Grechukh <gns@altlinux.ru> 20110915-alt1.132647.6
- new version

* Thu Aug 04 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20110416-alt1.132647.6
- built for new kernel release

* Tue Jul 12 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20110416-alt1.132647.5
- built for 2.6.39-alt5

* Wed Jun 29 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20110416-alt1.132647.4
- updated for sisyphus vhba sources (1.2.1.20110416)

* Fri Jun 24 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt4.g4a7df24.132647.4
- built for 2.6.39-alt4

* Wed May 25 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt4.g4a7df24.132647.4.g4a7df24
- built for 2.6.39-alt4.g4a7df24

* Mon May 23 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt3.132647.3
- built for 2.6.39-alt3

* Thu May 19 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt3.132647.2
- built for 2.6.39-alt2

* Tue May 10 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt3.132647.1.rc7
- built for rc7

* Wed May 04 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt3.132647.1.rc6
- built for rc6

* Tue May 03 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt3.132647.1.rc5.git7
- built for rc5-git7

* Wed Apr 27 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt3.132647.1.rc5
- built for .39-rc5

* Tue Apr 19 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt3.132647.1.rc4
- rc4

* Tue Apr 12 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt3.132647.1.rc3
- 39.rc3

* Tue Apr 12 2011 Mykola Grechukh <gns@altlinux.ru> 1.2.1.20100822-alt3.132647.1.rc2.1
- Build for kernel-image-pure-emerald-2.6.39-alt1.rc2.1.

* Sat Nov 20 2010 Nazarov Denis <nenderus@altlinux.org> 1.2.1.20100822-alt1
- Initial build for ALT Linux

