# -*- rpm-spec -*-
%define module_name	exfat
%define module_version  2.2.0
%define real_version	2.2.0-1arter97

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt1
Provides: kernel-source-%module_name-%module_version
Summary: %module_name filesystem module sources
License: Propreitary
Group: Development/Kernel
Url: https://github.com/arter97/exfat-linux
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%real_version.tar

BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
%module_name module sources for Linux kernel.

%prep
%setup -c -q

%install
mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%real_version/

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Sun Sep 15 2019 L.A. Kostis <lakostis@altlinux.ru> 2.2.0-alt1
- Initial build for ALTLinux.

