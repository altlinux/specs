# -*- rpm-spec -*-
%define module_name	bcmwl
%define module_version	5.100.82.38
%define real_version	5.100.82.38

#### MODULE SOURCES ####
Name: kernel-source-%{module_name}_%{module_version}
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

%description
%module_name module sources for Linux kernel. 


%prep
%setup -c -q
#__mv %module_name-%real_version %name-%version

pushd %name-%version
mv %_target_cpu/* .
rm -rf i586 x86_64
popd

%install
%__mkdir_p %kernel_srcdir
%__tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version/

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Wed Jan 26 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt2
- rebuilt

* Wed Jan 26 2011 Mykola Grechukh <gns@altlinux.ru> 5.100.82.38-alt1
- 5.100.82.38

* Mon Jun 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.60.48.36-alt1
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


