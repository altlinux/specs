%define module_name	rtl8168
%define module_version	8.026.00
%define module_release	alt1

%define kversion	2.6.32
%define krelease	alt55
%define flavour		xen-dom0

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/drivers/net

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.55

Summary: Linux driver for RealTek Ethernet controllers
License: GPLv2+
Group: System/Kernel and hardware

URL: http://www.realtek.com/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %ix86 x86_64

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

%description
RTL8168 is the Linux device driver released for RealTek RTL8168B/8111B,
RTL8168C/8111C, RTL8168CP/8111CP, RTL8168D/8111D, and RTL8168DP/8111DP
Gigabit Ethernet controllers with PCI-Express interface.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build KERNELDIR=%_usrsrc/linux-%kversion-%flavour modules

%install
install -Dp -m0744 src/r8168.ko %buildroot/%module_dir/r8168.ko

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir

%changelog
* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 8.026.00-alt1.132640.55
- Build for kernel-image-xen-dom0-2.6.32-alt55.

* Sat Oct 29 2011 Nazarov Denis <nenderus@altlinux.org> 8.026.00-alt1
- Version 8.026.00

* Fri Aug 26 2011 Nazarov Denis <nenderus@altlinux.org> 8.025.00-alt1
- Version 8.025.00

* Sun May 29 2011 Nazarov Denis <nenderus@altlinux.org> 8.024.00-alt1
- Version 8.024.00

* Sat Apr 23 2011 Nazarov Denis <nenderus@altlinux.org> 8.023.00-alt1
- Version 8.023.00

* Sun Mar 27 2011 Nazarov Denis <nenderus@altlinux.org> 8.022.00-alt1
- Version 8.022.00

* Tue Feb 01 2011 Nazarov Denis <nenderus@altlinux.org> 8.021.00-alt1
- Version 8.021.00

* Mon Jan 03 2011 Nazarov Denis <nenderus@altlinux.org> 8.020.00-alt1
- Initial build for ALT Linux
