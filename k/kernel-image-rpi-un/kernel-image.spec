%def_disable check
%def_disable docs
%def_disable domU

Name: kernel-image-rpi-un
Release: alt1
epoch:1
%define kernel_need_version	6.1
# Used when kernel-source-x.y does not currently exist in repository.
%define kernel_base_version	6.1
%define kernel_sublevel .0
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
* Thu Dec 15 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:6.1.0-alt1
- Updated to 6.1
- https://github.com/raspberrypi/linux.git rpi-6.1.y 0a4f128460cf07f865a59daa6468de8e37985b45
- Baikal-M support git.alt/people/asheplyakov/linux.git commit 2961a8f1be9d47f4ce2e5e662f880c78e3afca93

* Thu Oct 20 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:6.0.2-alt1
- Updated to 6.0.2
- https://github.com/raspberrypi/linux.git rpi-6.0.y commit 45681bb2eec45e87e4907348e04cb151595a5dcd
- Baikal-M support git.alt/people/asheplyakov/linux.git commit d7ce44a27cf36dfbfe5dde1d4abda71b97d3ecf7

* Tue Jun 28 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.18.7-alt1
- Updated to 5.18.7
- https://github.com/raspberrypi/linux.git rpi-5.18.y commit 66742fe5d8a4ecd489f11aa315b6530c32eb126b
- Baikal-M support git.alt/people/asheplyakov/linux.git commit 1adbc886c19b040851abd3975e8f45839e4207c0
- Baikal-M: added PCI-E driver for "new" (SDK-M 5.5) firmware
- Baikal-M: preliminary support of SDK-M 5.5 firmware
- Build with GCC 10 to avoid spurious build failures

* Thu May 26 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.18.0-alt1
- Updated to 5.18.0
- https://github.com/raspberrypi/linux.git rpi-5.18.y commit 596cca29caedbd932949a0f9835306d6c5d03ac4
- Baikal-M support git.alt/people/asheplyakov/linux.git commit 30585df684ee2b8bbfeeee583055d5f702103ae1
- Baikal-M: supported boards: ET101 rev 1.2, AQBM1000, TF307 (rev 1.4 aka MB-S-D)
- Baikal-M: supported firmwares: based on SDK-M 5.3
- Baikal-M: firmwares from SDK-M 5.4 and 5.5 are known to NOT work
- adjusted spec due to drivers/scsi/scsi.h removal in v5.18

* Wed Apr 06 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.17.1-alt1
- Updated to 5.17.1
- https://github.com/raspberrypi/linux.git rpi-5.17.y commit c86339fd1731b6c6776c9f3e609a0f5ef25045dc
- Baikal-M support from git.alt/people/asheplyakov/linux.git commit 7f62cff013879a19b3b7709644163015f684bf2b

* Fri Mar 18 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.15.28-alt1
- Updated to 5.15.28
- https://github.com/raspberrypi/linux.git rpi-5.15.y commit 53c0d5c6893c940cb762d3a474103706b1e5e383
- Baikal-M: HD audio support
- Baikal-M: new supported boards: et101 (Elpitech), AQBM1000 (Aquarius)

* Wed Mar 02 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.15.25-alt1
- Updated to 5.15.25
- https://github.com/raspberrypi/linux.git rpi-5.15.y commit 0efbe86e7248ad9b80a42b37a91c44860f91eee4
- Baikal-M support from git.alt/people/asheplyakov/linux.git commit 1699ee28abaf2d53f5437f47d1cf6985eb3dd1cd

* Mon Jan 10 2022 Dmitry Terekhin <jqt4@altlinux.org> 1:5.15.13-alt1
- Updated to 5.15.13
- https://github.com/raspberrypi/linux.git rpi-5.15.y
- commit 38b39910c34d774e01f0b4d5a61ac581c7cf14c1
- Change the build scheme: don't use the kernel-source package

* Fri Dec 17 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.15.6-alt1
- Updated to 5.15.6
- https://github.com/raspberrypi/linux.git rpi-5.15.y
- commit be49bc5cd53b095fbbc9dde271adf580025e5adc
- Add TF307 revision D and ROCK PI 4 Model C support from
- https://github.com/altlinux/linux-arm/tree/rpi-baikalm-5.15.y
- Replaced config-aarch64 file based on baikal_rpi_rockpi4_defconfig
- Move v4l and staging modules to kernel-image package
- Remove package dependencies rpi4-boot-switch
  and rpi4-boot-nouboot-filetrigger

* Fri Jul 23 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.12.17-alt1
- Updated to 5.12.17 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.12.y
- commit 3e4b21b3e558cf90fa399b2f372b8779a7f85478

* Wed Jul 07 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.12.6-alt2
- Remove dependency on startup package. See ALT bug 39840.

* Mon May 31 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.12.6-alt1
- Updated to 5.12.6 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.12.y
- commit 8b85410e9cc2ef9cd30187815ae4f766997848a6

* Mon May 10 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.35-alt1
- Updated to 5.10.35 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.10.y
- commit 6867d7fa52e18525c79df3708e7ff05af10fd250
- To allow put comments in iptables ruleset
- CONFIG_NETFILTER_XT_MATCH_COMMENT=m

* Wed Apr 07 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.27-alt1
- Updated to 5.10.27 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.10.y
- commit 7773c5ccb1b23de78b34f7234ff3aafd12ecac53
- (closes: 39767)
- CONFIG_PPS=y
- CONFIG_PPS_CLIENT_KTIMER=m
- CONFIG_PPS_CLIENT_LDISC=m
- CONFIG_PPS_CLIENT_GPIO=m

* Thu Mar 11 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.20-alt1
- Updated to 5.10.20 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.10.y
- commit c1cfa734c2e07ced2040211d18b4d3d2578dba1e
- To VC4 driver can emulate framebuffer on RPi3
- CONFIG_DRM_FBDEV_OVERALLOC=100

* Wed Feb 24 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.17-alt1
- Updated to 5.10.17 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.10.y
- commit 12fdeddcde1ce67177ae0e13931ff24944015625
- To work bluetooth on RPi3
- CONFIG_SERIAL_DEV_BUS=y
- CONFIG_SERIAL_DEV_CTRL_TTYPORT=y
- CONFIG_BT_HCIUART_BCM=y

* Wed Jan 20 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.7-alt1
- Updated to 5.10.7 (still RPi-specific)
- https://github.com/raspberrypi/linux.git rpi-5.10.y
- commit 839c811efeb43c92345dd47d1e3d3bbac4474024

* Fri Dec 25 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.2-alt2
- add ZRam support
- CONFIG_ZSMALLOC=m
- CONFIG_ZRAM=m

* Wed Dec 23 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.10.2-alt1
- Updated to 5.10.2 (still RPi-specific)

* Tue Sep 01 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.8.2-alt1
- Updated to 5.8.2 (still RPi-specific)

* Tue Aug 18 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.7.8-alt3
- CONFIG_VIRTIO_NET=y add network support in QEmu
- add ACPI support
- set all VIRTIO as modules

* Wed Jul 22 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.7.8-alt2
- CONFIG_DEBUG_INFO is off, because p9 packages is huge

* Sat Jul 18 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.7.8-alt1
- Updated to 5.7.8 (still RPi-specific)
- CONFIG_DEBUG_INFO=y

* Mon Jun 08 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.6.16-alt1
- Updated to 5.6.16
- Build for armh is off

* Fri May 29 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.6.10-alt2
- Add armh
- Add file config-armh based on file bcm2711_defconfig
- Set some CONFIG in config-armh based on config-aarch64
- CONFIG_I2C_BCM2835=y
- CONFIG_SPI_BCM2835=y
- CONFIG_SPI_BCM2835AUX=y
- CONFIG_SND=y
- CONFIG_SND_TIMER=y
- CONFIG_SND_PCM=y
- CONFIG_SND_BCM2835=y
- CONFIG_BCM2835_VCHIQ_MMAL=y
- CONFIG_BCM_VC_SM_CMA=y

* Mon May 04 2020 Evgeny Sinelnikov <sin@altlinux.org> 1:5.6.10-alt1
- Update to latest mainstream release 5.6.10
- Build with native kernel-source-5.6 instead of kernel-source-5.5

* Thu Apr 23 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.6.2-alt3
- CONFIG_BCM2711_THERMAL=y for working thermal sensor on RPi4

* Mon Apr 06 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.6.2-alt2
- Rebuild for p9

* Sun Apr 05 2020 Evgeny Sinelnikov <sin@altlinux.org> 1:5.6.2-alt1
- Update to latest mainstream release 5.6.2
- Add requires to post script filetrigger for booting without U-Boot

* Wed Mar 25 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.6.0.rc2-alt0.2
- CONFIG_BT_HCIUART_BCM=y for bluetooth work

* Tue Mar 24 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.6.0.rc2-alt0.1
- updated to 5.6.0.rc2 (still RPi-specific)

* Mon Mar 09 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.5.5-alt0.3
- replaced bcm2711-rpi-4-b.dts file with other modified by firmware

* Wed Mar 04 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.5.5-alt0.2
- replaced bcm2711-rpi-4-b.dts file with modified by firmware
- CONFIG_GPIO_SYSFS=y /sys/class/gpio/ is on

* Thu Feb 27 2020 Dmitry Terekhin <jqt4@altlinux.org> 1:5.5.5-alt0.1
- updated to 5.5.5 (still RPi-specific)

* Thu Nov 07 2019 Dmitry Terekhin <jqt4@altlinux.org> 1:5.3.5-alt0.4
- added dtb file from rpi4 fiwmware
- packing dtbo files in package

* Thu Oct 17 2019 Dmitry Terekhin <jqt4@altlinux.org> 1:5.3.5-alt0.3
- changed kernel flavour to rpi-un

* Wed Oct 16 2019 Dmitry Terekhin <jqt4@altlinux.org> 1:5.3.5-alt0.2
- simplify spec
- removed unnecessary subpackages
- CONFIG_LOCALVERSION=""

* Tue Oct 15 2019 Dmitry Terekhin <jqt4@altlinux.org> 1:5.3.5-alt0.1
- completely replaced spec file based on sample kernel-image-un-def
- all PreReq converted to Requires(pre) for no flood in build log
- CONFIG_RFKILL=m
- CONFIG_INPUT_EVBUG, CONFIG_IOMMU_DEBUGFS is off
- CONFIG_IOMMU_DEFAULT_PASSTHROUGH is off
- CONFIG_INPUT_EVDEV=y
- CONFIG_LOCALVERSION="rpi"
- CONFIG_DEFAULT_HOSTNAME="rpi.example.lan"

* Mon Oct 14 2019 Gremlin from Kremlin <gremlin@altlinux.org> 5.3.6-alt1
- updated to 5.3.6 (still RPi-specific)

* Fri Aug 30 2019 Gremlin from Kremlin <gremlin@altlinux.org> 5.3.0-alt0rc6
- first build with RPi 4 support (arm64 a.k.a. aarch64)
