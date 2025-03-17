%define module_name	yt6801
%define module_version	1.0.29
%define module_release	alt1


%define flavour 6.12
%define karch   x86_64 loongarch64

BuildRequires(pre): kernel-headers-modules-6.12
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Driver for Motorcomm YT6801 ethernet adapter
Name:    kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2.0
Group: System/Kernel and hardware

ExclusiveOS: Linux
URL: https://www.motor-comm.com/product/ethernet-control-chip
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: bc

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre,postun): coreutils
Requires(pre):    kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %karch

%description
%summary.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%make_build KSRC=%_usrsrc/linux-%kversion-%flavour modules

%install
install -Dp -m600 src/%module_name.ko %buildroot/%module_dir/%module_name.ko

%files
%module_dir/%module_name.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Mar 17 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.29-alt1
- initial build for ALT
