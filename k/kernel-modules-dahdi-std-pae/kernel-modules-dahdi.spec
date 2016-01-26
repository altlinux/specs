%define _unpackaged_files_terminate_build	1

%define module_name	dahdi
%define module_version	2.11.0
%define module_release alt1

%define flavour	std-pae
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-pae

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

%define kernel_headers_dir %prefix/src/linux-%kversion-%flavour-%krelease
%define module_headers_dir %kernel_headers_dir/drivers/%module_name

Summary: %module_name modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Requires: dahdi-udev

ExclusiveOS: Linux
Url: http://www.asterisk.org/index.php?menu=download

# Automatically added by buildreq on Sun Nov 07 2004
BuildRequires: kernel-source-%module_name
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease

%if "%kversion" == "2.6.37"
Patch1: kernel-2.6.37-build-fixes.patch
%endif

%if "%kversion" >= "2.6.39"
Patch2: dahdi-remove-spinlock_unlocked.patch
%endif

%if "%kversion" >= "3.2"
Patch3: dahdi-build-3.2.patch
%endif

%description
dahdi modules, that needed for all Digium hardware, and some compatible
devices for telephony.

%package -n kernel-headers-%module_name-%flavour
Summary: dahdi driver headers
Group: Development/Kernel
PreReq: kernel-headers-modules-%flavour = %kversion-%krelease
Requires(postun): kernel-headers-modules-%flavour = %kversion-%krelease
Provides: kernel-headers-%module_name-%kversion-%flavour-%krelease = %version-%release

%description -n kernel-headers-%module_name-%flavour
This package contains dahdi driver headers and other files needed for
compiling kernel modules which interface with dahdi drivers.

%prep
rm -rf kernel-source-%module_name-%module_version

tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2

%setup -D -T -n kernel-source-%module_name-%module_version

%build
pushd dahdi
export KERNEL_SOURCE=%_usrsrc/linux-%kversion-%flavour
subst s!-I/usr/src/linux-2.4/!-I%_usrsrc/linux-%kversion-%flavour!g Makefile
subst s!^KINCLUDES=.*$/!KINCLUDES=%_usrsrc/linux-%kversion-%flavour!g Makefile
subst 's! # ztdummy! ztdummy!' Makefile
subst 's!PRIMARY=.*!PRIMARY=ztdummy!' Makefile

. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc

#chmod +x menuselect/configure

#./configure
#make version.h
#make tones.h tor2fw.h radfw.h
make \
	KVERS=%kversion \
	KSRC=%_usrsrc/linux-%kversion-%flavour

#make -C %_usrsrc/linux-%kversion-%flavour SUBDIRS=`realpath .` modules \
popd
%install
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
pushd dahdi
make \
	KVERS=%kversion \
	KSRC=%_usrsrc/linux-%kversion-%flavour \
	DESTDIR=%buildroot \
	install-modules

#make -C %_usrsrc/linux-%kversion-%flavour \
#    SUBDIRS=`realpath .`/kernel \
#    DESTDIR=%buildroot \
#    install

#    INSTALL_MOD_PATH=%buildroot/%module_dir \

#mv %buildroot/%module_dir/lib/modules/*/extra/* %buildroot/%module_dir/
#rmdir %buildroot/%module_dir/lib/modules/*/extra
rm -f %buildroot/lib/modules/%kversion-%flavour-%krelease/modules.*
#rmdir %buildroot/%module_dir/lib/modules/*
#rmdir %buildroot/%module_dir/lib/modules
#rmdir %buildroot/%module_dir/lib

mkdir -p %buildroot%module_headers_dir
pushd include/dahdi
cp -p *.h \
	%buildroot%module_headers_dir/

echo "%name = %version-%release" \
	> %buildroot%kernel_headers_dir/kernel-modules-%module_name.release
popd
pushd drivers/dahdi
sed -e 's|%_builddir/||' < Module.symvers \
	> %buildroot%kernel_headers_dir/kernel-modules-%module_name.symvers
sed -e 's|%_builddir/||' < Module.symvers \
	> %buildroot%module_headers_dir/Module.symvers
popd

%files
%module_dir

%files -n kernel-headers-%module_name-%flavour
%module_headers_dir
%kernel_headers_dir/kernel-modules-%module_name.release
%kernel_headers_dir/kernel-modules-%module_name.symvers

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Jun 23 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.10.2-alt1
- new version

* Fri Feb 27 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.10.1-alt1
- new version

* Thu Oct 23 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.10.0.1-alt1
- new version

* Wed Sep  3 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.9.2-alt1
- new version

* Mon Dec 23 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.7.0.2-alt1
- new version

* Thu Jul  4 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.7.0-alt1
- new version

* Mon Apr 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.6.2-alt1
- new version

* Wed Feb 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.6.1-alt3
- build with kernel 3.8 fixed

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.1-alt2
- new template

* Sun Sep 02 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.1-alt1
- 2.6.1

* Mon Feb 13 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.0-alt1
- 2.6.0

* Mon Jan 16 2012 Anton Protopopov <aspsk@altlinux.org> 2.5.0.2-alt3
- build with kernel 3.2 fixed

* Wed Dec 14 2011 Anton Protopopov <aspsk@altlinux.org> 2.5.0.2-alt2
- technical

* Thu Oct 27 2011 Anton Protopopov <aspsk@altlinux.org> 2.5.0.2-alt1
- 2.5.0.2

* Fri Sep 16 2011 Anton Protopopov <aspsk@altlinux.org> 2.5.0-alt3
- Force big release version

* Tue Aug 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Fri Jul 08 2011 Anton Protopopov <aspsk@altlinux.org> 2.4.1.2-alt2
- Remove wget from BR (it's useless due to network isolation)

* Tue Jun 28 2011 Anton Protopopov <aspsk@altlinux.org> 2.4.1.2-alt1
- 2.4.1.2

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 2.3.0-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 2.3.0-alt2
- technical

* Tue Apr 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Apr 01 2010 Michail Yakushin <silicium@altlinux.ru> 2.2.1.1-alt1
- 2.2.1.1

* Sun Mar 14 2010 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Nov 17 2009 Anton Protopopov <aspsk@altlinux.org> 2.2.0.1-alt6
- A faulse one to enforce sisyphus check

* Thu Sep 03 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0.1-alt4
- rebuild

* Tue Sep 01 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0.1-alt3
- fix requires

* Tue Sep 01 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0.1-alt2
- first build for Sisyphus

