%define module_name	omnibook
%define module_version  20090714
%define module_release	alt1

%define kversion	2.6.32
%define krelease	alt38
%define flavour		el-smp

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Kernel module for some Toshiba and HP laptops
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.38
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Patch0: kernel-source-omnibook-0.0-alt.patch
Patch1: omnibook-2.6.30.patch

ExclusiveOS: Linux
URL: http://omnibook.sourceforge.net/
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
This package is intended to provide Linux kernel support for HP OmniBook,
HP Pavilion, Toshiba Satellite, Tecra, Equium and Compal laptops.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%patch0 -p1
#%patch1 -p1 

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules SUBDIRS=`pwd`

%install
install -d %buildroot%module_dir
install -p -m644 omnibook.ko %buildroot%module_dir

install -d %buildroot%_docdir/%name-%version-%release
install -p -m644 doc/{BUGS,CREDITS,ChangeLog,README} \
	%buildroot%_docdir/%name-%version-%release
cp -pr misc %buildroot%_docdir/%name-%version-%release

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir
%doc %_docdir/%name-%version-%release

%changelog
* Wed Jul 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 20090714-alt1.132640.38
- Build for kernel-image-el-smp-2.6.32-alt38.

* Thu Sep 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20090714-alt1
- updated from git

* Sun Jul 20 2008 Igor Zubkov <icesik@altlinux.org> 0.0-alt1.r274.132633.7
- build for kernel-image-std-def-2.6.25-alt7

* Sat Mar 22 2008 Igor Zubkov <icesik@altlinux.org> 0.0-alt1.r274
- build for Sisyphus

