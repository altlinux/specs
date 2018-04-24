%define module_name	wireguard
%define module_version	0.0.20180413
%define module_release	alt1

%define flavour		un-def
BuildRequires(pre): kernel-headers-modules-un-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Wireguard is a fast, modern, secure VPN tunnel module for Linux kernel
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: https://www.wireguard.com/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %karch 

%description
WireGuard kernel module.
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more
useful than IPSec, while avoiding the massive headache. It intends to be
considerably more performant than OpenVPN. WireGuard is designed as a general
purpose VPN for running on embedded interfaces and super computers alike, fit
for many different circumstances. Initially released for the Linux kernel, it
plans to be cross-platform and widely deployable. It is currently under heavy
development, but already it might be regarded as the most secure, easiest to
use, and simplest VPN solution in the industry.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version/src

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules SUBDIRS=`pwd`

%install
install -d %buildroot%module_dir
install wireguard.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Apr 17 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20180413-alt1
- Initial build

