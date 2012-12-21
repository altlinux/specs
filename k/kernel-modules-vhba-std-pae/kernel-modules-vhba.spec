%define module_name     vhba
%define module_version  20120422
%define module_release alt2

%define flavour         std-pae
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-pae

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/extra

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: VHBA virtual host bus adapter module
License: GPLv2
Group: System/Kernel and hardware

Url: http://cdemu.sourceforge.net/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source2: vhba.init

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel

BuildRequires: module-init-tools
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
Requires: vhba-udev-rules
ExclusiveArch: %karch

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
install -Dp -m0755 %SOURCE2 %buildroot%_initdir/%module_name

%preun
%preun_service %module_name
/sbin/service %module_name condstop ||:

%post
%post_service %module_name
/sbin/service %module_name condrestart ||:

%files
%module_dir
%attr(0755,root,root) %_initdir/%module_name

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 20120422-alt2
- new template

* Wed Apr 25 2012 Nazarov Denis <nenderus@altlinux.org> 20120422-alt1
- Version 20120422

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
