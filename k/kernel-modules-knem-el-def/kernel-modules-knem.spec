%define module_name knem
%define module_version 1.1.0
%define module_release alt1

%define flavour el-def
BuildRequires(pre): kernel-headers-modules-el-def

%setup_kernel_module %flavour

%define strip_mod_opts --strip-unneeded -R .comment
%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Linux kernel modules for KNEM
Name: kernel-modules-%module_name-%flavour
%define ksname %module_name
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: BSD
Group: System/Kernel and hardware
URL: http://runtime.bordeaux.inria.fr/%module_name
BuildRequires(pre): rpm-build-kernel
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release
Prereq: kernel-image-%flavour = %kversion-%krelease
ExclusiveOS: Linux

BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

ExclusiveArch: %karch

%description
This module is the kernel-dependant driver for KNEM.


%prep
%setup -c -T
tar -xf %_usrsrc/kernel/sources/%ksname-%module_version.tar*


%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
cd %ksname-%module_version
./check_kernel_headers.sh %{module_name}_checks.h \
	%_usrsrc/linux-%kversion-%flavour \
	%_usrsrc/linux-%kversion-%flavour \
	"%kversion"
%make_build -C %_usrsrc/linux-%kversion-%flavour \
	M=$PWD V=1 \
	EXTRA_CFLAGS="-include $PWD/%{module_name}_config.h -include $PWD/%{module_name}_checks.h" \
	modules


%install
install -d -m 0755 %buildroot%module_dir
install -m 0644 %ksname-%module_version/*.ko %buildroot%module_dir/

%{!?_enable_debug:strip %strip_mod_opts %buildroot%module_dir/*.ko}


%files
%module_dir


%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Dec 03 2013 Led <led@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon May 14 2012 Led <led@massivesolutions.co.uk> 0.9.8-cx1
- initial build
