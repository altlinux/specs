#### MODULE SOURCES ####
Version: 0.40
%define module_name     tp_smapi
%define module_version  %version
%define module_release  alt1

Name: kernel-source-%module_name-%module_version
Release: %module_release
Summary: IBM ThinkPad SMAPI Driver - module sources
License: GPL
Group: Development/Kernel
Url: http://tpctl.sourceforge.net
BuildArch: noarch

Source: http://prdownloads.sourceforge.net/tpctl/%{module_name}-%version.tar.gz

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

%description
ThinkPad laptops include a proprietary interface called SMAPI BIOS
(System Management Application Program Interface) which provides some
hardware control functionality that is not accessible by other means.

This driver exposes some features of the SMAPI BIOS through a sysfs
interface. It is suitable for newer models, on which SMAPI is invoked
through IO port writes. Older models use a different SMAPI interface;
for those, try the "thinkpad" module.

%prep
%setup -q -c -n %name
%__mv %module_name-%module_version/* .
%__rm -fR %module_name-%module_version

%install
%__mkdir_p %buildroot%_usrsrc/kernel/sources/
pushd ..
%__tar -c kernel-source-%module_name-%module_version | %__bzip2 -c > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2
popd

%files
%attr(644,root,root) %_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2

%changelog
* Thu Feb 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.40-alt1
- 0.40

* Mon Jun 02 2008 Michail Yakushin <silicium@altlinux.ru> 0.37-alt1
- 0.37

* Tue Feb 12 2008 Michail Yakushin <silicium@altlinux.ru> 0.36-alt1
- new upstream version

* Sat Jan 27 2007 Grigory Batalov <bga@altlinux.ru> 0.30-alt1
- New upstream release.
- Import into git.

* Fri Apr 28 2006 Grigory Batalov <bga@altlinux.ru> 0.19-alt1
- Initial ALTLinux release
