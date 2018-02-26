%define module_name	acpi_call
%define module_version	0.1

%define module_release	alt2

%define kversion  	3.4.4	
%define krelease	alt1
%define flavour		std-def

%define base_arch %(echo %_target_cpu | sed 's/i.86/i386/;s/athlon/i386/')

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: acpi_call module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.197636.1
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: https://github.com/mkottman/acpi_call
BuildRequires(pre): rpm-build-kernel
BuildRequires: perl
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86 x86_64

Requires: %module_name

%description
This package contains acpi_call module

%prep
rm -rf %module_name-%{module_version}*
tar xf %kernel_src/%module_name-%module_version.tar.*
%setup -D -T -n %module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour-%krelease/gcc_version.inc
make KDIR=%_usrsrc/linux-%kversion-%flavour-%krelease

%install
%__mkdir_p %buildroot/%module_dir
%__install -pD -m644 %module_name.ko \
    %buildroot%module_dir/

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Mon Jun 25 2012 Anton Protopopov <aspsk@altlinux.org> 0.1-alt2.197636.1
- Build for kernel-image-std-def-3.4.4-alt1.

* Wed May 11 2011 Anton Protopopov <aspsk@altlinux.org> 0.1-alt2
- Use kernelarch macro for %%buildarch

* Tue Apr 19 2011 Mykola Grechukh <gns@altlinux.ru> 0.1-alt1.132647.1.rc4
- rc4

* Fri Apr 15 2011 Mykola Grechukh <gns@altlinux.ru> 0.1-alt1.132647.1.rc3
- first build for ALT Linux
