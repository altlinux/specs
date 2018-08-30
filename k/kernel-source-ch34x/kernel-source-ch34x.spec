%define module_name ch34x
%define module_version 20180821
%define module_release	alt1

%define module_source	kernel-source-%module_name-%module_version.tar

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: %module_release
Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name modules sources for CH340 serial to usb chip.
License: GPL
Group: Development/Kernel
BuildArch: noarch

BuildRequires: kernel-build-tools

Source0: %module_source
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

%description
%module_name modules sources for CH340 serial to usb chip.

%prep
%setup

%install
%__mkdir_p %kernel_srcdir
cd ..
%__tar -c  kernel-source-%module_name-%module_version | %__bzip2 -c > \
	%kernel_srcdir/kernel-source-%module_name-%module_version.tar.bz2

%files
%_usrsrc/*

%changelog
* Thu Aug 30 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 20180821-alt1
- initial build


