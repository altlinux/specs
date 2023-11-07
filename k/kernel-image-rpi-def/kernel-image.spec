%def_without cross_toolchain_aarch64
%def_disable check
%def_disable docs
%def_disable domU

Name: kernel-image-rpi-def
Release: alt1
epoch:1
%define kernel_need_version	5.15
# Used when kernel-source-x.y does not currently exist in repository.
%define kernel_base_version	5.15
%define kernel_sublevel .92
%define kernel_extra_version	%nil
# kernel version is need version
Version: %kernel_need_version%kernel_sublevel%kernel_extra_version
# Numeric extra version scheme developed by Alexander Bokovoy:
# 0.0.X -- preX
# 0.X.0 -- rcX
# 1.0.0 -- release
%define kernel_extra_version_numeric 1.0.0

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	10

#Remove oss
%def_disable oss
## Don't edit below this line ##################################

%define kversion	%kernel_need_version%kernel_sublevel%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware
Url: http://www.kernel.org/
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

ExclusiveArch: aarch64

%define make_target Image
%ifarch %arm
%define make_target zImage
%endif

%define image_path arch/%base_arch/boot/%make_target

%define arch_dir %base_arch

%define kvm_modules_dir arch/%arch_dir/kvm

%define qemu_pkg %_arch

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: flex
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version gcc%kgcc_version-c++
BuildRequires: gcc%kgcc_version-plugin-devel libgmp-devel libmpc-devel
BuildRequires: module-init-tools >= 3.16
BuildRequires: lzma-utils
BuildRequires: libelf-devel
BuildRequires: bc
BuildRequires: rsync
BuildRequires: openssl-devel
BuildRequires: u-boot-tools
%if_with cross_toolchain_aarch64
BuildRequires: gcc-aarch64-linux-gnu
%endif

# for check
%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system-%qemu_pkg-core ipxe-roms-qemu glibc-devel-static}}
Provides:  kernel-modules-v4l-%kversion-%flavour-%krelease = %version-%release
Provides:  kernel-modules-staging-%kversion-%flavour-%krelease = %version-%release

%if_enabled docs
BuildRequires: python3-module-sphinx /usr/bin/sphinx-build perl-Pod-Usage python3-module-sphinx_rtd_theme
BuildRequires: fontconfig
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
Requires(pre): rpi4-boot-switch
Requires(pre): rpi4-boot-nouboot-filetrigger

Provides: kernel = %kversion

Requires(pre): coreutils
Requires(pre): module-init-tools >= 3.1
Requires(pre): mkinitrd >= 1:2.9.9-alt1

%description
This package contains the Linux kernel that is used to boot and run
your system.

Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).

There are some kernel variants in ALT systems:
* std-def: standard longterm kernel without preemption;
* std-pae: variant of std-def kernel for i686 with 64G memory support;
* std-debug: variant of std-def kernel kernel with some DEBUG options enabled;
* un-def: more modern then std-def and with voluntary (on ppc64le) and
  forced (on x86) preemption enabled.

%package -n kernel-image-domU-%flavour
Summary: Uncompressed linux kernel for XEN domU boot 
Group: System/Kernel and hardware
Requires(pre): coreutils
Requires(pre): module-init-tools >= 3.1

%description -n kernel-image-domU-%flavour
Most XEN virtualization system versions can not boot lzma-compressed
kernel images. This is an optional package with uncompressed linux
kernel image for this special case. If you do not know what is it XEN
it seems that you do not need this package.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version
#Provides: kernel-headers-%base_flavour = %version-%release

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
Requires: libelf-devel

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source
directory.

%package -n kernel-doc-%base_flavour
Summary: Linux kernel %kversion-%base_flavour documentation
Group: System/Kernel and hardware
BuildArch: noarch

%description -n kernel-doc-%base_flavour
This package contains documentation files for ALT Linux kernel packages:
 * kernel-image-%base_flavour-up-%kversion-%krelease
 * kernel-image-%base_flavour-smp-%kversion-%krelease

The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.

%prep
%setup
%patch0 -p1

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
%if_without cross_toolchain_aarch64
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile
%endif

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

chmod +x tools/objtool/sync-check.sh

%build
export ARCH=%base_arch
export NPROCS=%__nprocs
%if_with cross_toolchain_aarch64
export CROSS_COMPILE=aarch64-linux-gnu-
%endif
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper


#configuration construction

CONFIGS="config-%_target_cpu"

scripts/kconfig/merge_config.sh -m $CONFIGS

%make_build oldconfig
#%make_build include/linux/version.h
%make_build %make_target
%make_build modules
%make_build dtbs

echo "Kernel built $KernelVer"

%if_enabled docs
# psdocs, pdfdocs don't work yet
%make_build htmldocs
%endif

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 %image_path \
	%buildroot/boot/vmlinuz-$KernelVer
%if_enabled domU
install -Dp -m644 vmlinux %buildroot/boot/vmlinux-$KernelVer
%endif
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

make modules_install INSTALL_MOD_PATH=%buildroot
find %buildroot -name '*.ko' | xargs gzip

mkdir -p %buildroot/lib/devicetree/$KernelVer
find arch/%arch_dir/boot/dts -type f -name \*.dtb | xargs -iz install -pm0644 z %buildroot/lib/devicetree/$KernelVer

mkdir -p %buildroot/lib/devicetree/$KernelVer/overlays
find -L arch/%arch_dir/boot/dts/overlays -type f -name \*.dtbo | xargs -iz install -pm0644 z %buildroot/lib/devicetree/$KernelVer/overlays

mkdir -p %buildroot%kbuild_dir/arch/%arch_dir
install -d %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir/include
cp -a arch/%arch_dir/include %buildroot%kbuild_dir/arch/%arch_dir

# drivers-headers install
install -d %buildroot%kbuild_dir/drivers/scsi
install -d %buildroot%kbuild_dir/drivers/md
install -d %buildroot%kbuild_dir/drivers/usb/core
install -d %buildroot%kbuild_dir/drivers/net/wireless
install -d %buildroot%kbuild_dir/net/mac80211
install -d %buildroot%kbuild_dir/kernel
install -d %buildroot%kbuild_dir/lib
cp -a drivers/scsi/scsi.h \
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
make headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

#provide symlink to autoconf.h for back compat
pushd %buildroot%old_kbuild_dir/include/linux
ln -s ../generated/autoconf.h
ln -s ../generated/utsrelease.h
ln -s ../generated/uapi/linux/version.h
popd

# remove *.bin files
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,devname,softdep,symbols}

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%base_flavour-%version/
cp -a Documentation/* %buildroot%_docdir/kernel-doc-%base_flavour-%version/
%endif # if_enabled docs

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist /boot/vmlinuz-*


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
qemu_arch=%_arch
qemu_opts=""
console=ttyS0
%ifarch %ix86
qemu_arch=i386
%endif
%ifarch ppc64le
qemu_arch=ppc64
console=hvc0
%endif
%ifarch aarch64
qemu_opts="-machine accel=tcg,type=virt -cpu cortex-a57 -drive if=pflash,unit=0,format=raw,readonly,file=%_datadir/AAVMF/QEMU_EFI-pflash.raw"
%endif
timeout --foreground 600 qemu-system-"$qemu_arch" $qemu_opts -kernel %buildroot/boot/vmlinuz-$KernelVer -nographic -append console="$console" -initrd initrd.img > boot.log &&
grep -q "^$msg" boot.log &&
grep -qE '^(\[ *[0-9]+\.[0-9]+\] *)?reboot: Power down' boot.log || {
	cat >&2 boot.log
	echo >&2 'Marker not found'
	exit 1
}

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
/lib/devicetree/%kversion-%flavour-%krelease

%if_enabled domU
%files -n kernel-image-domU-%flavour
/boot/vmlinux-%kversion-%flavour-%krelease
%endif

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir/
%modules_dir/build

%if_enabled docs
%files -n kernel-doc-%base_flavour
%doc %_docdir/kernel-doc-%base_flavour-%version
%endif

%changelog
* Tue Nov 07 2023 Dmitry Terekhin <jqt4@altlinux.org> 1:5.15.92-alt1
- Updated to 5.15.92
- https://github.com/raspberrypi/linux.git rpi-5.15.y commit 14b35093ca68bf2c81bbc90aace5007142b40b40
- Add support for RBS Repka Pi 3 board

* Fri Oct 14 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.15.73-alt1
- Updated to 5.15.73
- https://github.com/raspberrypi/linux.git rpi-5.15.y commit ab70db591ba6a3688192e773e967cd5015a693a8
- AQBM1000: realtek phy leds configuration via device tree

* Thu Sep 29 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.15.70-alt2
- Added forgotten serdev-serio driver (necessary for Elpitech laptop)

* Tue Sep 27 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.15.70-alt1
- Updated to 5.15.70
- https://github.com/raspberrypi/linux.git rpi-5.15.y commit b5fb803e192afa566351481edf03bb44b56d48e7

* Thu Sep 06 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.15.65-alt1
- Updated to 5.15.65
- https://github.com/raspberrypi/linux.git rpi-5.15.y commit 5ca1fc5dc8d24599e91199602592f52d11ca57d6
- Baikal-M: Elpitech laptop support: added serio_serdev, enabled ps2mult, iwlwifi

* Thu Jun 23 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.15.48-alt1
- Updated to 5.15.48
- https://github.com/raspberrypi/linux.git rpi-5.15.y commit b0a1e3b995b7d3161a7414dc5fc6d59ae44d910c
- Baikal-M: added PCI-E driver for boards with new firmware (SDK-M 5.5)
- Build with GCC 10 to avoid spurious build failures (staging WiFi drivers and others)

* Thu May 05 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.15.36-alt1
- Updated to 5.15.36
- https://github.com/raspberrypi/linux.git rpi-5.15.y commit 9bc1ec59bd8db07e41067717aeea2749314ec801
- Restored legacy_cursor_update for Xorg (closes: #42604)
  Note: "legacy_cursor_update hack" has been removed by rpi-5.15.y commit 575197eedf2aae854cb1ce14882e0b910a382737

* Wed Apr 20 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.15.33-alt1
- Updated to 5.15.33
- https://github.com/raspberrypi/linux.git rpi-5.15.y commit 784f0a39c945c79fcb52dbb01db08b3bcc8ff7a5
- Baikal-M support from git.alt/people/asheplyakov/linux.git commit d047c3a6e1562e46fc0aaa753c39860784099b36
- Baikal-M: HD audio support
- Baikal-M: new supported boards: et101 (Elpitech), AQBM1000 (Aquarius)
- Keep spec and .gear in a dedicated branch (separate from code)
- Don't build docs to avoid spurious sphynx failures

* Thu Mar 03 2022 Dmitry Terekhin <jqt4@altlinux.org> 1:5.15.25-alt1
- Updated to 5.15.25 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.15.y
- commit 2f17f80d7fa9734b1af6ae94ecd35cd9c71770fa
- Replaced config-aarch64 file based on rpi-un
- Move v4l and staging modules to kernel-image package
- Add the ability to build a package using a cross compiler

* Tue Nov 30 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.81-alt1
- Updated to 5.10.81 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.10.y
- commit e16e31540935728ce57f22a1de56e8b2da5dd33b
- CONFIG_NF_TABLES=m
- Add some NFT modules
- (closes: 41084)
- Build for armh is off

* Thu Oct 07 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.63-alt1
- Updated to 5.10.63 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.10.y
- commit 6237d09759ba6c8746cd1e19b16faee50c97bfac
- CONFIG_WIREGUARD=m
- Add some CRYPTO modules
- (closes: 41046)
- Enabled loading compressed firmware blobs on armh
- CONFIG_FW_LOADER_PAGED_BUF=y
- CONFIG_FW_LOADER_USER_HELPER=y
- CONFIG_FW_LOADER_COMPRESS=y
- (closes: 41070)

* Tue Jul 20 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.50-alt1
- Updated to 5.10.50 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.10.y
- commit 55f43ec57e13d6aeac6f126df8083b67d68705db

* Wed Jul 07 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.36-alt2
- Remove dependency on startup package. See ALT bug 39840.

* Wed May 19 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.36-alt1
- Updated to 5.10.36 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.10.y
- commit b657cd2f27d9171b75c846f21e7b4bb581b3ed29
- To allow put comments in iptables ruleset
- CONFIG_NETFILTER_XT_MATCH_COMMENT=m
- (closes: 39767)
- CONFIG_PPS=y
- CONFIG_PPS_CLIENT_KTIMER=m
- CONFIG_PPS_CLIENT_LDISC=m
- CONFIG_PPS_CLIENT_GPIO=m
- To VC4 driver can emulate framebuffer on RPi3
- CONFIG_DRM_FBDEV_OVERALLOC=100
- add ZRam support
- CONFIG_ZSMALLOC=m
- CONFIG_ZRAM=m

* Mon Mar 01 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.4.83-alt2
- To work bluetooth on RPi3
- CONFIG_SERIAL_DEV_BUS=y
- CONFIG_SERIAL_DEV_CTRL_TTYPORT=y
- CONFIG_BT_HCIUART_BCM=y
- To work thermal sensor on RPi3 (armh)
- CONFIG_BCM2835_THERMAL=y

* Tue Jan 19 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.4.83-alt1
- Updated to 5.4.83 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.4.y
- commit bd204130252690fffb35e9f4f9495d322329bc59

* Tue Sep 08 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.4.61-alt1
- Updated to https://github.com/raspberrypi/linux.git rpi-5.4.y
    commit 9a1dd17906692f1ab76e45b9f59976b063b37034

* Tue Sep 08 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.4.59-alt2
- Set all I2C and SPI as modules
- CONFIG_SPI_SPIDEV is on for aarch64
- CONFIG_DEBUG_INFO is on

* Mon Aug 24 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.4.59-alt1
- Updated to 5.4.59 (still RPi-specific)

* Mon Aug 24 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.4.51-alt4
- Enable VIRTIO modules
- Set all VIRTIO as modules for aarch64
- CONFIG_VIRTIO_NET=m add network support in QEmu
- Add ACPI support for aarch64
- Change kernel format to zImage for armh

* Wed Aug 05 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.4.51-alt3
- Add armh
- Add file config-armh

* Wed Jul 22 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.4.51-alt2
- CONFIG_DEBUG_INFO is off, because p9 packages is huge

* Sat Jul 18 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.4.51-alt1
- updated to 5.4.51 (still RPi-specific)

* Fri Nov 08 2019 Dmitry Terekhin <jqt4@altlinux.org> 1:4.19.71-alt0.6
- added dtb file from rpi4 fiwmware
- packing dtbo files in package

* Wed Oct 23 2019 Dmitry Terekhin <jqt4@altlinux.org> 1:4.19.71-alt0.5
- CONFIG_RFKILL=m
- CONFIG_INPUT_EVBUG, CONFIG_IOMMU_DEBUGFS is off
- CONFIG_IOMMU_DEFAULT_PASSTHROUGH is off
- completely replaced spec file based on sample kernel-image-std-def
- all source files moved from linux/
- CONFIG_LOCALVERSION=""
- CONFIG_AUTOFS4_FS=m
- changed kernel flavour to rpi-def

* Tue Oct 01 2019 Dmitry Terekhin <jqt4@altlinux.org> 4.19.71-alt0.4
- add System.map
- add config
- only one devicetree directory
- fix flavour
- fix KERNELRELEASE to %version%flavour-%release

* Tue Oct 01 2019 Dmitry Terekhin <jqt4@altlinux.org> 4.19.71-alt0.3
- install devicetree

* Tue Oct 01 2019 Dmitry Terekhin <jqt4@altlinux.org> 4.19.71-alt0.2
- simplify spec
- add devicetree
- add modules_dir

* Tue Oct 01 2019 Dmitry Terekhin <jqt4@altlinux.org> 4.19.71-alt0.1
- spec and config changed - first test

* Fri Aug 30 2019 Gremlin from Kremlin <gremlin@altlinux.org> 4.19.71-alt1
- first build with RPi 4 support (arm64 a.k.a. aarch64)
