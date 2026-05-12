%define _unpackaged_files_terminate_build 1

Name: firmware-oneplus-sdm845
Version: 1
Release: alt1
Summary: OnePlus 6(t) firmware files
License: Distributable
Group: System/Kernel and hardware
Url: https://gitlab.com/sdm845-mainline/firmware-oneplus-sdm845
VCS: https://gitlab.com/sdm845-mainline/firmware-oneplus-sdm845.git
ExclusiveArch: aarch64

Source: %name-%version.tar

Requires: firmware-linux

%add_verify_elf_skiplist /lib/firmware/*

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot/lib/firmware/oneplus-sdm845/qca
cp -rv lib/firmware/qcom %buildroot/lib/firmware
cp -rv lib/firmware/qca %buildroot/lib/firmware
cp -v lib/firmware/postmarketos/tfa98xx.cnt %buildroot/lib/firmware
# This file conflicts with firmware-linux. Custom fw search path required!
cp -v lib/firmware/postmarketos/qca/crbtfw21.tlv %buildroot/lib/firmware/oneplus-sdm845/qca

%files
/lib/firmware

%changelog
* Sat May 09 2026 Vasiliy Doylov <neko@altlinux.org> 1-alt1
- Initial build for ALT
