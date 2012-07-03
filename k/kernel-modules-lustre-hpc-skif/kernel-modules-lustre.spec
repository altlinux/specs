%define module_name	lustre
%define module_version	1.8.4
%define module_release	alt1

%define kversion	2.6.32
%define krelease	alt24
%define flavour		hpc-skif

%define module_dir /lib/modules/%kversion-%flavour-%krelease

%define _unpackaged_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

Summary: Modules of Lustre FS
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.24

Url: https://ftg.lbl.gov/CheckpointRestart/CheckpointRestart.shtml
License: GPL2
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>


Prereq:         kernel-image-%flavour = %kversion-%krelease
Prereq:   coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %version-%release
Requires(postun): %name = %version-%release
Requires(postun): kernel-image-%flavour = %kversion-%krelease

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: libnet-snmp-devel perl-devel quilt %mpiimpl gcc-c++
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
%ifarch %ix86
BuildRequires: ElectricFence
%endif

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release
BuildRequires: kernel-source-lustre = %module_version
ExclusiveArch: %ix86 x86_64

%description 
Modules of Lustre FS.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
# do not even try to build ldiskfs modules here
echo -e 'all:\n\nsources:\n' > ldiskfs/Makefile.in
touch ldiskfs/Module.symvers

%build
%configure --enable-modules --with-linux=%_usrsrc/linux-%kversion-%flavour-%krelease \
	--enable-server --enable-ext4 --enable-quota --enable-health-write --enable-lru-resize \
	--enable-adaptive-timeouts --enable-mpitest=%mpidir \
%ifarch %ix86
	--enable-efence \
%endif
	--target=%_target
%make_build modules

%install
mkdir -p %buildroot%buildroot%module_dir
find . -type f -name \*.ko |cpio -pmd %buildroot%module_dir

%post 
%post_kernel_modules %kversion-%flavour-%krelease

%postun 
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir/*

%changelog
* Wed Oct 20 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.4-alt1.132640.24
- Build for kernel-image-hpc-skif-2.6.32-alt24.

* Fri Oct 01 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Wed Nov 11 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.1.1-alt1
- 1.8.1.1

* Sun Jul 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0.1-alt1
- Intial build for Sisyphus
