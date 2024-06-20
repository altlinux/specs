%define module_name	ch341
%define git 84b4b8c
%define module_version	1.0.0
%define module_release	alt1.g%{git}

%define flavour		6.8
%define karch %ix86 x86_64 aarch64 ppc64le armh

BuildRequires(pre): kernel-headers-modules-6.8
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: ch341 kernel module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: https://github.com/frank-zago/ch341-i2c-spi-gpio
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

%requires_kimage

Requires: %{module_name}-blacklist

ExclusiveArch: %karch

Patch: spi-ch341-kernel-6.9.patch

%description
WinChipHead CH341 linux driver for I2C, SPI and GPIO mode

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%patch -p1

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour M=`pwd` V=1 modules

%install
install -d %buildroot%module_dir
install *.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Thu Jun 20 2024 L.A. Kostis <lakostis@altlinux.org> 1.0.0-alt1.g84b4b8c
- Initial build for Sisyphus.
