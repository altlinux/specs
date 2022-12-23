Name: kernel-image-centos

%define centos_release 226

Version: 5.14.0.%{centos_release}
Release: alt1.el9

%define kernel_base_version  %version
%define kernel_extra_version %nil
%define kernel_real_version  5.14
# Numeric extra version scheme developed by Alexander Bokovoy:
# 0.0.X -- preX
# 0.X.0 -- rcX
# 1.0.0 -- release
%define kernel_extra_version_numeric 1.0.0

%define krelease %release

%define flavour      %( s='%name';    printf %%s "${s#kernel-image-}" )
%define base_flavour %( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour  %( s='%flavour'; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version %__gcc_version_base

# Enable/disable SGML docs formatting
%def_disable docs

# Enable/disable ALSA modules build
%def_enable alsa

# Enable/disable media modules build
%def_enable media

# Enable/disable staging modules build
%def_disable staging

## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*
%add_verify_elf_skiplist %modules_dir/*

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist /boot/vmlinuz-*

# don't try this with your spec.
%define _deps_optimization 2

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://gitlab.com/redhat/centos-stream/src/kernel/centos-stream-9

Source0: %name.tar
Patch0001: 0001-Fix-build-with-new-pahole-adjust-flags.patch
Patch0002: 0002-fscache-Convert-fscache_set_page_dirty-to-fscache_di.patch

ExclusiveOS: Linux
ExclusiveArch: x86_64 aarch64

%define make_target bzImage
%ifarch ppc64le
%define make_target vmlinux
%endif
%ifarch aarch64
%define make_target Image
%endif
%ifarch %arm
%define make_target zImage
%endif

%define image_path arch/%base_arch/boot/%make_target
%ifarch ppc64le
%define image_path %make_target.stripped
%endif

%define arch_dir %base_arch
%ifarch %ix86 x86_64
%define arch_dir x86
%endif

BuildRequires(pre): rpm-build-kernel
%ifarch %ix86 x86_64
BuildRequires: dev86
%endif
BuildRequires: flex, bc
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version gcc%kgcc_version-c++
BuildRequires: gcc%kgcc_version-plugin-devel libgmp-devel libmpc-devel
BuildRequires: module-init-tools >= 3.16, lzma-utils, zlib-devel
# in-kernel signature checking stuff
BuildRequires: openssl-devel openssl
BuildRequires: dwarves >= 1.16
# for tools/objtool
BuildRequires: libelf-devel
BuildRequires: rsync
BuildRequires: /usr/sbin/initrd-scanmod

%define qemu_pkg %_arch
%ifarch %ix86 x86_64
%define qemu_pkg x86
%endif
%ifarch ppc64le
%define qemu_pkg ppc
%endif
%ifarch %arm
%define qemu_pkg arm
%endif

%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system-%qemu_pkg-core ipxe-roms-qemu glibc-devel-static}}

Provides: kernel-modules-eeepc-%flavour = %EVR
Provides: kernel-modules-drbd83-%flavour = %EVR
Provides: kernel-modules-igb-%flavour = %EVR
Provides: kernel-modules-kvm-%flavour = %EVR
Provides: kernel-modules-kvm-%kversion-%flavour-%krelease = %EVR

%if_enabled docs
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink perl-Pod-Usage python3-module-sphinx_rtd_theme
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

Requires(pre): module-init-tools >= 3.1
Requires(pre): coreutils
Requires(pre): mkinitrd >= 1:2.9.9-alt1

%description
The kernel package contains the Linux kernel (vmlinuz), the core of any
Linux operating system.  The kernel handles the basic functions
of the operating system: memory allocation, process allocation, device
input and output, etc.

This is a "centos stream" variant of kernel packages.

The list of certified hardware and cloud instances for RHEL9 can be viewed
at the Red Hat Ecosystem Catalog, https://catalog.redhat.com.

%package -n kernel-modules-drm-%flavour
Summary: The Direct Rendering Infrastructure modules
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-%kversion-%flavour-%krelease > %version-%release
Requires(pre): coreutils
Requires(pre): module-init-tools >= 3.1
Requires(pre,post,postun): %name = %EVR

%description -n kernel-modules-drm-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework for
allowing direct access to graphics hardware in a safe and efficient manner. It
includes changes to the X server, to several client libraries, and to the
kernel. The first major use for the DRI is to create fast OpenGL
implementations.

%package -n kernel-modules-alsa-%flavour
Summary: ALSA sound driver modules
Group: System/Kernel and hardware
Provides:  kernel-modules-alsa-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-alsa-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-alsa-%kversion-%flavour-%krelease > %version-%release
Requires(pre): coreutils
Requires(pre): module-init-tools >= 3.1
Requires(pre,post,postun): %name = %EVR

%description -n kernel-modules-alsa-%flavour
This package contains ALSA sound driver modules for the Linux kernel
package %name-%version-%release.

%package -n kernel-modules-media-%flavour
Summary: Media drivers modules
Group: System/Kernel and hardware
Provides:  kernel-modules-media-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-media-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-media-%kversion-%flavour-%krelease > %version-%release
Requires(pre): coreutils
Requires(pre): module-init-tools >= 3.1
Requires(pre,post,postun): %name = %EVR

%description -n kernel-modules-media-%flavour
This package contains media drivers modules for the Linux kernel
package %name-%version-%release.

%package -n kernel-modules-staging-%flavour
Summary: Staging drivers modules
Group: System/Kernel and hardware
Provides:  kernel-modules-staging-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-staging-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-staging-%kversion-%flavour-%krelease > %version-%release
Requires(pre): coreutils
Requires(pre): module-init-tools >= 3.1
Requires(pre,post,postun): %name = %EVR

%description -n kernel-modules-staging-%flavour
This package contains staging drivers modules for the Linux kernel
package %name-%version-%release.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version
Provides: kernel-headers-%base_flavour = %version-%release

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).

Note that such usage of kernel headers in userspace is not supported
by the upstream kernel maintainers and often breaks compilation.
Therefore installing and using this package is not recommended.

If possible, try to use glibc-kernheaders instead of this package.

%package -n kernel-headers-modules-%flavour
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel
Requires: gcc%kgcc_version

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
 * kernel-image-%base_flavour-*-%kversion-%krelease

The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.


%prep
%setup -c -n kernel-image-%flavour-%kversion-%krelease
%autopatch -p1

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version.%centos_release-%flavour-%krelease/g' Makefile
subst 's/CC.*$(CROSS_COMPILE)gcc/CC := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

chmod +x tools/objtool/sync-check.sh

# This Prevents scripts/setlocalversion from mucking with our version numbers.
touch .scmversion

# Extend config from fedora config.
for o in \
	CONFIG_9P_FS:'CONFIG_9P_FS=m' \
	CONFIG_9P_FSCACHE:'CONFIG_9P_FSCACHE=y' \
	CONFIG_9P_FS_POSIX_ACL:'CONFIG_9P_FS_POSIX_ACL=y' \
	CONFIG_9P_FS_SECURITY:'CONFIG_9P_FS_SECURITY=y' \
	CONFIG_NET_9P:'CONFIG_NET_9P=m' \
	CONFIG_NET_9P_DEBUG:'# CONFIG_NET_9P_DEBUG is not set' \
	CONFIG_NET_9P_RDMA:'CONFIG_NET_9P_RDMA=m' \
	CONFIG_NET_9P_VIRTIO:'CONFIG_NET_9P_VIRTIO=m' \
	CONFIG_NET_9P_XEN:'CONFIG_NET_9P_XEN=m' \
;
do
	echo "${o##*:}" > "redhat/configs/custom-overrides/generic/${o%%%%:*}"
done

%build
mkdir .bin
ln -s /bin/true .bin/git
export PATH="$PWD/.bin:$PATH"

export ARCH=%base_arch
export NPROCS=%__nprocs
KernelVer=%kversion-%flavour-%krelease

%make_build mrproper

echo "Building Kernel $KernelVer"

KVER=`make --no-print-directory kernelversion EXTRAVERSION=`

# Generate a config.
%make_build -C redhat dist-configs-commit \
	FLAVOR=rhel \
	SPECVERSION="$KVER" \
	TOPDIR="$PWD"

cp -vf redhat/configs/kernel-$KVER-%_target_cpu.config .config

# Refresh config
%make_build olddefconfig

# Build kernel image
%make_build %make_target

%ifarch ppc64le
eu-strip --remove-comment -o %image_path vmlinux
%endif

# Build kernel modules
%make_build modules

%ifarch aarch64 %arm
# Devicetree files
%make_build dtbs
%endif

echo "Kernel built $KernelVer"

%if_enabled docs
# psdocs, pdfdocs don't work yet
%make_build SPHINXOPTS="-j $([ %__nprocs -ge 8 ] && echo 8 || echo %__nprocs)" htmldocs
%endif

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map  %buildroot/boot/System.map-$KernelVer
install -Dp -m644 %image_path %buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config     %buildroot/boot/config-$KernelVer

# Override $(mod-fw) because we don't want it to install any firmware
# we'll get it from the linux-firmware package and we don't want conflicts
%make_build modules_install INSTALL_MOD_PATH=%buildroot mod-fw=

%ifarch aarch64 %arm
make dtbs_install INSTALL_DTBS_PATH=%buildroot/lib/devicetree/$KernelVer
%ifarch aarch64
find %buildroot/lib/devicetree/$KernelVer -mindepth 1 -type d |\
	while read d; do
		mv $d/* $d/../
		rmdir $d
		ln -srv $d/../ $d
	done
%endif
%endif

mkdir -p %buildroot%modules_dir/updates
mkdir -p %buildroot%kbuild_dir/arch/%arch_dir

cp -a include                %buildroot%kbuild_dir/include
cp -a arch/%arch_dir/include %buildroot%kbuild_dir/arch/%arch_dir

# drivers-headers install
mkdir -p %buildroot%kbuild_dir/drivers/scsi
mkdir -p %buildroot%kbuild_dir/drivers/md
mkdir -p %buildroot%kbuild_dir/drivers/usb/core
mkdir -p %buildroot%kbuild_dir/drivers/net/wireless
mkdir -p %buildroot%kbuild_dir/net/mac80211
mkdir -p %buildroot%kbuild_dir/kernel
mkdir -p %buildroot%kbuild_dir/lib

cp -a drivers/md/dm*.h             %buildroot%kbuild_dir/drivers/md/
cp -a drivers/usb/core/*.h         %buildroot%kbuild_dir/drivers/usb/core/
cp -a drivers/net/wireless/Kconfig %buildroot%kbuild_dir/drivers/net/wireless/
cp -a lib/hexdump.c                %buildroot%kbuild_dir/lib/
cp -a kernel/workqueue.c           %buildroot%kbuild_dir/kernel/
cp -a net/mac80211/ieee80211_i.h   %buildroot%kbuild_dir/net/mac80211/
cp -a net/mac80211/sta_info.h      %buildroot%kbuild_dir/net/mac80211/

# Install files required for building external modules (in addition to headers)
KbuildFiles="
	Makefile
	Makefile.rhelver
	Module.symvers
	arch/%arch_dir/Makefile
%ifarch %ix86 x86_64
	arch/x86/Makefile_32
	arch/x86/Makefile_32.cpu
%ifarch x86_64
	arch/x86/Makefile_64
%endif
%endif
%ifarch aarch64 ppc64le
       arch/%arch_dir/kernel/module.lds
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
	scripts/module.lds
	scripts/recordmcount.pl
	scripts/recordmcount.h
	scripts/recordmcount.c
	scripts/recordmcount
	scripts/gcc-x86_*-has-stack-protector.sh
	scripts/modules-check.sh
	scripts/module-common.lds
	scripts/subarch.include
	scripts/depmod.sh
	scripts/gcc-plugins/*.so
	scripts/ld-version.sh
	scripts/pahole-flags.sh
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
%make_build headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

#provide symlink to autoconf.h for back compat
pushd %buildroot%old_kbuild_dir/include/linux
ln -s ../generated/autoconf.h
ln -s ../generated/utsrelease.h
ln -s ../generated/uapi/linux/version.h
popd

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%base_flavour-%version/
cp -a Documentation/* %buildroot%_docdir/kernel-doc-%base_flavour-%version/
cat > kernel-doc.files <<EOF
%%doc %_docdir/kernel-doc-%base_flavour-%version
EOF
%endif # if_enabled docs

cat > kernel-headers-modules.files <<EOF
%kbuild_dir
%old_kbuild_dir
%%dir %modules_dir/
%modules_dir/build
EOF

cat > kernel-headers.files <<EOF
%kheaders_dir
EOF

filter()
{
	rm -f -- .scanmod-[0-9]*
	for arg; do
		num="${arg%%%%:*}"
		echo >> ".scanmod-$num" "${arg#*:}"
	done
	/usr/sbin/initrd-scanmod -k "$KernelVer" -b "%buildroot" .scanmod-* |
		sed -r -e 's#^.*(/lib/modules/)#\1#' |
		sort -u
}

# Generate kernel-modules-drm-flavour
filter \
	0:"filename .*/drivers/gpu/drm/.*" \
	1:"filename kernel/drivers/media/cec/core/cec.ko" \
	2:"filename kernel/drivers/usb/typec/altmodes/typec_displayport.ko" \
	> kernel-modules-drm.files

# Generate kernel-modules-alsa-flavour
filter \
	0:"filename .*/kernel/sound/.*" \
	1:"symbol ^snd_(register|card|ac97|soc|hda|seq|timer|intel)" \
	> kernel-modules-alsa.files

# Generate kernel-modules-media-flavour
filter \
	0:"filename .*/drivers/media/.*" \
	> kernel-modules-media.list

sort kernel-modules-*.files |
	comm -13 - kernel-modules-media.list > kernel-modules-media.files

# Generate kernel-modules-staging-flavour
filter \
	0:"filename .*/drivers/staging/.*" \
	> kernel-modules-staging.files

# Generate kernel-image
find %buildroot%modules_dir -type f -name '*.ko*' |
	sed -r -e 's#^.*(/lib/modules/)#\1#' |
	sort -o kernel-modules.list
{
	find %buildroot%modules_dir -type d |
		sed -r -e 's#^.*(/lib/modules/)#%%dir \1#'

	find %buildroot%modules_dir -mindepth 1 -maxdepth 1 -type f \( -name 'modules.*' -a \! -name '*.bin' \) |
		sed -r -e 's#^.*(/lib/modules/)#\1#'

	find %buildroot%modules_dir -mindepth 1 -maxdepth 1 -type f -name 'modules.*.bin' |
		sed -r -e 's#^.*(/lib/modules/)#%%ghost \1#'

	cat <<-EOF
%ifarch aarch64 %arm
	/lib/devicetree/%kversion-%flavour-%krelease
%endif
	/boot/vmlinuz-%kversion-%flavour-%krelease
	/boot/System.map-%kversion-%flavour-%krelease
	/boot/config-%kversion-%flavour-%krelease
	%%defattr(0600,root,root,0700)
	EOF
	sort kernel-modules-*.files |
		comm -13 - kernel-modules.list
} > kernel-image.files

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

%ifarch %arm
qemu_arch=arm
qemu_opts="-machine virt"
console=ttyAMA0
%endif

timeout --foreground 600 \
	qemu-system-"$qemu_arch" -m 512 -no-reboot -nographic $qemu_opts \
		-kernel %buildroot/boot/vmlinuz-$KernelVer \
		-initrd initrd.img \
		-append console="$console no_timer_check" \
		> boot.log &&
grep -q "^$msg" boot.log &&
grep -qE '^(\[ *[0-9]+\.[0-9]+\] *)?reboot: Power down' boot.log || {
	cat >&2 boot.log
	echo >&2 'Marker not found'
	exit 1
}

%files -f kernel-image.files
%files -f kernel-headers-modules.files -n kernel-headers-modules-%flavour
%files -f kernel-headers.files         -n kernel-headers-%flavour
%files -f kernel-modules-alsa.files    -n kernel-modules-alsa-%flavour
%files -f kernel-modules-drm.files     -n kernel-modules-drm-%flavour
%files -f kernel-modules-media.files   -n kernel-modules-media-%flavour
%if_enabled staging
%files -f kernel-modules-staging.files -n kernel-modules-staging-%flavour
%endif # if_enabled staging
%if_enabled docs
%files -f kernel-doc.files             -n kernel-doc-%base_flavour
%endif

%changelog
* Fri Dec 23 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.226-alt1.el9
- Updated to kernel-5.14.0-226.el9 (fixes: CVE-2022-21505, CVE-2022-3628, CVE-2022-42896):
  + Backport Aspeed conversion to shmem
  + block: Do not reread partition table on exclusively open device
  + Bluetooth: L2CAP: Fix accepting connection request for invalid SPSM
  + bonding: driver update to v6.1
  + CNB: ipsec: be explicit with XFRM offload direction
  + hwmon: (pwm-fan) Refactor fan power on/off
  + iavf driver update
  + igbvf: Driver Update
  + lib/irq_poll: Prevent softirq pending leak in irq_poll_cpu_dead()
  + lockdown: Fix kexec lockdown bypass with ima policy
  + macsec: backports from upstream
  + net: tls: rebase to 6.0+
  + net/tunnel: wait until all sk_user_data reader finish before releasing the sock
  + [s390]: RHEL9 - KVM: s390: pv: don't allow userspace to set the clock under PV
  + tipc: re-fetch skb cb after tipc_msg_validate
  + v5.18 backports for s390 expolines
  + wifi: brcmfmac: Fix potential buffer overflow in brcmf_fweh_event_worker()
  + wireless: update to v6.0
  + wireless update to v6.0: base with all dependencies
  + x86/bugs: Add late bug fixes to x86 speculation bugs

* Thu Dec 22 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.222-alt1.el9
- Updated to kernel-5.14.0-222.el9:
  + bpf, xdp: update to 5.19
  + Update drivers/base to match Linux v6.0
  + Update net/bluetooth and drivers/bluetooth to upstream v6.0

* Wed Dec 21 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.219-alt1.el9
- Updated to kernel-5.14.0-219.el9 (fixes: CVE-2022-2873):
  + Add fixes to drivers/misc/sram to support NVIDIA Orin
  + Bring MD code the latest upstream
  + CNB: fortify: Provide a memcpy trap door for sharp corners
  + CNB: tracing/events: Add __vstring() and __assign_vstr() helper macros
  + crypto: backport wireguard s390 fix
  + hyper-v: Video and HID driver updates for RHEL-9.2
  + i2c: ismt: Fix an out-of-bounds bug in ismt_access()
  + kernfs: switch global kernfs_rwsem lock to per-fs lock
  + powerpc/rtas: Allow ibm,platform-dump RTAS call with null buffer address
  + redhat/configs: Enable CONFIG_CRYPTO_CURVE25519
  + Redo missing uapi/linux/stddef.h: Add include guards
  + vmxnet3: driver update to v6.0
  + x86/fpu: Drop fpregs lock before inheriting FPU permissions

* Sat Dec 17 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.217-alt1.el9
- Updated to kernel-5.14.0-217.el9 (fixes: CVE-2022-2959, CVE-2022-43945):
  + arm64: dts: imx93-pinfunc: drop execution permission
  + Drivers: hv: vmbus: Updates for 9.2
  + drm/vc4: update to 5.18
  + dt-bindings: soc: adds for i.MX93 SRC, mediamix blk ctrl, i2c-imx-lpi2c
  + Enable the GNSS subsystem
  + Fix a problem with the time handling of nested KVM guests
  + hwmon: Handle failure to register sensor with thermal zone correctly
  + i40e: driver update
  + igc: Driver Update
  + NFSD/SUNRPC - fix send buffer overflow
  + ovs: backports P1 for 9.2
  + PCI: hv: Updates for RHEL 9.2
  + pinctrl: amd: Don't save/restore interrupt status and wake status bits
  + pipe: Fix missing lock in pipe_resize_ring()
  + redhat: configs: disable vDPA on all archs except x86_64
  + redhat/Makefile: Drop message about BUILDID deprecation
  + scsi: qla2xxx: Fix crash when I/O abort times out
  + scsi: storvsc: Fix handling of srb_status and capacity change events
  + sfc: driver update to v6.0
  + tcp: Add listening address to SYN flood message
  + UFS backport fixups
  + Update amd-pstate cpufrequency driver
  + Update drivers/mailbox for Arm SystemReady IR platforms
  + Update DTS bindings for Tegra234 (NVIDIA Orin)
  + Volume Management Device (VMD) driver fixes
  + x86: hyperv: Updates for RHEL 9.2

* Wed Dec 14 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.212-alt1.el9
- Updated to kernel-5.14.0-212.el9:
  + ceph: backport mainline changes up to v6.0 for RHEL 9.2
  + powercap: intel_rapl: support new layout of Psys PowerLimit Register
  + udp: some performance optimizations

* Tue Dec 13 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.211-alt1.el9
- Updated to kernel-5.14.0-211.el9:
  + Add fixes to drivers/clksrc for NVIDIA Orin
  + Backport Aspeed conversion to shmem
  + Backport DFS related fixes from upstream.
  + clocksource: hyper-v: Updates for RHEL 9.2
  + misc: rtsx: Rework runtime power management flow
  + net: hyper-v: netvsc driver updates for RHEL-9.2
  + net: mana: Microsoft Azure Network Adapter (MANA) driver updates
  + RDMA: Bug fixes from v6.1
  + vgacon: Propagate console boot parameters before calling `vc_resize'

* Sat Dec 10 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.210-alt1.el9
- Updated to kernel-5.14.0-210.el9:
  + ALSA: backport for RHEL 9.2
  + bonding: fix ICMPv6 header handling when receiving IPv6 messages
  + EDAC/ghes: Set the DIMM label unconditionally
  + fs: dlm: fix race in lowcomms
  + mmc: sdhci-tegra: Updates
  + [RHEL-9] NFSD: Mark exports of NFS as unsupported
  + rv: Add Runtime Verification (RV) interface

* Thu Dec 08 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.208-alt1.el9
- Updated to kernel-5.14.0-208.el9:
  + crypto: Provide support for RFC 7919 FFDHE group parameters (CRYPTO_DH_RFC7919_GROUPS)
  + livepatch: rebase to linux v5.19
  + scsi: hyper-v: storvsc: driver update for RHEL-9.2

* Tue Dec 06 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.207-alt1.el9
- Updated to kernel-5.14.0-207.el9:
  + [9.2] DRM backport part 2: main backport
  + block: fix direct io device mapper errors
  + CNB: ptp: introduce helpers to adjust by scaled parts per million
  + dt-bindings: gpio: gpio-vf610: Updates
  + dt-bindings: serial: fsl-lpuart: Updates
  + fs: allow cross-vfsmount reflink/dedupe
  + fuse: add file_modified() to fallocate
  + ice: Driver Update to 6.0
  + ISH updates and bug fixes
  + Merge commit '4fc3237d0cf85530cfd3c73be94441ea20ab2df3'
  + mm: migrate: fix THP's mapcount on isolation
  + ping: convert to RCU lookups, get rid of rwlock
  + Rebase selftests/rseq to v6.0
  + redhat/configs: Change the amd-pstate driver from builtin to loadable
  + skx_common: use driver decoder when possible
  + spec: Update bpftool versioning scheme
  + x86/sgx: update sgx subsystem upto v6.0
  + Various changes and improvements that are poorly described in merge.

* Fri Dec 02 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.205-alt1.el9
- Updated to kernel-5.14.0-205.el9:
  + Add rtla subpackage for kernel-tools
  + arm64: dts: freescale: Add i.MX93 SoC-level information support
  + ata: libata-core: Print timeout value when internal command times
  + Backport fbcon to fix race condition in fbcon
  + build: Fix generating BTF with pahole >=1.24
  + clk: imx: add i.MX93 clk
  + CNB: ethtool: add header/data split indication
  + CNB: ipv6: Use ipv6_only_sock() helper in condition
  + CNB: net: remove noblock parameter from skb_recv_datagram()
  + CNB: net: wrap the wireless pointers in struct net_device in an ifdef
  + CNB: PM: core: Remove static qualifier in DEFINE_SIMPLE_DEV_PM_OPS macro
  + CNB: slab: Introduce kmalloc_size_roundup()
  + CNB:  usb: remove third argument of usb_maxpacket()
  + CXL update from 5.18
  + drm: Move nomodeset kernel parameter to the DRM subsystem
  + dt-bindings: mailbox: imx-mu: Add bindings for i.MX93
  + dt-bindings: mmc: imx-esdhc: Updates
  + e1000e: Driver update for RHEL-9.2.0
  + ext4: Use folio_invalidate()
  + gpio: vf610: remove the SOC_VF610 dependency for GPIO_VF610
  + iavf: Add waiting for response from PF in set mac
  + ice: Driver Update to 5.19
  + intel_idle: Add AlderLake-N support
  + locking: rwsem & other locking code updates
  + Merge commit '6e39eb8ca7100c27aa42409b0491592be0d67a0d'
  + Merge commit 'aa830fac8952cf6440f19c00317847b311f00214'
  + Merge remote-tracking branch 'centos-stream-9/merge-requests/1372' into therm-v0
  + nfp: driver update to kernel version 5.19
  + NFS / NFSD fixes rollup for 9.2
  + percpu_ref_init(): clean ->percpu_count_ref on failure
  + perf: internal-testsuite instruction-decoder-new-instructions failed
  + pinctrl: imx93: updates for pinctrl driver support
  + platform/x86/intel/pmt: Sapphire Rapids PMT errata fix
  + powerpc/64/kdump: Limit kdump base to 512MB
  + powerpc: Don't select HAVE_IRQ_EXIT_ON_IRQ_STACK
  + Rebase rhel9 kernel kexec/kdump code to upstream kernel 6.0
  + Revert "powerpc/rtas: Implement reentrant rtas call"
  + s390/block: fix add disk warning
  + [s390]: RHEL9 - boot: Add secure boot trailer
  + [s390]: RHEL9 - kernel: missing exception table entries
  + smartpqi updates
  + sunrpc: Set sk_allocation to GFP_NOFS to avoid using current->task_frag.
  + udp: backports from upstream
  + Update drivers/thermal in order to support Arm SystemReady IR
  + Update kernel's PCI subsystem to v6.1
  + Update mlxsw driver to upstream v5.19
  + update powerpc/fadump
  + x86/ftrace: remove return_to_handler SYM_FUNC_END macro
  + Various changes and improvements that are poorly described in merge.

* Wed Nov 23 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.201-alt1.el9
- Updated to kernel-5.14.0-201.el9:
  + CNB: Update TC subsystem to upstream v6.0
  + CNB: vdpa: Add support for querying vendor statistics
  + fix compile_comands.json generation
  + fuse: fix readdir cache race
  + Merge commit '27dadcb8127ff8b29517cedc0388c4e718e37c66'
  + perf: Sync with upstream v6.0
  + rpminspect: disable kmidiff and abidiff
  + sctp: backports from upstream
  + Updates for  automotive_full pipeline
  + vdpa_sim_blk: backport latests features [rhel-9.2.0]
  + XFS update to v5.16
  + Various changes and improvements that are poorly described in merge.

* Tue Nov 22 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.200-alt1.el9
- Updated to kernel-5.14.0-200.el9:
  + arm64: kdump: Reimplement crashkernel=X fixup
  + bnx2x: driver updates
  + BPF and XDP rebase to v5.18
  + ipvlan/macvlan: phase-1 backports for RHEL-9.2
  + net: raw: Convert to raw sockets to RCU.
  + qed*: driver update
  + soc: imx: add i.MX93 SRC power domain and media blk ctrl drivers

* Sat Nov 19 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.198-alt1.el9
- Updated to kernel-5.14.0-198.el9:
  + Add fixes to drivers/firmware for NVIDIA Orin support
  + atlantic: fix deadlock at aq_nic_stop
  + CNB: net: add skb_[inner_]tcp_all_headers helpers
  + crypto: ccp - Add support for new CCP/PSP device ID
  + megaraid_sas: driver update
  + Merge remote-tracking branch 'origin/merge-requests/1372' into bz2115520
  + mm, oom: do not trigger out_of_memory from the #PF
  + powerpc/pseries: Enable POWER Architecture Platform Watchdog Driver
  + sched: Persistent user requested cpu affinity
  + Scheduler updates for 9.2
  + scsi: mpi3mr: driver update
  + scsi: mpt3sas: driver update
  + tcp: BIG TCP implementation
  + tg3: Driver update for RHEL-9.2.0
  + Update drivers/powercap to enable support for Arm SystemReady IR platforms

* Tue Nov 15 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.196-alt1.el9
- Updated to kernel-5.14.0-196.el9:
  + blk-mq: avoid double ->queue_rq() because of early timeout
  + cifs: bring us close to 6.0
  + CNB: devlink: Add support for line cards
  + CNB: flow_dissector: add support to dissect PPPoE fields and number of VLAN tags
  + CNB: net: drop the weight argument from netif_napi_add
  + dm: sync with upstream 6.1
  + Fix KVM selftests build failure on s390x
  + fs: dlm: -EINVAL, queue_work() race and DLM_LKF_VALBLK
  + gfs2: Register fs after creating workqueues
  + [IBM 9.2 FEAT] KVM: Crypto Passthrough Hotplug - kernel part
  + lpfc updates for centos-stream / rh9.2
  + Merge commit '8d69da5faaf1b2150e78b7b6227e7d46a3cacfdf'
  + Merge commit 'a5bd923742456b8cc6b55261868d65fc643532b9'
  + mmc: sdhci-esdhc-imx: updates for SDHCI Freescale eSDHC/uSDHC i.MX controller
  + mm/kmemleak: Fix kmemleak hang problem
  + mm: Proactive Fixes for 9.2
  + netfilter: nft_fib: Fix for rpath check with VRF devices
  + net/mptcp: phase-1  rebase for RHEL-9.2
  + scsi: core: Fix a use-after-free
  + scsi: qla2xxx: update driver to latest upstream
  + soc: qcom: update to v6.0-rc3
  + Sync rtla with upstream v5.19
  + tcp: phase-1 backports for RHEL-9.2
  + vdpa_sim_blk: set number of address spaces and virtqueue groups
  + Various changes and improvements that are poorly described in merge.

* Fri Nov 11 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.192-alt1.el9
- Updated to kernel-5.14.0-192.el9 (fixes: CVE-2022-2663, CVE-2022-3028, CVE-2022-42703):
  + af_key: Do not call xfrm_probe_algs in parallel
  + audit: backport fixes and cleanups up to upstream v6.1
  + Backport fs v6.0 and earlier commits for kernel-rt
  + block: update with v6.1-rc2
  + CNB: ethernet: add a helper for assigning port addresses
  + CNB: inet: Separate DSCP from ECN bits and use dscp_t for TOS fields
  + CNB: net: disambiguate the TSO and GSO limits
  + CNB: net: HW counters for soft devices
  + CNB: net/sched: act_police: allow 'continue' action offload
  + crypto: xts - restrict key lengths to approved values in FIPS mode
  + drm: fix duplicated code in drm_connector_register
  + drm/mgag200: Fix PLL setup for G200_SE_A rev >=4
  + Enable the RTC rv8803 driver
  + Fix and stabilize vm selftests results before including in CI
  + iavf: Fix adminq error handling
  + iomap update to v5.16
  + io_uring: update to v5.16
  + io_uring: update to v5.17
  + io_uring: update to v5.18
  + ipv4: Backport upstream fixes.
  + kselftests 9.2 P1 backport
  + KVM on s390x resync, Protected dump, Enhanced Interpretation for PCI Functions and  CPU topology
  + KVM: selftests: replace assertion with warning in access_tracking_perf_test
  + KVM: VMX: fully disable SGX if SECONDARY_EXEC_ENCLS_EXITING unavailable
  + memcg: Add memory.reclaim support
  + memcg: Backport some useful upstream patches
  + Merge commit '0e769f75b4fb40e853ac8c3a8974516424a57c23'
  + Merge commit '5df889efab934c03c35799d3338d36bd722e093c'
  + mm/rmap: Fix use-after-free related to leaf anon_vma double reuse (CVE-2022-42703)
  + mm: slub: fix flush_cpu_slab()/__free_slab() invocations in task context.
  + netfilter: 9.2 phase 1 backports
  + netfilter: fix message handling flaw
  + net: team: Unsync device addresses on ndo_stop
  + NFS/SUNRPC:  Client needs to handle session trunking group membership changes
  + owners: Remove Inaki Malerba from the owner's list as he is leaving the company
  + PCI: hv: Do not set PCI_COMMAND_MEMORY to reduce VM boot time
  + perf/arm-cmn:  cmn updates, cmn650/700 support
  + perf: Sync with upstream v5.19
  + powerpc/pseries: Use lparcfg to reconfig VAS windows for DLPAR CPU
  + powerpc/pseries/vas: Pass hw_cpu_id to node associativity HCALL
  + redhat: create /boot symvers link if it doesn't exist
  + redhat: fix the branch we pull from the documentation tree
  + redhat/Makefile: Rename LOCALVERSION to DISTLOCALVERSION
  + remoteproc: imx_rproc : updates
  + [RHEL-9.2] iommu: amd: Updates for 9.2
  + scsi: fix mpi3mr: for rt-kernels
  + scsi: iscsi: driver updates
  + scsi: qedi: update driver to latest upstream
  + scsi: scsi_transport_fc: Use %u for dev_loss_tmo
  + selftests/bpf: Limit unroll_count for pyperf600 test
  + spec: fix path to `installing_core` stamp file for subpackages
  + tipc: backports from upstream
  + Update ACPI to match Linux v6.0
  + Update drivers/rtc for known edge platforms
  + Update kernel's PCI subsystem to v6.0
  + Update objtool to v5.19
  + Update USB And Thunderbolt to v6.0
  + watchdog: imx7ulp: updates
  + x86/fpu: Do not leak fpstate pointer on fork
  + x86/fpu: Prevent FPU state corruption
  + xfrm: backports from upstream
  + Various changes and improvements that are poorly described in merge.

* Tue Nov 01 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.184-alt1.el9
- Updated to kernel-5.14.0-184.el9:
  + DRM 6.0 backport dependencies
  + MDRAID - Update to the latest upstream
  + platform/x86/intel: pmc/core: Add Raptor Lake support to pmc core driver
  + powercap: intel_rapl: Add support for RAPTORLAKE_P
  + [RHEL 9.2] IOMMU and DMA Mapping Updates

* Mon Oct 31 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.183-alt1.el9
- Updated to kernel-5.14.0-183.el9:
  + cgroup/cpuset: Add isolated partition type for disabling load balancing
  + crypto: ccp: update ccp driver upto v6.0
  + Follow on fixes for bz2120352
  + IPv6: 9.2 P1 backport from upstream
  + iwlwifi: mvm: fix double list_add at iwl_mvm_mac_wake_tx_queue
  + KVM: x86: Rebase to upstream 6.0
  + selftests: bpf: test_kmod.sh: Pass parameters to the module
  + Support for EFI confidential computing secret area in AMD SEV guests
  + tracing: Disable interrupt or preemption before acquiring arch_spinlock_t

* Wed Oct 26 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.181-alt1.el9
- Updated to kernel-5.14.0-181.el9 (fixes: CVE-2022-1462, CVE-2022-1882, CVE-2022-30594, CVE-2022-39188):
  + ACPI: processor idle: Practically limit "Dummy wait" workaround to old Intel systems
  + amd64_edac: add support for systems with different types of memory modules
  + arm64: kexec_file: use more system keyrings to verify kernel image signature
  + arm64/kexec: Fix missing extra range for crashkres_low
  + Backport selected PM commits for kernel-rt
  + block: update with upstream v6.0
  + cgroup: cgroup_get_from_id() must check the looked-up kn is a directory
  + crypto: cryptd - Protect per-CPU resource by disabling BH
  + dmaengine: Updates for 9.2
  + exfat: Stable update and fixes
  + fix pinctrl errors on Raspberry Pi 4
  + Fix UAF error in watch_queue
  + intel_idle: make SPR C1 and C1E be independent
  + io_uring: update to v5.15
  + irqdomain: Export irq_domain_disconnect_hierarchy()
  + Merge remote-tracking branch 'centos-stream-9/merge-requests/1299' into temporary-branch
  + Merge remote-tracking branch 'origin/merge-requests/1116' into HEAD
  + mm changes through v5.18 for 9.2
  + mm: prevent page_frag_alloc() from corrupting the memory
  + mmu_gather: Fix munmap() & unmap_mapping_range() race (CVE-2022-39188)
  + net: add skb drop reasons
  + net: stable backports for 9.2
  + nfp: driver update to kernel version 5.18
  + NFS refresh for RHEL-9.2
  + nvme update to v6.0
  + perf test: Record only user callchains on the "Check Arm64 callgraphs are complete in fp mode" test
  + ptrace: Check PTRACE_O_SUSPEND_SECCOMP permission on PTRACE_SEIZE
  + RDMA: update to v6.0
  + redhat/configs: enable UINPUT on aarch64
  + redhat/Makefile: Remove hardcoded BUILD_TARGET entries
  + replace CONFIG_PTE_MARKER with CONFIG_PTE_MARKER_UFFD_WP
  + [s390]: [IBM 9.2 FEAT] Support Processor Activity Instrumentation Extension 1 (IBM z16) - kernel part
  + [s390]: [IBM 9.2 FEAT] Transparent DASD PPRC (Peer-to-Peer Remote Copy) handling - kernel part
  + [s390]: ['[IBM 9.2 FEAT] Upgrade the QETH driver to latest from upstream', ' e.g. kernel 5.20']
  + scsi: bnx2fc: update driver to latest upstream
  + scsi: qedf: update driver to latest upstream
  + SCSI updates for RHEL 9.2
  + tty: fix possible race condition in drivers/tty/tty_buffers.c
  + Update drivers/i2c for known edge platforms
  + Update drivers/phy to support Arm SystemReady IR
  + Update DTS bindings for known edge platforms
  + Updates to drivers/perf to support Arm SystemReady IR
  + VFIO 9.2 backports
  + wireguard: netlink: avoid variable-sized memcpy on sockaddr
  + Various changes and improvements that are poorly described in merge.

* Mon Oct 17 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.177-alt1.el9
- Updated to kernel-5.14.0-177.el9:
  + Backport printk v5.19 and earlier commits for kernel-rt
  + cpufreq: intel_pstate: Support Sapphire Rapids OOB mode
  + crypto: disallow plain DH and ECDH usage in FIPS mode
  + FS fixes for 9.2 on inotify
  + random: trigger reseeding DRBG on more occasions
  + target: Update to the latest upstream version
  + Update drivers/pinctrl for use with Arm SystemReady IR and other Edge platforms
  + Update turbostat to upstream 6.0
  + watchdog: Fix SBSA watchdog accesses

* Tue Oct 11 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.175-alt1.el9
- Updated to kernel-5.14.0-175.el9 (fixes: CVE-2021-26341):
  + bpf: Use bpf_capable() instead of CAP_SYS_ADMIN for blinding decision
  + Cleanup int3400 thermal OSC handling
  + crypto: qat: Update QAT drivers upto v6.1-rc1
  + gfs2: Use TRY lock in gfs2_inode_lookup for UNLINKED inodes
  + IPMI updates and bug fixes
  + Merge tag 'kernel-5.14.0-162.6.1.el9_1'
  + netfilter: late backports from upstream
  + nvme-tcp: handle number of queue changes
  + Raspberry Pi: fix irq-bcm2835/36 build errors
  + redhat: change default dist suffix for RHEL 9.1
  + redhat: fix elf got hardening for vm tools
  + [redhat] kabi: add symbols to stablelist
  + [redhat] kabi: re-enable build-time kabi-checks
  + redhat: Update directory with ARK changes
  + [s390]: [IBM 9.2 FEAT] Support IBM z16 Processor-Activity-Instrumentation Facility - kernel part
  + sfc: fix TX channel offset when using legacy interrupts
  + x86,config: Enable straight-line-speculation fix
  + xfs: sync to upstream v5.15

* Sat Oct 01 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.171-alt1.el9
- Updated to kernel-5.14.0-171.el9:
  + Add Device IDs for Raptor Lake and Raptor Lake S
  + bonding: fixes for 9.2
  + drm/bochs: fix blanking
  + irqchip/qcom-pdc: update to v5.19-rc4
  + opp: backport changes from v5.19-rc8

* Thu Sep 29 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.170-alt1.el9
- Updated to kernel-5.14.0-170.el9:
  + Backport scheduler related v5.19 and earlier commits for kernel-rt
  + bonding: fix NULL deref in bond_rr_gen_slave_id
  + configs: enable CONFIG_HP_ILO for aarch64
  + iwlwifi: limit fw version for AC9560 to avoid fw crash
  + Merge tag 'kernel-5.14.0-162.4.1.el9_1'
  + NFSv4.1+ session trunking discovery
  + [s390]: RHEL9.2 - KVM: PV: ext call delivered twice when receiver in PSW wait
  + [s390]: RHEL9.2 - s390/hugetlb: fix prepare_hugepage_range() check for 2 GB
  + [s390]: RHEL9.2 - s390/mm: do not trigger write fault when vma does not allow

* Tue Sep 27 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.168-alt1.el9
- Updated to kernel-5.14.0-168.el9 (fixes: CVE-2022-20141, CVE-2022-3077):
  + ACPI: Improve fwnode serial multi-instantiate driver
  + assoc_array: Fix BUG_ON during garbage collect
  + Backport fscache/cachefiles rework for 9.2
  + BPF and XDP rebase to v5.17
  + drm/amdgpu: Only disable prefer_shadow on hawaii
  + drm/hyperv : Removing the restruction of VRAM allocation with PCI bar size
  + drm/nouveau/kms/nv140-: Disable interlacing
  + i2c: ismt: prevent memory corruption in ismt_access()
  + i40e: Fix kernel crash during module removal
  + ice: Allow operation with reduced device MSI-X
  + igmp: Add ip_mc_list lock in ip_check_mc_rcu
  + ixgbe: Add locking to prevent panic when setting sriov_numvfs to zero
  + Merge tag 'kernel-5.14.0-162.3.1.el9'
  + nohz/full, sched/rt: Fix missed tick-reenabling bug in dequeue_task_rt()
  + NUMA related scheduler improvements
  + nvme-fc: fix the fc_appid_store return value
  + powerpc/mobility: Extend the NMI watchdog timer during the LPM
  + powerpc/perf: Optimize clearing the pending PMI and remove WARN_ON for PMI check in power_pmu_disable
  + rcu: Update RCU code base to v5.19 for 9.2 RT
  + Revert "net: macsec: update SCI upon MAC address change."
  + [s390]: [IBM 9.2 FEAT] Static PIE Support - kernel part
  + [s390]: RHEL9.0 - zfcp: fix missing auto port scan and thus missing target ports
  + sched/fair: Introduce SIS_UTIL to search idle CPU based on sum of util_avg
  + scsi: restore setting of scmd->scsi_done() in EH and reset ioctl paths
  + sysctl: returns -EINVAL when a negative value is passed to proc_doulongvec_minmax
  + x86/boot: Don't propagate uninitialized boot_params->cc_blob_address

* Thu Sep 15 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.164-alt1.el9
- Updated to kernel-5.14.0-164.el9:
  + Fix null pointer reference in nvmem_unregister
  + iavf: bug fixes August 2022
  + platform/x86/intel: pmc/core add support for ADL-N
  + Update Intel Platform Monitoring Technology
  + Update kernel's PCI subsystem to v5.19
  + Use final upstream fix for DMAR_UNITS_SUPPORTED
  + vfio/type1: Unpin zero pages

* Thu Sep 08 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.163-alt1.el9
- Updated to kernel-5.14.0-163.el9:
  + CNB: rebase/update devlink for RHEL 9.2 to upstream v5.18
  + New device IDs for RPL-S: NPK
  + [s390]: [IBM 9.1 FEAT] Long Kernel Commmand Line for s390x - kernel part
  + Upgrade drivers/firmware to support Arm SystemReady IR
  + Upgrade drivers/gpio to support Arm SystemReady IR
  + vdpa/mlx5: Update Control VQ callback information
  + x86/cpu: Add new Raptor Lake CPU model number

* Tue Sep 06 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.162-alt1.el9
- Updated to kernel-5.14.0-162.el9 (fixes: CVE-2022-2585):
  + Fix: posix cpu timer use-after-free
  + Revert "ixgbevf: Add support for new mailbox communication between PF and VF"

* Sat Sep 03 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.161-alt1.el9
- Updated to kernel-5.14.0-161.el9:
  + Fixes for bz-2121368
  + random: allow reseeding DRBG with getrandom
  + redhat: remove GL_DISTGIT_USER, RHDISTGIT and unify dist-git cloning

* Fri Aug 26 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.160-alt1.el9
- Updated to kernel-5.14.0-160.el9 (fixes: CVE-2022-1679, CVE-2022-26373):
  + ath9k: fix use-after-free in ath9k_hif_usb_rx_cb
  + Chelsio FCoE Initiator Driver (csiostor) update to upstream 5.19-rc4
  + iavf: Fix VLAN_V2 addition/rejection
  + net: qcom/emac: Fix improper merge resolution in device_get_mac_address
  + nvme-fc: restart admin queue if the caller needs to restart queue
  + Pull updated changes for gve driver from upstream
  + x86/speculation: Post-barrier Return Stack Buffer Predictions (CVE-2022-26373)

* Thu Aug 25 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.159-alt1.el9
- Updated to kernel-5.14.0-159.el9:
  + crypto: allow algs only in specific constructions in FIPS mode
  + i2c: qcom-geni: Pull up to v5.19-rc5
  + wireless: stack & drivers bugfixes update from v5.18

* Thu Aug 25 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.158-alt1.el9
- Updated to kernel-5.14.0-158.el9:
  + [9.1] DRM stable backport up 5.18.13
  + clk: qcom: add SC8280XP GCC
  + drm/nouveau: recognise GA103
  + interconnect: qcom: add sc8280xp support
  + iommu/arm-smmu-qcom: Add SC8280XP support
  + phy: qcom: update to v5.19-rc4
  + pinctrl: qcom: update to v5.19-rc3
  + Rebase mlx5 up to kernel 5.18
  + scsi: ufs: update to v5.19-rc4
  + soc: qcom: llcc: update to v5.19-rc6
  + soc: qcom: rpmhpd: update to 5.19-rc5
  + soc: qcom: smem: update to v5.19-rc6
  + spi: spi-geni-qcom: Pull up to v5.19-rc5

* Wed Aug 24 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.155-alt1.el9
- Updated to kernel-5.14.0-155.el9 (fixes: CVE-2022-2586, CVE-2022-36946):
  + ALSA: AMD - fix the ACPI tables to detect correctly Lenovo products using the DMIC (digital microphone)
  + be2net: Driver Update
  + i40e: Fix tunnel checksum offload with fragmented traffic
  + iavf: Fix deadlock in initialization
  + ice: bug fixes August 2022
  + KVM: nVMX: Inject #UD if VMXON is attempted with incompatible CR0/CR4
  + mm: Fix PASID use-after-free issue
  + netfilter: nf_queue: do not allow packet truncation below transport header offset
  + netfilter: nf_tables: do not allow to reference objects in foreign tables
  + raid1: ensure write behind bio has less than BIO_MAX_VECS sectors
  + redhat: update kabi tooling
  + selftests: mptcp: make sendfile selftest work
  + sfc: fix use after free when disabling sriov
  + wait: Fix __wait_event_hrtimeout for RT/DL tasks

* Tue Aug 23 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.154-alt1.el9
- Updated to kernel-5.14.0-154.el9:
  + AMD Secure Nested Paging (SEV-SNP) Guest Support

* Tue Aug 23 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.153-alt1.el9
- Updated to kernel-5.14.0-153.el9:
  + Driver upgrade for mlx4
  + netfilter: nf_log_syslog: Don't ignore unknown protocols
  + netfilter: nf_tables: fix crash when nf_trace is enabled
  + redhat: Use redhatsecureboot701 for ppc64le
  + Upgrade drivers/base/property.c to support Arm SystemReady IR

* Tue Aug 23 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.152-alt1.el9
- Updated to kernel-5.14.0-152.el9:
  + Rebase mlx5 up to kernel 5.17
  + Upgrade drivers/of to support Arm SystemReady IR

* Sun Aug 21 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.150-alt1.el9
- Updated to kernel-5.14.0-150.el9 (fixes: CVE-2022-2590):
  + CNB: rebase/update netdevsim for RHEL 9.1
  + Documentation: Describe net.ipv4.tcp_reflect_tos.
  + drm/amd/display: Fix new dmub notification enabling in DM
  + fs: dlm: fix potential recursive spinlock issue
  + In ACPI v5.18, revert explicit ghes_init() calls to avoid conflict with edac
  + KVM: selftests: Disable rseq_test for all architectures
  + KVM: x86: nSVM: implement nested VMLOAD/VMSAVE
  + megaraid: fix for a cpu hotplug
  + mm: Fix CVE-2022-2590 by reverting "mm/shmem: unconditionally set pte dirty in mfill_atomic_install_pte"
  + netfilter: conntrack: rebase to 5.19
  + nfsd: eliminate the NFSD_FILE_BREAK_* flags
  + nfs: fix hung DIO writes in -ENOSPC conditions
  + sfc: fix kernel panic when creating VF
  + SUNRPC don't resend a task on an offlined transport
  + vmxnet3: do not reschedule napi for rx processing

* Fri Aug 19 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.148-alt1.el9
- Updated to kernel-5.14.0-148.el9 (fixes: CVE-2022-21499):
  + fs: dlm: change posix lock sigint handling
  + fs: dlm: make dlm_callback_resume quite
  + lockdown: also lock down previous kgdb use
  + perf: fix endless loop in BPF tests
  + scsi: qla2xxx: Fix erroneous mailbox timeout after PCI error injection
  + vdpasim: control virtqueue support

* Thu Aug 18 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.147-alt1.el9
- Updated to kernel-5.14.0-147.el9:
  + ALSA: backport fixes for RHEL 9.1
  + ALSA: backport for RHEL 9.1

* Wed Aug 17 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.146-alt1.el9
- Updated to kernel-5.14.0-146.el9:
  + bnxt_en: additional commits for RHEL9.1
  + Chelsio iWARP (iw_cxgb4) update to upstream 5.19-rc4
  + Chelsio NIC (cxgb4/cxgb4vf/libcxgb) update to upstream 5.19-rc4
  + igc: Driver Update
  + KVM: x86: stable fixes since 5.18
  + mpt3sas: fix a problem with shutdown
  + qede: Reduce verbosity of ptp tx timestamp
  + redhat: nvme/tcp mistakenly uses blk_mq_tag_to_rq(nvme_tcp_tagset(queue))
  + update cpufreq to v5.18
  + Update Marvell OcteonTX2 device drivers to v5.18
  + virtio_ring: sync the vritio_ring with upstream

* Tue Aug 09 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.144-alt1.el9
- Updated to kernel-5.14.0-144.el9 (fixes: CVE-2022-1184):
  + ena: update driver to v5.18
  + ext4: fix use-after-free and memory errors when working with a corrupted directory
  + Fix outstanding device-mapper bugs from upstream 5.19 and 6.0
  + ipmi: When handling send message responses, don't process the message
  + NFS: Fix initialisation of nfs_client cl_flags field
  + opp: fix broken DT boot on Nvidia Jetson
  + scsi: qla2xxx: Fix imbalance vha->vref_count
  + smartpqi updates
  + xfs: Ensure important RHEL8 fixes are present in RHEL9

* Mon Aug 08 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.143-alt1.el9
- Updated to kernel-5.14.0-143.el9 (fixes: CVE-2022-23816, CVE-2022-23825, CVE-2022-29900, CVE-2022-29901):
  + Documentation: add a description for net.core.high_order_alloc_disable
  + net: ping6: Fix memleak in ipv6_renew_options().
  + rebase the input and HID stack in RHEL 9.1
  + [RHEL 9.1.0 BZ 2015209] A couple dma fixes
  + [RHEL9.1 BZ2100482] Revert dmaengine: idxd: Separate user and kernel pasid enabling
  + sched, cpuset: Fix dl_cpu_busy() panic due to empty cs->cpus_allowed
  + sit: do not call ipip6_dev_free() from sit_init_net()
  + x86: Fix RETBleed Vulnerabilities

* Wed Aug 03 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.141-alt1.el9
- Updated to kernel-5.14.0-141.el9:
  + ACPI: VIOT: Fix ACS setup
  + Documentation: Add an explanation of NFSv4 client identifiers
  + Documentation: filesystems: proc: update meminfo section
  + iommu/vt-d:  A couple of late landing fixes
  + mm: make slab and vmalloc allocators __GFP_NOLOCKDEP aware
  + mm/munlock: Fix sleeping function called from invalid context bug
  + powercap: intel_rapl: add support for ALDERLAKE_N
  + ppc64le: bpf: bpf_perf_event.h field 'regs' has incomplete type (perf:)
  + scsi: qla2xxx: Fix excessive I/O error messages by default
  + Update ACPI to match Linux v5.18

* Wed Aug 03 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.140-alt1.el9
- Updated to kernel-5.14.0-140.el9:
  + ibmvnic: Properly dispose of all skbs during a failover.
  + Increase PERF_MAX_TRACE_SIZE to handle Sentinel1 and docker together
  + perf stat report segfaults
  + powerpc/fadump: save CPU reg data in vmcore when PHYP terminates LPAR

* Mon Aug 01 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.139-alt1.el9
- Updated to kernel-5.14.0-139.el9:
  + cgroup: Miscellaneous bug fixes and enhancements
  + drm/mgag200: Add FB damage clips and gamma support
  + Fix kvm/selftests/rseq_test failure
  + net: mld: fix reference count leak in mld_{query | report}_work()
  + RDMA: Bug fixes from v5.19
  + update the non-x86 portions of drivers/platform to v5.18
  + vsock: backport latest commits for RHEL-9-1

* Mon Aug 01 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.138-alt1.el9
- Updated to kernel-5.14.0-138.el9:
  + Add support for MaxLinear NICs (GPY115/21x/24x driver)
  + blk-mq: don't create hctx debugfs dir until q->debugfs_dir is created
  + block: Fix handling of offline queues in blk_mq_alloc_request_hctx()
  + bonding: bugfix series from v5.19
  + Bring MD kernel up to date
  + CNB: net: Don't include filter.h from net/sock.h
  + crypto: qat: Update QAT drivers upto v5.19
  + Documentation: fix udp_wmem_min in ip-sysctl.rst
  + e1000e: Driver update for RHEL9.1
  + Enable MediaTek BT Support for RHEL-9 and bug fixes
  + fscache: Avoid ASSERTCMP if two threads race into fscache_disable_cookie
  + netdevsim: don't overwrite read only ethtool parms
  + NFSv4.1 support for NFS4_OPEN_RESULT_PRESERVE_UNLINKED
  + nvme: fix RCU hole that allowed for endless looping in multipath round robin
  + redhat/configs/common: Enable CONFIG_LZ4_COMPRESS
  + redhat: workaround CKI cross compilation for scripts
  + RHEL-9 nfsd server post_wcc fixes - clients see increased revalidations
  + sfc: fix efx_separate_tx_channels=y
  + tools/testing/nvdimm: Fix security_init() symbol collision
  + Update intel_idle with SPR and ADL support
  + Update USB and Thunderbolt to v5.19-rc5
  + vdpa/mlx5: Fix ethtool can not set combined numbers in vm when the vcpu < vqs
  + XDP/Networking BPF: 9.1 P2 backports from upstream

* Thu Jul 28 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.136-alt1.el9
- Updated to kernel-5.14.0-136.el9:
  + arm64: update GIC interrupt controller driver to v5.18 level
  + bpftool: Enable libbpf's strict mode by default
  + drivers/base: fix userspace break from using bin_attributes for cpumap and cpulist
  + ipv4: backport upstream fixes
  + nfsd: destroy percpu stats counters after reply cache shutdown
  + x86/kexec: fix memory leak of elf header buffer
  + xfs: fallocate doesn't drop privileges or capabilities

* Fri Jul 22 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.135-alt1.el9
- Updated to kernel-5.14.0-135.el9 (fixes: CVE-2022-34918):
  + ACPI, PCI: Power Management fixes
  + Additional SCSI updates for 9.1
  + audit: backport from upstream v5.18 to v5.19-rc3
  + block drivers: fix build warning on not checking add_disk*
  + IPv6: 9.1 P2 backports from upstream
  + kselftest: backport from upstream P2
  + Make signature verification FIPS compliant
  + mptcp: backports for 9.1p2
  + net: backport upstream fixes for IP tunnels
  + netfilter: 9.1 P2 backports
  + netfilter: nf_tables: stricter validation of element data
  + net: openvswitch: fix misuse of the cached connection on tuple changes
  + net/other: backports for 9.1 p2
  + net/sched: backports for 9.1 p2
  + redhat: fix kernel_variant_package option definition
  + tcp: fix possible divide-by-zero
  + tipc: backports from upstream, 2nd phase
  + tipc: move bc link creation back to tipc_node_create

* Wed Jul 20 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.133-alt1.el9
- Updated to kernel-5.14.0-133.el9 (fixes: CVE-2022-0854, CVE-2022-21123, CVE-2022-21125, CVE-2022-21166, CVE-2022-28893):
  + arm64: Update core arch code to upstream v5.18
  + dlm: fix missing lkb refcount handling
  + fix swiotlb information leak with DMA_FROM_DEVICE
  + igb: Driver Update
  + kdump: round up the total memory size to 128M for crashkernel reservation
  + lockd: set fl_owner when unlocking files
  + lpfc cs9 (rhel9.1) update to 14.2.0.5
  + nfs: reexport documentation
  + ovs: backports for 9.1 P2
  + remoteproc: updates for build issues
  + scsi: target: pscsi: Set SCF_TREAT_READ_AS_NORMAL flag only if there is valid data
  + SUNRPC: Ensure we flush any closed sockets before xs_xprt_free()
  + update cpuidle to v5.18
  + Update drivers/base to v5.18
  + x86/speculation/mmio: Fix Processor MMIO Stale Data Vulnerabilities

* Fri Jul 15 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.130-alt1.el9
- Updated to kernel-5.14.0-130.el9:
  + CNB: bpf: Let bpf_warn_invalid_xdp_action() report more info
  + mm: folio backports part 2
  + redhat: make kernel-zfcpdump-core to not provide kernel-core/kernel
  + scsi: csiostor: Add module softdep on cxgb4
  + scsi: iscsi: iSCSI transport bugfixes

* Fri Jul 15 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.129-alt1.el9
- Updated to kernel-5.14.0-129.el9:
  + DRM 5.18 backport
  + ext4,jbd2: Backport fixes from 5.18
  + iRDMA: Driver update to v5.19
  + Make NFSv4 OPEN(CREATE) less brittle
  + net/core: backport fixes from upstream for 9.1 P2
  + redhat/configs: enable CONFIG_SAMPLE_VFIO_MDEV_MTTY
  + spec: Keep .BTF section in modules
  + virtiofs: Add support for SELinux

* Tue Jul 12 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.128-alt1.el9
- Updated to kernel-5.14.0-128.el9:
  + block: kill warning of 'Directory XXXXX with parent 'block' already present!'
  + CNB: gro: get out of core files
  + sched: Fix balance_push() vs __sched_setscheduler()
  + selftests, xsk: Fix bpf_res cleanup test

* Sun Jul 10 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.127-alt1.el9
- Updated to kernel-5.14.0-127.el9:
  + aarch64: Enable NVIDIA Jetson Xavier SoCs
  + fs: dlm: filter messages case to avoid kernel crash
  + hyperv: Add support for AMD SEV-SNP for Azure/Hyper-V
  + igbvf: Driver Update
  + perf: Support Cstate PMU on SPR
  + powercap: intel_rapl: add support for RaptorLake
  + r8169: driver update
  + x86/sme: fix boot failure when memory encryption is enabled

* Fri Jul 08 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.126-alt1.el9
- Updated to kernel-5.14.0-126.el9:
  + cxl: Update CXL code from upstream 5.17.
  + kvm/arm64 rebase for RHEL9.1
  + mm/page_alloc: always attempt to allocate at least one page during bulk allocation

* Thu Jul 07 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.125-alt1.el9
- Updated to kernel-5.14.0-125.el9:
  + bnxt: Driver update for RHEL9.1
  + CIFS, backport two patches that fixes issues in smb2_compound_op
  + gfs2: Make sure FITRIM minlen is rounded up to fs block size
  + i40e: Driver Update
  + iavf: Driver update to upstream 5.18
  + ice: Driver update to upstream 5.18
  + time: Handle negative seconds correctly in timespec64_to_ns()

* Tue Jul 05 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.124-alt1.el9
- Updated to kernel-5.14.0-124.el9:
  + ceph: wait on async create before checking caps for syncfs
  + CNB: lib: bitmap: Introduce node-aware alloc API
  + dm: sync with upstream 5.19
  + scsi: ibmvfc: Allocate/free queue resource only during probe/remove

* Fri Jul 01 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.123-alt1.el9
- Updated to kernel-5.14.0-123.el9:
  + exec: Force single empty string when argv is empty
  + net: backport netdevice and netns refcount tracking and enable them for debug kernels
  + nfs: fix broken handling of the softreval mount option
  + powerpc: Enable execve syscall exit tracepoint
  + rcu: Fix rcu_tasks_verify_self_tests failure
  + scsi: ibmvfc: Store vhost pointer during subcrq allocation

* Thu Jun 30 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.122-alt1.el9
- Updated to kernel-5.14.0-122.el9:
  + Add MEI support for ADL-N
  + Backport fixes for ucounts
  + bonding: ARP monitor spams NETDEV_NOTIFY_PEERS notifiers
  + exec: Force single empty string when argv is empty
  + Intel SDSi: fix issue reading state certificate
  + iwlwifi: fix use-after-free
  + mptcp: fix checksum byte order
  + net: hyper-v: NetVSC driver updates for 9.1
  + [PATCHv3 00/28] support reserving crashkernel above 4G on arm64 kdump
  + s390/crypto: add SIMD implementation for ChaCha20

* Wed Jun 29 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.121-alt1.el9
- Updated to kernel-5.14.0-121.el9:
  + arm64: Update core arch code to upstream v5.16
  + crypto: fips - make proc files report fips module name and version
  + fuse: allow sharing existing sb
  + gfs2: File corruption with large writes when memory is tight
  + kbuild: Enable -std=gnu11
  + redhat/configs: Set CONFIG_VIRTIO_IOMMU on x86_64
  + redhat/kernel.spec.template: fix standalone tools build

* Mon Jun 27 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.120-alt1.el9
- Updated to kernel-5.14.0-120.el9 (fixes: CVE-2022-1998, CVE-2022-2078):
  + block: update with 5.18 for rhel 9.1
  + fanotify: Fix stale file descriptor in copy_event_to_user()
  + netfilter: nf_tables: sanitize nft_set_desc_concat_parse()
  + ntb: update from upstream v5.17
  + redhat: spec: trigger dracut when modules are installed separately
  + [s390] s390/zcrypt: Add admask to zcdn
  + scsi: mpi3mr: Add bsg device support
  + tcp: Don't acquire inet_listen_hashbucket::lock with disabled BH.
  + vmxnet3: Update network driver for RHEL 9.1

* Fri Jun 24 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.119-alt1.el9
- Updated to kernel-5.14.0-119.el9:
  + mt76: mt7921: Fix the error handling path of mt7921_pci_probe()
  + powerpc/pseries:  Added support for differentiated memory equivalent to ACPI special purpose memory (SPM) (SCM/pmem)
  + revert bus: Make remove callback return void
  + [s390] drivers/s390/char: Add Ultravisor io device
  + [s390] [IBM 9.1 FEAT] Upgrade the SMC driver to latest from upstream, e.g. kernel 5.18
  + tg3: Driver update for RHEL9.1
  + wireless: stack & drivers update to v5.18

* Thu Jun 23 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.118-alt1.el9
- Updated to kernel-5.14.0-118.el9:
  + ixgbe: Driver update for RHEL9.1
  + sfc: update to upstream v5.18
  + SGX updates from v5.17

* Wed Jun 22 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.117-alt1.el9
- Updated to kernel-5.14.0-117.el9:
  + Enable verbose error logging support for nvme
  + ionic: update driver to v5.18
  + Make DMAR_UNITS_SUPPORTED configurable
  + powerpc/rtas: rtas_busy_delay() improvements
  + [s390] zcrypt DD: Exploitation Support of new IBM Z Crypto Hardware - kernel part
  + scripts/pahole-flags.sh: use exit instead of return at the top level
  + Update kernel's PCI subsystem to v5.18
  + XDP and networking eBPF rebase to v5.16
  + xfs: validate inode fork size against fork format

* Tue Jun 21 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.116-alt1.el9
- Updated to kernel-5.14.0-116.el9:
  + CNB: Update TC subsystem to upstream v5.18
  + hv: vmbus: Driver updates for 9.1
  + ixgbevf: Driver update for RHEL9.1
  + [RHEL9.1] IOMMU/DMA Updates
  + video: fbdev: hyperv_fb: Allow resolutions with size > 64 MB for Gen1
  + x86/fpu: KVM: Set the base guest FPU uABI size to sizeof(struct kvm_xsave)

* Fri Jun 17 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.114-alt1.el9
- Updated to kernel-5.14.0-114.el9 (fixes: CVE-2022-1729):
  + block: ignore RWF_HIPRI hint for sync dio
  + lpfc cs9 (rhel9.1) update
  + perf: Fix sys_perf_event_open() race against self
  + redhat/configs: Drop outdated CRYPTO_ECDH and unify CRYPTO_USER configs
  + [s390] Upgrade the zfcp driver to latest from upstream, e.g. kernel 5.18
  + Update ext4 and jbd2 to upstream v5.17

* Thu Jun 16 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.113-alt1.el9
- Updated to kernel-5.14.0-113.el9:
  + bpf update v5.16
  + netfilter: nat: really support inet nat without l3 address
  + netfilter: nf_tables: double hook unregistration in netns path
  + powerpc/rtas: Keep MSR[RI] set when calling RTAS
  + [s390] - s390/dasd: Fix read inconsistency and failure for ESE devices
  + Update ACPI subsystem to match Linux 5.17
  + Watchdog driver  (sp5100_tco) support for AMD Family 17 and Family 19 CPUs

* Wed Jun 15 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.112-alt1.el9
- Updated to kernel-5.14.0-112.el9:
  + iio: updates
  + net: mana: MANA driver updates for RHEL 9.1
  + PCI: Hyper-V: PCI driver updates for RHEL 9.1
  + [s390] s390/dasd: Fix data corruption for ESE devices
  + VMCI: Update driver and enable ARM64 build

* Tue Jun 14 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.111-alt1.el9
- Updated to kernel-5.14.0-111.el9 (fixes: CVE-2022-1966):
  + Add pinctrl support for ADL-N
  + block, loop: support partitions without scanning
  + [Intel 9.1 FEAT] [RPL-P] perf: PerfMon support
  + ipv4: do not use per netns icmp sockets
  + netfilter: nf_tables: disallow non-stateful expression in sets earlier
  + remoteproc: updates
  + scsi: fnic: Finish scsi_cmnd before dropping the spinlock
  + turbostat: fix PC6 displaying on some systems

* Mon Jun 13 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.110-alt1.el9
- Updated to kernel-5.14.0-110.el9:
  + ACPI: sysfs: Fix BERT error region memory mapping
  + CNB: net: disable NET_RX_BUSY_POLL on PREEMPT_RT
  + Hyper-V: x86: x86_64 Updates for RHEL 9.1
  + KVM: x86: Rebase to v5.18
  + topology: make core_mask include at least cluster_siblings

* Fri Jun 10 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.109-alt1.el9
- Updated to kernel-5.14.0-109.el9:
  + Backport latest fixes from upstream s390x KVM for the RHEL 9.1 kernel
  + Brush up s390x/zfcpdump/ configs
  + CNB: net: consolidate neif_rx() and make it callable from any context
  + mptcp: better window sharing
  + ovs: 9.1 P1 backports
  + powerpc: Support for reporting NVDIMM performance stats (HMS/SCM/pmem)
  + redhat/configs: enable interconnect for NXP i.MX 8M
  + [s390] s390/cpumf: add new extended counter set for IBM z16
  + [s390] s390/perf: obtain sie_block from the right address
  + x86/split_lock: Enable the split lock feature on Raptor Lake

* Thu Jun 09 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.108-alt1.el9
- Updated to kernel-5.14.0-108.el9:
  + ahci: Add a generic 'controller2' RAID id
  + bnx2x: fix napi API usage sequence
  + CNB: net: add netif_set_real_num_queues() for device reconfig
  + interconnect: updates
  + net/af_packet: add VLAN support for AF_PACKET SOCK_RAW GSO
  + net: openvswitch: fix leak of nested actions
  + NFSv4: Fix free of uninitialized nfs4_label on referral lookup.
  + regulator: updates
  + rpmsg: updates
  + Scheduler late arriving fixes for 9.1
  + scsi: scsi_dh_alua: Properly handle the ALUA transitioning state
  + selftests/bpf: Fix btf_dump test under new clang
  + spmi: updates
  + vdpa: mlx5: prevent cvq work from hogging CPU

* Tue Jun 07 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.106-alt1.el9
- Updated to kernel-5.14.0-106.el9 (fixes: CVE-2022-24448):
  + clk: qcom: rpmhcc: add sc8280xp support to the RPMh clock controller
  + Documentation: add description for net.core.gro_normal_batch
  + Documentation/sysctl: document max_rcu_stall_to_panic
  + drivers/char: fix unused variable warning in mem.c
  + Fixes for nfs_atomic_open()
  + mm, compaction: fast_find_migrateblock() should return pfn in the target zone
  + PTP: backport fixes from upstream
  + [RHEL 9.1.0] IDXD fixes
  + [s390] Upgrade the qeth driver to latest from upstream

* Fri Jun 03 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.105-alt1.el9
- Updated to kernel-5.14.0-105.el9:
  + Add Alderlake and Raptorlake CPU model numbers
  + Documentation/sysctl: document page_lock_unfairness
  + iommu/virtio: Support bypass domains
  + NFSv4.2: Fix up an invalid combination of memory allocation flags
  + Update bluetooth to upstream 5.17-rc5
  + Update thermal/int340x for RPL
  + XDP and networking eBPF rebase to v5.15

* Thu Jun 02 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.104-alt1.el9
- Updated to kernel-5.14.0-104.el9:
  + bonding: driver update for 9.1
  + mptcp: fix subflow accounting on close
  + redhat: enable CONFIG_NET_ACT_CTINFO (as a module)
  + update qedi driver to latest upstream

* Wed Jun 01 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.103-alt1.el9
- Updated to kernel-5.14.0-103.el9:
  + dlm: fix plock invalid read
  + ipc/mqueue: use get_tree_nodev() in mqueue_get_tree()
  + MMIO support for SMBus and ASF controller in AMD APU/CPU
  + mpt3sas: driver update
  + powerpc/pseries/vas: Use QoS credits from the userspace
  + powerpc: support for perf sampling tests (PMU/performance counters/perf) [FEAT]
  + s390/cio: verify the driver availability for path_event call
  + [s390] RDMA/mlx5: Fix number of allocated XLT entries
  + [s390] s390/hypfs: include z/VM guests with access control group set
  + [s390] s390/tape: fix timer initialization in tape_std_assign()
  + scsi: mpi3mr: driver update
  + Sync osnoise/timerlat tracers with v5.17 upstream
  + tcp: stable backports for rhel 9.1 phase 1
  + vfs: make sync_filesystem return errors from ->sync_fs

* Tue May 31 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.102-alt1.el9
- Updated to kernel-5.14.0-102.el9:
  + Enable INTEL_HFI_THERMAL
  + livepatch: rebase to linux v5.17
  + perf: sync with upstream v5.17
  + thunderx nic: mark device as unmaintained
  + xfs: Fix the free logic of state in xfs_attr_node_hasname

* Sat May 28 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.101-alt1.el9
- Updated to kernel-5.14.0-101.el9:
  + mm: Backport upstream mm commits for kernel-rt
  + redhat: Exclude cpufreq.h from kernel-headers
  + tools: Fix radix-tree test build failure

* Thu May 26 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.100-alt1.el9
- Updated to kernel-5.14.0-100.el9:
  + bpf: update to v5.15
  + KVM: Enable storage key checking for intercepted instruction
  + PCI: vmd: IRQ domain assignment to sub devices

* Wed May 25 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.99-alt1.el9
- Updated to kernel-5.14.0-99.el9:
  + ceph: backport mainline changes up to v5.18 for RHEL 9.1
  + [EHL] Intel Sensor Hub (ISH): EClite driver enabling
  + Enable virtio-mem as tech-preview for aarch64
  + intel_idle: updates
  + megaraid_sas: driver update
  + net: drop_monitor: support drop reason
  + selftests: RHEL 9.1 backports from upstream
  + update tools/cpupower

* Tue May 24 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.98-alt1.el9
- Updated to kernel-5.14.0-98.el9:
  + hv_balloon: rate-limit "Unhandled message" warning
  + KVM: s390: pv: make use of ultravisor AIV support
  + update qla2xxx driver to latest upstream

* Mon May 23 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.97-alt1.el9
- Updated to kernel-5.14.0-97.el9 (fixes: CVE-2022-1012, CVE-2022-27666):
  + bridge: update bridge and switchdev to upstream v5.18
  + cifs: truncate the inode and mapping when we simulate fcollapse
  + Enable VM kselftests
  + net: esp: fix out-of-bounds writes (CVE-2022-27666)
  + quota: make dquot_quota_sync return errors from ->sync_fs
  + redhat/configs: enable GUP_TEST in debug kernel
  + ses: fix a fan issue
  + Sync SELinux/LSM code with upstream up to v5.18-rc5
  + tcp: Increase randomness for source port generation.

* Thu May 19 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.96-alt1.el9
- Updated to kernel-5.14.0-96.el9 (fixes: CVE-2022-28390):
  + can: ems_usb: ems_usb_start_xmit(): fix double dev_kfree_skb() in error path
  + powerpc/ibmvnic: Upgrade ibmvnic device driver to latest from upstream, e.g. kernel 5.18
  + powerps/pseries/dma: Add support for 2M IOMMU page size
  + soc/tegra: Add devm_tegra_core_dev_init_opp_table_common()
  + VFIO refresh to v5.18

* Thu May 19 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.95-alt1.el9
- Updated to kernel-5.14.0-95.el9:
  + mm: create a new system state and fix core_kernel_text()
  + openvswitch: Fix setting ipv6 fields causing hw csum failure
  + vmxnet3: Update network driver for RHEL 9.1

* Wed May 18 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.94-alt1.el9
- Updated to kernel-5.14.0-94.el9:
  + arch/arm64: Fix topology initialization for core scheduling
  + arm64: enable CONFIG_MEMORY_HOTREMOVE
  + arm64: Fix KPTI disabling on ThunderX
  + CNB: eth: fwnode: remove the addr len from mac helpers
  + CNB: rebase/update devlink for RHEL 9.1
  + dm integrity: fix memory corruption when tag_size is less than digest size
  + drivers/char/random.c: Update for kernel-rt
  + efi: Allow to enable EFI runtime services by default on RT
  + ipvlan/macvlan: phase-1 updates for 9.1
  + locking: Backport upstream v5.18 locking/rcu commits for kernel-rt
  + md: fix NULL pointer deref with nowait but no mddev->queue
  + mptcp: rebase code to 5.18-net-next
  + net: backport core fixes from upstream
  + netfilter: phase 1 backports from upstream
  + netfilter: revert "kernel: lack of port sanity checking in natd and netfilter leads to exploit of OpenVPN clients"
  + NFSv4 only print the label when its queried
  + ntb_hw_amd: Add NTB PCI ID for new gen CPU
  + nvme: tp-8010 support
  + post upstream v5.14 backports for kprobes and arm64
  + scsi: target: update LIO to the latest version
  + xfs: punch out data fork delalloc blocks on COW writeback failure

* Sat May 14 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.92-alt1.el9
- Updated to kernel-5.14.0-92.el9:
  + aarch64: Enable NXP i.MX8M SoCs
  + ahci: update to latest
  + genirq/affinity: Consider that CPUs on nodes can be unbalanced
  + platform/x86: Add AMD system management interface
  + RDMA: update to v5.18-rc6
  + SCSI updates for 9.1
  + update qedf driver to latest upstream

* Fri May 13 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.90-alt1.el9
- Updated to kernel-5.14.0-90.el9:
  + bareudp: use ipv6_mod_enabled to check if IPv6 enabled
  + ip tunnels: backport upstream fixes
  + ipv4: Backport upstream fixes.
  + net: mpls: Fix notifications when deleting a device
  + Nvme misc fixes and quirks
  + other: backports from upstream
  + platform/x86/intel: Fix 'rmmod pmt_telemetry' panic
  + scsi: target: Allow changing dbroot if there are no registered devices
  + sctp: backports from upstream
  + tipc: backports from upstream
  + xfs: check sb_meta_uuid for dabuf buffer recovery

* Thu May 12 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.89-alt1.el9
- Updated to kernel-5.14.0-89.el9:
  + CNB: net: use eth_hw_addr_set()
  + Merge remote-tracking branch 'origin/merge-requests/627' into bz2069275
  + Merge remote-tracking branch 'origin/merge-requests/671' into bz2069275
  + Merge remote-tracking branch 'origin/merge-requests/673' into bz2069275
  + net: cipso: fix warnings in netlbl_cipsov4_add_std
  + sched/deadline: code cleanup
  + Scheduler header clean up
  + Scheduler RT prerequisites
  + wireguard: 9.1 P1 backports

* Wed May 11 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.88-alt1.el9
- Updated to kernel-5.14.0-88.el9:
  + mpt3sas: a bugfix
  + oom_kill.c: futex: delay the OOM reaper to allow time for proper futex cleanup
  + qed*: driver updates
  + sched/isolation: Split housekeeping cpumask per isolation features
  + Update ACPI code to match Linux v5.16
  + Update USB and Thunderbolt to v5.17
  + vrf: 9.1 P1 backports

* Mon May 09 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.87-alt1.el9
- Updated to kernel-5.14.0-87.el9 (fixes: CVE-2022-0617, CVE-2022-1353):
  + af_key: add __GFP_ZERO flag for compose_sadb_supported in function pfkey_register
  + Bring cifs.ko up to 5.16 plus some additional patches
  + cifs: destage any unwritten data to the server before calling copychunk_write
  + CNB: net: make use of helper netif_is_bridge_master()
  + CNB: xsk: Move tmp desc array from driver to pool
  + cpufreq: intel_pstate: updates
  + DAMON support
  + drivers/base/memory: determine and store zone for single-zone memory blocks
  + Fix CVE-2022-0617
  + General updates for kernel-rt
  + Information about perf-iostat is missing
  + macsec: backport fixes from upstream
  + mm: Optimize list lru memory consumption
  + proc/vmcore: pull back upstream commits to RHEL9
  + Redhat: enable Kfence on production servers
  + sctp: check asoc strreset_chunk in sctp_generate_reconf_event
  + tls: backport fixes from upstream
  + xfrm: backport fixes from upstream

* Sat May 07 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.86-alt1.el9
- Updated to kernel-5.14.0-86.el9:
  + cifs: fix NULL ptr dereference in smb2_ioctl_query_info()
  + CNB: skbuff: introduce skb_pull_data
  + CNB: stddef: Introduce DECLARE_FLEX_ARRAY() helper
  + CNB: virtchnl: Add support for new VLAN capabilities
  + configs: enable LOGITECH_FF
  + IDXD driver update for 9.1.0
  + perf: Sync with upstream v5.15
  + ping: a couple of fixes in ping_lookup
  + [RHEL-9.1.0 BZ 2068207] redhat: configs: Enable CONFIG_INTEL_IOMMU_DEBUGFS
  + veth: Ensure eth header is in skb's linear part

* Wed May 04 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.85-alt1.el9
- Updated to kernel-5.14.0-85.el9 (fixes: CVE-2022-1015, CVE-2022-1016):
  + bnx2x: driver updates
  + CNB: net: annotate accesses to dev->gso_max_* fields
  + CNB: net_tstamp: add new flag HWTSTAMP_FLAG_BONDED_PHC_INDEX
  + CNB: string.h: Introduce memset_after and memset_startat helpers
  + DRM 5.18 backport dependencies
  + Fix for two recent CVEs
  + Fix SCTP client-side peeloff issues with SELinux
  + ipv6: 9.1 P1 stable backports from upstream
  + mm: backport folio support
  + netfilter: conntrack: Add and use nf_ct_set_auto_assign_helper_warned()
  + net: mana: Add handling of CQE_RX_TRUNCATED
  + redhat/configs: Enable CONFIG_NFT_SYNPROXY
  + redhat/configs: enable CONFIG_RANDOMIZE_KSTACK_OFFSET_DEFAULT
  + [RHEL-9.1.0] IPMI update to kernel v5.17
  + Update kernel's PCI subsystem to v5.17

* Sat Apr 30 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.83-alt1.el9
- Updated to kernel-5.14.0-83.el9:
  + Add the amd_pstate driver
  + CNB: net: make dev_watchdog() less intrusive
  + net: fix NULL pointer reference in cipso_v4_doi_free
  + powerpc/pseries: Enable an interface to represent PAPR firmware attributes
  + redhat/configs: aarch64: enable CPU_FREQ_GOV_SCHEDUTIL
  + redhat: configs: Disable CONFIG_MPLS for s390x/zfcpdump
  + x86: intel_epb: Allow model specific normal EPB value
  + x86/platform/uv: UV Kernel support for UV5

* Fri Apr 29 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.82-alt1.el9
- Updated to kernel-5.14.0-82.el9:
  + bpf, test_offload.py: Skip base maps without names
  + CNB: Remove PDE_DATA() and replace by pde_data()
  + dmaengine: ptdma: Initial driver for the AMD PTDMA
  + e1000e: Add support for RPL-S
  + mm: lru_cache_disable: replace work queue synchronization with synchronize_rcu
  + mm/page_owner: Report memory cgroup info
  + mt76: mt7921e: fix possible probe failure after reboot
  + pci: fix multiple definition error when CONFIG_RHEL_DIFFERENCES is not set
  + perf: Fix typos in error messages
  + powerpc/lib/sstep: Don't use __{get/put}_user() on kernel addresses
  + Scheduler updates and fixes
  + selftests/bpf: Make test_lwt_ip_encap more stable and faster
  + Support PREEMPT_DYNAMIC on aarch64
  + ucounts: Backport fixes for ucount rlimits

* Wed Apr 27 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.81-alt1.el9
- Updated to kernel-5.14.0-81.el9:
  + Add LPSS support for RPL-S
  + Enable i2c-i801 support for RPL-S
  + kABI: Prepare mm SST for kABI Lockdown
  + pinctrl: Add support for RPL-S
  + powerpc/pseries/vas: Enable NX-GZIP support with DLPAR and LPM operations
  + pseries/eeh: Fix the kdump kernel crash during eeh_pseries_init
  + RDMA/qedr: Fix reporting max_{send/recv}_wr attrs
  + s390/kexec: fix memory leak of ipl report buffer
  + selftests: xsk: Make packet validation more robust
  + smartpqi updates
  + x86: Introduce Intel SDSi

* Thu Apr 21 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.80-alt1.el9
- Updated to kernel-5.14.0-80.el9 (fixes: CVE-2022-1015, CVE-2022-25636):
  + gfs2: Fix bugs revealed by the dct tool
  + Merge tag 'kernel-5.14.0-70.13.1.el9_0' from 9.0
  + netfilter: heap out of bounds write in nf_dup_netdev.c since 5.4
  + netfilter: nf_tables: validate registers coming from userspace.
  + redhat/configs: Enable CONFIG_RCU_SCALE_TEST & CONFIG_RCU_REF_SCALE_TEST
  + redhat: disable uncommon media device infrastructure
  + redhat: Enable KASAN on all ELN debug kernels
  + Sched/numa: fix allowed numa imbalance
  + scsi: iscsi: iSCSI Offload regression fixes
  + Update thermal/drivers/int340x

* Tue Apr 19 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.79-alt1.el9
- Updated to kernel-5.14.0-79.el9 (fixes: CVE-2020-36516):
  + audit: backport from upstream v5.13-rc1 to v5.16-rc6
  + block: update to v5.17
  + bpf/selftests: Fix namespace mount setup in tc_redirect
  + CNB: ipv6: separate ndisc_ns_create() from ndisc_send_ns()
  + Drivers: hv: Propagate VMBus coherence for performance
  + drivers/net: mark several as unmaintained
  + Fix panic while looking up a symlink due to NULL i_op->get_link
  + Fix "TSC Calibration failed" error
  + ibmvnic: fix race between xmit and reset
  + ice: bonding bug fixes
  + integrity: general upstream bugfixes
  + ipv4: avoid using shared IP generator for connected sockets
  + Merge tag 'kernel-5.14.0-70.11.1.el9_0' from 9.0
  + Merge tag 'kernel-5.14.0-70.12.1.el9_0' from 9.0
  + Merge up tags kernel-5.14.0-70.11.1.el9_0 to kernel-5.14.0-70.12.1.el9_0
  + mlxsw: Refactor parsing configuration
  + powerpc: fix some vm kernel selftests failures ( userfaultfd | userfaultfd_hugetlb | map_fixed_noreplace) [P10][DD2][Denali]
  + powerpc: P10 hardware counter (PMU/performance counters/perf:) Enhancements [FEAT]
  + powerpc: Support to handle control memory access error [FEAT]
  + powerpc/xive: Export XIVE IPI information for online-only processors.
  + Preallocate pgdat struct for all nodes during boot
  + rcu: Backport upstream RCU related commits up to v5.17
  + RDMA: update to v5.17
  + redhat/configs: disable CONFIG_CAN_SOFTING
  + redhat/configs: Enable WDT devices used by qemu VMs
  + Revert "xfs: actually bump warning counts when we send warnings"
  + Update kernel's PCI subsystem to v5.16

* Mon Apr 11 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.78-alt1.el9
- Updated to kernel-5.14.0-78.el9 (fixes: CVE-2022-0995, CVE-2022-1011, CVE-2022-23960):
  + arm64: Spectre-BHB mitigation (CVE-2022-23960)
  + block: release rq qos structures for queue without disk
  + cifs: modefromsids must add an ACE for authenticated users
  + configs: enable CONFIG_RMI4_F3A
  + crypto: fips - Add algorithm-specific limits for FIPS
  + fuse: fix pipe buffer lifetime for direct_io
  + integrity: enable policy rule for restricting hash algo
  + KVM: SVM: Allow AVIC support on system w/ physical APIC ID > 255
  + Merge branch 'main' into nic_rdma
  + Merge branch 'net-doc' into nic_rdma
  + Merge commit '3801d2d30749ddab3e04e4998145b29bce09ac9a' into 9.0
  + Merge tag 'kernel-5.14.0-70.10.1.el9_0' from 9.0
  + Merge tag 'kernel-5.14.0-70.6.1.el9_0' from 9.0
  + Merge tag 'kernel-5.14.0-70.7.1.el9_0' from 9.0
  + Merge tag 'kernel-5.14.0-70.8.1.el9_0' from 9.0
  + Merge tag 'kernel-5.14.0-70.9.1.el9_0' from 9.0
  + Merge up tags kernel-5.14.0-70.6.1.el9_0 to kernel-5.14.0-70.10.1.el9_0
  + NFS: Don't loop forever in nfs_do_recoalesce()
  + perf symbols: Fix symbol size calculation condition
  + perf/x86/intel/uncore: Make uncore_discovery clean for 64 bit addresses
  + redhat: Add parallel processing of configs in dist-configs
  + redhat/configs: drop some config options for rhel 9
  + redhat/configs: remove unnecessary GPIO Kconfig options
  + redhat/Makefile: Fix dist-dump-variables target
  + [RHEL9.0 BZ2053219] amd/iommu: Fix I/O page table memory leak and recover from event log overflow
  + [RHEL9 BZ2061621] iommu/vt-d: Fix double list_add when enabling VMD in scalable mode
  + s390/mm: fix 2KB pgtable release race
  + scsi: iscsi: offload sync session regression impacting qedi
  + watch_queue: Fix filter limit check
  + Various changes and improvements that are poorly described in merge.

* Sat Apr 09 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.77-alt1.el9
- Updated to kernel-5.14.0-77.el9 (fixes: CVE-2021-26401, CVE-2022-0001, CVE-2022-0002):
  + 2032117 - tpm: fix lpar crash when running on kexec with VTPM2.0 enabled [P10]
  + CNB: ethtool: update ethtool core to upstream v5.16
  + crypto: ccp: update ccp drivers upto v5.17
  + drm/i915/audio: Use BIOS provided value for RKL HDA link
  + Enable KVM AMX on SPR
  + futex: Fix PREEMPT_RT build
  + genirq: Provide new interfaces for affinity hints
  + ibmvnic: fix a race in ibmvnic_probe()
  + [Intel 9.1 Bug] SPR PMU Support: Uncore Events not enabled
  + KVM: use __vcalloc for very large allocations
  + lib/sbitmap: kill 'depth' from sbitmap_word
  + Merge tag 'kernel-5.14.0-70.5.1.el9_0' from 9.0
  + mm/memcg: Fix a lockdep splat in memory cgroup
  + mm: proactively backport MM fixes for RHEL-9.1
  + NFSD size, offset, and count sanity
  + perf tests attr: Add missing topdown metrics events
  + powerpc: Hard lockups are observed while running stress-ng and LPAR hangs [P8][P9][P10]
  + powerpc/papr_scm: Implement initial support for injecting smart errors
  + powerpc/pseries: Fix use after free panic
  + powerpc/smp: Update cpu_core_map on all PowerPc systems
  + redhat/configs: aarch64: Enable ARM_SPE_PMU
  + redhat: configs: Change aarch64 default dma domain to lazy
  + redhat: configs: Disable TPM 1.2 device drivers
  + redhat/configs: make SHA512_arch algos and CRYPTO_USER built-ins
  + redhat: fix make {distg-brew,distg-koji}
  + rename c9s pipeline from centos-stream-9 to c9s
  + SPR PMU Support: Uncore Events not enabled
  + Update kernel's PCI subsystem to v5.15
  + Update nvme to upstream 5.17-rc8
  + x86/speculation: Spectre-v2 BHI mitigation (CVE-2022-0001, CVE-2022-0002)

* Wed Mar 30 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.76-alt1.el9
- Updated to kernel-5.14.0-76.el9:
  + cifs: fix double free race when mount fails in cifs_get_root()
  + copy_process(): Move fd_install() out of sighand->siglock critical section
  + kernel/futex: backport new futex_waitv(2) system call
  + Merge tag 'kernel-5.14.0-70.4.1.el9_0' from 9.0
  + Move Intel PMT drivers into their own directory
  + Sync vDPA with upstream for RHEL9
  + tick/rcu: fix NOHZ tick-stop when performing DLPAR proc remove on ppc64le [P10]
  + x86/hyperv: Output host build info as normal Windows version number

* Sun Mar 27 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.75-alt1.el9
- Updated to kernel-5.14.0-75.el9 (fixes: CVE-2022-0742, CVE-2022-22942):
  + drm/ast: Create threshold values for AST2600
  + drm/vmwgfx: Fix stale file descriptors on failed usercopy
  + Fix FPU bugs that crash guest kernel after migration between newer->older cpu
  + gfs2: Fix fault_in_safe_writeable() for s390x
  + ipv6: fix skb drops in igmp6_event_query() and igmp6_event_report()
  + Merge tag 'kernel-5.14.0-70.3.1.el9_0' from 9.0
  + netfilter: nf_queue: fix socket refcount bugs
  + powerpc: drivers/char: Enable DLPAR operations with systems that have Guest Secure Boot and lockdown enabled
  + powerpc/pseries/ddw: Revert "Extend upper limit for huge DMA window for persistent memory"
  + redhat/configs: aarch64: Fix PAC/BTI config settings
  + redhat/configs: Disable KVM on POWER
  + redhat/configs: Disable watchdog components
  + RHEL9.0: arch_hw Update CONFIG_MOUSE_VSXXXAA=m
  + Sched: Fix fork versus cgroup race
  + scsi: mpi3mr: bug fixes
  + x86/cpu: Add Xeon Icelake-D to list of CPUs that support PPIN

* Tue Mar 22 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.74-alt1.el9
- Updated to kernel-5.14.0-74.el9:
  + Fix bad page state in process qemu-kvm when using TDP_MMU
  + powerpc/ibmvnic: DLPAR fix kernel Oops when add of vNIC device
  + redhat: rpminspect: disable 'patches' check for known empty patch files

* Mon Mar 21 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.73-alt1.el9
- Updated to kernel-5.14.0-73.el9 (fixes: CVE-2022-0516, CVE-2022-0847):
  + Add definition for RAPTOR_LAKE
  + block: kabi: reserve padding space for public structure
  + crypto: Make CRYPTO_EC* algos built-in
  + dm: fix crash and DM IO accounting
  + [EDAC] backport patches needed to support Genoa
  + Enable mellanox platform drivers to support LED, fan & watchdog devices
  + Fix edpc warning message
  + igb/igc: fix XDP registration
  + KVM: s390: Return error on SIDA memop on normal guest
  + lib/iov_iter: initialize "flags" in new pipe_buffer
  + Merge tag 'kernel-5.14.0-70.2.1.el9_0' from 9.0
  + nvmet-tcp: fix missing tech preview messages
  + powerpc: fix kernel panic on boot of PowerVM systems that are running on shared processing mode [Hash]
  + redhat: change default dist suffix for RHEL 9.0
  + redhat/configs: Enable CONFIG_ACER_WIRELESS
  + redhat: prepare to enter into zstream and adjust support for kabi
  + scsi: lpfc: Fix pt2pt NVMe PRLI reject LOGO loop
  + scsi: mpt3sas: driver fixes
  + virtio-net: fix pages leaking when building skb in big mode

* Thu Mar 17 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.72-alt1.el9
- Updated to kernel-5.14.0-72.el9:
  + Merge tag 'kernel-5.14.0-70.1.1.el9_0' from 9.0
  + redhat/configs: Disable CONFIG_SURFACE_PLATFORMS
  + redhat/configs: Enable CONFIG_INTEL_PCH_THERMAL for x86
  + redhat: use centos x509.genkey file if building under centos
  + Revert 8dffe2b6 "Merge: kabi: add lib ACKed symbols"
  + SCSI host-managed SMR drive support in RHEL 9 is unmaintained and needs kernel warning message
  + spec: Fix separate tools build
  + spec: make linux-firmware weak(er) dependency

* Wed Mar 09 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.71-alt1.el9
- Updated to kernel-5.14.0-71.el9:
  + MDRAID - Update to the latest upstream
  + redhat: Bump RHEL_MINOR for 9.1

* Thu Feb 24 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.70-alt1.el9
- Updated to kernel-5.14.0-70.el9 (fixes: CVE-2022-0435, CVE-2022-0492, CVE-2022-24122):
  + Backport fixes for ucounts
  + bpf, arm64: Use emit_addr_mov_i64() for BPF_PSEUDO_FUNC
  + cgroup-v1: Require capabilities to set release_agent (CVE-2022-0492)
  + mm: fix invalid page pointer returned with FOLL_PIN gups
  + net: stmmac: Fix excessive swiotlb memory in nic driver
  + tipc: improve size validations for received domain records

* Thu Feb 24 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.69-alt1.el9
- Updated to kernel-5.14.0-69.el9:
  + wireless update to v5.16+

* Wed Feb 23 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.68-alt1.el9
- Updated to kernel-5.14.0-68.el9 (fixes: CVE-2021-22600, CVE-2021-4028, CVE-2022-0330):
  + drm/i915: Flush TLBs before releasing backing store
  + ena: update elastic network adapter to the latest upstream
  + ext4: fix remount with 'abort' option
  + kernel/sched/sched.h: Exclude cpuidle from KABI
  + kernel.spec: Add glibc-static build requirement
  + libbpf: Use dynamically allocated buffer when receiving netlink messages
  + netfilter:  nf_conntrack incorrectly checking SEQ on syn-ack packets
  + net/packet: rx_owner_map depends on pg_vec
  + powerpc: security: Lock down the kernel if booted in secure boot mode
  + RDMA/cma: Do not change route.addr.src_addr.ss_family
  + redhat/configs: Disable arch_hw disabled CONFIGS
  + redhat/configs: Disable CONFIG_SENSORS_NCT6683 in RHEL for arm/aarch64
  + sfc: update to v5.16
  + Thunderbolt: various fixes

* Tue Feb 22 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.67-alt1.el9
- Updated to kernel-5.14.0-67.el9:
  + block: fix for recent update to v5.16
  + ice: westport channel GPIO and SDP support
  + kabi: add lib ACKed symbols
  + redhat: switch the vsyscall config to CONFIG_LEGACY_VSYSCALL_XONLY=y
  + usb: xhci: Enable runtime-pm by default on AMD Yellow Carp platform

* Mon Feb 21 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.66-alt1.el9
- Updated to kernel-5.14.0-66.el9:
  + Update NFS to upstream v5.16

* Sun Feb 20 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.65-alt1.el9
- Updated to kernel-5.14.0-65.el9:
  + ALSA: backport for RHEL 9.0

* Fri Feb 18 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.64-alt1.el9
- Updated to kernel-5.14.0-64.el9 (fixes: CVE-2021-3753):
  + EDAC/i10nm: Retrieve and print retry_rd_err_log registers
  + ice: bugfix update for 9.0
  + igc: driver update for 9.0
  + nvme-fabrics: fix state check in nvmf_ctlr_matches_baseopts()
  + scsi: reserve space in structures for KABI
  + vt_kdsetmode: extend console locking
  + Various changes and improvements that are poorly described in merge.

* Fri Feb 18 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.63-alt1.el9
- Updated to kernel-5.14.0-63.el9:
  + ionic: driver update for 9.0
  + wireguard: 9.0 P2 backports from upstream

* Thu Feb 17 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.62-alt1.el9
- Updated to kernel-5.14.0-62.el9 (fixes: CVE-2021-43389):
  + Backport page unpoisoning fixes
  + blktrace: switch trace spinlock to a raw spinlock
  + cgroup/cpuset: Fix RCU lockdep splat
  + CNB: net: create netdev->dev_addr assignment helpers
  + ext4: fix potential NULL pointer dereference in ext4_fill_super()
  + firmware: smccc: Fix check for ARCH_SOC_ID not implemented
  + ibmvnic: fix ethtool -L causing system to hang
  + ibmvnic: Update driver return codes
  + igb: driver update for 9.0
  + isdn: cpai: check ctr->cnr to avoid array index out of bound
  + netfilter: ipset: Emit deprecation warning at set creation time
  + NFSv4.1: handle NFS4ERR_NOSPC by CREATE_SESSION
  + powerpc/fadump: fix "seek error: kernel virtual address: c0000027f5e19000" observed while running crash tool on vmcore captured during fadump
  + rcu: Tighten rcu_advance_cbs_nowake() checks
  + redhat/configs: Disable CONFIG_MACINTOSH_DRIVERS
  + redhat/configs: Enable CONFIG_TEST_BPF
  + redhat: move CONFIG_ARM64_MTE to aarch64 config directory
  + s390/pv: fix the forcing of the swiotlb
  + scsi: bnx2fc: Flush destroy_work queue before calling bnx2fc_interface_put()
  + scsi: vmw_pvscsi: Set residual data length conditionally
  + tipc: backports from upstream, 2nd phase
  + Two small SELinux fixes

* Wed Feb 16 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.61-alt1.el9
- Updated to kernel-5.14.0-61.el9 (fixes: CVE-2021-4197, CVE-2021-4203, CVE-2022-0264):
  + bpf: Fix kernel address leakage in atomic fetch
  + cgroup: Use open-time credentials for process migraton perm checks
  + Enable KUNIT for CI Testing
  + IB/rdmavt: Validate remote_addr during loopback atomic tests
  + netfilter: P2 backports from upstream
  + nvme: fix a possible use-after-free in controller reset during load
  + ovs: backports P2 for 9.0
  + redhat/configs: enable CONFIG_CMA on aarch64 as tech-preview
  + [s390] s390/cpumf: Support for CPU Measurement Facility CSVN 7
  + [s390] scsi: zfcp: Fix failed recovery on gone remote port with non-NPIV FCP devices
  + tracing: Fix trace_percpu_buffer
  + x86: add ITBM support for AlderLake

* Tue Feb 15 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.60-alt1.el9
- Updated to kernel-5.14.0-60.el9 (fixes: CVE-2021-4083):
  + bnx2x: Fix enabling network interfaces without VFs
  + bonding: driver update or RHEL 9.0
  + Change "-auto" suffix to fix CI automotive pipeline issues
  + crypto: jitter - add oversampling of noise source
  + fget: check that the fd still exists after getting a ref to it
  + igbvf: driver update for 9.0
  + ipv6: 9.0 P2 backports from upstream
  + nfsd: fix use-after-free due to delegation race
  + NVMe command id changes for use-after-free CQE detection
  + Revert "ipv6: Honor all IPv6 PIO Valid Lifetime values"
  + sctp: backports from upstream, 2nd phase
  + tun: fix bonding active backup with arp monitoring
  + udp: backports from upstream, 2nd phase

* Sat Feb 12 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.59-alt1.el9
- Updated to kernel-5.14.0-59.el9:
  + gfs2: Upstream backports for mmap and deadlock fixes
  + x86/sgx: Update SGX subsystem code upto v5.16-rc5

* Thu Feb 10 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.58-alt1.el9
- Updated to kernel-5.14.0-58.el9 (fixes: CVE-2022-0185):
  + CI updates
  + Fix load tracking WARNINGs
  + Fix RTC based wakeup for Barcelo
  + Handle warning of allocation failure on DMA zone w/o managed pages
  + ipv4: stable backports for rhel 9.0  (phase 2)
  + KVM: x86: Fix Win11 guests with Hyper-V role + hv_evmcs
  + netfilter: nft_reject_bridge: Fix for missing reply from prerouting
  + PCI: hv: Add arm64 Hyper-V vPCI support
  + pinctrl: amd: Fix wakeups when IRQ is shared with SCI
  + [s390] s390/pci: move pseudo-MMIO to prevent MIO overlap
  + selftests/bpf: Enlarge select() timeout for test_maps
  + vfs: fs_context: fix up param length parsing in legacy_parse_param

* Wed Feb 09 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.57-alt1.el9
- Updated to kernel-5.14.0-57.el9 (fixes: CVE-2021-44733):
  + aacraid: add new messaging
  + arch/x86: KABI structs and array padding
  + dmaengine: idxd: Add wq occupancy information to sysfs attribute
  + dm: sync with upstream 5.17 and fix io accounting issue
  + fix use-after-free in tee driver
  + hpsa: add new messaging
  + lpfc: Add new messaging
  + mpi3mr: driver update
  + mpt3sas, megaraid_sas, mptsas: Add new messaging
  + mptcp: disable by default
  + net/sched: phase-2 stable backports for rhel9
  + NVMe/FC bug fixes for centos-stream-9
  + qla2xxx: Add new messaging
  + redhat: switch the kernel package to use certs from system-sb-certs
  + vrf: Reset IPCB/IP6CB when processing outbound pkts in vrf dev xmit

* Tue Feb 08 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.56-alt1.el9
- Updated to kernel-5.14.0-56.el9:
  + clocksource: Backport upstream fix for hpet fallback problem
  + CNB: pci: Make pci_enable_ptm() accessible for drivers
  + configs: disable CONFIG_CRAMFS
  + iommu/vt-d: Fix unmap_pages support
  + KVM: VMX: switch blocked_vcpu_on_cpu_lock to raw spinlock
  + Merge remote-tracking branch 'gitlab/rh/centos-stream-9/merge-requests/338' into cs9/bz2041931/kfree-skb-reason
  + net: backports before kABI freeze
  + PCI: Add kABI extensions for the kernel's PCI subsystem
  + ppp: ensure minimum packet size in ppp_write()
  + [RHEL-9.0] IPMI Add RH_KABI_RESERVE to kABI sensitive structs
  + x86/hyperv: Properly deal with empty cpumasks in hyperv_flush_tlb_multi()

* Sat Feb 05 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.55-alt1.el9
- Updated to kernel-5.14.0-55.el9:
  + nvme: drop scan_lock and always kick requeue list when removing namespaces
  + redhat/configs: Cleanup pending-common directory
  + redhat/configs: Enable CONFIG_PCI_P2PDMA
  + Resolve cpufreq errors on Alder Lake-S (ADL-S)
  + selftests: 9.0 P2 backport from upstream

* Fri Feb 04 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.54-alt1.el9
- Updated to kernel-5.14.0-54.el9:
  + Wireless stack and drivers update to v5.15

* Thu Feb 03 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.53-alt1.el9
- Updated to kernel-5.14.0-53.el9 (fixes: CVE-2021-40490):
  + ext4, jbd2 update for RHEL9.0

* Tue Feb 01 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.52-alt1.el9
- Updated to kernel-5.14.0-52.el9:
  + KVM: AArch64: Rebase to v5.15

* Tue Feb 01 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.51-alt1.el9
- Updated to kernel-5.14.0-51.el9:
  + Add packaged but empty /lib/modules/<kver>/systemtap
  + Add support for new AMD Family 19h models
  + irdma: Bug fixes from v5.16
  + powerpc/bpf: Update ldimm64 instructions during extra pass
  + RDMA: Bug fixes from v5.16
  + redhat: configs: add CONFIG_NTB and related items
  + redhat/configs: Enable CONFIG_DM_MULTIPATH_HST
  + Scheduler KABI padding
  + selftests: bpf: Fix bind on used port
  + tipc: backports from upstream

* Sat Jan 29 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.50-alt1.el9
- Updated to kernel-5.14.0-50.el9:
  + CNB: bridge: update bridge and switchdev to the latest upstream
  + CNB: rebase/update devlink for RHEL 9.0
  + kernel: Add redhat code
  + kernel/rh_taint.c: Update to new messaging
  + mptcp: rebase to 5.16 net-next

* Thu Jan 27 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.49-alt1.el9
- Updated to kernel-5.14.0-49.el9 (fixes: CVE-2021-3773, CVE-2021-4155, CVE-2021-4203):
  + adding support for c9s automotive coverage build
  + Add 'redhat/rhdocs/' from commit '8d40464cf1fcc46e23510dd722f9ec747a2ff432'
  + af_unix: fix races in sk_peer_pid and sk_peer_cred accesses
  + CNB: net: Remove redundant if statements
  + ip6_vti: initialize __ip6_tnl_parm struct in vti6_siocdevprivate
  + KVM: x86: Wait for IPIs to be delivered when handling Hyper-V TLB flush hypercall
  + netfilter: nat: force port remap to prevent shadowing well-known ports
  + net: introduce kfree_skb_reason
  + net: vlan: fix a UAF in vlan_dev_real_dev()
  + powerpc/cacheinfo: fix bigcores causing irq imbalance with irqbalance
  + powerpc: fix frame size warnings during kernel compilation with larger NR_CPUS value
  + powerpc: handle kdump appropriately with crash_kexec_post_notifiers option
  + powerpc/pseries: Fix memblock warning on bootup
  + redhat: Add documentation subtree
  + selftests/powerpc: fix security tests
  + xfs: map unwritten blocks in XFS_IOC_{ALLOC,FREE}SP just like fallocate
  + Various changes and improvements that are poorly described in merge.

* Tue Jan 25 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.48-alt1.el9
- Updated to kernel-5.14.0-48.el9:
  + net: mana: More MANA driver updates for RHEL 9.0
  + ibmvnic: fix error when allocating long term buffer during reset
  + [s390] Upgrade the qeth driver for s390x to latest
  + [s390] GLIBC: Support for new IBM Z Hardware - kernel part
  + ima: silence measurement list hexdump during kexec
  + scsi: lpfc: Update lpfc version to 14.0.0.4
  + scsi: lpfc: Fix non-recovery of remote ports following an unsolicited LOGO
  + mm/memcg: Exclude mem_cgroup pointer from kABI signature computation
  + NFS: Default change_attr_type to NFS4_CHANGE_TYPE_IS_UNDEFINED

* Sat Jan 22 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.47-alt1.el9
- Updated to kernel-5.14.0-47.el9 (fixes: CVE-2021-4001):
  + nvmet: make discovery NQN configurable
  + nitro_enclaves: Use get_user_pages_unlocked() call to handle mmap assert
  + include/linux/pci.h: Exclude struct hotplug_slot from KABI
  + net/vsock: backport vsock fixes for RHEL-9.0
  + include/linux/irq*.h: Pad irq structs for KABI
  + include/linux/fwnode.h: Exclude fwnode structs from KABI
  + bpf: Fix toctou on read-only map's constant scalar tracking
  + ACPI: tables: FPDT: Do not print FW_BUG message if record types are reserved
  + virtio: support virtio-mem on x86-64 as tech-preview

* Fri Jan 21 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.46-alt1.el9
- Updated to kernel-5.14.0-46.el9:
  + crypto: qat: Update QAT drivers upto v5.15

* Wed Jan 19 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.45-alt1.el9
- Workqueue update for RT prerequisites
- nvme: avoid race in shutdown namespace removal
- powerpc/xmon: Dump XIVE information for online-only processors.
- CVE-2021-20322 - ipv4: make exception cache less predictible
- [s390] s390/cio: make ccw_device_dma_* more robust
- [s390] s390/pci: add s390_iommu_aperture kernel parameter
- [s390] s390/pci: cleanup resources only if necessary
- [s390] s390/sclp: fix Secure-IPL facility detection
- Revert "[redhat] Generate a crashkernel.default for each kernel build"
- ibmvnic: fix kdump over nfs when auto priority disabled for ibmvnic
- ibmvnic: don't stop queue in xmit
- bpf/selftests: allow disabling tests
- kernel/crash_core: suppress unknown crashkernel parameter warning
- mm: fix memory onlining under the debug kernel
- Fixing CVE-2021-3752 for RHEL-9
- zstd: Sync with upstream 5.16 fixes and improvements

* Tue Jan 18 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.44-alt1.el9
- dm: sync with upstream 5.16 fixes and improvements
- redhat: Pull in openssl-devel as a build dependency correctly
- platform/x86: think-lmi: add debug_cmd
- include/linux/timer.h: Pad timer_list struct for KABI
- kernel: Include RHEL Ecosystem message
- include/linux/ioport.h: Pad resource struct for KABI
- include/linux/hrtimer.h: Pad hrtimer struct for KABI
- redhat/configs: Enable Zstandard compression
- Enable iSER on s390x

* Sat Jan 15 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.43-alt1.el9
- mm: fix for "CoW after fork()" "GUP after fork()" bug
- powerpc/xive: Change IRQ domain to a tree domain
- net: core stable backport for rhel 9.0
- vhost_net: fix OoB on sendmsg() failure.
- printk changes for kernel-rt

* Thu Jan 13 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.42-alt1.el9
- smartpqi updates
- powerpc/module_64: Fix livepatching for RO modules
- net-sysfs: try not to restart the syscall if it will fail eventually
- CI: Cleanup residue from ARK and enable RT check baselines
- redhat: tune rpminspect configuration for upstream and badfuncs tests
- redhat/configs: Enable CONFIG_CRYPTO_BLAKE2B
- netfilter: conntrack: switch to siphash and include zone id in hash again
- redhat: configs: increase CONFIG_DEBUG_KMEMLEAK_MEM_POOL_SIZE
- iommu/dma: Fix incorrect error return on iommu deferred attach
- RDMA/siw: Mark Software iWARP Driver as tech-preview
- genirq changes for kernel-rt

* Thu Jan 13 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.41-alt1.el9
- af_unix: Return errno instead of NULL in  unix_create1()
- ftrace: do CPU checking after preemption disabled
- redhat: build and include memfd to kernel-selftests-internal
- netfilter: stable backports for rhel 9.0
- netfilter: ipvs: make global sysctl readonly in non-init netns
- netfilter: ipvs: make global sysctl readonly in non-init netns
- net/sched: 9.0 P1 backports from upstream
- redhat/configs/evaluate_configs: Add find dead configs option

* Tue Jan 11 2022 Alexey Gladkov <legion@altlinux.ru> 5.14.0.40-alt1.el9
- Replace deprecated CPU-hotplug functions for kernel-rt
- Input: i8042 - Add quirk for Fujitsu Lifebook T725
- sctp: backports from upstream
- sctp: enhancements for the verification tag
- Fix CVE-2020-27820
- redhat/configs: NFS: disable UDP, insecure enctypes

* Fri Dec 24 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.39-alt1.el9
- cpuidle: pseries: Fixup CEDE0 latency only for POWER10 onwards
- powerpc/mce: Fix access error in mce handler
- powerpc/pseries/mobility: ignore ibm, platform-facilities updates
- KVM: SVM: Do not terminate SEV-ES guests on GHCB validation failure
- redhat/configs: enable DWARF5 feature if toolchain supports it
- init: make unknown command line param message clearer
- Enable BT WCN6855 2.1 module
- cgroup: Make rebind_subsystems() disable v2 controllers all at once
- bnxt_en: PTP related commits for inclusion in RHEL 9.0

* Thu Dec 23 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.38-alt1.el9
- Enable AMX(TMUL) for Sapphire Rapids

* Tue Dec 21 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.35-alt1.el9
- drm/hyperv: Fix device removal on Gen1 VMs
- redhat/configs: Always enable CONFIG_PCI_IOV for RHEL on s390x
- wireguard: device: reset peer src endpoint when netns exits
- NVMe-TCP fixes
- ovl: fix missing negative dentry check in ovl_rename()
- selftests/bpf: Fix some issues for selftest test_xdp_redirect_multi.sh

* Sun Dec 19 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.34-alt1.el9
- block: update to v5.16

* Thu Dec 16 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.32-alt1.el9
- mm: update generic MM code to upstream v5.15

* Wed Dec 15 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.31-alt1.el9
- Disable CONFIG_DEBUG_PREEMPT to restore performance
- tcp: phase 1 stable backport for rhel 9.0
- ibmvnic: Fixes for check failover_pending
- kernfs: upstream kernfs concurrency improvement series
- drm/hyperv: Fix double mouse pointers
- Revert "watchdog: iTCO_wdt: Account for rebooting on second timeout"
- redhat/kernel.spec.template: enable dependencies generation
- redhat: configs: Update configs for vmware
- redhat/configs: Enable CONFIG_DRM_VMWGFX on aarch64

* Tue Dec 14 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.30-alt1.el9
- Rebase KVM x86 to 5.15

* Fri Dec 10 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.29-alt1.el9
- hrtimer updates for RT prerequisites

* Thu Dec 09 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.28-alt1.el9
- Backport v5.15 rcu/locking/cgroup dependencies for kernel-rt

* Wed Dec 08 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.27-alt1.el9
- x86: change default to spec_store_bypass_disable=prctl spectre_v2_user=prctl
- Provide and Configure DYNAMIC_PREEMPT
- x86/sgx: mark tech preview
- net: ipv6 p1 stable backport from upstream
- ipv4: stable backports for rhel 9.0
- crypto: ccp - fix resource leaks in ccp_run_aes_gcm_cmd()
- net/l2tp: Fix reference count leak in l2tp_udp_recv_core
- megaraid_sas: driver update
- tpm: Avoid error message when process gets signal while waiting and other upstream fixes

* Tue Dec 07 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.26-alt2.el9
- Add 9p modules.

* Mon Dec 06 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.26-alt1.el9
- ceph: bring ceph client code up to v5.16-rc1

* Fri Dec 03 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.25-alt1.el9
- fix  '/proc/pid/wchan is always "0"'
- powerpc/bpf: Fix write protecting JIT code
- vfs: check fd has read access in kernel_read_file_from_fd()
- Disable idmapped mounts
- Sync s390x KVM code with upstream kernel v5.15
- redhat/configs: Remove CONFIG_INFINIBAND_I40IW

* Thu Dec 02 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.24-alt1.el9
- perf test: Handle fd gaps in test__dso_data_reopen
- perf tests vmlinux-kallsyms: Ignore hidden symbols
- perf script: Fix PERF_SAMPLE_WEIGHT_STRUCT support
- redhat/kernel.spec.template: Link perf with --export-dynamic
- xfs: fix I_DONTCACHE
- Fix virtio problem on s390x with raw DASD devices
- net/tls: backport fixes from 5.15
- x86: hv: Hyper-V x86-64 updates for Centos Stream 9
- Upgrade the SMC driver for s390x to latest from upstream
- cifs: enable SMB_DIRECT in RHEL9
- mpt3sas: driver update
- Support DMA implementation of Offload Service Engine (OSE) for Elkhart Lake
- vmxnet3: Update network driver for RHEL 9.0

* Tue Nov 30 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.23-alt1.el9
- CNB: pci: add several VPD helpers

* Sat Nov 27 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.22-alt1.el9
- Add automotive CI jobs
- post 5.14 scheduler fixes

* Fri Nov 26 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.21-alt2.el9
- Add files needed for kbuild.

* Fri Nov 26 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.21-alt1.el9
- clocksource: Workaround the hpet fallback problem
- scsi: target: Fix the pgr/alua_support_store functions
- redhat: fix typo and make the output more silent for dist-git sync
- Improve performace of AMD C3 entry for Family 17h and later
- lpfc updates for centos-9 14.0.0.3
- x86/Kconfig: Do not enable AMD_MEM_ENCRYPT_ACTIVE_BY_DEFAULT automatically
- ucounts: Fix signal ucount refcounting
- x86/cpu: Fix migration safety with X86_BUG_NULL_SEL
- net: gre: fix csum validation for gre4 and gre6
- redhat/configs: enable KEXEC_SIG for aarch64
- kernel.spec: add bpf_testmod.ko to kselftests/bpf
- netfilter: Add deprecation notices for xtables

* Thu Nov 25 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.20-alt1.el9
- powerpc/svm: Don't issue ultracalls if !mem_encrypt_active() (Herton R. Krzesinski)

* Sun Nov 21 2021 Alexey Gladkov <legion@altlinux.ru> 5.14.0.19-alt1.el9
- First build for ALTLinux.

