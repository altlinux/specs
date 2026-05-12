%define firmware_dir	/lib/firmware/aic8800_fw/SDIO/aic8800D80

Name: kernel-source-aic8800-sdio
Version: 5.0
Release: alt1.22a6531

Summary: aic8800-sdio kernel module

License: GPL-3.0
Group: Development/Kernel
URL: https://github.com/radxa-pkg/aic8800
VCS: https://github.com/radxa-pkg/aic8800

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source: %name-%version.tar
Patch0: fix-linux-6.1-build.patch
Patch1: fix-linux-6.5-build.patch
Patch2: fix-linux-6.7-build.patch
Patch3: fix-linux-6.9-build.patch
Patch4: fix-linux-6.13-build.patch
Patch5: fix-linux-6.14-build.patch
Patch6: fix-linux-6.15-build.patch
Patch7: fix-linux-6.16-build.patch
Patch8: fix-linux-6.17-build.patch
Patch9: fix-sdio-fall-through.patch
Patch10: fix-sdio-firmware-path.patch
Patch11: fix-Lower-the-debugging-log-level.patch
Patch12: fix-vmalloc-not-include.patch

BuildArch: noarch

BuildPreReq: kernel-build-tools

%description
Linux driver for AICSemi AIC8800D80, SDIO version.

%package -n firmware-aic8800-sdio
Summary: aic8800-sdio firmware
Group: System/Kernel and hardware
BuildArch: noarch

%description -n firmware-aic8800-sdio
Firmware for AICSemi AIC8800D80 WiFi chip, SDIO verison.

%prep
%setup -c -q
pushd %name-%version
sed -i 's/\r$//' src/USB/driver_fw/drivers/aic8800/aic_load_fw/aic_bluetooth_main.c
%autopatch -p1
popd

%install
# kernel-source-aic8800-sdio
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version/src/SDIO/driver_fw/driver

# firmware-aic8800-sdio
mkdir -p %buildroot%firmware_dir
install -m644 %name-%version/src/SDIO/driver_fw/fw/aic8800D80/* %buildroot%firmware_dir

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n firmware-aic8800-sdio
/lib/firmware/*

%changelog
* Wed Apr 08 2026 Vladislav Tatjanin <l27001@altlinux.org> 5.0-alt1.22a6531
- Initial build.
