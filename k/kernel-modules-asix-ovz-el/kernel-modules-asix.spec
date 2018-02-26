%define module_name	asix
%define module_version	4.1.0
%define module_release	alt2

%define kversion       2.6.32
%define krelease       alt71
%define flavour        ovz-el

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/drivers/usb/net/

Summary:	asix kernel module from vendor
Name:		kernel-modules-%module_name-%flavour
Version:	1.0.%module_version
Release:	%module_release.132640.71
License:	GPL
Group:		System/Kernel and hardware

Packager:       Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS:	Linux
URL:		http://asix.com.tw
Patch1:	asix-build-kernel3.2.patch
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-headers-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq:		coreutils
Prereq:         kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease

ExclusiveArch:  %ix86 x86_64

%description
Kernel modules for ASIX AX8817X based USB 2.0 Ethernet Devices from vendor

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%if "%kversion" >= "3.2"
%patch1 -p1
%endif

%build
%make_build -C /usr/src/linux-%kversion-%flavour-%krelease SUBDIRS=$(pwd) modules

%install
mkdir -p $RPM_BUILD_ROOT/%module_dir
install -p -m644 %module_name.ko $RPM_BUILD_ROOT/%module_dir

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Wed Jun 27 2012 Anton Protopopov <aspsk@altlinux.org> 1.0.4.1.0-alt2.132640.71
- Build for kernel-image-ovz-el-2.6.32-alt71.

* Fri Jan 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.4.1.0-alt2
- fix to build with 3.2 kernel

* Mon Jun 06 2011 Anton Protopopov <aspsk@altlinux.org> 1.0.4.1.0-alt1
- Initial build for ALT
