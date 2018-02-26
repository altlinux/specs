%define module_name	subfs
%define module_version	0.9

%define kversion	2.6.32
%define krelease	alt55
%define flavour		xen-dom0

%define module_release	alt10.5
Packager:       Kernel Maintainer Team <kernel@packages.altlinux.org>

Name:		kernel-modules-%module_name-%flavour
Version:	%module_version
Release:	%module_release.132640.55
%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/fs/%module_name

Group:		System/Kernel and hardware
Summary:	%module_name kernel module for submount
URL:		http://submount.sourceforge.net/
License: GPL 

# http://sourceforge.net/tracker/download.php?group_id=81174&atid=562198&file_id=331853&aid=2810034
Patch: submount-0.9-compat.patch

ExclusiveOS:	Linux
BuildRequires: kernel-build-tools >= 0.7
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: rpm-build-licenses
ExclusiveArch: %ix86 x86_64

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq:		coreutils
Prereq:         kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
Requires: submount

%description
Subfs is the kernel portion of the submount removable media handling system.
For submount to function, it needs both the subfs kernel module and the
submount package to be installed.

Submount is a system for automatically mounting and unmounting
removable media drives like CD-ROMs, flash and floppy disk drives. Once
installed, it allows removable media drives to be accessed as if they
were permanently mounted.


%prep
rm -rf kernel-source-%module_name-%{module_version}*
tar xfz %kernel_src/kernel-source-%module_name-%module_version.tar.*
%setup -D -T -n kernel-source-%module_name-%module_version

%patch -p1

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make -C %_usrsrc/linux-%kversion-%flavour TEMP_DIR=$(pwd) V=1 SUBDIRS=$(pwd) modules

%install
install -D -m 0644 %module_name.ko %buildroot/%module_dir/%module_name.ko

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%dir %module_dir
%module_dir/*

%changelog
* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt10.5.132640.55
- Build for kernel-image-xen-dom0-2.6.32-alt55.

* Sat Jun 27 2009 Michael A. Kangin <prividen@altlinux.org> 0.9-alt10.5.132638.1
- build for kernel-image-std-def-2.6.30-alt1.

* Sat Jun 27 2009 Michael A. Kangin <prividen@altlinux.org> 0.9-alt10.5
- merge lakostis@ commits 

* Tue Jun 23 2009 Michail Yakushin <silicium@altlinux.ru> 0.9-alt10.4
- build for 2.6.29

* Sat Nov 01 2008 Michail Yakushin <silicium@altlinux.ru> 0.9-alt10.3
- build for 2.6.27 

* Mon Jun 02 2008 Michail Yakushin <silicium@altlinux.ru> 0.9-alt10.2
- build for 2.6.25 

* Wed Mar 12 2008 Led <led@altlinux.ru> 0.9-alt10
- build for std-def-2.6.24-alt4

* Thu Feb 14 2008 Led <led@altlinux.ru> 0.9-alt10
- rebuild with new kernel-source-%module_name
- cleaned up spec

* Thu Oct 25 2007 Led <led@altlinux.ru> 0.9-alt10
- added:
  + submount-0.9-2.6.19.patch
  + submount-0.9-2.6.20.patch

* Mon Jan 29 2007 Sergey Vlasov <vsu@altlinux.ru> 0.9-alt9
- Removed unneeded "Prereq: modutils".

* Sun Dec 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.9-alt8.132626.8
- Added:
  + submount-0.9-2.6.18.patch: fix compatibility with kernel 2.6.18 
    (tnx to dsd at gentoo.org).

* Sat Mar 11 2006 Sergey Vlasov <vsu@altlinux.ru> 0.9-alt7
- Added:
  + subfs-0.9-alt-i_mutex.patch: fix compatibility with kernel 2.6.16.

* Sun Dec 26 2004 Sergey Vlasov <vsu@altlinux.ru> 0.9-alt6
- Rebuild for kernel 2.4.28.

* Wed Nov 24 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt5
- add requires to submount

* Sun Oct 17 2004 Sergey Vlasov <vsu@altlinux.ru> 0.9-alt4
- Rebuild for kernel 2.4.27.

* Tue Aug 03 2004 Sergey Vlasov <vsu@altlinux.ru> 0.9-alt3
- Use %%post_kernel_modules and %%postun_kernel_modules macros in scripts.

* Wed Jul 14 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt2
- update package description

* Wed May 12 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt1
- initial.spec
