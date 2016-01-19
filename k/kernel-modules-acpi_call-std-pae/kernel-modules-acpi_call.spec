%define module_name	acpi_call
%define module_version	0.1

%define module_release alt4

%define flavour		std-pae
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-pae

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: acpi_call module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: https://github.com/mkottman/acpi_call
BuildRequires(pre): rpm-build-kernel
BuildRequires: perl
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

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
mkdir -p %buildroot/%module_dir
install -pD -m644 %module_name.ko \
    %buildroot%module_dir/

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt3
- new template

* Wed May 11 2011 Anton Protopopov <aspsk@altlinux.org> 0.1-alt2
- Use kernelarch macro for %%buildarch

* Tue Apr 19 2011 Mykola Grechukh <gns@altlinux.ru> 0.1-alt1.132647.1.rc4
- rc4

* Fri Apr 15 2011 Mykola Grechukh <gns@altlinux.ru> 0.1-alt1.132647.1.rc3
- first build for ALT Linux
