%def_without check

Name: kernel-image-rk3588
Release: alt1
%define kernel_src_version	6.12
%define kernel_base_version	6.12
%define kernel_sublevel	.58
%define kernel_extra_version	%nil
%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
%define kernel_latest	latest
Version: %kversion

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; expr + "$s" : '[[:digit:]]\\+\\.[[:digit:]]\\+$' >/dev/null && s=def; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	%__gcc_version_base

%def_disable domU

#Remove oss
%def_disable oss
## Don't edit below this line ##################################

%define modules_dir	/lib/modules/%kversion-%flavour-%krelease
%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*
%add_verify_elf_skiplist %modules_dir/*

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: http://www.kernel.org/
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: %name-%version-%release.patch
# Armbian patches
Patch0001: 0001-Import-DTS-from-Armbian.patch
Patch0002: add-board-helios64.patch
Patch0003: board-firefly-rk3399-dts.patch
Patch0004: board-helios64-dts-fix-stability-issues.patch
Patch0005: board-helios64-remove-pcie-ep-gpios.patch
Patch0006: board-nanopc-t4-add-typec-dp.patch
Patch0007: board-nanopi-m4v2-dts-add-sound-card.patch
Patch0008: board-nanopi-r2c-plus.patch
Patch0009: board-nanopi-r2s.patch
Patch0010: board-nanopi-r3s-fix-leds.patch
Patch0011: board-nanopi-r4s-pwmfan.patch
Patch0012: board-odroidm1-add-nodes-for-i2c-pwm-uart-spi.patch
Patch0013: board-orangepi3b-add-uwe5622-wifi-bt-nodes.patch
Patch0014: board-orangepi-r1-plus.patch
Patch0015: board-orangepi-rk3399-pcie.patch
Patch0016: board-pbp-add-dp-alt-mode.patch
Patch0017: board-radxa-e25-sdmmc0-fix.patch
Patch0018: board-radxa-e25-usb3-and-emmc-fix.patch
Patch0019: board-rk3328-roc-cc-dts-enable-dmc.patch
Patch0020: board-rk3328-roc-cc-dts-ram-profile.patch
Patch0021: board-rk3328-roc-pc-dts-ram-profile.patch
Patch0022: board-rk3328-roc-pc.patch
Patch0023: board-rock3a-0001-emmc-sfc.patch
Patch0024: board-rock3a-0002-usb3.patch
Patch0025: board-rock3a-0003-add-gpio-names.patch
Patch0026: board-rock64-mail-supply.patch
Patch0027: board-rockpi3-enable-dmc.patch
Patch0028: board-rockpi4-0003-arm64-dts-pcie.patch
Patch0029: board-rockpis-dts-fixes.patch
Patch0030: board-rockpro64-0001-Add-pcie-bus-scan-delay.patch
Patch0031: board-rockpro64-change-rx_delay-for-gmac.patch
Patch0032: board-rockpro64-fix-emmc.patch
Patch0033: board-rockpro64-fix-spi1-flash-speed.patch
Patch0034: board-rockpro64-work-led-heartbeat.patch
Patch0035: board-rocks0-0001-deviceTree.patch
Patch0036: board-rocks0-0002-Revert-arm64-dts-rockchip-Fix-sdmmc-access-on-rk3308.patch
Patch0037: board-station-m2.patch
Patch0038: board-station-p2.patch
Patch0039: drivers-regulator-fan53555-bug-fixed.patch
Patch0040: drv-spi-spidev-remove-warnings.patch
Patch0041: general-add-hdmi-mks-ips50-resolutions.patch
Patch0042: general-add-miniDP-dt-doc.patch
Patch0043: general-add-miniDP-virtual-extcon.patch
Patch0044: general-add-overlay-compilation-support.patch
Patch0045: general-add-overlay-configfs.patch
Patch0046: general-add-panel-simple-dsi.patch
Patch0047: general-add-pll-hdmi-timings.patch
Patch0048: general-add-xtx-spi-nor-chips.patch
Patch0049: general-clk-rockchip-rk3568-Add-PLL-rate-for-33.3MHz.patch
Patch0050: general-cryptov1-trng.patch
Patch0051: general-disable-mtu-validation.patch
Patch0052: general-driver-tm16xx-led-driver.patch
Patch0053: general-fix-es8316-kernel-panic.patch
Patch0054: general-fix-inno-usb2-phy-init.patch
Patch0055: general-fix-mmc-signal-voltage-before-reboot.patch
Patch0056: general-hdmi-clock-fixes.patch
Patch0057: general-increase-spdif-dma-burst.patch
Patch0058: general-increasing_DMA_block_memory_allocation_to_2048.patch
Patch0059: general-pl330-01-fix-periodic-transfers.patch
Patch0060: general-pl330-02-add-support-for-interleaved-transfers.patch
Patch0061: general-pl330-04-bigger-mcode-buffer.patch
Patch0062: general-pl330-05-fix-unbalanced-power-down.patch
Patch0063: general-pl330-06-fix-buffer-underruns.patch
Patch0064: general-possibility-of-disabling-rk808-rtc.patch
Patch0065: general-rk3328-dtsi-trb-ent-quirk.patch
Patch0066: general-rk808-configurable-switch-voltage-steps.patch
Patch0067: general-rockchip-overlays.patch
Patch0068: general-rt5651-add-mclk.patch
Patch0069: general-st7796-driver.patch
Patch0070: general-v4l2-iep-driver.patch
Patch0071: general-v4l2-rkvdec-00-fixes.patch
Patch0072: general-v4l2-rkvdec-01-vp9.patch
Patch0073: general-v4l2-rkvdec-02-hevc.patch
Patch0074: general-workaround-broadcom-bt-serdev.patch
Patch0075: kernel-6.8-tools-cgroup-makefile.patch
Patch0076: media-0001-Add-rkvdec2-Support-v3.patch
Patch0077: media-0002-v4l2-core-Initialize-h264-frame_mbs_only_flag-.patch
Patch0078: media-0003-rk3568-disable-hantro-h264.patch
Patch0079: net-usb-r8152-add-LED-configuration-from-OF.patch
Patch0080: regulator-add-fan53200-driver.patch
Patch0081: rk3308-0001-pinctrl-slew-mux.patch
Patch0082: rk3308-0003-pinctrl-io-voltage-domains.patch
Patch0083: rk3308-acodec-vendor-driver.patch
Patch0084: rk3308-add-gmac-alias.patch
Patch0085: rk3308-add-missing-i2s-controllers.patch
Patch0086: rk3308-add-tsadc-driver.patch
Patch0087: rk3308-dts-legacy-cryptov2.patch
Patch0088: rk3308-dts-thermal-zones.patch
Patch0089: rk3308-fix-uart-dma.patch
Patch0090: rk3308-i2s-default-rate.patch
Patch0091: rk3308-internal-rgb-lcdc.patch
Patch0092: rk3308-vop-output.patch
Patch0093: rk3328-add-dmc-driver.patch
Patch0094: rk3328-add-rga-node.patch
Patch0095: rk3328-dtsi-mali-opp-table.patch
Patch0096: rk3328-dtsi-spdif.patch
Patch0097: rk3328-dtsi-usb3-reset-properties.patch
Patch0098: rk3328-gpu-cooling-target.patch
Patch0099: rk3328-roc-cc-add-missing-nodes.patch
Patch0100: rk3399-add-sclk-i2sout-src-clock.patch
Patch0101: rk3399-dmc-polling-rate.patch
Patch0102: rk3399-enable-dwc3-xhci-usb-trb-quirk.patch
Patch0103: rk3399-fix-pci-lanes.patch
Patch0104: rk3399-fix-pci-phy.patch
Patch0105: rk3399-fix-usb-phy.patch
Patch0106: rk3399-rp64-pcie-Reimplement-rockchip-PCIe-bus-scan-delay.patch
Patch0107: rk3399-sd-drive-level-8ma.patch
Patch0108: rk3399-sd-pwr-pinctrl.patch
Patch0109: rk3399-unlock-temperature.patch
Patch0110: rk356x-add-rkvdec2-support.patch
Patch0111: rk3588-0010-fix-clk-divisions.patch
Patch0112: rk3588-0011-irqchip-fix-its-timeout-issue.patch
Patch0113: rk3588-0113-add-synopsys-designware-hdmi-rx-controller.patch
Patch0114: rk3588-0132-phy-phy-rockchip-samsung-hdptx-Add-FRL-EARC-support.patch
Patch0115: rk3588-0135-arm64-dts-rockchip-Add-HDMI0-bridge-CLK-to-rk3588.patch
Patch0116: rk3588-0140-drm-bridge-synopsys-Add-DW-HDMI-QP-TX-Controller-support-library.patch
Patch0117: rk3588-0141-dt-bindings-display-rockchip-Add-schema-for-RK3588-HDMI-TX-Controller.patch
Patch0118: rk3588-0142-drm-rockchip-Add-basic-RK3588-HDMI-output-support.patch
Patch0119: rk3588-0170-drm-rockchip-vop2-add-clocks-reset-support.patch
Patch0120: rk3588-0801-wireless-add-bcm43752.patch
Patch0121: rk3588-0802-wireless-add-clk-property.patch
Patch0122: rk3588-1010-arm64-dts-rock-5b-Slow-down-emmc-to-hs200-and-add-ts.patch
Patch0123: rk3588-1012-arm64-dts-rockchip-Enable-HDMI0-on-rock-5b.patch
Patch0124: rk3588-1013-arm64-dts-rockchip-disable-emmc-hs400-for-rock-5-itx.patch
Patch0125: rk3588-1014-arm64-dts-rockchip-Make-use-of-HDMI0-PHY-PLL-on-rock5b.patch
Patch0126: rk3588-1020-Add-HDMI-and-VOP2-to-Rock-5A.patch
Patch0127: rk3588-1021-arch-arm64-dts-enable-gpu-node-for-rock-5a.patch
Patch0128: rk3588-1031-arm64-dts-rockchip-Add-HDMI-support-to-ArmSoM-Sige7.patch
Patch0129: rk3588-1032-arm64-dts-rockchip-Add-ap6275p-wireless-support-to-A.patch
Patch0130: rk3588-1040-board-khadas-edge2-add-nodes.patch
Patch0131: rk3588-1041-board-khadas-edge2-mcu.patch
Patch0132: rk3588-1051-board-nanopc-t6-Add-FAN-support.patch
Patch0133: rk3588-1052-board-nanopc-t6-Add-HDMI-support.patch
Patch0134: rk3588-1053-board-nanopc-t6-fix-usb3-a.patch
Patch0135: rk3588-1060-arm64-dts-rockchip-Split-pcie30x1m1-pinctrl.patch
Patch0136: rk3588-1060-board-cm3588-nas-Add-HDMI-support.patch
Patch0137: rk3588-1061-arm64-dts-rockchip-Add-PCIe-3.0-pinctrl-to-Turing-RK.patch
Patch0138: rk3588-1062-arm64-dts-rockchip-Enable-GPU-node-on-Turing-RK1.patch
Patch0139: rk3588-1063-arm64-dts-rockchip-Enable-automatic-fan-control-on-t.patch
Patch0140: rk3588-1064-arm64-dts-rockchip-Add-missing-hym8563-clock-frequen.patch
Patch0141: rk3588-1071-arm64-dts-Add-missing-nodes-to-Orange-Pi-5-Plus.patch
Patch0142: rk35xx-montjoie-crypto-v2-rk35xx.patch
Patch0143: wifi-4003-add-bcm43342-chip.patch
Patch0144: wifi-4003-ssv-6051-driver.patch

# ALT Patches
Patch2000: 2000-OrangePI5-Enable-UART0-and-pps_gpio.patch

ExclusiveArch: aarch64

%define make_target Image
%define image_path arch/%base_arch/boot/%make_target
%define arch_dir %base_arch
%define kvm_modules_dir arch/%arch_dir/kvm

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist /boot/vmlinuz-*

%define _unpackaged_files_terminate_build 1
%ifnarch ppc64le
%define _stripped_files_terminate_build 1
%endif

ExclusiveOS: Linux

Requires(pre,postun): bootloader-utils
Requires(pre,postun): kmod
Requires(pre,postun): mkinitrd

BuildRequires(pre): rpm-build-kernel
BuildRequires: banner
BuildRequires: bc
BuildRequires: dwarves >= 1.16
BuildRequires: flex
BuildRequires: gcc%kgcc_version
BuildRequires: gcc%kgcc_version-c++
BuildRequires: gcc%kgcc_version-plugin-devel
BuildRequires: kernel-source-%kernel_src_version
BuildRequires: kmod
BuildRequires: libdb4-devel
BuildRequires: libelf-devel
BuildRequires: libgmp-devel
BuildRequires: libmpc-devel
BuildRequires: lzma-utils
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: rsync
BuildRequires: zlib-devel
BuildRequires: u-boot-tools
Provides: kernel-modules-ipset-%flavour = %version-%release
Provides: kernel-modules-kvdo-%flavour = %version-%release
%if_enabled ccache
BuildRequires: ccache
%endif
%ifdef use_ccache
BuildRequires: ccache
%endif

%description
This package contains the Linux kernel %kernel_base_version that is used to boot and run
your system and supports ARM Rockchip SoC rk3588.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common
AutoReqProv: nocpp

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).

Since Linux 2.6.18 the kernel build system supports creation of
sanitized kernel headers for use in userspace (by deleting headers
which are not usable in userspace and removing #ifdef __KERNEL__
blocks from installed headers).  This package contains sanitized
headers instead of raw kernel headers which were present in some
previous versions of similar packages.

If possible, try to use glibc-kernheaders instead of this package.

%package -n kernel-headers-modules-%flavour
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel
Requires: gcc%kgcc_version
AutoReqProv: nocpp

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source
directory.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_src_version
tar -xf %kernel_src/kernel-source-%kernel_src_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_src_version
%define _default_patch_flags -s
%autopatch -p1

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

%build
banner build
export ARCH=%base_arch
export NPROCS=%__nprocs
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper
make -s kernelversion | grep -Fx '%kversion-%flavour-%krelease'

#configuration construction
CONFIGS="config config-rk3588"
scripts/kconfig/merge_config.sh -m $CONFIGS

%make_build oldconfig
%{?kconfig_hook}
make -s kernelrelease | grep -Fx '%kversion-%flavour-%krelease'
%make_build %make_target || {
	%make %make_target V=1
	exit 1
}
%make_build modules || {
	%make modules V=1
	exit 1
}
%ifarch aarch64
%make_build dtbs
%endif

echo "Kernel built $KernelVer"

%install
banner install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 %image_path \
	%buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

%make_build modules_install INSTALL_MOD_PATH=%buildroot

install -d %buildroot%modules_dir/updates

# Move some modules to kernel-image package tree
# rmi2-core deps
install -d %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/common/videobuf2/ %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/mc/ %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/v4l2-core/videodev.ko* %buildroot%modules_dir/kernel/drivers/media-core/
# other deps
mv %buildroot%modules_dir/kernel/drivers/media/rc/rc-core.ko* %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/dvb-core/dvb-core.ko* %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/radio/tea575x.ko* %buildroot%modules_dir/kernel/drivers/media-core/

make dtbs_install INSTALL_DTBS_PATH=%buildroot/boot/devicetree/$KernelVer

mkdir -p %buildroot%kbuild_dir/arch/%arch_dir
install -d %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir/include
cp -a arch/%arch_dir/include %buildroot%kbuild_dir/arch/%arch_dir
# Delete CONFIG_ files and stray .cmds
find %buildroot%kbuild_dir/include/config -name '[0-9A-Z]*' -delete
find %buildroot%kbuild_dir -name '*.cmd' -delete

# drivers-headers install
install -d %buildroot%kbuild_dir/drivers/scsi
install -d %buildroot%kbuild_dir/drivers/md
install -d %buildroot%kbuild_dir/drivers/usb/core
install -d %buildroot%kbuild_dir/drivers/net/wireless
install -d %buildroot%kbuild_dir/net/mac80211
install -d %buildroot%kbuild_dir/kernel
install -d %buildroot%kbuild_dir/lib
cp -a drivers/md/dm*.h \
	%buildroot%kbuild_dir/drivers/md/
cp -a drivers/usb/core/*.h \
	%buildroot%kbuild_dir/drivers/usb/core/
cp -a drivers/net/wireless/Kconfig \
	%buildroot%kbuild_dir/drivers/net/wireless/
cp -a lib/hexdump.c %buildroot%kbuild_dir/lib/
cp -a kernel/workqueue.c %buildroot%kbuild_dir/kernel/
cp -a net/mac80211/ieee80211_i.h \
	%buildroot%kbuild_dir/net/mac80211/
cp -a net/mac80211/sta_info.h \
	%buildroot%kbuild_dir/net/mac80211/

# Remove -Werror from Makefile for external modules
sed -i '/^KBUILD_.* += -Werror$/,+2d' Makefile

# Install files required for building external modules (in addition to headers)
KbuildFiles="
	Makefile
	Module.symvers
	arch/%arch_dir/Makefile
	scripts/pnmtologo
	scripts/mod/modpost
	scripts/mkmakefile
	scripts/mkversion
	scripts/link-vmlinux.sh
	scripts/mod/mk_elfconfig
	scripts/kconfig/conf
	scripts/mkcompile_h
	scripts/makelst
	scripts/Makefile.*
	scripts/Makefile
	scripts/modules-check.sh
	scripts/Kbuild.include
	scripts/kallsyms
	scripts/genksyms/genksyms
	scripts/basic/fixdep
	scripts/basic/hash
	scripts/extract-ikconfig
	scripts/conmakehash
	scripts/checkversion.pl
	scripts/checkincludes.pl
	scripts/checkconfig.pl
	scripts/bin2c
	scripts/gcc-version.sh
	scripts/gcc-goto.sh
	scripts/module.lds
	scripts/recordmcount.pl
	scripts/recordmcount.h
	scripts/recordmcount.c
	scripts/recordmcount
	scripts/gcc-x86_*-has-stack-protector.sh
	scripts/module-common.c
	scripts/module-common.lds
	scripts/subarch.include
	scripts/depmod.sh
	scripts/gcc-plugins/*.so
	scripts/ld-version.sh
	scripts/pahole-flags.sh
	scripts/check-local-export
	tools/objtool/objtool

	.config
	.kernelrelease
	gcc_version.inc
	System.map
       arch/%arch_dir/kernel/module.lds
"
for f in $KbuildFiles; do
	[ -e "$f" ] || continue
	[ -x "$f" ] && mode=755 || mode=644
	install -Dp -m$mode "$f" %buildroot%kbuild_dir/"$f"
done

# Fix symlinks to kernel sources in /lib/modules
rm -f %buildroot%modules_dir/{build,source}
ln -s %kbuild_dir %buildroot%modules_dir/build

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
%make_build headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

#provide symlink to autoconf.h for back compat
pushd %buildroot%old_kbuild_dir/include/linux
ln -s ../generated/autoconf.h
ln -s ../generated/utsrelease.h
ln -s ../generated/uapi/linux/version.h
popd

# ghostify *.bin files
truncate -s0 %buildroot%modules_dir/modules.*.bin

%check
banner check
# First boot-test no matter have KVM or not.
timeout 300 vm-run --loglevel=debug --append='earlycon oops=panic panic_on_warn=1' \
	'uname -a'
# Longer LTP tests only if there is KVM (which is present on all main arches).
if ! timeout 999 vm-run --kvm=cond --klog --append='altha=1 oops=panic panic_on_warn=1' \
	runltp -f kernel-alt-vm -S skiplist-alt-vm -o out; then
	cat /usr/lib/ltp/output/LTP_RUN_ON-out.failed >&2
	sed '/TINFO/i\\' /usr/lib/ltp/output/out | awk '/TFAIL/' RS= >&2
	exit 1
fi

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
%dir %modules_dir
%modules_dir/modules.alias
%modules_dir/modules.builtin
%modules_dir/modules.builtin.modinfo
%modules_dir/modules.dep
%modules_dir/modules.devname
%modules_dir/modules.order
%modules_dir/modules.*dep
%modules_dir/modules.symbols
%ghost %modules_dir/modules.*.bin
%defattr(0600,root,root,0700)
%modules_dir/updates
%modules_dir/kernel
%exclude %modules_dir/build
/boot/devicetree/%kversion-%flavour-%krelease

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir/
%modules_dir/build

%changelog
* Fri Nov 14 2025 Alexei Takaseev <taf@altlinux.org> 6.12.58-alt1
- v6.12.58 (2025-11-13).
- In order to support rk3588j, CONFIG_NVMEM_ROCKCHIP_OTP has to be set to Y
- config: CONFIG_SOUNDWIRE_AMD=m
- config: CONFIG_SND_SOC_AMD_ACP_COMMON=m
- config: Unset CONFIG_BASE_SMALL
- spec: Add %kconfig_hook macro invocation just after oldconfig

* Mon Nov 03 2025 Alexei Takaseev <taf@altlinux.org> 6.12.57-alt1
- v6.12.57 (2025-11-02).

* Fri Oct 31 2025 Alexei Takaseev <taf@altlinux.org> 6.12.56-alt1
- v6.12.56 (2025-10-29).

* Fri Oct 24 2025 Alexei Takaseev <taf@altlinux.org> 6.12.55-alt1
- v6.12.55 (2025-10-23).

* Mon Oct 20 2025 Alexei Takaseev <taf@altlinux.org> 6.12.54-alt1
- v6.12.54 (2025-10-19).

* Thu Oct 16 2025 Alexei Takaseev <taf@altlinux.org> 6.12.53-alt1
- v6.12.53 (2025-10-15).
- arm64: rockchip: Add Thin_88RK-1A Board support.
- config: Enable ZONE_DEVICE, DEVICE_PRIVATE, HSA_AMD_SVM, GPIO_PCA953X_IRQ, CONFIG_RTC_DRV_RX8111=m

* Mon Oct 13 2025 Alexei Takaseev <taf@altlinux.org> 6.12.52-alt1
- v6.12.52 (2025-10-12).
- config: enable all accelerometers.
- config: Enable PS4/PS5 controllers.

* Tue Oct 07 2025 Alexei Takaseev <taf@altlinux.org> 6.12.51-alt1
- v6.12.51 (2025-10-06).
- config: Enable CONFIG_HID_UNIVERSAL_PIDFF=m.
- config-rk3588: CONFIG_REGULATOR_AXP20X=y.

* Fri Oct 03 2025 Alexei Takaseev <taf@altlinux.org> 6.12.50-alt1
- v6.12.50 (2025-10-02).

* Fri Sep 26 2025 Alexei Takaseev <taf@altlinux.org> 6.12.49-alt1
- v6.12.49 (2025-09-25).

* Sat Sep 20 2025 Alexei Takaseev <taf@altlinux.org> 6.12.48-alt1
- v6.12.48 (2025-09-19).

* Sun Sep 14 2025 Alexei Takaseev <taf@altlinux.org> 6.12.47-alt1
- v6.12.47 (2025-09-11).

* Fri Aug 29 2025 Alexei Takaseev <taf@altlinux.org> 6.12.44-alt1
- v6.12.44 (2025-08-28).
- config: Build NVME as a module instead of built-in.
- config: Disable CONFIG_PSI_DEFAULT_DISABLED (reset to the default value)
- Add patch:
    * rk3588-1051-board-nanopc-t6-Add-FAN-support.patch
    * rk3588-1053-board-nanopc-t6-fix-usb3-a.patch
- Update patch:
    * general-v4l2-rkvdec-01-vp9.patch
    * rk3588-1052-board-nanopc-t6-Add-HDMI-support.patch
- Remove patch:
    * rk3588-1051-board-nanopc-t6-Add-USB3-psu-and-fan-support.patch

* Fri Aug 22 2025 Alexei Takaseev <taf@altlinux.org> 6.12.43-alt1
- v6.12.43 (2025-08-20).
- config: Enable RTRS and Security Infiniband options.
- config: Enable more VFIO drivers.
- config: Enable more Mellanox ConnectX options.

* Sat Aug 16 2025 Alexei Takaseev <taf@altlinux.org> 6.12.42-alt1
- v6.12.42 (2025-08-15).
- config: Enable CONFIG_LEGACY_VSYSCALL_XONLY=y (ALT#55552).
- kiosk: add secureexec parameter.
- pcie-baikal: forced enable dma-coherent for pcie on Baikal-M.
- config: Enable NVMe TCP TLS and AUTH for host and target.
- config: Enable CONFIG_MLX5_DPLL=m.

* Sat Aug 02 2025 Alexei Takaseev <taf@altlinux.org> 6.12.41-alt1
- v6.12.41 (2025-08-01).
- config: Enable CONFIG_MTK_T7XX=m.

* Tue Jul 29 2025 Alexei Takaseev <taf@altlinux.org> 6.12.40-alt1
- v6.12.40 (2025-07-24).
- Update 0001-Import-DTS-from-Armbian.patch
- Remove patch add-board-fine3399-dts.patch
- Update patches:
    * board-rockpis-dts-fixes.patch
    * rk3588-0132-phy-phy-rockchip-samsung-hdptx-Add-FRL-EARC-support.patch

* Sat Jul 12 2025 Alexei Takaseev <taf@altlinux.org> 6.12.37-alt1
- v6.12.37 (2025-07-10).
- config: Enable CONFIG_BUG_ON_DATA_CORRUPTION=y.
- config: Enable CONFIG_DEBUG_WX=y.
- config: Enable CONFIG_SND_SOC_SOF_AMD_ACP70=m.

* Sat Jun 28 2025 Alexei Takaseev <taf@altlinux.org> 6.12.35-alt1
- v6.12.35 (2025-06-27).
- config: Disable CONFIG_NL80211_TESTMODE.
- config: Enable more RTW88 hardware

* Fri Jun 20 2025 Alexei Takaseev <taf@altlinux.org> 6.12.34-alt1
- v6.12.34 (2025-06-19).
- config: Enable more MediaTek wireless devices (ALT#54848).
- config: Enable build drivers for Software Defined Radio devices.
- config: Enable CONFIG_LEGACY_VSYSCALL_NONE=y.
- Split one big patch to original files from Armbian git
- Resolve conflict between 5aac41632fffe7eb4708d9e88e203a2cb13283c9 and
  rk3588-0132-phy-phy-rockchip-samsung-hdptx-Add-FRL-EARC-support.patch

* Wed Jun 11 2025 Alexei Takaseev <taf@altlinux.org> 6.12.33-alt1
- v6.12.33 (2025-06-10).

* Thu Jun 05 2025 Alexei Takaseev <taf@altlinux.org> 6.12.32-alt1
- v6.12.32 (2025-06-04).

* Sat May 31 2025 Alexei Takaseev <taf@altlinux.org> 6.12.31-alt1
- v6.12.31 (2025-05-29).
- config: enable more led-trigger configs config-aarch64: enable config
  of mchp23 spi sram.
- spec: Fix packaging modules.weakdep appeared after kmod update.
- config: Enable CONFIG_INIT_STACK_ALL_ZERO=y
- Update DTS for Rockchip from Armbian
- Update 0002-Armbian_rockchip64-6.12.patch

* Fri May 23 2025 Alexei Takaseev <taf@altlinux.org> 6.12.30-alt1
- v6.12.30 (2025-05-22).

* Mon May 19 2025 Alexei Takaseev <taf@altlinux.org> 6.12.29-alt1
- v6.12.29 (2025-05-18).

* Sat May 10 2025 Alexei Takaseev <taf@altlinux.org> 6.12.28-alt1
- v6.12.28 (2025-05-09).
- config-rk3588: Undo from 6.12.24-alt1 Disable No Safety Features Timestamping in PHY devices
- config-rk3588: CONFIG_IRQ_TIME_ACCOUNTING=y

* Tue May 06 2025 Alexei Takaseev <taf@altlinux.org> 6.12.27-alt1
- v6.12.27 (2025-05-05).

* Fri May 02 2025 Alexei Takaseev <taf@altlinux.org> 6.12.26-alt1
- v6.12.26 (2025-05-02).

* Mon Apr 28 2025 Alexei Takaseev <taf@altlinux.org> 6.12.25-alt1
- v6.12.25 (2025-04-25).

* Mon Apr 21 2025 Alexei Takaseev <taf@altlinux.org> 6.12.24-alt1
- v6.12.24 (2025-04-20).
- config-rk3588: Disable No Safety Features Timestamping in PHY devices
- config-rk3588: Remove obsolete REISERFS, ISDN-related and ATM-related modules and configuration options

* Fri Apr 11 2025 Alexei Takaseev <taf@altlinux.org> 6.12.23-alt1
- v6.12.23 (2025-04-10).

* Mon Apr 07 2025 Alexei Takaseev <taf@altlinux.org> 6.12.22-alt1
- v6.12.22 (2025-04-07).
- config: add prefix DISPLAY for CONFIG_DRM_DP_CEC, DRM_DP_AUX_CHARDEV.
- config: Enable CONFIG_SND_SOC_INTEL_AVS=m (ALT#53634).

* Mon Mar 31 2025 Alexei Takaseev <taf@altlinux.org> 6.12.21-alt1
- v6.12.21 (2025-03-28).
- arm64: dts: rockchip: add dts to support NP-504a board.
- config-rk3588: add some NIC, WiFi and USB devices

* Sun Mar 23 2025 Alexei Takaseev <taf@altlinux.org> 6.12.20-alt1
- v6.12.20 (2025-03-22).
- config: Disable obsolete input tablet drivers.
- config-aarch64: enable more configs of battery and charger.
- arm64: add dts for SoM NMS-SM-RK3568 and computer VSNF.466459.001 on
  its basis.

* Fri Mar 14 2025 Alexei Takaseev <taf@altlinux.org> 6.12.19-alt1
- v6.12.19 (2025-03-13).

* Sat Mar 08 2025 Alexei Takaseev <taf@altlinux.org> 6.12.18-alt1
- v6.12.18 (2025-03-07).
- Use overlays for change DTS

* Fri Feb 28 2025 Alexei Takaseev <taf@altlinux.org> 6.12.17-alt1
- v6.12.17 (2025-02-27).
- kiosk: MIN_UID 500 -> 1000.

* Thu Feb 27 2025 Alexei Takaseev <taf@altlinux.org> 6.12.16-alt2
- Sync patches with Amrbian rockchip64
- Merge all Armbian patches to one
- Sync kernel config woth Armbian rockchip64

* Sat Feb 22 2025 Alexei Takaseev <taf@altlinux.org> 6.12.16-alt1
- v6.12.16 (2025-02-21).

* Tue Feb 18 2025 Alexei Takaseev <taf@altlinux.org> 6.12.15-alt1
- v6.12.15 (2025-02-18).

* Tue Feb 18 2025 Alexei Takaseev <taf@altlinux.org> 6.12.14-alt1
- v6.12.14 (2025-02-17).
- Disable BLK_DEV_FD.
- config: Enable CONFIG_DRM_PANIC=y.

* Mon Feb 10 2025 Alexei Takaseev <taf@altlinux.org> 6.12.13-alt1
- v6.12.13 (2025-02-08).
- config: Enable CONFIG_TMPFS_INODE64=y.

* Mon Feb 03 2025 Alexei Takaseev <taf@altlinux.org> 6.12.12-alt1
- v6.12.12 (2025-02-01).

* Fri Jan 24 2025 Alexei Takaseev <taf@altlinux.org> 6.12.11-alt1
- v6.12.11 (2025-01-23).

* Sat Jan 18 2025 Alexei Takaseev <taf@altlinux.org> 6.12.10-alt1
- v6.12.10 (2025-01-17).

* Fri Jan 10 2025 Alexei Takaseev <taf@altlinux.org> 6.12.9-alt1
- v6.12.9 (2025-01-09).

* Mon Jan 06 2025 Alexei Takaseev <taf@altlinux.org> 6.12.8-alt1
- v6.12.8 (2025-01-02).

* Sun Dec 29 2024 Alexei Takaseev <taf@altlinux.org> 6.12.7-alt1
- v6.12.7 (2024-12-27).
- config: Enable more zram compression backends.
    * CONFIG_ACPI_APEI_EINJ=y
    * CONFIG_XEN_NETDEV_FRONTEND=m
    * CONFIG_DW_WATCHDOG=y
    * CONFIG_TRUSTED_KEYS=y

* Wed Dec 25 2024 Alexei Takaseev <taf@altlinux.org> 6.12.6-alt2
- build rockchip pmic drivers as built-in:
    * CONFIG_REGMAP_SPI=y
    * CONFIG_MFD_RK8XX=y
    * CONFIG_MFD_RK8XX_I2C=y
    * CONFIG_MFD_RK8XX_SPI=y
    * CONFIG_REGULATOR_RK808=y
    * CONFIG_PHY_ROCKCHIP_SNPS_PCIE3=y

* Fri Dec 20 2024 Alexei Takaseev <taf@altlinux.org> 6.12.6-alt1
- v6.12.6 (2024-12-19).

* Sun Dec 15 2024 Alexei Takaseev <taf@altlinux.org> 6.12.5-alt1
- Enable PREEMPT for low latency GPIO
- Use config-rk3588 and common config
- Build for rk3588
- Add patches from Armbian
