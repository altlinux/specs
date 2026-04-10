%define module_name	yt6801
%define module_version	1.0.31
%define module_release	alt2

%define flavour 6.12
%define karch   x86_64 loongarch64

BuildRequires(pre): kernel-headers-modules-6.12
%setup_kernel_module %flavour

%define install_mod_dir kernel/drivers/net/ethernet/motorcomm
%define module_dir /lib/modules/%kversion-%flavour-%krelease/%install_mod_dir

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
%make_build -C %_usrsrc/linux-%kversion-%flavour M=$(pwd)/src \
	modules

%install
%make_build -C %_usrsrc/linux-%kversion-%flavour M=$(pwd)/src \
	INSTALL_MOD_PATH=%buildroot INSTALL_MOD_DIR=%install_mod_dir \
	modules_install

%files
%module_dir/%module_name.ko*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Thu Apr 02 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.31-alt2
- Move module file back to drivers/net/ethernet (ALT#58491)

* Fri Mar 13 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.31-alt1
- 1.0.31.

* Mon Mar 17 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.29-alt2
- Use modules_install target to install module (enables compression
  for certain kernels).
- Install the module under kernel/drivers/net/ethernet.

* Mon Mar 17 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.29-alt1
- Initial build for ALT.
