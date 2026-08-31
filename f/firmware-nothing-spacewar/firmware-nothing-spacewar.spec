%define _unpackaged_files_terminate_build 1

Name: firmware-nothing-spacewar
Version: 1
Release: alt1
Summary: Nothing Phone (1) firmware files
License: Distributable
Group: System/Kernel and hardware
Url: https://github.com/mainlining/firmware-nothing-spacewar
VCS: https://github.com/mainlining/firmware-nothing-spacewar.git
ExclusiveArch: aarch64

Source: %name-%version.tar

Requires: firmware-linux

%add_verify_elf_skiplist /lib/firmware/*

%description
%summary.

%prep
%setup

%install
# This file obtained and converted from downstream android kernel
# https://github.com/NothingOSS/android_kernel_msm-5.4_nothing_sm7325/
install -pDm0644 focaltech_ts_novatek.bin %buildroot/lib/firmware/qcom/sm7325/nothing/spacewar/focaltech_ts_novatek.bin
# Any other firmware will be automatically loaded via droid-juicer.

%files
/lib/firmware

%changelog
* Sat Aug 29 2026 Vasiliy Doylov <neko@altlinux.org> 1-alt1
- Initial build for ALT.
