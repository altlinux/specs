%define module_name     vhba
%define module_version  20110915
%define module_release  alt4

%define kversion        2.6.32
%define krelease        alt55
%define flavour         xen-dom0

%define module_dir /lib/modules/%kversion-%flavour-%krelease/extra

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.55

Summary: VHBA virtual host bus adapter module
License: GPLv2
Group: System/Kernel and hardware

URL: http://cdemu.sourceforge.net/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source2: vhba.init

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
Requires: vhba-udev-rules
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
install -Dp -m0755 %SOURCE2 %buildroot%_initrddir/%module_name

%preun
%preun_service %module_name
/sbin/service %module_name condstop ||:

%post
%post_kernel_modules %kversion-%flavour-%krelease
%post_service %module_name
/sbin/service %module_name condrestart ||:
  
%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir
%attr(0755,root,root) %_initrddir/%module_name

%changelog
* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 20110915-alt4.132640.55
- Build for kernel-image-xen-dom0-2.6.32-alt55.

* Tue Oct 11 2011 Anton Protopopov <aspsk@altlinux.org> 20110915-alt4
- Don't pack 60-vhba.rules, use vhba-udev-rules package (ALT 26335)

* Tue Sep 20 2011 Anton Protopopov <aspsk@altlinux.org> 20110915-alt3
- Technical

* Tue Sep 20 2011 Nazarov Denis <nenderus@altlinux.org> 20110915-alt2
- Add init script

* Sun Sep 18 2011 Nazarov Denis <nenderus@altlinux.org> 20110915-alt1
- Version 20110915

* Thu Jun 09 2011 Nazarov Denis <nenderus@altlinux.org> 1.2.1.20110416-alt1
- Version 1.2.1.20110416

* Sat Nov 20 2010 Nazarov Denis <nenderus@altlinux.org> 1.2.1.20100822-alt1
- Initial build for ALT Linux
