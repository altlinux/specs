%define module_name ipt-netflow

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: 1.7.1
Release: alt1
Summary: ipt_NETFLOW linux 2.6 kernel module sources

License: GPL
Group: Development/Kernel
Url: http://sourceforge.net/projects/ipt-netflow/
BuildArch: noarch
Source0: %module_name-%version.tar

Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

%description
Ipt-netflow is very fast and effective Netflow exporting module
for Linux kernel (up to 2.6.37). Designed for Linux router with
heavy network load.

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
* Thu May 26 2011 Anton Protopopov <aspsk@altlinux.org> 1.7.1-alt1
- Initial build for ALT
