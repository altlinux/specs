Name: kernel-image-magicbook
Release: alt1.magicbook.art14.1
%define kernel_src_version	7.0
%define kernel_base_version	7.0
%define kernel_sublevel	.13
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

ExclusiveArch: x86_64

%ifarch ppc64le
%define make_target vmlinux
%elifarch aarch64
%define make_target Image
%elifarch %arm
%define make_target zImage
%else
%define make_target bzImage
%endif

%ifarch ppc64le
%define image_path %make_target.stripped
%else
%define image_path arch/%base_arch/boot/%make_target
%endif

%ifarch %ix86 x86_64
%define arch_dir x86
%else
%define arch_dir %base_arch
%endif

%define kvm_modules_dir arch/%arch_dir/kvm

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist /boot/vmlinuz-*

%define _unpackaged_files_terminate_build 1
%ifnarch ppc64le
%define _stripped_files_terminate_build 1
%endif

ExclusiveOS: Linux

%if "%sub_flavour" == "def"
Provides: kernel = %kversion
Provides: kernel-%kernel_latest = %version-%release
Provides: kernel-modules-eeepc-%flavour = %version-%release
Provides: kernel-modules-drbd83-%flavour = %version-%release
Provides: kernel-modules-igb-%flavour = %version-%release
Provides: kernel-modules-alsa = %version-%release
Provides: kernel-modules-kvm-%flavour = %version-%release
Provides: kernel-modules-kvm-%kversion-%flavour-%krelease = %version-%release
%endif

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
BuildRequires: libzstd-devel
BuildRequires: lzma-utils
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: rsync
BuildRequires: zlib-devel
%ifarch aarch64
BuildRequires: u-boot-tools
%endif
Provides: kernel-modules-ipset-%flavour = %version-%release
Provides: kernel-modules-kvdo-%flavour = %version-%release
%if_enabled ccache
BuildRequires: ccache
%endif
%ifdef use_ccache
BuildRequires: ccache
%endif

# for check
%{?!_without_check:%{?!_disable_check:
BuildRequires: iproute2
BuildRequires: ltp >= 20210524-alt2
BuildRequires: rpm-build-vm-run >= 1.30
BuildRequires: rtcheck
}}

%description
This package contains the Linux kernel %kernel_base_version that is used to boot and run
your system.

Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).

%package -n kernel-modules-drm-%flavour
Summary: The Direct Rendering Infrastructure modules
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Provides:  kernel-modules-v4l-%flavour = %version-%release
Conflicts: kernel-modules-drm-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-%kversion-%flavour-%krelease > %version-%release
Requires(pre,postun): kmod
Requires(pre,postun): %name = %EVR

%description -n kernel-modules-drm-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.

These are modules for your ALT Linux system

%package -n kernel-modules-drm-nouveau-%flavour
Summary: The Direct Rendering Infrastructure modules for NVIDIA cards
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-nouveau-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-nouveau-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-nouveau-%kversion-%flavour-%krelease > %version-%release
Requires: kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Requires(pre,postun): kmod
Requires(pre,post,postun): %name = %EVR

%description -n kernel-modules-drm-nouveau-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.

These are modules for your ALT Linux system

%package -n kernel-modules-staging-%flavour
Summary:  Kernel modules under development
Group: System/Kernel and hardware
Provides:  kernel-modules-staging-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-staging-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-staging-%kversion-%flavour-%krelease > %version-%release
Requires: kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Requires(pre,postun): kmod
Requires(pre,post,postun): %name = %EVR

%description -n kernel-modules-staging-%flavour
Drivers and filesystems that are not ready to be merged into the main
portion of the Linux kernel tree at this point in time for various
technical reasons.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common
AutoReqProv: nocpp
%if "%sub_flavour" == "def"
Provides: kernel-headers = %version
Provides: kernel-headers-%kernel_latest = %version-%release
%endif

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
AutoReqProv: nocpp nopython nopython3
%if "%sub_flavour" == "def"
Provides: kernel-headers-modules-%kernel_latest = %version-%release
%endif

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
This package contains documentation files for ALT Linux
kernel-image-%base_flavour-* kernel packages.

The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_src_version
tar -xf %kernel_src/kernel-source-%kernel_src_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_src_version
%define _default_patch_flags -s
%autopatch -p1

%if "%base_flavour" == "rt"
# fix -rt suffix
rm -f localversion*
%endif

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

%ifarch %ix86 armh
sed -Ei '/-flags/s/-j\S*//' scripts/Makefile.btf
%endif

c=.gear/signing-%flavour.pem
[ -s $c ] && cp $c certs/trusted.pem

%conf
banner build
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease
echo "Configuring Kernel $KernelVer"
%make_build mrproper
make -s kernelversion | grep -Fx '%kversion-%flavour-%krelease'

#configuration construction
CONFIGS="config config-%_target_cpu"
%if "%base_flavour" == "rt"
CONFIGS="$CONFIGS config-rt"
%endif
%if "%sub_flavour" == "pae"
CONFIGS="$CONFIGS config-pae"
%elif "%sub_flavour" == "kasan"
CONFIGS="$CONFIGS config-kasan"
%undefine _stripped_files_terminate_build
%endif
scripts/kconfig/merge_config.sh -m $CONFIGS

%make_build oldconfig

%build
export ARCH=%base_arch
export NPROCS=%__nprocs
export KBUILD_BUILD_USER=$(echo %buildhost | sed 's/[-.].*//')
export KBUILD_BUILD_HOST='%{?disttag}%{!?disttag:%buildhost}'
export KBUILD_BUILD_TIMESTAMP="$(LC_ALL=C date -ud @$SOURCE_DATE_EPOCH)"
KernelVer=%kversion-%flavour-%krelease
echo "Building Kernel $KernelVer"
make -s kernelrelease | grep -Fx '%kversion-%flavour-%krelease'
%make_build %make_target || {
	%make %make_target V=1
	exit 1
}
%make_build scripts_gdb
%ifarch ppc64le
eu-strip --remove-comment -o %image_path vmlinux
%endif
%make_build modules || {
	%make modules V=1
	exit 1
}
%ifarch aarch64 %arm
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

%ifarch aarch64 %arm
make dtbs_install INSTALL_DTBS_PATH=%buildroot/boot/devicetree/$KernelVer
%endif

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
%ifarch %ix86 x86_64
	arch/x86/Makefile_32
	arch/x86/Makefile_32.cpu
%ifarch x86_64
	arch/x86/Makefile_64
%endif
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
%ifarch aarch64 ppc64le
       arch/%arch_dir/kernel/module.lds
%endif
"
for f in $KbuildFiles; do
	[ -e "$f" ] || continue
	[ -x "$f" ] && mode=755 || mode=644
	install -Dp -m$mode "$f" %buildroot%kbuild_dir/"$f"
done
cp -va	scripts/gdb \
	scripts/livepatch \
	-t %buildroot%kbuild_dir/scripts

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

%if "%sub_flavour" == "def"
# install documentation
install -d %buildroot%_docdir/kernel-doc-%base_flavour-%version/
cp -a Documentation/* %buildroot%_docdir/kernel-doc-%base_flavour-%version/
%endif

%check
banner check
# First boot-test no matter have KVM or not.
timeout 300 vm-run --loglevel=debug --append='earlycon oops=panic panic_on_warn=1' \
%if "%base_flavour" == "rt"
	--tcg --mem=1G --cpu=2 --qemu="-rtc clock=vm -icount 0,sleep=off" \
	'uname -a; rtcheck -v'
%else
	'uname -a'
%endif
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
%exclude %modules_dir/kernel/drivers/accel/
%exclude %modules_dir/kernel/drivers/media/
%exclude %modules_dir/kernel/drivers/staging/
%exclude %modules_dir/kernel/drivers/gpu/
%exclude %modules_dir/kernel/drivers/usb/typec/altmodes/typec_displayport.ko*
%exclude %modules_dir/kernel/drivers/usb/typec/altmodes/typec_nvidia.ko*
%ifarch aarch64
%exclude %modules_dir/kernel/drivers/phy/qualcomm/phy-qcom-qmp-combo.ko*
%exclude %modules_dir/kernel/drivers/soc/qcom/pmic_glink_altmode.ko*
%exclude %modules_dir/kernel/drivers/usb/typec/tcpm/qcom/qcom_pmic_tcpm.ko*
%exclude %modules_dir/kernel/drivers/leds/flash/leds-qcom-flash.ko*
%endif
%ifarch armh aarch64
# usb_f_uvc now depends on drm causing "kernel image shouldn't require
# kernel modules" "sisyphus_check: check-kernel ERROR: kernel package.
%exclude %modules_dir/kernel/drivers/usb/gadget/function/usb_f_uvc.ko*
%endif
%ifarch aarch64 %arm
/boot/devicetree/%kversion-%flavour-%krelease
%endif

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir/
%modules_dir/build

%if "%sub_flavour" == "def"
%files -n kernel-doc-%base_flavour
%doc %_docdir/kernel-doc-%base_flavour-%version
%endif

%files -n kernel-modules-drm-%flavour
%modules_dir/kernel/drivers/gpu/
%modules_dir/kernel/drivers/accel/
%modules_dir/kernel/drivers/media/
%modules_dir/kernel/drivers/usb/typec/altmodes/typec_displayport.ko*
%modules_dir/kernel/drivers/usb/typec/altmodes/typec_nvidia.ko*
%ifarch aarch64
%modules_dir/kernel/drivers/phy/qualcomm/phy-qcom-qmp-combo.ko*
%modules_dir/kernel/drivers/soc/qcom/pmic_glink_altmode.ko*
%modules_dir/kernel/drivers/usb/typec/tcpm/qcom/qcom_pmic_tcpm.ko*
%modules_dir/kernel/drivers/leds/flash/leds-qcom-flash.ko*
%endif
%ifarch armh aarch64
%modules_dir/kernel/drivers/usb/gadget/function/usb_f_uvc.ko*
%endif
%exclude %modules_dir/kernel/drivers/gpu/drm/nouveau

%files -n kernel-modules-drm-nouveau-%flavour
%modules_dir/kernel/drivers/gpu/drm/nouveau

%files -n kernel-modules-staging-%flavour
%modules_dir/kernel/drivers/staging/

%changelog
* Tue Jun 30 2026 Andrey Limachko <liannnix@altlinux.org> 7.0.13-alt1.magicbook.art14.1
- Patches for Honor Magicbook Art 14 2025 (Intel Core Ultra 255H) and other
  Honor Magicbook devices:
  + sched: add BORE (Burst-Oriented Response Enhancer) v6.6.2
  + sched: add PoC cpu selector v2.5.0-rc2
  + sched/topology: force-enable EAS with SMT
  + sched/cpufreq: schedutil powersave mode
  + cpufreq: add Reflex governor v0.2.1
  + cpufreq: allow setpolicy drivers to enable EAS
  + cpufreq: intel_pstate: enable EAS on Meteor Lake
  + cpufreq: intel_pstate: force CAS (capacity asymmetry scaling)
  + cpufreq: intel_pstate: unlinear energy model v4
  + cpufreq: intel_pstate: add Arrow Lake EAS scaling factor
  + cpufreq: reflex: pass policy to cpufreq_driver_adjust_perf
  + cpuidle: add NAP (Neural Adaptive Predication) governor v0.2.1
  + intel_idle: add Arrow Lake (ARL) cpuidle states
  + mm: add kcompressd swap compression (unofficial 0.5)
  + platform/x86: add acpi-call module
  + platform/x86: update huawei-wmi driver to latest v5
  + platform/x86: huawei-wmi add key mappings for MRA-XXX
  + platform/x86: huawei-wmi sync fixes with upstream
  + drm/i915: force D3cold on suspend
  + config: Enable BORE, PoC cpu selector, Reflex governor,
    NAP governor, ACPI_CALL

* Fri Jun 19 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.13-alt1
- v7.0.13 (2026-06-19).

* Tue Jun 09 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.12-alt1
- v7.0.12 (2026-06-09).

* Tue Jun 02 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.0.11-alt2
- Applied patches adding support for enabling automatic lockdown in UEFI Secure
  Boot mode (thx egori@).
- config: Enable LOCK_DOWN_IN_EFI_SECURE_BOOT=y.

* Mon Jun 01 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.11-alt1
- v7.0.11 (2026-06-01).

* Sat May 23 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.10-alt1
- v7.0.10 (2026-05-23).
- config: Enable CONFIG_LIVEPATCH=y.

* Sun May 17 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.9-alt1
- v7.0.9 (2026-05-17).

* Fri May 15 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.8-alt1
- v7.0.8 (2026-05-15).

* Thu May 14 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.7-alt1
- v7.0.7 (2026-05-14).

* Mon May 11 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.6-alt1
- v7.0.6 (2026-05-11).

* Fri May 08 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.5-alt1
- v7.0.5 (2026-05-08).

* Thu May 07 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.4-alt1
- v7.0.4 (2026-05-07).
- config: Enable platform and machine keyrings.
- config: Disable CONFIG_AX25.
- config: Disable CONFIG_CRYPTO_USER_API.

* Thu Apr 30 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.3-alt1
- v7.0.3 (2026-04-30).

* Mon Apr 27 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.2-alt1
- v7.0.2 (2026-04-27).
- config: Disable CONFIG_MTD_TESTS.

* Thu Apr 23 2026 Kernel Bot <kernelbot@altlinux.org> 7.0.1-alt1
- v7.0.1 (2026-04-22).
- config,spec: Install out-of-tree modules signing certificate.
- config-aarch64: CONFIG_VIDEO_ROCKCHIP_CIF=m.
- config-aarch64: enable SoC Cix CD8180/CD8160 support.

* Sun Apr 12 2026 Vitaly Chikunov <vt@altlinux.org> 7.0.0-alt1
- Update to v7.0 (2026-04-12) release.
- config: Install gdb scripts (CONFIG_GDB_SCRIPTS=y).
- config: Enable CONFIG_IPV6_SEG6_ options.

* Mon Apr 06 2026 Vitaly Chikunov <vt@altlinux.org> 7.0.0-alt0.rc7
- Update to v7.0-rc7 (2026-04-05).

* Sun Mar 29 2026 Vitaly Chikunov <vt@altlinux.org> 7.0.0-alt0.rc6
- Update to v7.0-rc6 (2026-03-29).
- config: Enable USB_SERIAL_CONSOLE=y.

* Sun Mar 22 2026 Vitaly Chikunov <vt@altlinux.org> 7.0.0-alt0.rc5
- Update to v7.0-rc5 (2026-03-22).

* Sun Mar 15 2026 Vitaly Chikunov <vt@altlinux.org> 7.0.0-alt0.rc4
- Update to v7.0-rc4 (2026-03-15).

* Mon Mar 09 2026 Vitaly Chikunov <vt@altlinux.org> 7.0.0-alt0.rc3
- Update to v7.0-rc3 (2026-03-08).

* Sun Mar 01 2026 Vitaly Chikunov <vt@altlinux.org> 7.0.0-alt0.rc2
- Update to v7.0-rc2 (2026-03-01).
- config: Enable CONFIG_DWMAC_MOTORCOMM=m.

* Mon Feb 23 2026 Vitaly Chikunov <vt@altlinux.org> 7.0.0-alt0.rc1
- Rebase to v7.0-rc1 (2026-02-22).

* Thu Feb 19 2026 Kernel Bot <kernelbot@altlinux.org> 6.19.3-alt1
- v6.19.3 (2026-02-19).

* Mon Feb 16 2026 Kernel Bot <kernelbot@altlinux.org> 6.19.2-alt1
- v6.19.2 (2026-02-16).

* Mon Feb 16 2026 Kernel Bot <kernelbot@altlinux.org> 6.19.1-alt1
- v6.19.1 (2026-02-16).
- config-aarch64: CONFIG_RTC_DRV_HYM8563=m.

* Sun Feb 08 2026 Vitaly Chikunov <vt@altlinux.org> 6.19.0-alt1
- Update to v6.19 (2026-02-08) release.
- config: CONFIG_LEDS_PCA955X_GPIO=y.

* Sun Feb 01 2026 Vitaly Chikunov <vt@altlinux.org> 6.19.0-alt0.rc8
- Update to v6.19-rc8 (2026-02-01).

* Sun Jan 25 2026 Vitaly Chikunov <vt@altlinux.org> 6.19.0-alt0.rc7
- Update to v6.19-rc7 (2026-01-25).
- config: Enable CONFIG_PINCTRL_AMDISP=m.

* Mon Jan 19 2026 Vitaly Chikunov <vt@altlinux.org> 6.19.0-alt0.rc6
- Update to v6.19-rc6 (2026-01-18).

* Mon Jan 12 2026 Vitaly Chikunov <vt@altlinux.org> 6.19.0-alt0.rc5
- Update to v6.19-rc5 (2026-01-11).

* Mon Jan 05 2026 Vitaly Chikunov <vt@altlinux.org> 6.19.0-alt0.rc4
- Update to v6.19-rc4 (2026-01-04).

* Sun Dec 28 2025 Vitaly Chikunov <vt@altlinux.org> 6.19.0-alt0.rc3
- Update to v6.19-rc3 (2025-12-28).

* Mon Dec 22 2025 Vitaly Chikunov <vt@altlinux.org> 6.19.0-alt0.rc2
- Update to v6.19-rc2 (2025-12-21).

* Sun Dec 14 2025 Vitaly Chikunov <vt@altlinux.org> 6.19.0-alt0.rc1
- Rebase to v6.19-rc1 (2025-12-14).

* Sat Dec 13 2025 Vitaly Chikunov <vt@altlinux.org> 6.18.1-alt2
- spec: Fix usage of the newly introduced %conf section.

* Sat Dec 13 2025 Kernel Bot <kernelbot@altlinux.org> 6.18.1-alt1
- v6.18.1 (2025-12-12).
- config: CONFIG_SND_SOC_AMD_RPL_ACP6x=m.
- config-aarch64: CONFIG_DRM_ACCEL_ROCKET=m.
- config: CONFIG_SYSFB_SIMPLEFB=n, CONFIG_DRM_VESADRM=y,
  CONFIG_DRM_EFIDRM=y.

* Mon Dec 01 2025 Vitaly Chikunov <vt@altlinux.org> 6.18.0-alt1
- Update to v6.18 (2025-11-30) release.

* Mon Nov 24 2025 Vitaly Chikunov <vt@altlinux.org> 6.18.0-alt0.rc7
- Update to v6.18-rc7 (2025-11-23).
- config-rt: CONFIG_DRM_MGAG200_DISABLE_WRITECOMBINE=y.
- config: CONFIG_DRM_MGAG200=m.

* Sun Nov 16 2025 Vitaly Chikunov <vt@altlinux.org> 6.18.0-alt0.rc6
- Update to v6.18-rc6 (2025-11-16).
- config-aarch64: add CONFIG_ROCKCHIP_DW_DP=y.

* Sun Nov 09 2025 Vitaly Chikunov <vt@altlinux.org> 6.18.0-alt0.rc5
- Update to v6.18-rc5 (2025-11-09).
- spec: Do not package -domU kernels.
- config: Enable CONFIG_HYPERV=y, CONFIG_HYPERV_VMBUS=m.
- config: CONFIG_SND_SOC_AMD_ACP_COMMON=m.
- config: CONFIG_SOUNDWIRE_AMD=m.

* Sun Nov 02 2025 Vitaly Chikunov <vt@altlinux.org> 6.18.0-alt0.rc4
- Update to v6.18-rc4 (2025-11-02).

* Sun Oct 26 2025 Vitaly Chikunov <vt@altlinux.org> 6.18.0-alt0.rc3
- Update to v6.18-rc3 (2025-10-26).

* Mon Oct 20 2025 Vitaly Chikunov <vt@altlinux.org> 6.18.0-alt0.rc2
- Update to v6.18-rc2 (2025-10-19).
- config: Enable PCI_P2PDMA, HSA_AMD_P2P, DMABUF_MOVE_NOTIFY.
- config: Enable NETFILTER_XTABLES_LEGACY (ip_tables, ip6_tables).
- config: Enable ZONE_DEVICE, DEVICE_PRIVATE, HSA_AMD_SVM.
- config-aarch64: CONFIG_VIDEO_SYNOPSYS_HDMIRX=m.

* Sun Oct 12 2025 Vitaly Chikunov <vt@altlinux.org> 6.18.0-alt0.rc1
- Rebase to v6.18-rc1 (2025-10-12).

* Sun Oct 12 2025 Kernel Bot <kernelbot@altlinux.org> 6.17.2-alt1
- v6.17.2 (2025-10-12).
- config: enable all accelerometers.
- config: Enable PS4/PS5 controllers (ALT#52522).

* Mon Oct 06 2025 Kernel Bot <kernelbot@altlinux.org> 6.17.1-alt1
- v6.17.1 (2025-10-06).
- config: Enable CONFIG_HID_UNIVERSAL_PIDFF=m.
- config-aarch64: CONFIG_REGULATOR_AXP20X=y, CONFIG_MFD_AXP20X_I2C=y.

* Mon Sep 29 2025 Vitaly Chikunov <vt@altlinux.org> 6.17.0-alt1
- Update to v6.17 (2025-09-28) release.
- config: Enable more OmniVision cameras.
- config: Enable TPS68470 related options for Intel IPU3 cameras.
- config: Enable IPU6/MIPI cameras related options (IPU_BRIDGE, LJCA,
  DMABUF).

* Mon Sep 22 2025 Vitaly Chikunov <vt@altlinux.org> 6.17.0-alt0.rc7
- Update to v6.17-rc7 (2025-09-21).

* Sun Sep 14 2025 Vitaly Chikunov <vt@altlinux.org> 6.17.0-alt0.rc6
- Update to v6.17-rc6 (2025-09-14).

* Mon Sep 08 2025 Vitaly Chikunov <vt@altlinux.org> 6.17.0-alt0.rc5
- Update to v6.17-rc5 (2025-09-07).

* Sun Aug 31 2025 Vitaly Chikunov <vt@altlinux.org> 6.17.0-alt0.rc4
- Update to v6.17-rc4 (2025-08-31).
- config: Disable CONFIG_PSI_DEFAULT_DISABLED.
- config: Build NVME as a module instead of built-in.

* Sun Aug 24 2025 Vitaly Chikunov <vt@altlinux.org> 6.17.0-alt0.rc3
- Update to v6.17-rc3 (2025-08-24).
- config: Enable CONFIG_SCHED_CLASS_EXT=y.
- config: Enable CONFIG_MLX5_MACSEC=y.
- config: Enable RTRS and Security Infiniband options.

* Mon Aug 18 2025 Vitaly Chikunov <vt@altlinux.org> 6.17.0-alt0.rc2
- Update to v6.17-rc2 (2025-08-17).
- config: Enable CONFIG_MLX5_DPLL=m.
- config: Enable NVMe TCP TLS and AUTH for host and target.
- config: Disable CONFIG_LATENCYTOP.
- config-aarch64: CONFIG_CLK_RP1=m, CONFIG_PINCTRL_RP1=m,
  CONFIG_MISC_RP1=m.

* Sun Aug 10 2025 Vitaly Chikunov <vt@altlinux.org> 6.17.0-alt0.rc1
- Rebase to v6.17-rc1 (2025-08-10).

* Sun Jul 27 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt1
- Update to v6.16 (2025-07-27) release.
- config: Enable CONFIG_MTK_T7XX=m.

* Sun Jul 20 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt0.rc7
- Update to v6.16-rc7 (2025-07-20).

* Mon Jul 14 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt0.rc6
- Update to v6.16-rc6 (2025-07-13).

* Wed Jul 09 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt0.rc5.1
- Update to v6.16-rc5-38-g733923397fd9 (2025-07-08).
- config: Enable CONFIG_BUG_ON_DATA_CORRUPTION=y.
- config: Enable CONFIG_DEBUG_WX=y.
- config: Enable more AMD peripherals (ISP, HSMP, WBRF).
- config: Enable CONFIG_DRM_ACCEL_AMDXDNA=m.
- config: Enable CONFIG_SND_SOC_SOF_AMD_ACP70=m.
- config: Enable more Intel peripherals (IPU6, IVSC, PCM3168A, THC).
- config: Enable CONFIG_IWLMLD=m.

* Sun Jul 06 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt0.rc5
- Update to v6.16-rc5 (2025-07-06).
- config: Enable more VFIO drivers.
- config: Enable CONFIG_VIRTIO_RTC=m.
- config: Enable CONFIG_SND_HDA_ACPI=m.
- config: Enable CONFIG_SND_HDA_SCODEC_TAS2781=m.
- config: Enable CONFIG_SENSORS_LT3074=m.
- config: Enable more PHY hardware.
- config: Enable CONFIG_OVPN=m.
- config: Enable CONFIG_PCI_PWRCTRL_SLOT=m.

* Sun Jun 29 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt0.rc4
- Update to v6.16-rc4 (2025-06-29).
- config: Disable CONFIG_NL80211_TESTMODE.
- config: Enable more RTW88 hardware.

* Mon Jun 23 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt0.rc3
- Update to v6.16-rc3 (2025-06-22).
- config: Enable more MediaTek wireless devices.
- config: Enable build drivers for Software Defined Radio devices.
- config-aarch64: enable more configs.

* Mon Jun 16 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt0.rc2.1
- Update to v6.16-rc2-24-g9afe652958c3 (2025-06-16).
- Change %%kernel_latest definition to point to 'mainline' fixing CI workflows.

* Sun Jun 15 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt0.rc2
- Update to v6.16-rc2 (2025-06-15).

* Mon Jun 09 2025 Vitaly Chikunov <vt@altlinux.org> 6.16.0-alt0.rc1
- Rebase to v6.16-rc1 (2025-06-08).

* Thu Jun 05 2025 Kernel Bot <kernelbot@altlinux.org> 6.15.1-alt1
- v6.15.1 (2025-06-04).
- config: Enable CONFIG_LEGACY_VSYSCALL_NONE=y.
- config: enable new DRM_PANEL configs.
- config-aarch64: enable new configs for Rockchip, Qualcomm, Raspberry Pi.
- config-aarch64: enable some sensors and cameras on PinePhone.
- config: enable more led-trigger configs config-aarch64: enable config
  of mchp23 spi sram.

* Mon May 26 2025 Vitaly Chikunov <vt@altlinux.org> 6.15.0-alt1
- Update to v6.15 (2025-05-25) release.
- spec: Fix packaging modules.weakdep appeared after kmod update.
- config: Enable CONFIG_INIT_ON_ALLOC_DEFAULT_ON=y.

* Mon May 19 2025 Vitaly Chikunov <vt@altlinux.org> 6.15.0-alt0.rc7
- Update to v6.15-rc7 (2025-05-18).
- config: Enable CONFIG_INIT_STACK_ALL_ZERO=y.

* Mon May 12 2025 Vitaly Chikunov <vt@altlinux.org> 6.15.0-alt0.rc6
- Update to v6.15-rc6 (2025-05-11).

* Mon May 05 2025 Vitaly Chikunov <vt@altlinux.org> 6.15.0-alt0.rc5
- Update to v6.15-rc5 (2025-05-04).

* Mon Apr 28 2025 Vitaly Chikunov <vt@altlinux.org> 6.15.0-alt0.rc4
- Update to v6.15-rc4 (2025-04-27).

* Sun Apr 20 2025 Vitaly Chikunov <vt@altlinux.org> 6.15.0-alt0.rc3
- Update to v6.15-rc3 (2025-04-20).
- config-aarch64: CONFIG_VIDEO_RASPBERRYPI_PISP_BE=m.
- config-aarch64: enable more configs for qualcomm SoC's support.

* Sun Apr 13 2025 Vitaly Chikunov <vt@altlinux.org> 6.15.0-alt0.rc2
- Update to v6.15-rc2 (2025-04-13).

* Mon Apr 07 2025 Vitaly Chikunov <vt@altlinux.org> 6.15.0-alt0.rc1
- Rebase to v6.15-rc1 (2025-04-06).

* Mon Apr 07 2025 Kernel Bot <kernelbot@altlinux.org> 6.14.1-alt1
- v6.14.1 (2025-04-07).
- config: add prefix DISPLAY for CONFIG_DRM_DP_CEC, DRM_DP_AUX_CHARDEV.
- config: Enable more Intel hardware.
- config: Enable CONFIG_SND_SOC_INTEL_AVS=m.
- config: Enable CONFIG_NTSYNC=m (ALT#53603).
- config: Disable obsolete input tablet drivers.

* Mon Mar 24 2025 Vitaly Chikunov <vt@altlinux.org> 6.14.0-alt1
- Update to v6.14 (2025-03-24).

* Sun Mar 16 2025 Vitaly Chikunov <vt@altlinux.org> 6.14.0-alt0.rc7
- Update to v6.14-rc7 (2025-03-16).

* Mon Mar 10 2025 Vitaly Chikunov <vt@altlinux.org> 6.14.0-alt0.rc6
- Update to v6.14-rc6 (2025-03-09).

* Thu Mar 06 2025 Vitaly Chikunov <vt@altlinux.org> 6.14.0-alt0.rc5
- Update to v6.14-rc5 (2025-03-02).

* Mon Feb 24 2025 Vitaly Chikunov <vt@altlinux.org> 6.14.0-alt0.rc4
- Update to v6.14-rc4 (2025-02-23).
- kiosk: MIN_UID 500 -> 1000.

* Tue Feb 18 2025 Vitaly Chikunov <vt@altlinux.org> 6.14.0-alt0.rc3
- Update to v6.14-rc3 (2025-02-16).
- Disable BLK_DEV_FD.
- config: Enable CONFIG_DRM_PANIC=y.

* Mon Feb 10 2025 Vitaly Chikunov <vt@altlinux.org> 6.14.0-alt0.rc2
- Update to v6.14-rc2 (2025-02-09).
- config: Enable CONFIG_TMPFS_INODE64=y.

* Tue Feb 04 2025 Vitaly Chikunov <vt@altlinux.org> 6.14.0-alt0.rc1
- Rebase to v6.14-rc1 (2025-02-02).

* Tue Feb 04 2025 Kernel Bot <kernelbot@altlinux.org> 6.13.1-alt1
- v6.13.1 (2025-02-01).

* Mon Jan 20 2025 Vitaly Chikunov <vt@altlinux.org> 6.13.0-alt1
- Update to v6.13 (2025-01-19).

* Tue Jan 14 2025 Vitaly Chikunov <vt@altlinux.org> 6.13.0-alt0.rc7
- Update to v6.13-rc7 (2025-01-12).

* Mon Jan 06 2025 Vitaly Chikunov <vt@altlinux.org> 6.13.0-alt0.rc6
- Update to v6.13-rc6 (2025-01-05).

* Tue Dec 31 2024 Vitaly Chikunov <vt@altlinux.org> 6.13.0-alt0.rc5
- Update to v6.13-rc5 (2024-12-29).
- config: Enable more zram compression backends.

* Mon Dec 23 2024 Vitaly Chikunov <vt@altlinux.org> 6.13.0-alt0.rc4
- Update to v6.13-rc4 (2024-12-22).
- config: Disable CONFIG_ATM.
- config-aarch64: enable more configs for Qualcomm Platforms support.

* Mon Dec 16 2024 Vitaly Chikunov <vt@altlinux.org> 6.13.0-alt0.rc3
- Update to v6.13-rc3 (2024-12-15).

* Mon Dec 09 2024 Vitaly Chikunov <vt@altlinux.org> 6.13.0-alt0.rc2
- Update to v6.13-rc2 (2024-12-08).
- config-aarch64: add Qualcomm SoCs based devices support.
- config-aarch64: CONFIG_ROCKCHIP_DW_HDMI_QP=y.

* Mon Dec 02 2024 Vitaly Chikunov <vt@altlinux.org> 6.13.0-alt0.rc1
- Rebase to v6.13-rc1 (2024-12-01).

* Fri Nov 22 2024 Kernel Bot <kernelbot@altlinux.org> 6.12.1-alt1
- v6.12.1 (2024-11-22).
- config: Enable CONFIG_NVME_HWMON=y.
- config: Enable CONFIG_HWMON=y.

* Mon Nov 18 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.0-alt1
- Update to v6.12 (2024-11-17).

* Sun Nov 10 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.0-alt0.rc7
- Update to v6.12-rc7 (2024-11-10).

* Mon Nov 04 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.0-alt0.rc6
- Update to v6.12-rc6 (2024-11-03).

* Sun Oct 27 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.0-alt0.rc5
- Update to v6.12-rc5 (2024-10-27).
- config: Enable CONFIG_SCSI_MPI3MR=m (ALT#51728).
- config: CONFIG_SQUASHFS=y.

* Mon Oct 21 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.0-alt0.rc4
- Update to v6.12-rc4 (2024-10-20).

* Mon Oct 14 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.0-alt0.rc3
- Update to v6.12-rc3 (2024-10-13).
- spec: headers-modules: Install scripts/module-common.c.

* Mon Oct 07 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.0-alt0.rc2
- Update to v6.12-rc2 (2024-10-06).

* Mon Sep 30 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.0-alt0.rc1
- Rebase to v6.12-rc1 (2024-09-29).

* Mon Sep 30 2024 Vitaly Chikunov <vt@altlinux.org> 6.11.1-alt1
- Update to v6.11.1 (2024-09-30).
- config: Enable CONFIG_FPROBE=y.
- config: Enable CONFIG_WDAT_WDT=m.
- config: Enable more Realtek Wi-Fi drivers.
- config: Enable CONFIG_ATH12K=m (Wi-Fi 7).
- config: Enable CONFIG_AMD_PMF=m.
- config: CONFIG_DRM_XE=m.
- config: Enable CONFIG_IOMMUFD=m.
- config: Enable CONFIG_INTEL_TPMI=m.

* Sun Sep 15 2024 Vitaly Chikunov <vt@altlinux.org> 6.11.0-alt1
- Update to v6.11 (2024-09-15) release.
- config: Enable more Intel drivers.

* Sun Sep 08 2024 Vitaly Chikunov <vt@altlinux.org> 6.11.0-alt0.rc7
- Update to v6.11-rc7 (2024-09-08).
- altha: Remove sentinel elements from sysctl tables.
- config: Enable DRM_ACCEL drivers.
- config: Enable some Intel audio-related settings.

* Mon Sep 02 2024 Vitaly Chikunov <vt@altlinux.org> 6.11.0-alt0.rc6
- Update to v6.11-rc6 (2024-09-01).

* Sun Aug 25 2024 Vitaly Chikunov <vt@altlinux.org> 6.11.0-alt0.rc5
- Update to v6.11-rc5 (2024-08-25).
- config: CONFIG_SERIAL_SC16IS7XX_SPI=m.
- arm64: Add dts for SoM NMS-SM-RK3568.

* Sun Aug 18 2024 Vitaly Chikunov <vt@altlinux.org> 6.11.0-alt0.rc4
- Update to v6.11-rc4 (2024-08-18).
- config: Enable CONFIG_EDAC_DEBUG=y.
- spec: Add kernel-new provides for testing newest kernels.

* Mon Aug 12 2024 Vitaly Chikunov <vt@altlinux.org> 6.11.0-alt0.rc3
- Update to v6.11-rc3 (2024-08-11).
- spec: Remove devicetree symlinking for old u-boot.

* Mon Aug 05 2024 Vitaly Chikunov <vt@altlinux.org> 6.11.0-alt0.rc2
- Update to v6.11-rc2 (2024-08-04).

* Mon Jul 29 2024 Vitaly Chikunov <vt@altlinux.org> 6.11.0-alt0.rc1
- Rebase to v6.11-rc1 (2024-07-28).

* Sat Jul 27 2024 Kernel Bot <kernelbot@altlinux.org> 6.10.2-alt1
- v6.10.2 (2024-07-27).

* Wed Jul 24 2024 Kernel Bot <kernelbot@altlinux.org> 6.10.1-alt1
- v6.10.1 (2024-07-24).
- config-aarch64: CONFIG_NR_CPUS=512.
- config: Enable CONFIG_MHI_WWAN_CTRL (ALT#50941).

* Mon Jul 15 2024 Vitaly Chikunov <vt@altlinux.org> 6.10.0-alt1
- Update to v6.10 (2024-07-14).

* Mon Jul 08 2024 Vitaly Chikunov <vt@altlinux.org> 6.10.0-alt0.rc7
- Update to v6.10-rc7 (2024-07-07).

* Thu Jul 04 2024 Vitaly Chikunov <vt@altlinux.org> 6.10.0-alt0.rc6
- Update to v6.10-rc6 (2024-06-30).

* Sun Jun 30 2024 Vitaly Chikunov <vt@altlinux.org> 6.10.0-alt0.rc5
- v6.10-rc5 (2024-06-23).

* Fri Jun 21 2024 Kernel Bot <kernelbot@altlinux.org> 6.9.6-alt1
- v6.9.6 (2024-06-21).

* Sun Jun 16 2024 Kernel Bot <kernelbot@altlinux.org> 6.9.5-alt1
- v6.9.5 (2024-06-16).

* Wed Jun 12 2024 Kernel Bot <kernelbot@altlinux.org> 6.9.4-alt1
- v6.9.4 (2024-06-12).

* Thu May 30 2024 Kernel Bot <kernelbot@altlinux.org> 6.9.3-alt1
- v6.9.3 (2024-05-30).

* Sat May 25 2024 Kernel Bot <kernelbot@altlinux.org> 6.9.2-alt1
- v6.9.2 (2024-05-25).

* Fri May 17 2024 Kernel Bot <kernelbot@altlinux.org> 6.9.1-alt1
- v6.9.1 (2024-05-17).

* Wed May 15 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.9.0-alt2
- Bumped release to pesign with the new key.

* Tue May 14 2024 Vitaly Chikunov <vt@altlinux.org> 6.9.0-alt1
- Rebase to v6.9 (2024-05-12).

* Thu May 02 2024 Kernel Bot <kernelbot@altlinux.org> 6.8.9-alt1
- v6.8.9 (2024-05-02).

* Sat Apr 27 2024 Kernel Bot <kernelbot@altlinux.org> 6.8.8-alt1
- v6.8.8 (2024-04-27).
- Restore kernel and kernel-headers provides.
- config: CONFIG_CONSOLE_LOGLEVEL_QUIET=3 (ALT#50098).

* Wed Apr 17 2024 Kernel Bot <kernelbot@altlinux.org> 6.8.7-alt1
- v6.8.7 (2024-04-17).

* Sat Apr 13 2024 Kernel Bot <kernelbot@altlinux.org> 6.8.6-alt1
- v6.8.6 (2024-04-13).
- config: DYNAMIC_DEBUG=y (ALT#50002).

* Thu Apr 11 2024 Vitaly Chikunov <vt@altlinux.org> 6.8.5-alt1
- Update to v6.8.5 (2024-04-10).

* Fri Apr 05 2024 Kernel Bot <kernelbot@altlinux.org> 6.8.4-alt1
- v6.8.4 (2024-04-04).

* Thu Apr 04 2024 Kernel Bot <kernelbot@altlinux.org> 6.8.3-alt1
- v6.8.3 (2024-04-03).

* Wed Mar 27 2024 Kernel Bot <kernelbot@altlinux.org> 6.8.2-alt1
- v6.8.2 (2024-03-26).

* Sat Mar 16 2024 Kernel Bot <kernelbot@altlinux.org> 6.8.1-alt1
- v6.8.1 (2024-03-15).

* Tue Mar 12 2024 Vitaly Chikunov <vt@altlinux.org> 6.8.0-alt1
- Rebase to v6.8 (2024-03-10).

* Wed Mar 06 2024 Kernel Bot <kernelbot@altlinux.org> 6.7.9-alt1
- v6.7.9 (2024-03-06).

* Sun Mar 03 2024 Kernel Bot <kernelbot@altlinux.org> 6.7.8-alt1
- v6.7.8 (2024-03-02).

* Fri Mar 01 2024 Kernel Bot <kernelbot@altlinux.org> 6.7.7-alt1
- v6.7.7 (2024-03-01).

* Sat Feb 24 2024 Kernel Bot <kernelbot@altlinux.org> 6.7.6-alt1
- v6.7.6 (2024-02-23).
- config-aarch64: Do not disable CONFIG_DEBUG_INFO_BTF.

* Sun Feb 18 2024 Vitaly Chikunov <vt@altlinux.org> 6.7.5-alt1
- v6.7.5 (2024-02-16) (based on un-def/sisyphus).

* Sat Feb 17 2024 Kernel Bot <kernelbot@altlinux.org> 1:6.6.17-alt1
- v6.6.17 (2024-02-16).
