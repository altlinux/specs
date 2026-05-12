%define _unpackaged_files_terminate_build 1

Name: firmware-xiaomi-beryllium
Version: 1
Release: alt1
Summary: Xiaomi POCO F1 firmware files
License: Distributable
Group: System/Kernel and hardware
Url: https://gitlab.com/sdm845-mainline/firmware-xiaomi-beryllium
VCS: https://gitlab.com/sdm845-mainline/firmware-xiaomi-beryllium.git
ExclusiveArch: aarch64

Source: %name-%version.tar

Requires: firmware-linux

%add_verify_elf_skiplist /lib/firmware/*

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot/lib/firmware
cp -rv lib/firmware/qcom %buildroot/lib/firmware
cp -v lib/firmware/tas2559_uCDSP.bin %buildroot/lib/firmware

%files
/lib/firmware

%changelog
* Sat May 09 2026 Vasiliy Doylov <neko@altlinux.org> 1-alt1
- Initial build for ALT
