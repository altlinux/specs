%define _unpackaged_files_terminate_build 1

Name: firmware-linux-altemu
Version: 20260601
Release: alt1
Summary: Set of firmware files used by the Linux kernel for ARM-based game consoles
License: GPL-2.0-or-later MIT
# Also Redistributable, no modification permitted


Group: System/Kernel and hardware
Url: https://gitlab.com/kernel-firmware/linux-firmware
# https://lore.kernel.org/linux-firmware/

Source: %name-%version.tar

BuildArch: noarch
Provides: linux-firmware-altemu

BuildRequires: hardlink
BuildRequires: parallel /proc
BuildRequires: python3
Requires: udev
AutoReqProv: no

%add_verify_elf_skiplist /lib/firmware/*

%description
Kernel-firmware includes firmware files
required for some devices to operate.

%package RTL8188FU
Group: System/Kernel and hardware
Summary: firmware for Realtek 8188FU wifi/bluetooth chip
Url: https://github.com/ROCKNIX/distribution/tree/next/projects/ROCKNIX/packages/linux-firmware/kernel-firmware/extra-firmware/rtl_bt
AutoProv: no
AutoReq: no symlinks

%description RTL8188FU
firmware for Realtek 8188FU wifi/bluetooth chip

%package anbernic-panels
Group: System/Kernel and hardware
Summary: firmware for displays in Anbernic consoles
Url: https://github.com/ROCKNIX/distribution/tree/next/projects/ROCKNIX/packages/linux-firmware/kernel-firmware/extra-firmware/panels
AutoProv: no
AutoReq: no symlinks

%description anbernic-panels
firmware for displays in Anbernic consoles

%package cirrus-cs35l41
Group: System/Kernel and hardware
Summary: firmware for Cirrus Logic CS35L41
Url: https://github.com/ROCKNIX/distribution/tree/next/projects/ROCKNIX/packages/linux-firmware/kernel-firmware/extra-firmware/cirrus
AutoProv: no
AutoReq: no symlinks

%description cirrus-cs35l41
firmware for Cirrus Logic CS35L41

%package rockchip-rk322x
Group: System/Kernel and hardware
Summary: firmware for Broadcom-based Wi-Fi/Bluetooth modules in Rockchip-based SBCs
Url: https://github.com/armbian/firmware
AutoProv: no
AutoReq: no symlinks

%description rockchip-rk322x
firmware for Broadcom-based Wi-Fi/Bluetooth modules in Rockchip-based SBCs

%prep
%setup

%install

DESTDIR=%buildroot FIRMWAREDIR=lib/firmware %make_build install-xz
du -shc %buildroot/lib/firmware
hardlink -y memcmp -c %buildroot/lib/firmware

%files
%doc  WHENCE LICENCE.ueagle LICENCE.rtlwifi_firmware.txt LICENSE.cirrus
/lib/firmware
%exclude /lib/firmware/rtl_bt/*
%exclude /lib/firmware/anbernic-panels/*
%exclude /lib/firmware/cirrus/*
%exclude /lib/firmware/brcm/*
%exclude /lib/firmware/eagle_fw*

%files RTL8188FU
%doc LICENCE.rtlwifi_firmware.txt
/lib/firmware/rtl_bt

%files anbernic-panels
%dir /lib/firmware/anbernic-panels
/lib/firmware/anbernic-panels/*

%files cirrus-cs35l41
%doc LICENSE.cirrus
/lib/firmware/cirrus

%files rockchip-rk322x
%doc LICENCE.ueagle
/lib/firmware/eagle_fw*
/lib/firmware/brcm

%changelog
* Mon Jun  1 2026 Artyom Bystrov <arbars@altlinux.org> 20260601-alt1
- Inital build for SIsyphus (based on linux-firmware by vt@)