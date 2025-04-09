%define TRUSTED_FIRMWARE_DIR contrib/arm-trusted-firmware
%define U_BOOT_DIR contrib/u-boot-2020-04-rc3
%define HYP_DIR contrib/aw-el2-barebone
%define RBS_VER 1

%set_gcc_version 11

Name: u-boot-repka4
Version: 2020.04.rc3.%RBS_VER
Release: alt2

Summary: Boot Loader for Repka Pi 4
License: GPLv2+
Group: System/Kernel and hardware
Url: https://repka-pi.ru/
Vcs: https://gitflic.ru/project/npo_rbs/repka-os_boot-loader.git

ExclusiveArch: aarch64

Source: %name-%version.tar
Patch: %name-%version-alt-pylibfdt-fix-build.patch

BuildRequires: flex
BuildRequires: swig
BuildRequires: bc
BuildRequires: dtc
BuildRequires: python3-module-setuptools

%description
%summary.

%prep
%setup
%autopatch -p1

%build
pushd %TRUSTED_FIRMWARE_DIR
%make_build PLAT=sun50i_h6 PRELOADED_BL33_BASE=0x40010000 LDFLAGS='--no-warn-rwx-segment'
popd

pushd %HYP_DIR
%make_build CROSS_COMPILE=''
popd

cp -v %TRUSTED_FIRMWARE_DIR/build/sun50i_h6/release/bl31.bin %U_BOOT_DIR/
cp -v %HYP_DIR/el2-bb.bin %U_BOOT_DIR/hyp.bin
cp -v %U_BOOT_DIR/.configs/.config-not-silent %U_BOOT_DIR/.config
pushd %U_BOOT_DIR
%make_build BL31=./bl31.bin
popd

%install
install -Dpm0644 %U_BOOT_DIR/u-boot-sunxi-with-spl.bin -t %buildroot%_datadir/u-boot/repka_pi4/

%files
%doc README.*
%_datadir/u-boot/repka_pi4/*

%changelog
* Wed Apr 09 2025 Anton Kurachenko <srebrov@altlinux.org> 2020.04.rc3.1-alt2
- Switched to use gcc11.

* Tue Mar 25 2025 Anton Kurachenko <srebrov@altlinux.org> 2020.04.rc3.1-alt1
- Initial build for ALT Linux.
