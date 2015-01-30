%define module_name sobol
%define module_version 1
%define module_release	alt1

%define module_source	%module_name-%module_version.tar

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: %module_release
Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name modules sources for Sobol.
License: BSD 3-clause, distributable
Group: Development/Kernel
BuildArch: noarch

BuildRequires: kernel-build-tools

Source0: %module_source
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

%description
%module_name modules for CryptoProCSP products sources for Linux kernel.

%prep
%setup -n %module_name-%module_version

%install
%__mkdir_p %kernel_srcdir
cd ..
%__mv %module_name-%module_version kernel-source-%module_name-%module_version
%__tar -c  kernel-source-%module_name-%module_version | %__bzip2 -c > \
	%kernel_srcdir/kernel-source-%module_name-%module_version.tar.bz2

%files
%_usrsrc/*

%changelog
* Tue Jan 20 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1-alt1
- initial build

