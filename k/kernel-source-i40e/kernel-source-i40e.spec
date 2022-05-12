%define module_name i40e
%define module_version 2.18.9

%define module_source %module_name.tar

Name: kernel-source-%module_name
Version: %module_version
Release: alt1

Group: Development/Kernel
Summary: Linux %module_name modules sources
License: GPL-2
URL: http://sourceforge.net/projects/e1000
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

BuildRequires: rpm-build-kernel

%description
%module_name modules sources for the Intel(R) 40-10 Gigabit Ethernet.

%prep
%setup -c -q

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%module_name-%version.tar.bz2 %name-%version

%files
%_usrsrc/*

%changelog
* Wed May 11 2022 Alexey Shabalin <shaba@altlinux.org> 2.18.9-alt1
- Initial build.

