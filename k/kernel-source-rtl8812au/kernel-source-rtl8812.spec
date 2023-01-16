# -*- rpm-spec -*-
%define module_name rl8812au
%define module_version 5.6.4.2
%define module_release gitee29979

#### MODULE SOURCES ####
Name: kernel-source-rtl8812au
Version: %module_version
Release: alt2.%module_release
Epoch: 1
Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name Realtek 8812 WiFi chipset series module sources
License: GPLv2
Group: Development/Kernel
URL: https://github.com/aircrack-ng/rtl8812au
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source: %name-%module_version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
This is a fork of the Realtek 802.11ac (rtl8812au) v4.2.2 (7502.20130507)
driver altered to build on Linux kernel version >= 3.10.

%module_name module sources for Linux kernel.

%prep
%setup -c
cd %name-%module_version

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Mon Jan 16 2023 Andrey Cherepanov <cas@altlinux.org> 1:5.6.4.2-alt2.gitee29979
- Supported kernel 6.1.

* Mon Aug 29 2022 Andrey Cherepanov <cas@altlinux.org> 1:5.6.4.2-alt1.20220827.gite7a4a39
- New version from https://github.com/aircrack-ng/rtl8812au.

* Fri May 13 2022 Andrey Cherepanov <cas@altlinux.org> 7502.20220511-alt1
- build with kernel >= 5.17

* Fri Nov 12 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 7502.20210405-alt2
- build with kernel >=5.15 fixed

* Mon Apr 05 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 7502.20210405-alt1
- updated from git
- build with kernel >=5.10 fixed

* Wed Feb 05 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 7502.20200205-alt1
- updated from git
- build with kernel >=5.4 fixed

* Fri Nov  8 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 7502.20191011-alt1
- resurrect in sisyphus
- updated from git

* Mon Mar 27 2017 Hihin Ruslan <ruslandh@altlinux.ru> 7502.20130507-alt1
- first build for Sisyphus
