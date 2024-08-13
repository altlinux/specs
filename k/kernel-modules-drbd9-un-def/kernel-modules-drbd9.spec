%define module_name     drbd9
%define module_version  9.2.11
%define module_release  alt1
%define flavour         un-def
%define karch x86_64 aarch64 ppc64le

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/updates
%add_verify_elf_skiplist %module_dir/*

Summary: Kernel driver for DRBD
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Epoch: 1
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2+
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
Url: http://www.drbd.org/

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-un-def
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: coccinelle >= 1.0.8
Requires: dmsetup
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Kernel driver for DRBD

%prep
rm -rf %module_name-%module_version
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar*

%setup -D -T -n %module_name-%module_version

%build
#sed -i s/SUBDIRS=/M=/g Makefile
make -C drbd KDIR=/lib/modules/*/build

%install
install -d %buildroot/%module_dir
# Before 5.4: drbd/build-current/drbd-kernel-compat/handshake/handshake.ko
install -m644 -D drbd/build-current/drbd*.ko %buildroot/%module_dir/

%files
%module_dir/*.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %epoch:%version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
