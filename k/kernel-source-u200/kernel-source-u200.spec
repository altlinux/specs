%define module_name u200

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: 1.0
Release: alt1
Summary: u200 linux kernel module sources

License: GPL
Group: Development/Kernel
BuildArch: noarch
Source0: %module_name-%version.tar

Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

%description
Samsung SWC-U200 Mobile WiMax USB dongle

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
* Wed Jun 08 2011 Anton Protopopov <aspsk@altlinux.org> 1.0-alt1
- Build as separate module for ALT
