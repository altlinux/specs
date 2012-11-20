%define gcc_ver 4.7
%define module_name	blcr
%define module_version	0.8.3
%define module_release	alt2

%define kversion	2.6.32
%define krelease	alt25
%define flavour		hpc-skif

%define module_dir /lib/modules/%kversion-%flavour-%krelease/extra

%define _unpackaged_files_terminate_build 1

Summary: Berkeley Lab Checkpoint/Restart for Linux modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.25

Url: https://ftg.lbl.gov/CheckpointRestart/CheckpointRestart.shtml
License: GPL2
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>


Prereq:         kernel-image-%flavour = %kversion-%krelease
Prereq:   coreutils
Requires(postun): kernel-image-%flavour = %kversion-%krelease

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: gcc%gcc_ver-c++

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release
BuildRequires: kernel-source-blcr = %module_version
ExclusiveArch: %ix86 x86_64

%description 
Linux kernel modules for Berkeley Lab Checkpoint/Restart (BLCR).

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%set_gcc_version %gcc_ver
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
./configure \
	--with-kmod-dir=%module_dir \
	--with-installed-util \
	--with-installed-libcr \
	--with-components=modules \
	--disable-init-script \
	--with-linux=%kversion-%flavour-%krelease \
	--with-linux-src=%_usrsrc/linux-%kversion-%flavour-%krelease/ \
	--with-system-map=/usr/src/linux-%kversion-%flavour-%krelease/System.map
for m in %{module_name}_imports cr_module; do
	%make_build -C $m
done
#make_build SUBARCH=x86

%install
for m in %{module_name}_imports cr_module; do
	%make_install -C $m DESTDIR=%buildroot install
done
#make install DESTDIR=%buildroot SUBARCH=x86

%post 
%post_kernel_modules %kversion-%flavour-%krelease

%postun 
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%module_dir/*

%changelog
* Tue Nov 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt2.132640.25
- Build for kernel-image-hpc-skif-2.6.32-alt25.

* Tue Nov 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt2
- Version 0.8.3

* Mon Jul 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1
- Version 0.8.2

* Wed Jun 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.1
- Intial build for Sisyphus

