# -*- rpm-spec -*-
%define module_name	bcmwl
%define module_version  6.30.223.271
%define real_version	6.30.223.271
# for patched version
%define git 6adc981

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt5.g%{git}
Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name Broadcom WiFi chipset series module sources
License: Propreitary
Group: Development/Kernel
Url: https://github.com/antoineco/broadcom-wl
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%real_version.tar

ExclusiveArch: x86_64
BuildPreReq: kernel-build-tools

%description
%module_name module sources for Linux kernel.

Patched for Linux >= 4.7

%prep
%setup -c -q

%install
mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version/bcmwl

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Wed Oct 19 2022 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt5.g6adc981
- GIT 6adc981 from github (kernel 6.x compatible).

* Sat Apr 16 2022 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt4.gb76c5dc
- GIT b76c5dc from github (kernel 5.18 compatible).
- Drop %%ix86 support (who cares).

* Fri Dec 10 2021 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt3
- Make sources arch dependant.

* Tue May 18 2021 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt2
- Use version from github patch for 4.7+ compatibility.

* Wed Jun 29 2016 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt1
- 6.30.223.271.

* Wed Aug 07 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.30-alt1
- 6.30.223.30

* Thu Jan 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.100.82.112-alt1
- 5.100.82.112

* Thu Sep 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.60.48.36-alt1
- 5.60.48.36

* Mon Jan 11 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.10.91.9.3-alt3
- Build on i586 fixed

* Wed Dec 30 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.10.91.9.3-alt2
- 5.10.91.9.3

* Tue May 26 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.91.9-alt1
- 5.10.91.9

* Tue Apr 07 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt2
- fix Summary 

* Wed Mar 25 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt1
- initial build 


