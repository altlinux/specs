%define module_name	txgbe
%define module_version	1.3.6.9
%define module_release	alt1

%define flavour 6.18
%define karch   x86_64 loongarch64

BuildRequires(pre): kernel-headers-modules-6.18
%setup_kernel_module %flavour

# install the module to /lib/modules/RELEASE/updates, to override
# the module with the same name that comes with kernel-image
%define install_mod_dir updates
%define module_dir /lib/modules/%kversion-%flavour-%krelease/%install_mod_dir

Summary: Wangxun 10 Gigabit Ethernet driver
Name:    kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2.0
Group: System/Kernel and hardware

ExclusiveOS: Linux
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
%make_build -C src KSRC=%_usrsrc/linux-%kversion-%flavour

%install
%make_build -C %_usrsrc/linux-%kversion-%flavour M=$(pwd)/src \
	INSTALL_MOD_PATH=%buildroot INSTALL_MOD_DIR=%install_mod_dir \
	modules_install

%files
%module_dir/%module_name.ko*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Mar 24 2026 Ivan A. Melnikov <iv@altlinux.org> 1.3.6.9-alt1
- 1.3.6.9
- linux v6.17+ compatibility

* Tue Jul 29 2025 Ivan A. Melnikov <iv@altlinux.org> 1.3.6.7-alt1
- Initial build for ALT.
