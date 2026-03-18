%define module_name	mt7902e
%define module_version	0.0.1
%define module_release	alt1

%define flavour		6.12

BuildRequires(pre): kernel-headers-modules-6.12
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: MediaTek MT7902E WiFi kernel module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL-2.0-only
Group: System/Kernel and hardware
URL: https://github.com/hmtheboy154/mt7902

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

Requires: firmware-%module_name

%requires_kimage

ExclusiveArch: x86_64 aarch64

%description
MediaTek MT7902E PCIe WiFi driver kernel module.
Based on mt76 driver with patches to support MT7902 hardware.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour M=`pwd`/src V=1 modules

%install
install -d %buildroot%module_dir
install src/*.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Mar 16 2026 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- initial build for ALT Sisyphus
