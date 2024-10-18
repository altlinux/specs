%define module_name    mpi3mr
%define module_version 8.10.0.5.0
%define module_release alt1

%define flavour		6.6
%define karch		x86_64 aarch64

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-6.6

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
Epoch: 1

Summary: Broadcom Limited Avenger MR8.10 Linux Driver
License: GPL-2.0
Group: System/Kernel and hardware
Url: https://docs.broadcom.com/docs/LINUX_DRIVER_8.10.0.5.0-1.zip

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Broadcom Limited Avenger MR8.10 Linux Driver.

Supported Controllers
* Avenger 9600-16e
* Avenger 9600-8i8e
* Avenger 9600-16i
* Avenger 9600-24i
* Avenger 9600w-16e
* Avenger 9620-16i
* Avenger 9660-16i
* Avenger 9670W-16i
* Avenger 9670-24i

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make -C %_usrsrc/linux-%kversion-%flavour-%krelease \
    M=$(pwd)

%install
install -d %buildroot/%module_dir
cp -a %module_name.ko %buildroot/%module_dir/

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %epoch:%version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
