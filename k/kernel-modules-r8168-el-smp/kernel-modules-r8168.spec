%define module_name	r8168
%define module_version	8.035.00
%define module_release	alt2

%define flavour		el-smp

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/drivers/net

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Linux driver for RealTek Ethernet controllers
License: GPLv2+
Group: System/Kernel and hardware

URL: http://www.realtek.com/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %karch

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-el-smp

BuildRequires: module-init-tools
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease

Requires: r8168-blacklist
 
Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release kernel-modules-rtl8168-%flavour
Obsoletes: kernel-modules-rtl8168-%flavour
Conflicts: kernel-modules-rtl8168-%flavour
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release kernel-modules-rtl8168-%kversion-%flavour-%krelease
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release kernel-modules-rtl8168-%kversion-%flavour-%krelease

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
install -Dp -m0744 src/%module_name.ko %buildroot/%module_dir/%module_name.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Wed Jan 30 2013 Nazarov Denis <nenderus@altlinux.org> 8.035.00-alt2
- New template

* Tue Jan 29 2013 Nazarov Denis <nenderus@altlinux.org> 8.035.00-alt1
- Version 8.035.00

* Sat Dec 03 2011 Nazarov Denis <nenderus@altlinux.org> 8.027.00-alt2
- Add provides and obsoletes

* Fri Dec 02 2011 Nazarov Denis <nenderus@altlinux.org> 8.027.00-alt1
- Version 8.027.00

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
