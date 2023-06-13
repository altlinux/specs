%define module_name      iavf
%define module_version   4.8.3
%define module_release   alt1

%define flavour          std-def
%define karch            x86_64 aarch64

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/updates
%add_verify_elf_skiplist %module_dir/*

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Intel(R) Ethernet Adaptive Virtual Function Driver
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
This package contains the Intel(R) Ethernet Adaptive Virtual Function Driver.

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

* Tue Jun 13 2023 Anton Farygin <rider@altlinux.ru> 4.8.3-alt1
- Initial build for ALT

