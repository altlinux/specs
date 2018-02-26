%define module_name e1000e
%define module_version 1.6.3
%define module_release alt1

%define module_source %module_name.tar

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: %module_release
Summary: Linux %module_name modules sources
License: GPL
Group: Development/Kernel
URL: https://sourceforge.net/projects/e1000
BuildArch: noarch

BuildRequires: kernel-build-tools

Source0: %module_source
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

%description
%module_name modules sources for e1000e Linux kernel driver

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
* Wed Nov 16 2011 Anton Protopopov <aspsk@altlinux.org> 1.6.3-alt1
- New version

* Mon Feb 21 2011 Anton Protopopov <aspsk@altlinux.org> 1.2.20-alt1
- Build for sisyphus
