%define module_name sysdig
%define module_version 7.3.0
%define module_release alt1

%define flavour	6.12
%define karch aarch64 x86_64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-6.12

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/net/wireless

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Realtek RTL8188EU Wireless Lan Driver for Linux
License: GPL-2.0
Group: System/Kernel and hardware
URL: https://github.com/ivanovborislav/rtl8188eu

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %karch

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

%description
%{summary}.

%prep
rm -rf %module_name-%module_version
tar xvf %kernel_src/%module_name-*.tar.bz2
%setup -D -T -n scap-%module_version+driver
# Fix module license
subst 's|Dual MIT/||' main.c

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build KERNELDIR=%_usrsrc/linux-%kversion-%flavour

%install
install -Dm0644 scap.ko %buildroot/%module_dir/scap.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
