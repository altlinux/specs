%define module_name igb
%define module_version 2.4.13
%define module_release	alt1

%define module_source	%module_name.tar

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: %module_release
Summary: Linux %module_name modules sources
License: GPL
Group: Development/Kernel
URL: http://www.intel.com/
BuildArch: noarch

BuildRequires: kernel-build-tools

Source0: %module_source
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

%description
%module_name modules sources for Linux kernel, there are three Linux
Base Drivers for Intel Gigabit Network Connections.

%prep
%setup -c -q
cd %module_name

find . -name '*.orig' -print -delete
cd ..
%__mv %module_name kernel-source-%module_name-%module_version

%install
%__mkdir_p %kernel_srcdir
%__tar -c  kernel-source-%module_name-%module_version | %__bzip2 -c > \
	%kernel_srcdir/kernel-source-%module_name-%module_version.tar.bz2

%files
%_usrsrc/*

%changelog
* Thu Mar 24 2011 Anton Protopopov <aspsk@altlinux.org> 2.4.13-alt1
- 2.4.13

* Fri Feb 18 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.4.12-alt1
- 2.4.12

* Sat Oct 16 2010 Michail Yakushin <silicium@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Tue May 26 2009 Michail Yakushin <silicium@altlinux.ru> 1.3.19.3-alt1
- 1.3.19.3 

* Tue Apr 29 2008 Michail Yakushin <silicium@altlinux.ru> 1.2.24-alt1
- inital build 

