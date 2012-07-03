%define module_name	pf_ring
%define module_version	4.4.1
%define module_release	alt3

%define kversion	3.4.4
%define krelease	alt1
%define flavour		std-pae

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: pf_ring kernel modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.197636.1
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: http://www.ntop.org/PF_RING.html
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86

Patch1: 2.6.38.patch
Patch2: 2.6.39.patch
%if "%kversion" >= "3.1.1"
Patch3: 3.1.1.patch
%endif

%description
PF_RING kernel modules.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%patch1 -p1
%patch2 -p1
%if "%kversion" >= "3.1.1"
%patch3 -p2
%endif

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules SUBDIRS=`pwd`

%install
install -d %buildroot%module_dir
install -p -m644 *.ko %buildroot%module_dir

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Mon Jun 25 2012 Anton Protopopov <aspsk@altlinux.org> 4.4.1-alt3.197636.1
- Build for kernel-image-std-pae-3.4.4-alt1.

* Mon Nov 14 2011 Anton Protopopov <aspsk@altlinux.org> 4.4.1-alt3
- Fix build with 3.1.1

* Fri Apr 08 2011 Anton Protopopov <aspsk@altlinux.org> 4.4.1-alt2
- Use %ix86

* Fri Oct 15 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Wed Feb 17 2010 Alexey Shabalin <shaba@altlinux.ru> 4.1.3-alt1
- fisrt build for Sisyphus
