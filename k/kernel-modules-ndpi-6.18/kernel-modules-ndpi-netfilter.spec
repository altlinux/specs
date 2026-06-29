%define module_name	ndpi
%define module_version	5.0

%define module_release alt1

%define flavour		6.18
%define karch x86_64 aarch64 loongarch64 e2k e2kv4 e2kv5 e2kv6
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-6.18
BuildRequires: libiptables-devel

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Deep packet inspection module for Linux kernel
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>


ExclusiveOS: Linux
Url: https://github.com/vel21ripn/nDPI/tree/netfilter
BuildRequires(pre): rpm-build-kernel
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release
Requires: ndpi-netfilter

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Deep packet inspection module for Linux kernel


%prep
rm -rf %module_name-%{module_version}*
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar.*
%setup -D -T -n kernel-source-%module_name-%version

%build
make KERNEL_DIR=%_usrsrc/linux-%kversion-%flavour

%install
mkdir -p %buildroot/%module_dir
install src/xt_ndpi.ko %buildroot/%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
