%define module_name rt3070

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: 2.5.0.2
Release: alt1
Summary: Linux RT3070 modules sources
License: Distributable
Group: Development/Kernel
Url: http://www.ralinktech.com/support.php?s=2
BuildArch: noarch

Source0: %module_name-%version.tar

Patch0: rt3070-2.5.0.2-alt-chipset.patch
Patch1: rt3070-2.5.0.2-alt-fix-build-for-rt3070.patch
Patch2: rt3070-2.5.0.2-alt-tftpboot.patch
Patch3: rt3070-2.5.0.2-alt-license.patch
Patch4: rt3070-2.5.0.2-alt-return.patch
Patch5: rt3070-2.5.0.2-alt-WPA-supplicant.patch

Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

%description
This package contains sources of the Linux driver for the Ralink
RT3070 802.11 b/g/n adapter.

%prep
%setup -c
pushd %module_name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p1
%patch4 -p1
%patch5 -p1
popd

%install
mkdir -p %buildroot%_usrsrc/kernel/sources/
mv %module_name-%version kernel-source-%module_name-%version
tar -c kernel-source-%module_name-%version | bzip2 -c > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%version.tar.bz2

%files
%_usrsrc/kernel/sources/kernel-source-%module_name-%version.tar.bz2

%changelog
* Fri Jul 22 2011 Timur Aitov <timonbl4@altlinux.org> 2.5.0.2-alt1
- Initial build for ALT Linux

