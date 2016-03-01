%define module_name	eprd
%define module_version	0.5.0
%define module_release	alt4

%define flavour		std-def
BuildRequires(pre): kernel-headers-modules-std-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: eprd kernel module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: http://sourceforge.net/projects/eprd/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: gcc4.9

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %karch 

%description
An eventually persistent ramdisk / disk cache.
This project can be useful whenever one needs more IOPS
in a non critical environment. There is more to this
project though. I am working on a kernel based high
performance deduplicating block device. This project
will share code and ideas from EPRD as well as Lessfs

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%set_gcc_version 4.9
%make_build KDIR=%_usrsrc/linux-%kversion-%flavour SUBDIRS=`pwd`

%install
install -d %buildroot%module_dir
install -d %buildroot%_docdir/%module_name-%module_version
install eprd.ko %buildroot%module_dir
install -D -m 755 eprd_setup %buildroot%_sbindir/eprd_setup
install -D -m 644 README %buildroot%_docdir/%module_name-%module_version/README

%files
%module_dir
%_sbindir/eprd_setup
%_docdir/%module_name-%module_version/README
%dir %_docdir/%module_name-%module_version

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Mar 01 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.0-alt4
- Fixed repocop warning about %_sbindir/eprd_setup permissions

* Mon Dec 15 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.0-alt3
- Minor .spec updates
- (ALT #31626)

* Sun Sep 06 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.0-alt2
- Spec changed (updated summary)

* Wed Sep 02 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.0-alt1
- Initial build for ALT

