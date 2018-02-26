# -*- rpm-spec -*-
%define module_name	rtl8192
%define module_version  0018.1025
%define real_version	0018.1025

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt1
Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name Realtek 819x WiFi chipset series module sources
License: GPLv2
Group: Development/Kernel
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source0: %name-%real_version.tar

ExclusiveArch: i586 x86_64
BuildPreReq: kernel-build-tools

%description
%module_name module sources for Linux kernel. 

%package -n firmware-rtl8192
Summary: firmware for Realtek RTL8192SE chipsets

License: Distributable
Group: System/Kernel and hardware

%description -n firmware-rtl8192
This is a firmware for the Realtek 8192SE 802.11 b/g/n chips.

%prep
%setup -c -q
#__mv %module_name-%real_version %name-%version


%install
%__mkdir_p %kernel_srcdir
%__tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version/
mkdir -p %buildroot/lib/firmware/RTL8192SE
install -m644 -D %name-%version/firmware/RTL8192SE/* %buildroot/lib/firmware/RTL8192SE


%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n firmware-rtl8192
/lib/firmware/*


%changelog
* Sat Nov 27 2010 Andriy Stepanov <stanv@altlinux.ru> 0018.1025-alt1
- New version

* Fri Sep 24 2010 Andriy Stepanov <stanv@altlinux.ru> 0017.0705-alt2
- Put firmware ro right place

* Mon Sep 13 2010 Andriy Stepanov <stanv@altlinux.ru> 0017.0705-alt1
- New version

* Fri May 28 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0015.0127-alt1
- first build for Sisyphus
