%define module_name netatop
%define module_version 3.2.2
%define module_release alt1

%define flavour 6.12
%define karch x86_64 i586 aarch64
BuildRequires(pre): kernel-headers-modules-6.12
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/drivers/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: %module_name kernel module

License: GPL-2.0-only
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre,postun): coreutils
Requires(pre):    kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %karch

%description
Linux driver for netatop.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n .

%build
%make netatop.ko KERNDIR=%_usrsrc/linux-%kversion-%flavour

%install
mkdir -p %buildroot%module_dir
install netatop.ko %buildroot%module_dir

%files
%module_dir/netatop.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Wed Sep 10 2025 Leontiy Volodin <lvol@altlinux.org> 3.2.2-alt1
- Initial build for ALT Sisyphus (ALT #48546).
