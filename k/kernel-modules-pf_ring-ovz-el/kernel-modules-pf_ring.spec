%define module_name	pf_ring
%define module_version	5.5.2
%define module_release	alt3
%define modules_list intel/e1000e/e1000e-2.0.0.1 intel/igb/igb-3.4.7

%define flavour		ovz-el
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-ovz-el

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: pf_ring kernel modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Patch0: pf_ring-5.5.2-rhel.patch
Patch1: pf_ring-5.5.2-rhel8.6.patch

ExclusiveOS: Linux
URL: http://www.ntop.org/PF_RING.html
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
PF_RING kernel modules.

%package -n kernel-modules-%module_name-drivers-%flavour
Summary: Standard drivers that have been enhanced with PF_RING native support
Group: System/Kernel and hardware

Provides:  kernel-modules-%module_name-drivers-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-drivers-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-drivers-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease kernel-modules-%module_name-%kversion-%flavour-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86 x86_64

%description -n kernel-modules-%module_name-drivers-%flavour
Standard drivers that have been enhanced with PF_RING native support

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%patch0 -p1
%patch1 -p1


%build
pushd kernel
    %make_build -C %_usrsrc/linux-%kversion-%flavour modules SUBDIRS=`pwd`
popd

for m in %modules_list; do
    pushd drivers/PF_RING_aware/$m
	. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
# SMP build does not work
        make -C src KSRC=%_usrsrc/linux-%kversion-%flavour KVER_CODE=%kcode
    popd
done

%install
pushd kernel
    install -d %buildroot%module_dir
    install -p -m644 *.ko %buildroot%module_dir
popd

for m in %modules_list; do
    pushd drivers/PF_RING_aware/$m
	install -p -m644 src/*.ko %buildroot%module_dir
    popd
done

mkdir -p %buildroot%_sysconfdir/depmod.d
cat << EOF > %buildroot%_sysconfdir/depmod.d/%module_name-%kversion-%flavour-%krelease.conf
override e1000e %kversion-%flavour-%krelease %module_name
override igb %kversion-%flavour-%krelease %module_name
EOF

%files
%defattr(644,root,root,755)
%dir %module_dir
%module_dir/pf_ring*

%files -n kernel-modules-%module_name-drivers-%flavour
%_sysconfdir/depmod.d/*
%module_dir/*
%exclude %module_dir/pf_ring*


%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease

* Fri Oct 21 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.5.2-alt3
- fixed build with EL kernel >= 6.8.

* Fri Mar 14 2014 Led <led@altlinux.ru> 5.5.2-alt2
- fixed build with EL kernel >= 6.5

* Sat Mar 02 2013 Led <led@altlinux.ru> 5.5.2-alt1
- 5.5.2

* Wed Feb 20 2013 Led <led@altlinux.ru> 5.4.4-alt2
- new template

* Mon Jul 09 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.4.4-alt1
- 5.4.4

* Sun Feb 05 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.2.1-alt1
- 5.2.1

* Fri Apr 08 2011 Anton Protopopov <aspsk@altlinux.org> 4.4.1-alt2
- Use @kernelarch@

* Fri Oct 15 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Wed Feb 17 2010 Alexey Shabalin <shaba@altlinux.ru> 4.1.3-alt1
- fisrt build for Sisyphus
