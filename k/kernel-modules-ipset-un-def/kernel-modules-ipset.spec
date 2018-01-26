%define module_name	ipset
%define module_version	6.35
%define module_release	alt1

%define flavour		un-def
BuildRequires(pre): kernel-headers-modules-un-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: ipset kernel modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: http://ipset.netfilter.org/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: libmnl-devel

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %karch

%description
ipset kernel modules.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
autoreconf -fisv

%build
%configure --with-kbuild=%_usrsrc/linux-%kversion-%flavour --with-ksource=%_usrsrc/linux-%kversion-%flavour
make modules

%install
install -d %buildroot%module_dir
install -p -m644 kernel/net/netfilter/ipset/*.ko %buildroot%module_dir
install -p -m644 kernel/net/netfilter/*.ko %buildroot%module_dir


%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Jul 26 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.29-alt2
- build with 4.7 kernel fixed

* Tue Jun 28 2016 Anton Farygin <rider@altlinux.ru> 6.29-alt1
- new version

* Tue Sep 29 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.26-alt1
- new version

* Wed Feb 11 2015 Anton Farygin <rider@altlinux.ru> 6.24-alt1
- new version

* Wed Sep 24 2014 Anton Farygin <rider@altlinux.ru> 6.23-alt1
- new version

* Mon Mar 24 2014 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.21-alt1
- new version

* Fri Nov 15 2013 Anton Farygin <rider@altlinux.ru> 6.20.1-alt1
- new version

* Fri Jun 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.19-alt1
- new version

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 4.4-alt1
- new version

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 4.3-alt1
- new version 

* Mon Jan 25 2010 Anton Farygin <rider@altlinux.ru> 4.1-alt1
- fisrt build for Sisyphus, specfile from Igor Zubkov
