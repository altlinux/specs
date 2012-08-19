%define module_name	u200
%define module_version	1.0
%define module_release	alt3

%define kversion       3.5.2
%define krelease       alt2
%define flavour        std-def

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/drivers/net/usb/

Summary:	u200 kernel module
Name:		kernel-modules-%module_name-%flavour
Version:	1.0.%module_version
Release:	%module_release.197890.2
License:	GPL
Group:		System/Kernel and hardware
%if "%kversion" >= "3.2"
Patch1:	u200-build-kernel3.2.patch
%endif
%if "%kversion" >= "3.5"
Patch2:	u200-build-kernel3.5.patch
Patch3:	u200-build-kernel3.5-2.patch
%endif

Packager:       Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS:	Linux
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
Samsung SWC-U200 Mobile WiMax USB dongle

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%if "%kversion" >= "3.2"
%patch1 -p1
%endif
%if "%kversion" >= "3.5"
%patch2 -p1
%patch3 -p1
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
* Sun Aug 19 2012 Anton Protopopov <aspsk@altlinux.org> 1.0.1.0-alt3.197890.2
- Build for kernel-image-std-def-3.5.2-alt2.

* Sat Aug 18 2012 Anton Protopopov <aspsk@altlinux.org> 1.0.1.0-alt3
- fix to build with 3.5 kernel

* Fri Jan 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.1.0-alt2
- fix to build with 3.2 kernel

* Wed Jun 08 2011 Anton Protopopov <aspsk@altlinux.org> 1.0.1.0-alt1
- Initial build for ALT
