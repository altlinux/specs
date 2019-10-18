%define module_name     usb-vhci
%define module_version  1.15
%define module_release  alt1
%define flavour         std-def
%define karch %ix86 x86_64 aarch64 ppc64le

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: USB Virtual Host Controller Driver (VHCI)
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Epoch: %(echo %kepoch | sed s/://)
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
Url: https://sourceforge.net/p/usb-vhci/vhci_hcd/ci/master/tree/

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Requires: dmsetup
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
USB Virtual Host Controller Driver (VHCI).

%prep
rm -rf %module_name-%module_version
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar*
%setup -D -T -n %module_name-%module_version

%build
make KDIR=/lib/modules/*/build

%install
install -d %buildroot/%module_dir
install -m644 -D usb-vhci-hcd.ko usb-vhci-iocifc.ko %buildroot/%module_dir/

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %kepoch%version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
