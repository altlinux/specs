%define module_name	pf_ring
%define module_version	5.4.4
%define module_release	alt1
%define modules_list intel/e1000e/e1000e-2.0.0.1 intel/igb/igb-3.4.7

%define kversion	2.6.32
%define krelease	alt71
%define flavour		ovz-el

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: pf_ring kernel modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.71
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
ExclusiveArch: %ix86 x86_64

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

%build
pushd kernel
    %make_build -C %_usrsrc/linux-%kversion-%flavour modules SUBDIRS=`pwd`
popd

for m in %modules_list; do
    pushd drivers/PF_RING_aware/$m
	. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
# SMP build does not work
        make -C src KSRC=%_usrsrc/linux-%kversion-%flavour
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

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%post -n kernel-modules-%module_name-drivers-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-%module_name-drivers-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%dir %module_dir
%module_dir/pf_ring*

%files -n kernel-modules-%module_name-drivers-%flavour
%_sysconfdir/depmod.d/*
%module_dir/*
%exclude %module_dir/pf_ring*


%changelog
* Mon Jul 09 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.4.4-alt1.132640.71
- Build for kernel-image-ovz-el-2.6.32-alt71.

* Mon Jul 09 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.4.4-alt1
- 5.4.4

* Sun Feb 05 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.2.1-alt1
- 5.2.1

* Fri Oct 15 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Wed Feb 17 2010 Alexey Shabalin <shaba@altlinux.ru> 4.1.3-alt1
- fisrt build for Sisyphus
