%define module_name             netup
%define module_version          0.0.1
%define module_release          alt1

%define kernel_base_version	3.14
%define kernel_extra_version_numeric	1.0.0

%define flavour		std-def
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: NetUP Universal Dual DVB-CI card module for Linux kernel
License: GPLv2
Group: System/Kernel and hardware
Url: http://www.netup.tv/en-EN/netup-universal-dual-dvb-ci

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
%module_name NetUP Universal Dual DVB-CI card module for Linux kernel

%prep
rm -rf %module_name-%module_version
tar -jxvf %kernel_src/%module_name-%module_version.tar.bz2

rm -rf kernel-source-%kernel_base_version
tar -jxf %kernel_src/kernel-source-%kernel_base_version.tar.bz2

%setup -D -T -n %module_name-%module_version

pushd ../kernel-source-%kernel_base_version
    cp -R drivers/media/dvb-core/*.h ../%module_name-%module_version/dvb-frontends
popd


%build
export KDIR=%_usrsrc/linux-%kversion-%flavour
export FEDIR=`pwd`/dvb-frontends

make -C dvb-frontends
make -C netup_unidvb

%install
install -d %buildroot/%module_dir
install -m644 -D dvb-frontends/*.ko %buildroot/%module_dir
install -m644 -D netup_unidvb/*.ko %buildroot/%module_dir

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Sat Mar 21 2015 Alexei Takaseev <taf@altlinux.org> 0.0.1-alt1
- Initial buld for ALT Linux
