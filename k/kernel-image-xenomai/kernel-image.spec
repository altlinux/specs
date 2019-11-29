%define flavour			xenomai
Name: kernel-image-%flavour
Release: alt3

%define kernel_base_version	4.14
# ipipe-core-4.14.134-x86-8
%define kernel_sublevel		.134
%define kernel_extra_version	%nil
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
# Numeric extra version scheme developed by Alexander Bokovoy:
# 0.0.X -- preX
# 0.X.0 -- rcX
# 1.0.0 -- release
%define kernel_extra_version_numeric 1.0.0

%define krelease	%release

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	%__gcc_version_base

# not for xenomai
%def_disable docs

#Remove oss
%def_disable oss
## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*

Summary: The Linux kernel %version with Xenomai real-time Cobalt core and I-pipe
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://xenomai.org/
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: stable-%version.patch
Patch1: ipipe-core-%version-x86-8.patch
Patch2: alt-%version-%release.patch

ExclusiveArch: x86_64

%define qemu_pkg %_arch
%ifarch %ix86 x86_64
 %define qemu_pkg x86
%endif
%ifarch ppc64le
 %define qemu_pkg ppc
%endif

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version gcc%kgcc_version-c++
BuildRequires: gcc%kgcc_version-plugin-devel libgmp-devel libmpc-devel
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric
BuildRequires: xenomai-kernel-source
BuildRequires: module-init-tools >= 3.16
BuildRequires: lzma-utils
BuildRequires: libelf-devel
BuildRequires: bc
BuildRequires: openssl-devel 
# for check
%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system-%qemu_pkg-core glibc-devel-static}}

%if_enabled docs
BuildRequires: python-module-sphinx perl-Pod-Usage 
%endif

%if_enabled ccache
BuildRequires: ccache
%endif

%ifdef use_ccache
BuildRequires: ccache
%endif

Requires: bootloader-utils >= 0.4.24-alt1
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.8.3-alt1

Provides: kernel = %kversion

Requires(pre,postun): coreutils
Requires(pre,postun): module-init-tools >= 3.1
Requires(pre,postun): mkinitrd >= 1:2.9.9-alt1

%description
This package contains the Linux kernel %version with Xenomai real-time
Cobalt core and Interrupt pipeline (I-pipe) patches.

Xenomai brings POSIX and traditional RTOS APIs for porting time-critical
applications to Linux-based platforms. When the native Linux kernel cannot meet
the response time requirements of the application, Xenomai supplements it with
Cobalt, a small real-time infrastructure which schedules time-critical
activities independently from the main kernel logic.

The Cobalt real-time core depends on the Interrupt pipeline (I-pipe) patch to
the mainline Linux kernel, which introduces a separate, high-priority execution
stage for running out-of-band interrupt handlers immediately upon IRQ receipt,
which cannot be delayed by the regular kernel work.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel %name-%version-%release
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).

%package -n kernel-headers-modules-%flavour
Summary: Files needed for building modules for Linux kernel %name-%version-%release
Group: Development/Kernel 
Requires: gcc%kgcc_version
Requires: libelf-devel

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source directory.


%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -s -p1
%patch1 -s -p1
%patch2 -s -p1

# ALT glibc contains strlcpy, so we need disable it there:
sed -i /strlcpy/d tools/include/linux/string.h

/usr/src/xenomai-kernel-source/scripts/prepare-kernel.sh --arch=%_arch

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

chmod +x tools/objtool/sync-check.sh

%build
export ARCH=%base_arch
export NPROCS=%__nprocs
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper

# Configuration construction
%make_build defconfig
scripts/config -e IKCONFIG

scripts/config -e IPIPE
scripts/config -e XENOMAI

# All options from Xenomai .travis.yml except DEBUG
scripts/config -e XENO_OPT_SCHED_CLASSES
scripts/config -e XENO_OPT_SCHED_WEAK
scripts/config -e XENO_OPT_SCHED_TP
scripts/config -e XENO_OPT_SCHED_SPORADIC
scripts/config -e XENO_OPT_SCHED_QUOTA
scripts/config -e XENO_OPT_SHIRQ
scripts/config -e XENO_OPT_SCALABLE_SCHED
scripts/config -e XENO_DRIVERS_16550A
scripts/config -e XENO_DRIVERS_16550A_ANY
scripts/config -e XENO_DRIVERS_16550A_PCI
scripts/config -e XENO_DRIVERS_16550A_PCI_MOXA
scripts/config -e XENO_DRIVERS_IMX_UART
scripts/config -e XENO_DRIVERS_RTDMTEST
scripts/config -e XENO_DRIVERS_CAN
scripts/config -e XENO_DRIVERS_CAN_LOOPBACK
scripts/config -e XENO_DRIVERS_CAN_VIRT
scripts/config -e XENO_DRIVERS_CAN_FLEXCAN
scripts/config -e XENO_DRIVERS_CAN_SJA1000
scripts/config -e XENO_DRIVERS_CAN_SJA1000_ISA
scripts/config -e XENO_DRIVERS_CAN_SJA1000_MEM
scripts/config -e XENO_DRIVERS_CAN_SJA1000_PEAK_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_IXXAT_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_ADV_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_PLX_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_EMS_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_ESD_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_PEAK_DNG
scripts/config -m XENO_DRIVERS_NET
scripts/config -e XENO_DRIVERS_RTNET_CHECKED
scripts/config -e XENO_DRIVERS_NET_ETH_P_ALL
scripts/config -e XENO_DRIVERS_NET_RTIPV4_NETROUTING
scripts/config -e XENO_DRIVERS_NET_RTIPV4_ROUTER
scripts/config -m XENO_DRIVERS_NET_NOMAC
scripts/config -m XENO_DRIVERS_NET_DRV_PCNET32
scripts/config -m XENO_DRIVERS_NET_DRV_TULIP
scripts/config -e XENO_DRIVERS_NET_DRV_EEPRO100_DBG
scripts/config -m XENO_DRIVERS_NET_DRV_E1000E
scripts/config -m XENO_DRIVERS_NET_DRV_NATSEMI
scripts/config -m XENO_DRIVERS_NET_DRV_VIA_RHINE
scripts/config -m XENO_DRIVERS_NET_DRV_IGB
scripts/config -m XENO_DRIVERS_NET_DRV_R8169
scripts/config -m XENO_DRIVERS_NET_DRV_SMC91111
scripts/config -e XENO_DRIVERS_NET_EXP_DRIVERS
scripts/config -m XENO_DRIVERS_NET_DRV_3C59X
scripts/config -m XENO_DRIVERS_NET_DRV_E1000_NEW
scripts/config -m XENO_DRIVERS_NET_DRV_RT2500
scripts/config -m XENO_DRIVERS_NET_ADDON_RTCAP
scripts/config -m XENO_DRIVERS_NET_ADDON_PROXY
scripts/config -e XENO_DRIVERS_NET_ADDON_PROXY_ARP
scripts/config -e XENO_DRIVERS_ANALOGY
scripts/config -e XENO_DRIVERS_ANALOGY_FAKE
scripts/config -e XENO_DRIVERS_ANALOGY_NI_PCIMIO
scripts/config -e XENO_DRIVERS_ANALOGY_S526
scripts/config -e XENO_DRIVERS_RTIPC
scripts/config -e XENO_DRIVERS_UDD
scripts/config -e XENO_DRIVERS_GPIO
scripts/config -e XENO_DRIVERS_GPIO_BCM2835
scripts/config -e XENO_DRIVERS_GPIO_MXC
scripts/config -e XENO_DRIVERS_GPIO_SUN8I_H3
scripts/config -e XENO_DRIVERS_GPIO_ZYNQ7000
scripts/config -e XENO_DRIVERS_GPIO_XILINX
scripts/config -e XENO_DRIVERS_GPIOPWM
scripts/config -e XENO_DRIVERS_SPI_BCM2835
scripts/config -e XENO_DRIVERS_SPI_SUN6I

# Enable EFI handover support
scripts/config -e EFI
scripts/config -e EFI_STUB

scripts/config -m ISO9660_FS
scripts/config -m UDF_FS
scripts/config -m VFAT_FS

# For test SM box
scripts/config -m IGB
scripts/config -m DRM_AST
scripts/config -m I2C_PIIX4
scripts/config -m SENSORS_K10TEMP
scripts/config -m DRM_RADEON
scripts/config -m FB_RADEON
scripts/config -m USB_XHCI_HCD
scripts/config -m SCSI_DH
scripts/config -m SCSI_DH_EMC
scripts/config -m SCSI_DH_RDAC
scripts/config -m SCSI_DH_ALUA

scripts/config -m IPMI_SI
scripts/config -m IPMI_DEVICE_INTERFACE
scripts/config -m IPMI_HANDLER
scripts/config -m IPMI_SSIF
scripts/config -m IPMI_WATCHDOG

# Additional options
scripts/config -e CONFIG_USER_NS
scripts/config -e CONFIG_SQUASHFS -e CONFIG_SQUASHFS_XZ
scripts/config -e CONFIG_SCSI_VIRTIO -e CONFIG_SCSI_LOWLEVEL -e CONFIG_VIRTIO_PCI \
	       -e CONFIG_VIRTIO_BLK -e CONFIG_VIRTIO_NET -e CONFIG_VIRTIO_CONSOLE \
	       -e CONFIG_HW_RANDOM_VIRTIO -e CONFIG_VIRTIO_BALLOON
%ifarch %ix86 x86_64
scripts/config -e CONFIG_KGDB -e CONFIG_KGDB_KDB -e CONFIG_LKDTM
%endif

# Disable what is recommended in https://gitlab.denx.de/Xenomai/xenomai/wikis/Configuring_For_X86_Based_Dual_Kernels
scripts/config -d CONFIG_CPU_FREQ
scripts/config -d CONFIG_CPU_IDLE
scripts/config -d CONFIG_APM
scripts/config -d CONFIG_ACPI_PROCESSOR -d X86_INTEL_PSTATE -d SCHED_MC_PRIO
scripts/config -d CONFIG_INTEL_IDLE
scripts/config -d CONFIG_INPUT_PCSPKR

%make_build olddefconfig
egrep 'IPIPE|XENO' .config

# Verify that bad options are still disabled
grep -w -e ^CONFIG_CPU_FREQ \
	-e ^CONFIG_CPU_IDLE \
	-e ^CONFIG_APM \
	-e ^CONFIG_ACPI_PROCESSOR \
	-e ^CONFIG_INTEL_IDLE \
	-e ^CONFIG_INPUT_PCSPKR .config && exit 1

%make_build bzImage
%make_build modules

echo "Kernel built $KernelVer"

%if_enabled docs
# psdocs, pdfdocs don't work yet
%make_build htmldocs
%endif

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 arch/%base_arch/boot/bzImage \
	%buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

make modules_install INSTALL_MOD_PATH=%buildroot
find %buildroot -name '*.ko' | xargs gzip

mkdir -p %buildroot%kbuild_dir/arch/x86
install -d %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir/include
cp -a arch/x86/include %buildroot%kbuild_dir/arch/x86


# drivers-headers install
install -d %buildroot%kbuild_dir/drivers/scsi
install -d %buildroot%kbuild_dir/drivers/md
install -d %buildroot%kbuild_dir/drivers/usb/core
install -d %buildroot%kbuild_dir/drivers/net/wireless
install -d %buildroot%kbuild_dir/net/mac80211
install -d %buildroot%kbuild_dir/kernel
install -d %buildroot%kbuild_dir/lib
cp -a drivers/scsi/{{scsi,scsi_typedefs}.h,scsi_module.c} \
	%buildroot%kbuild_dir/drivers/scsi/
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

# Install files required for building external modules (in addition to headers)
KbuildFiles="
	Makefile
	Module.symvers
	arch/%base_arch/Makefile
%ifarch x86_64
	arch/x86/Makefile
	arch/x86/Makefile_32
	arch/x86/Makefile_32.cpu
	arch/x86/Makefile_64
%endif
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
	scripts/recordmcount.pl
	scripts/recordmcount.h
	scripts/recordmcount.c
	scripts/recordmcount
	scripts/gcc-x86_*-has-stack-protector.sh
	scripts/module-common.lds
	scripts/subarch.include
	scripts/depmod.sh
	scripts/gcc-plugins/*.so
	scripts/ld-version.sh
	tools/objtool/objtool

	.config
	.kernelrelease
	gcc_version.inc
	System.map
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
make headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

find %buildroot%kheaders_dir -name ..install.cmd -delete

#provide symlink to autoconf.h for back compat
pushd %buildroot%old_kbuild_dir/include/linux
ln -s ../generated/autoconf.h
ln -s ../generated/utsrelease.h
ln -s ../generated/uapi/linux/version.h
popd

# remove *.bin files
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin


%check
KernelVer=%kversion-%flavour-%krelease
mkdir -p test
cd test
msg='Booted successfully'
%__cc %optflags -s -static -xc -o init - <<__EOF__
#include <unistd.h>
#include <sys/reboot.h>
int main()
{
	static const char msg[] = "$msg\n";
	write(2, msg, sizeof(msg) - 1);
	reboot(RB_POWER_OFF);
	pause();
}
__EOF__
echo init | cpio -H newc -o | gzip -9n > initrd.img
QEMU=qemu-system-%_arch
QEMU_OPTS="-bios bios.bin -nographic -no-reboot -m 256M -initrd initrd.img"
CONSOLE=ttyS0
%ifarch %ix86
 QEMU=qemu-system-i386
%endif
%ifarch aarch64
 QEMU=qemu-system-aarch64
 QEMU_OPTS+=" -machine virt -cpu max"
 CONSOLE=ttyAMA0
%endif
%ifarch ppc64le
 QEMU=qemu-system-ppc64
 QEMU_OPTS+="-cpu power8,compat=power7"
 CONSOLE=hvc0
%endif
timeout --foreground 600 $QEMU $QEMU_OPTS -kernel %buildroot/boot/vmlinuz-$KernelVer -append "console=$CONSOLE panic=-1" > boot.log &&
grep -q "^$msg" boot.log &&
grep -qE '^(\[ *[0-9]+\.[0-9]+\] *)?reboot: Power down' boot.log || {
	cat >&2 boot.log
	echo >&2 'Marker not found'
	exit 1
}
grep -i -e I-pipe -e Xenomai boot.log
grep -q "head domain Xenomai registered" boot.log
grep -q "Cobalt v[0-9.]\+" boot.log
! grep -q "init failed" boot.log

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
%dir %modules_dir/
%defattr(0600,root,root,0700)
%modules_dir/*
%exclude %modules_dir/build
%ghost %modules_dir/modules.alias.bin
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols.bin
%ghost %modules_dir/modules.builtin.bin

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir/
%modules_dir/build

%changelog
* Fri Nov 29 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.134-alt3
- Enable kdb/kgdb/lkdtm on x86.

* Sun Nov 24 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.134-alt2
- Actually disable ACPI_PROCESSOR, CPU_FREQ, and CPU_IDLE
- Add more options based on -rt kernel experience.
- Enable virtio for debugging.
- Fix license tag and other minor spec changes.

* Sat Aug 24 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.134-alt1
- Update to ipipe-core-4.14.134-x86-8.
- Fix qemu run.

* Fri Jun 28 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.128-alt4
- Clean up ..install.cmd files (reported by repocop).

* Wed Jun 26 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.128-alt3
- Add filesystems required for fstab to finish system boot

* Tue Jun 25 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.128-alt2
- Enable EFI handover support
- Enable igb and some other drivers useful for SM

* Fri Jun 21 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.128-alt1
- v4.14.128 with spec based on kernel-image-std-def-4.14.104-alt1
- I-pipe 4.14.128 with Xenomai Cobalt
