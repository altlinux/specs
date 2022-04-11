Name: kernel-image-centos

%define centos_release 78

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
	KVERSION="$KVER" \
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

cp -a drivers/scsi/scsi.h          %buildroot%kbuild_dir/drivers/scsi/
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

