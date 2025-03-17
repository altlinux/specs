%define module_name	bcmdhd
%define module_release	alt1.k
%define module_version	101.10.591.52.27

%define flavour rk
%define karch aarch64

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/drivers/net/wireless/rockchip_wlan/rkwifi/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Linux driver for wireless adapters based on the Broadcom ap6xxx chipset.
License: GPLv2+
Group: System/Kernel and hardware

URL: https://github.com/armbian/%module_name-dkms/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %karch

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-rk

BuildRequires: module-init-tools
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

%description
Linux driver for wireless adapters based on the Broadcom ap6xxx chipset.

%package -n kernel-modules-%module_name-sdio-%flavour
Summary: Linux driver for wireless adapters based on the Broadcom ap6xxx chipset.
Group: System/Kernel and hardware
Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
%requires_kimage
Requires: %module_name-blacklist
Requires: firmware-rockchip

%description -n kernel-modules-%module_name-sdio-%flavour
Linux driver for wireless adapters based on the Broadcom ap6xxx chipset.

This package provides SDIO interface driver.

%package -n kernel-modules-%module_name-pcie-%flavour
Summary: Linux driver for wireless adapters based on the Broadcom ap6xxx chipset.
Group: System/Kernel and hardware
%requires_kimage
Requires: %module_name-blacklist
Requires: firmware-rockchip

%description -n kernel-modules-%module_name-pcie-%flavour
Linux driver for wireless adapters based on the Broadcom ap6xxx chipset.

This package provides PCI-E interface driver.

%package -n kernel-modules-%module_name-usb-%flavour
Summary: Linux driver for wireless adapters based on the Broadcom ap6xxx chipset.
Group: System/Kernel and hardware
%requires_kimage
Requires: %module_name-blacklist
Requires: firmware-rockchip

%description -n kernel-modules-%module_name-usb-%flavour
Linux driver for wireless adapters based on the Broadcom ap6xxx chipset.

This package provides USB interface driver.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%__mkdir altbuild
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc

# Build SDIO interface
%make_build -C %_usrsrc/linux-%kversion-%flavour M=${PWD} CONFIG_BCMDHD_SDIO=y CONFIG_BCMDHD_PCIE= CONFIG_BCMDHD_USB=
%__cp %{module_name}_sdio.ko altbuild/
%__cp dhd_static_buf_sdio.ko altbuild/
%make clean

# Build PCI-E interface
%make_build -C %_usrsrc/linux-%kversion-%flavour M=${PWD} CONFIG_BCMDHD_SDIO= CONFIG_BCMDHD_PCIE=y CONFIG_BCMDHD_USB=
%__cp %{module_name}_pcie.ko altbuild/
%__cp dhd_static_buf_pcie.ko altbuild/
%make clean

# Build USB interface
%make_build -C %_usrsrc/linux-%kversion-%flavour M=${PWD} CONFIG_BCMDHD_SDIO= CONFIG_BCMDHD_PCIE= CONFIG_BCMDHD_USB=y
%__cp %{module_name}_usb.ko altbuild/
%__cp dhd_static_buf_usb.ko altbuild/
%make clean

%install
%__install -Dp -m600 altbuild/%{module_name}_sdio.ko %buildroot/%module_dir/%{module_name}_sdio.ko
%__install -Dp -m600 altbuild/dhd_static_buf_sdio.ko %buildroot/%module_dir/dhd_static_buf_sdio.ko
%__install -Dp -m600 altbuild/%{module_name}_pcie.ko %buildroot/%module_dir/%{module_name}_pcie.ko
%__install -Dp -m600 altbuild/dhd_static_buf_pcie.ko %buildroot/%module_dir/dhd_static_buf_pcie.ko
%__install -Dp -m600 altbuild/%{module_name}_usb.ko %buildroot/%module_dir/%{module_name}_usb.ko
%__install -Dp -m600 altbuild/dhd_static_buf_usb.ko %buildroot/%module_dir/dhd_static_buf_usb.ko

%files -n kernel-modules-%module_name-sdio-%flavour
%module_dir/%{module_name}_sdio.ko
%module_dir/dhd_static_buf_sdio.ko

%files -n kernel-modules-%module_name-pcie-%flavour
%module_dir/%{module_name}_pcie.ko
%module_dir/dhd_static_buf_pcie.ko

%files -n kernel-modules-%module_name-usb-%flavour
%module_dir/%{module_name}_usb.ko
%module_dir/dhd_static_buf_usb.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Mar 17 2025 Nazarov Denis <nenderus@altlinux.org> 101.10.591.52.27-alt1.k
- Initial build for ALT Linux
