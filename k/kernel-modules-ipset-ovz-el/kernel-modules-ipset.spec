%define module_name	ipset
%define module_version	6.12.1
%define module_release	alt1

%define kversion	2.6.32
%define krelease	alt71
%define flavour		ovz-el

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: ipset kernel modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.71
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

%if "%kversion" <= "2.6.32"
Patch0: kernel-source-ipset-6.9-alt-build.patch
%endif

Patch1: kernel-source-ipset-6.12-alt-build.patch

ExclusiveOS: Linux
URL: http://ipset.netfilter.org/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86 x86_64

%description
ipset kernel modules.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%if "%kversion" <= "2.6.32"
%patch0 -p1
%endif
%patch1 -p1

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules SUBDIRS=`pwd`/net/netfilter IP_SET_MAX=256 NOSTDINC_FLAGS=-I`pwd`/include

%install
install -d %buildroot%module_dir
install -p -m644 $(find . -name *.ko) %buildroot%module_dir

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Wed Jun 27 2012 Anton Protopopov <aspsk@altlinux.org> 6.12.1-alt1.132640.71
- Build for kernel-image-ovz-el-2.6.32-alt71.

* Mon Jun 11 2012 Anton Protopopov <aspsk@altlinux.org> 6.12.1-alt1
- Update to 6.12.1

* Sun Jun 03 2012 Anton Protopopov <aspsk@altlinux.org> 6.9.1-alt3
- Remove patch to build with recent ovz-el

* Thu May 31 2012 Anton Protopopov <aspsk@altlinux.org> 6.9.1-alt2
- Add patch to build with recent ovz-el

* Mon Sep 19 2011 Anton Protopopov <aspsk@altlinux.org> 6.9.1-alt1
- Update to 6.9.1

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 4.4-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 4.4-alt2
- technical

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 4.4-alt1
- new version

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 4.3-alt1
- new version 

* Mon Jan 25 2010 Anton Farygin <rider@altlinux.ru> 4.1-alt1
- fisrt build for Sisyphus, specfile from Igor Zubkov
