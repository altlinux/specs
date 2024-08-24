%define module_name 88x2bu
%define module_version 5.13.1
%define module_release alt1

%define flavour	6.10

%setup_kernel_module %flavour

%define _moduledir /lib/modules/%kversion-%flavour-%krelease

Name: kernel-modules-%module_name-%flavour
Group: System/Kernel and hardware
Summary: Module for USB WiFi Adapters that are based on the RTL8812BU and RTL8822BU Chipsets
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
Url: https://github.com/morrownr/88x2bu-20210702
License: GPLv2

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %ix86 x86_64 armh aarch64

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Provides: kernel-modules-rtl%{module_name}-%kversion-%flavour-%krelease = %version-%release
Obsoletes: kernel-modules-rtl%{module_name}-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

BuildRequires(pre): rpm-build-kernel, bc
BuildRequires(pre): kernel-headers-modules-6.10
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Requires: %{module_name}-conf

%description
These packages contain kernel driver for USB WiFi Adapters that are based on
the RTL8812BU and RTL8822BU Chipsets.

%prep
rm -rf kernel-source-%module_name-%module_version
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build \
    ARCH=%base_arch \
    CROSS_COMPILE= \
    KSRC=%_usrsrc/linux-%kversion-%flavour \
    modules

%install
install -D -m 644 88x2bu.ko %buildroot%_moduledir/net/wireless/realtek/rtlwifi/%module_name.ko

%files
%dir %_moduledir/net
%dir %_moduledir/net/wireless
%dir %_moduledir/net/wireless/realtek
%dir %_moduledir/net/wireless/realtek/rtlwifi
%_moduledir/net/wireless/realtek/rtlwifi/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
