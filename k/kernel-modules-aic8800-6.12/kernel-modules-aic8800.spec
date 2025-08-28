%define module_name aic8800
%define module_version 0.0.4.b4e4
%define module_release alt1

%define flavour 6.12
%define karch x86_64 aarch64 ppc64le loongarch64
BuildRequires(pre): kernel-headers-modules-6.12
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/drivers/net/wireless/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: %module_name kernel module

License: GPL-3.0-only
Group: System/Kernel and hardware

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
Linux driver for AICSemi AIC8800DC, ID a69c:88de.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
pushd drivers/aic8800
%make all KDIR=%_usrsrc/linux-%kversion-%flavour
popd

%install
pushd drivers/aic8800
%makeinstall_std \
  KDIR=%_usrsrc/linux-%kversion-%flavour \
  MODDESTDIR=%buildroot%module_dir
popd

%files
%module_dir/aic*.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Thu Aug 28 2025 Leontiy Volodin <lvol@altlinux.org> 0.0.4.b4e4-alt1.%kcode.%kbuildrelease
- Initial build for ALT Sisyphus (ALT #55709).
