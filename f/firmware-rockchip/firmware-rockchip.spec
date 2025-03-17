%define git_commit 794da2662def953ddd64cd8ac14298571b797326

%add_findprov_skiplist /lib/firmware/*
%add_findreq_skiplist /lib/firmware/*

Name: firmware-rockchip
Version: 20231105
Release: alt1.git794da26

Summary: Specific firmware for ARM Rockhip SoC
License: GPL-2.0-or-later and MIT and Redistributable, no modification permitted
Group: System/Kernel and hardware

URL: https://github.com/Joshua-Riek/firmware
Packager: Nazarov Denis <nenderus@altlinux.org>

BuildArch: noarch

# https://github.com/Joshua-Riek/firmware/archive/%git_commit/firmware-%git_commit.tar.gz
Source: firmware-%git_commit.tar

BuildRequires: firmware-bcm4345
BuildRequires: firmware-linux

Requires: firmware-bcm4345
Requires: firmware-linux

%description
Specific firmware for ARM Rockhip SoC

%prep
%setup -n firmware-%git_commit

%install
%__mkdir_p %buildroot/lib/firmware
%__cp -r * %buildroot/lib/firmware/

# Remove duplicate and unnecessary files
%__rm -r %buildroot/lib/firmware/{brcm/brcmfmac43456-sdio.{bin,clm_blob,txt},debian,README.md}

# Fix symlinks
pushd %buildroot/lib/firmware/rtl_bt
ln -sf rtl8821cs_config.bin.xz rtl8821cs_config
ln -sf rtl8821cs_fw.bin.xz rtl8821cs_fw
popd

%files
%doc README.md
/lib/firmware

%changelog
* Mon Mar 17 2025 Nazarov Denis <nenderus@altlinux.org> 20231105-alt1.git794da26
- Initial build for ALT Linux
