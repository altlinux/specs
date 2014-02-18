# -*- rpm-spec -*-
%define module_name	bcmwl
%define module_version  6.30.223.141
%define real_version	6.30.223.141

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt2
Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name Broadcom WiFi chipset series module sources
License: Propreitary
Group: Development/Kernel
Url: http://www.broadcom.com/support/802.11/linux_sta.php 
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%real_version.tar

ExclusiveArch: i586 x86_64
BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
%module_name module sources for Linux kernel. 


%prep
%setup -c -q
#__mv %module_name-%real_version %name-%version

%install
%__mkdir_p %kernel_srcdir
%__tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version/

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Tue Feb 18 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.141-alt2
- lost sources updated

* Mon Feb 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.141-alt1
- 6.30.223.141

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


