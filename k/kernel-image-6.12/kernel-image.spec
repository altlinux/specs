Name: kernel-image-6.12
Release: alt1
%define kernel_src_version	6.12
%define kernel_base_version	6.12
%define kernel_sublevel	.94
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

%if "%sub_flavour" == "pae"
ExclusiveArch: i586
%elif "%base_flavour" == "rt"
ExclusiveArch: x86_64 aarch64
%else
ExclusiveArch: i586 x86_64 ppc64le aarch64 armh
%endif

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

%package checkinstall
Summary: Verify EFI-stub signature
Group: System/Kernel and hardware
Requires: %name = %EVR
Requires(post): rpm-pesign-checkinstall

%description checkinstall
Verify EFI-stub signature.

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

%build
banner build
export ARCH=%base_arch
export NPROCS=%__nprocs
export KBUILD_BUILD_USER=$(echo %buildhost | sed 's/[-.].*//')
export KBUILD_BUILD_HOST='%{?disttag}%{!?disttag:%buildhost}'
export KBUILD_BUILD_TIMESTAMP="$(LC_ALL=C date -ud @$SOURCE_DATE_EPOCH)"
KernelVer=%kversion-%flavour-%krelease
echo "Building Kernel $KernelVer"
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
%{?kconfig_hook}
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
cp -a scripts/gdb -t %buildroot%kbuild_dir/scripts

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

%post checkinstall
check-pesign-helper

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

%files checkinstall

%changelog
* Fri Jun 19 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.94-alt1
- v6.12.94 (2026-06-19).

* Tue Jun 09 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.93-alt1
- v6.12.93 (2026-06-09).

* Thu Jun 04 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.12.92-alt2
- Applied patches adding support for enabling automatic lockdown in UEFI Secure
  Boot mode (thx egori@).
- config: Enable LOCK_DOWN_IN_EFI_SECURE_BOOT=y.

* Mon Jun 01 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.92-alt1
- v6.12.92 (2026-06-01).

* Sat May 23 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.91-alt1
- v6.12.91 (2026-05-23).
- config: Enable CONFIG_LIVEPATCH=y.

* Sun May 17 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.90-alt1
- v6.12.90 (2026-05-17).

* Fri May 15 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.89-alt1
- v6.12.89 (2026-05-15).

* Thu May 14 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.88-alt1
- v6.12.88 (2026-05-14).

* Fri May 08 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.87-alt1
- v6.12.87 (2026-05-08).

* Thu May 07 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.86-alt1
- v6.12.86 (2026-05-07).
- config: Enable platform and machine keyrings.
- config: Disable CONFIG_AX25.

* Thu Apr 30 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.85-alt1
- v6.12.85 (2026-04-30).

* Mon Apr 27 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.84-alt1
- v6.12.84 (2026-04-27).
- net: stmmac: dwmac-baikal: add another compatible string.

* Thu Apr 23 2026 Vitaly Chikunov <vt@altlinux.org> 6.12.83-alt2
- config: Disable CONFIG_MTD_TESTS.
- spec: Workaround brp-related eu-strip problems.

* Thu Apr 23 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.83-alt1
- v6.12.83 (2026-04-22).
- config,spec: Install out-of-tree modules signing certificate.
- config: Install gdb scripts (CONFIG_GDB_SCRIPTS=y).

* Sat Apr 18 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.82-alt1
- v6.12.82 (2026-04-18).

* Sat Apr 11 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.81-alt1
- v6.12.81 (2026-04-11).

* Thu Apr 02 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.80-alt1
- v6.12.80 (2026-04-02).
- net/netlabel: Add mark s0 flag for NetLabel subsystem.

* Fri Mar 27 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.79-alt1
- v6.12.79 (2026-03-27).

* Wed Mar 25 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.78-alt1
- v6.12.78 (2026-03-25).
- config: Enable USB_SERIAL_CONSOLE=y.
- config: add selinux to CONFIG_LSM.

* Fri Mar 13 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.77-alt1
- v6.12.77 (2026-03-13).

* Thu Mar 05 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.76-alt1
- v6.12.76 (2026-03-05).
- config: Enable CONFIG_SCHED_CLASS_EXT=y.

* Wed Mar 04 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.75-alt1
- v6.12.75 (2026-03-04).

* Thu Feb 19 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.74-alt1
- v6.12.74 (2026-02-19).

* Mon Feb 16 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.73-alt1
- v6.12.73 (2026-02-16).

* Mon Feb 16 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.72-alt1
- v6.12.72 (2026-02-16).

* Thu Feb 12 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.71-alt1
- v6.12.71 (2026-02-12).
- config-aarch64: CONFIG_RTC_DRV_HYM8563=m.

* Wed Feb 11 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.70-alt1
- v6.12.70 (2026-02-11).
- Additional patches for HDMI0 on RK3588.

* Fri Feb 06 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.69-alt1
- v6.12.69 (2026-02-06).
- config: CONFIG_LEDS_PCA955X_GPIO=y (ALT#57765).

* Fri Jan 30 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.68-alt1
- v6.12.68 (2026-01-30).

* Fri Jan 23 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.67-alt1
- v6.12.67 (2026-01-23).

* Sat Jan 17 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.66-alt1
- v6.12.66 (2026-01-17).

* Sun Jan 11 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.65-alt1
- v6.12.65 (2026-01-11).

* Fri Jan 09 2026 Vitaly Chikunov <vt@altlinux.org> 6.12.64-alt2
- spec: check: Resolve rtcheck boot problem on aarch64.

* Thu Jan 08 2026 Kernel Bot <kernelbot@altlinux.org> 6.12.64-alt1
- v6.12.64 (2026-01-08).

* Thu Dec 18 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.63-alt1
- v6.12.63 (2025-12-18).

* Sat Dec 13 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.62-alt1
- v6.12.62 (2025-12-12).
- config: CONFIG_SND_SOC_AMD_RPL_ACP6x=m.

* Sun Dec 07 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.61-alt1
- v6.12.61 (2025-12-07).

* Mon Dec 01 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.60-alt1
- v6.12.60 (2025-12-01).

* Mon Nov 24 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.59-alt1
- v6.12.59 (2025-11-24).
- input: serio: add an alias to the sersev-serio driver.
- sound: hda: enable jack detection in polling mode on Baikal-M.
- config-rt: CONFIG_DRM_MGAG200_DISABLE_WRITECOMBINE=y.
- config: CONFIG_DRM_MGAG200=m.
- sound: hda: add driver for HDA controller on Baikal-M.

* Fri Nov 14 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.58-alt1
- v6.12.58 (2025-11-13).
- spec: Do not package -domU kernels.
- config-rt: SCHED_AUTOGROUP=n, SLUB_CPU_PARTIAL=n, etc.
- arm64: dts: rockchip: Add NMS-SM-EVM v1 Board support.
- config: CONFIG_SND_SOC_AMD_ACP_COMMON=m.
- config: CONFIG_SOUNDWIRE_AMD=m.

* Sun Nov 02 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.57-alt1
- v6.12.57 (2025-11-02).

* Wed Oct 29 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.56-alt1
- v6.12.56 (2025-10-29).

* Thu Oct 23 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.55-alt1
- v6.12.55 (2025-10-23).
- config: Enable CONFIG_X86_USER_SHADOW_STACK=y.

* Sun Oct 19 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.54-alt1
- v6.12.54 (2025-10-19).

* Wed Oct 15 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.53-alt1
- v6.12.53 (2025-10-15).
- arm64: rockchip: Add Thin_88RK-1A Board support.
- config: Enable ZONE_DEVICE, DEVICE_PRIVATE, HSA_AMD_SVM.
- dw-hdmi: add flag SNDRV_PCM_INFO_BATCH for audio via hdmi on Baikal-M.

* Sun Oct 12 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.52-alt1
- v6.12.52 (2025-10-12).
- config: enable all accelerometers.
- config: Enable PS4/PS5 controllers.

* Mon Oct 06 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.51-alt1
- v6.12.51 (2025-10-06).
- config: Enable CONFIG_HID_UNIVERSAL_PIDFF=m (ALT#54887).
- config-aarch64: CONFIG_REGULATOR_AXP20X=y, CONFIG_MFD_AXP20X_I2C=y.

* Thu Oct 02 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.50-alt1
- v6.12.50 (2025-10-02).

* Thu Sep 25 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.49-alt1
- v6.12.49 (2025-09-25).
- config-aarch64: CONFIG_ROCKCHIP_DW_HDMI_QP=y.
- aarch64: Enable HDMI0 support on rk3588 and same other improvements
  from v6.14.

* Fri Sep 19 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.48-alt1
- v6.12.48 (2025-09-19).

* Thu Sep 11 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.47-alt1
- v6.12.47 (2025-09-11).

* Wed Sep 10 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.46-alt1
- v6.12.46 (2025-09-09).

* Fri Sep 05 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.45-alt1
- v6.12.45 (2025-09-04).
- config: Disable CONFIG_PSI_DEFAULT_DISABLED.

* Thu Aug 28 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.44-alt1
- v6.12.44 (2025-08-28).
- config: Build NVME as a module instead of built-in.

* Thu Aug 21 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.43-alt1
- v6.12.43 (2025-08-20).
- config: Enable RTRS and Security Infiniband options.
- config: Enable more VFIO drivers.
- config: Enable more Mellanox ConnectX options.
- config: Enable NVMe TCP TLS and AUTH for host and target.

* Fri Aug 15 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.42-alt1
- v6.12.42 (2025-08-15).
- pcie-baikal: forced enable dma-coherent for pcie on Baikal-M.
- kiosk: add secureexec parameter.
- config: Enable CONFIG_LEGACY_VSYSCALL_XONLY=y (ALT#55552).
- config-aarch64: enable more configs to improve Sunxi SoCs support.

* Fri Aug 01 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.41-alt1
- v6.12.41 (2025-08-01).
- config: Enable CONFIG_MTK_T7XX=m.

* Thu Jul 24 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.40-alt1
- v6.12.40 (2025-07-24).

* Fri Jul 18 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.39-alt1
- v6.12.39 (2025-07-17).

* Mon Jul 14 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.38-alt1
- v6.12.38 (2025-07-14).

* Thu Jul 10 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.37-alt1
- v6.12.37 (2025-07-10).
- config: Enable CONFIG_BUG_ON_DATA_CORRUPTION=y.
- config: Enable CONFIG_DEBUG_WX=y.
- config: Enable more Intel peripherals (IPU6, VSC).
- config: Enable more AMD peripherals (ISP, HSMP, WBRF).
- config: Enable CONFIG_SND_SOC_SOF_AMD_ACP70=m.

* Sun Jul 06 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.36-alt1
- v6.12.36 (2025-07-06).
- drm: baikal-vdu: remove unsupported framebuffer formats.

* Fri Jun 27 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.35-alt1
- v6.12.35 (2025-06-27).
- config: Disable CONFIG_NL80211_TESTMODE.

* Thu Jun 19 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.34-alt1
- v6.12.34 (2025-06-19).
- config: Enable more MediaTek wireless devices (ALT#54848).
- config: Enable build drivers for Software Defined Radio devices.
- config: Enable CONFIG_LEGACY_VSYSCALL_NONE=y.
- config: Enable CONFIG_INIT_ON_ALLOC_DEFAULT_ON=y.

* Tue Jun 10 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.33-alt1
- v6.12.33 (2025-06-10).

* Wed Jun 04 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.32-alt1
- v6.12.32 (2025-06-04).
- config: Enable CONFIG_INIT_STACK_ALL_ZERO=y.

* Thu May 29 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.31-alt1
- v6.12.31 (2025-05-29).
- config-aarch64: enable some sensors and cameras on PinePhone.

* Fri May 23 2025 Vitaly Chikunov <vt@altlinux.org> 6.12.30-alt2
- config: enable more led-trigger configs config-aarch64: enable config
  of mchp23 spi sram.
- spec: Fix packaging modules.weakdep appeared after kmod update.

* Thu May 22 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.30-alt1
- v6.12.30 (2025-05-22).

* Sun May 18 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.29-alt1
- v6.12.29 (2025-05-18).

* Fri May 09 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.28-alt1
- v6.12.28 (2025-05-09).
- arm64: dts: add devicetree for repka pi4 optimal.

* Mon May 05 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.27-alt1
- v6.12.27 (2025-05-05).

* Fri May 02 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.26-alt1
- v6.12.26 (2025-05-02).

* Fri Apr 25 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.25-alt1
- v6.12.25 (2025-04-25).

* Sun Apr 20 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.24-alt1
- v6.12.24 (2025-04-20).
- config-aarch64: CONFIG_VIDEO_RASPBERRYPI_PISP_BE=m.
- config-aarch64: enable more configs for qualcomm SoC's support.

* Thu Apr 10 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.23-alt1
- v6.12.23 (2025-04-10).

* Mon Apr 07 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.22-alt1
- v6.12.22 (2025-04-07).
- config: add prefix DISPLAY for CONFIG_DRM_DP_CEC, DRM_DP_AUX_CHARDEV.
- config: Enable CONFIG_SND_SOC_INTEL_AVS=m (ALT#53634).

* Sat Mar 29 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.21-alt1
- v6.12.21 (2025-03-28).
- arm64: dts: rockchip: add dts to support NP-504a board.

* Sun Mar 23 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.20-alt1
- v6.12.20 (2025-03-22).
- config: Disable obsolete input tablet drivers.
- config-aarch64: enable more configs of battery and charger.
- arm64: add dts for SoM NMS-SM-RK3568 and computer VSNF.466459.001 on
  its basis.

* Thu Mar 13 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.19-alt1
- v6.12.19 (2025-03-13).

* Sat Mar 08 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.18-alt1
- v6.12.18 (2025-03-07).

* Thu Feb 27 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.17-alt1
- v6.12.17 (2025-02-27).
- kiosk: MIN_UID 500 -> 1000.

* Fri Feb 21 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.16-alt1
- v6.12.16 (2025-02-21).

* Tue Feb 18 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.15-alt1
- v6.12.15 (2025-02-18).

* Mon Feb 17 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.14-alt1
- v6.12.14 (2025-02-17).
- Disable BLK_DEV_FD.
- config: Enable CONFIG_DRM_PANIC=y.

* Sat Feb 08 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.13-alt1
- v6.12.13 (2025-02-08).
- config: Enable CONFIG_TMPFS_INODE64=y.

* Sun Feb 02 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.12-alt1
- v6.12.12 (2025-02-01).
- Add support for Baikal-M SoC family.

* Thu Jan 23 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.11-alt1
- v6.12.11 (2025-01-23).

* Fri Jan 17 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.10-alt1
- v6.12.10 (2025-01-17).

* Thu Jan 09 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.9-alt1
- v6.12.9 (2025-01-09).

* Thu Jan 02 2025 Kernel Bot <kernelbot@altlinux.org> 6.12.8-alt1
- v6.12.8 (2025-01-02).

* Fri Dec 27 2024 Kernel Bot <kernelbot@altlinux.org> 6.12.7-alt1
- v6.12.7 (2024-12-27).
- config: Enable more zram compression backends.
- config: Disable CONFIG_ATM.
- config-aarch64: enable more configs for Qualcomm Platforms support.

* Fri Dec 20 2024 Kernel Bot <kernelbot@altlinux.org> 6.12.6-alt1
- v6.12.6 (2024-12-19).

* Sun Dec 15 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.5-alt2
- spec: Fix ExclusiveArch conditionals.

* Sun Dec 15 2024 Kernel Bot <kernelbot@altlinux.org> 6.12.5-alt1
- v6.12.5 (2024-12-14).

* Fri Dec 13 2024 Vitaly Chikunov <vt@altlinux.org> 6.12.4-alt2
- spec: Add -rt flavor to be built from the same source tree.

* Mon Dec 09 2024 Kernel Bot <kernelbot@altlinux.org> 6.12.4-alt1
- v6.12.4 (2024-12-09).
- config-aarch64: add Qualcomm SoCs based devices support.

* Fri Dec 06 2024 Kernel Bot <kernelbot@altlinux.org> 6.12.3-alt1
- v6.12.3 (2024-12-06).

* Thu Dec 05 2024 Kernel Bot <kernelbot@altlinux.org> 6.12.2-alt1
- v6.12.2 (2024-12-05).

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
