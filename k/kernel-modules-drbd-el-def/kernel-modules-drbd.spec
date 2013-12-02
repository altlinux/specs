%define module_name drbd
%define module_version 8.3.16
%define module_release alt1

%define flavour el-def
BuildRequires(pre): kernel-headers-modules-el-def

%setup_kernel_module %flavour

%define strip_mod_opts --strip-unneeded -R .comment
%define module_dir /lib/modules/%kversion-%flavour-%krelease/block

Summary: Linux kernel modules for DRBD
Name: kernel-modules-%module_name-%flavour
%define ksname %module_name
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2+
Group: System/Kernel and hardware
URL: http://www.%module_name.org
BuildRequires(pre): rpm-build-kernel
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq: kernel-image-%flavour = %kversion-%krelease
ExclusiveOS: Linux

BuildRequires: rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

ExclusiveArch: %karch

%description
This module is the kernel-dependant driver for DRBD.


%prep
%setup -c -T
tar -xf %_usrsrc/kernel/sources/%ksname-%module_version.tar*


%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build -C %ksname-%module_version/%module_name \
	KDIR=%_usrsrc/linux-%kversion-%flavour \
	V=1 \
	kbuild


%install
install -d -m 0755 %buildroot%module_dir
install -m 0644 %ksname-%module_version/%module_name/*.ko %buildroot%module_dir/
strip %strip_mod_opts %buildroot%module_dir/*.ko


%files
%module_dir


%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Dec 02 2013 Led <led@altlinux.ru> 8.3.16-alt1
- 8.3.16

* Thu Oct 25 2012 Led <led@altlinux.ru> 8.3.14-alt1
- 8.3.14

* Sun May 13 2012 Led <led@massivesolutions.co.uk> 8.3.13-cx1
- initial build
