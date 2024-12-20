%def_without check

Name: kernel-image-rk3588
Release: alt1
%define kernel_src_version	6.12
%define kernel_base_version	6.12
%define kernel_sublevel	.6
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
Patch0001: 0000-Import-DTS-from-Armbian.patch
Patch0002: 0001-general-add-overlay-support.patch
Patch0003: 0002-tools-disable-sched_ext_clean.patch
Patch0010: 0010-fix-clk-divisions.patch
Patch0011: 0011-irqchip-fix-its-timeout-issue.patch
Patch0024: 0024-RK3588-Add-Crypto-Support.patch
Patch0027: 0027-RK3588-Add-rkvdec2-Support-v3.patch
Patch0028: 0028-media-v4l2-core-Initialize-h264-frame_mbs_only_flag-.patch
Patch0113: 0113-add-synopsys-designware-hdmi-rx-controller.patch
Patch0132: 0132-phy-phy-rockchip-samsung-hdptx-Add-FRL-EARC-support.patch
Patch0133: 0133-drm-rockchip-vop2-Improve-display-modes-handling.patch
Patch0135: 0135-arm64-dts-rockchip-Add-HDMI0-bridge-CLK-to-rk3588.patch
Patch0140: 0140-drm-bridge-synopsys-Add-DW-HDMI-QP-TX-Controller-support-library.patch
Patch0141: 0141-dt-bindings-display-rockchip-Add-schema-for-RK3588-HDMI-TX-Controller.patch
Patch0142: 0142-drm-rockchip-Add-basic-RK3588-HDMI-output-support.patch
Patch0170: 0170-drm-rockchip-vop2-add-clocks-reset-support.patch
Patch0801: 0801-wireless-add-bcm43752.patch
Patch0802: 0802-wireless-add-clk-property.patch
Patch1010: 1010-arm64-dts-rock-5b-Slow-down-emmc-to-hs200-and-add-ts.patch
Patch1012: 1012-arm64-dts-rockchip-Enable-HDMI0-on-rock-5b.patch
Patch1014: 1014-arm64-dts-rockchip-Make-use-of-HDMI0-PHY-PLL-on-rock5b.patch
Patch1020: 1020-Add-HDMI-and-VOP2-to-Rock-5A.patch
Patch1021: 1021-arch-arm64-dts-enable-gpu-node-for-rock-5a.patch
Patch1031: 1031-arm64-dts-rockchip-Add-HDMI-support-to-ArmSoM-Sige7.patch
Patch1032: 1032-arm64-dts-rockchip-Add-ap6275p-wireless-support-to-A.patch
Patch1040: 1040-board-khadas-edge2-add-nodes.patch
Patch1041: 1041-board-khadas-edge2-mcu.patch
Patch1051: 1051-board-nanopc-t6-Add-USB3-psu-and-fan-support.patch
Patch1052: 1052-board-nanopc-t6-Add-HDMI-support.patch
Patch1059: 1060-arm64-dts-rockchip-Split-pcie30x1m1-pinctrl.patch
Patch1060: 1060-board-cm3588-nas-Add-HDMI-support.patch
Patch1061: 1061-arm64-dts-rockchip-Add-PCIe-3.0-pinctrl-to-Turing-RK.patch
Patch1062: 1062-arm64-dts-rockchip-Enable-GPU-node-on-Turing-RK1.patch
Patch1063: 1063-arm64-dts-rockchip-Enable-automatic-fan-control-on-t.patch
Patch1064: 1064-arm64-dts-rockchip-Add-missing-hym8563-clock-frequen.patch
Patch1071: 1071-arm64-dts-Add-missing-nodes-to-Orange-Pi-5-Plus.patch
# ALT Patches
Patch2000: 2000-OrangePI5-Enable-UART0-and-pps_gpio.patch

ExclusiveArch: aarch64

%define make_target Image
%define image_path arch/%base_arch/boot/%make_target
%define arch_dir %base_arch
%define kvm_modules_dir arch/%arch_dir/kvm

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
your system and supports ARM Rockhip SoC rk3588.

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

#configuration construction
CONFIGS="config config-rk3588"
scripts/kconfig/merge_config.sh -m $CONFIGS

%make_build oldconfig
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

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist /boot/vmlinuz-*

%define _unpackaged_files_terminate_build 1

%check
banner check
# First boot-test no matter have KVM or not.
timeout 300 vm-run --loglevel=debug --append=earlycon --heredoc <<-EOF
	uname -a
%if "%base_flavour" == "rt"
	rtcheck -v
%endif
EOF
# Longer LTP tests only if there is KVM (which is present on all main arches).
if ! timeout 999 vm-run --kvm=cond --klog --append=altha=1 \
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
%modules_dir/modules.softdep
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
* Fri Dec 20 2024 Alexei Takaseev <taf@altlinux.org> 6.12.6-alt1
- v6.12.6 (2024-12-19).

* Sun Dec 15 2024 Alexei Takaseev <taf@altlinux.org> 6.12.5-alt1
- Enable PREEMPT for low latency GPIO
- Use config-rk3588 and common config
- Build for rk3588
- Add patches from Armbian
