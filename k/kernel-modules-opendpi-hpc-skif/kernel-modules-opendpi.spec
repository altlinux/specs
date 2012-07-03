%define module_name	opendpi
%define module_version	1.3.0
%define module_release	alt1

%define kversion	2.6.32
%define krelease	alt24
%define flavour		hpc-skif
%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name


Name:		kernel-modules-%module_name-%flavour
Version:	%module_version
Release:	%module_release.132640.24

Group:		System/Kernel and hardware
Summary:	This package is a GPL implementation of an iptables and netfilter module for OpenDPI integration into the Linux kernel.
URL:		http://opendpi.org/
License: GPLv4

ExclusiveOS:	Linux
BuildRequires: kernel-build-tools >= 0.7
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: rpm-build-licenses iptables-devel
ExclusiveArch: %ix86 x86_64

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq:		coreutils
Prereq:         kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
Requires: iptables-opendpi

%description
This package is a GPL implementation of an iptables and netfilter module for OpenDPI integration into the Linux kernel.

%prep
rm -rf kernel-source-%module_name-%{module_version}*
tar xjf %kernel_src/kernel-source-%module_name-%module_version.tar.*
%setup -D -T -n kernel-source-%module_name-%module_version

%build
export OPENDPI_PATH=$(pwd)
cd wrapper
%make KERNEL_DIR=%_usrsrc/linux-%kversion-%flavour

%install
mkdir -p %buildroot/%module_dir
install -D -m0644 wrapper/src/xt_opendpi.ko  %buildroot%module_dir/

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir/*

%changelog
* Thu Sep 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.0-alt1.132640.24
- Build for kernel-image-hpc-skif-2.6.32-alt24.

* Mon Aug 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.0-alt1
- new version

* Sun Apr 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.0-alt1
- first build for Sisyphus
