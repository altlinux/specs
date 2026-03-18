%define module_name mt7902e

Name: kernel-source-%module_name
Version: 0.0.1
Release: alt1

Summary: Linux kernel module source for MediaTek MT7902E WiFi adapter

License: GPL-2.0-only
Group: Development/Kernel
URL: https://github.com/hmtheboy154/mt7902
# Source-url: https://github.com/hmtheboy154/mt7902/archive/refs/heads/backport.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-kernel

%description
Source code for the MediaTek MT7902E PCIe WiFi driver kernel module.
This is the mt76 driver with patches to support MT7902 hardware.

The module will be built automatically by kernel-build-tools
when building kernel packages.

%package -n firmware-%module_name
Summary: Firmware for MediaTek MT7902E WiFi adapter
Group: System/Kernel and hardware
BuildArch: noarch

%description -n firmware-%module_name
Firmware files for the MediaTek MT7902E PCIe WiFi adapter.

%prep
%setup

%install
# kernel module source
mkdir -p %kernel_srcdir
cd ..
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version
cd %name-%version

# firmware
mkdir -p %buildroot/lib/firmware/mediatek/%module_name/
install -m644 firmware/*.bin %buildroot/lib/firmware/mediatek/%module_name/

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n firmware-%module_name
/lib/firmware/mediatek/%module_name/

%changelog
* Mon Mar 16 2026 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- initial build for ALT Sisyphus
