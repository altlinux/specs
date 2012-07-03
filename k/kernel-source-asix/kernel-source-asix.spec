%define module_name asix

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: 4.1.0
Release: alt1
Summary: asix linux kernel module sources

License: GPL
Group: Development/Kernel
Url: http://asix.com.tw/
BuildArch: noarch
Source0: %module_name-%version.tar

Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

%description
Source of kernel modules for ASIX AX8817X based USB 2.0
Ethernet Devices from vendor

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
* Mon Jun 06 2011 Anton Protopopov <aspsk@altlinux.org> 4.1.0-alt1
- Initial build for ALT
