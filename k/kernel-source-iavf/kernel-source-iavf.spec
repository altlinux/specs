%define module_name iavf
%define module_version 4.8.3

%define module_source %module_name.tar

Name: kernel-source-%module_name
Version: %module_version
Release: alt1

Group: Development/Kernel
Summary: Linux %module_name modules sources for Intel(R) Ethernet Adaptive Virtual Function Driver
License: GPL-2
URL: http://sourceforge.net/projects/e1000
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

BuildRequires: rpm-build-kernel

%description
%module_name modules sources for the Intel(R) Ethernet Adaptive Virtual Function
Driver.

%prep
%setup -c -q

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%module_name-%version.tar.bz2 %name-%version

%files
%_usrsrc/*

%changelog
* Tue Jun 13 2023 Anton Farygin <rider@altlinux.ru> 4.8.3-alt1
- Initial build for ALT.
