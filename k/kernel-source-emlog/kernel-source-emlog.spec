%define module_name emlog

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: 0.51
Release: alt1
Summary: emlog kernel module sources
License: Distributable
Group: Development/Kernel
Url: http://www.linuxconsulting.ro/emlog/
BuildArch: noarch

Source0: %module_name-%version.tar

Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

%description
This package contains sources of emlog.

%prep
%setup -c

%install
mkdir -p %buildroot%_usrsrc/kernel/sources/
mv %module_name-%version kernel-source-%module_name-%version
tar -c kernel-source-%module_name-%version | bzip2 -c > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%version.tar.bz2

%files
%_usrsrc/kernel/sources/kernel-source-%module_name-%version.tar.bz2

%changelog
* Fri Sep 02 2011 Timur Aitov <timonbl4@altlinux.org> 0.51-alt1
- Initial build for ALT Linux

