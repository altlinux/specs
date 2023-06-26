%define module_name      i40e
%define module_version   2.22.20
%define module_release   alt1

%define flavour          std-def
%define karch            x86_64 aarch64

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/updates
%add_verify_elf_skiplist %module_dir/*

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Intel(R) 10GbE PCI Express Linux Network Driver
License: GPLv2
Group: System/Kernel and hardware
Url: http://www.intel.com/network/connectivity/products/server_adapters.htm

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name


Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
This package contains the Intel(R) 40-10 Gigabit Ethernet Connection Network Driver.

%prep
rm -rf %module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
pushd src
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build KSRC=%_usrsrc/linux-%kversion-%flavour
popd

%install
install -Dp -m600 src/%module_name.ko %buildroot/%module_dir/%module_name.ko
if [ ! -e "%_usrsrc/linux-%kversion-%flavour/include/linux/auxiliary_bus.h" ]; then
        install -Dp -m600 src/intel_auxiliary.ko %buildroot/%module_dir/intel_auxiliary.ko
fi

%files
%module_dir/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Jun 26 2023 Anton Farygin <rider@altlinux.ru> 2.22.20-alt1
- 2.22.20

* Sat May 27 2023 Anton Farygin <rider@altlinux.ru> 2.22.18-alt2
- auxiliary.ko renamed to intel_auxiliary.ko in upstream (fix build for 5.10)

* Wed Apr 26 2023 Alexey Shabalin <shaba@altlinux.org> 2.22.18-alt1
- update to 2.22.18.

* Wed May 11 2022 Alexey Shabalin <shaba@altlinux.org> 2.18.9-alt1
- Initial build.

