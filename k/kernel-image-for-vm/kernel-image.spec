Name: kernel-image-for-vm
Release: alt1
%define kernel_src_version	6.18
%define kernel_base_version	6.18
%define kernel_sublevel	.35
%define kernel_extra_version	%nil
%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
%define kernel_latest	latest
Version: %kversion

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; expr + "$s" : '[[:digit:]]\\+\\.[[:digit:]]\\+$' >/dev/null && s=def; printf %%s "${s#*-}" )
%define is_main	%([ "%sub_flavour" = def -o "%sub_flavour" = vm ] && echo 1 || echo 0)

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
Url: https://www.kernel.org/
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

%if %is_main
Provides: kernel = %kversion
Provides: kernel-%kernel_latest = %version-%release
Provides: kernel-modules-kvm-%flavour = %version-%release
Provides: kernel-modules-kvm-%kversion-%flavour-%krelease = %version-%release
%endif
%if "%sub_flavour" == "def"
Provides: kernel-modules-eeepc-%flavour = %version-%release
Provides: kernel-modules-drbd83-%flavour = %version-%release
Provides: kernel-modules-igb-%flavour = %version-%release
Provides: kernel-modules-alsa = %version-%release
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

%if "%sub_flavour" != "vm"
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
%endif

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common
AutoReqProv: nocpp
%if %is_main
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
%if %is_main
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

%package -n kernel-doc-%flavour
Summary: Linux kernel %kversion-%flavour documentation
Group: System/Kernel and hardware
BuildArch: noarch

%description -n kernel-doc-%flavour
This package contains documentation files for ALT Linux
kernel-image-%flavour-* kernel packages.

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
%elif "%sub_flavour" == "vm"
CONFIGS="$CONFIGS config-for-vm"
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
%if "%sub_flavour" != "vm"
%make_build dtbs
%endif
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
# (the vm flavour disables MEDIA_SUPPORT, so there is nothing to move)
%if "%sub_flavour" != "vm"
# rmi2-core deps
install -d %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/common/videobuf2/ %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/mc/ %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/v4l2-core/videodev.ko* %buildroot%modules_dir/kernel/drivers/media-core/
# other deps
mv %buildroot%modules_dir/kernel/drivers/media/rc/rc-core.ko* %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/dvb-core/dvb-core.ko* %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/radio/tea575x.ko* %buildroot%modules_dir/kernel/drivers/media-core/
%endif

%ifarch aarch64 %arm
%if "%sub_flavour" != "vm"
make dtbs_install INSTALL_DTBS_PATH=%buildroot/boot/devicetree/$KernelVer
%endif
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

%if %is_main
# install documentation
install -d %buildroot%_docdir/kernel-doc-%flavour-%version/
cp -a Documentation/* %buildroot%_docdir/kernel-doc-%flavour-%version/
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
%if "%sub_flavour" != "vm"
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
%endif
%ifarch aarch64 %arm
%if "%sub_flavour" != "vm"
/boot/devicetree/%kversion-%flavour-%krelease
%endif
%endif

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir/
%modules_dir/build

%if %is_main
%files -n kernel-doc-%flavour
%doc %_docdir/kernel-doc-%flavour-%version
%endif

%if "%sub_flavour" != "vm"
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
%endif

%files checkinstall

%changelog
* Tue Jun 09 2026 Anton Farygin <rider@altlinux.org> 6.18.35-alt1
- initial build for ALT Linux, based on 6.18.34-alt1 kernel config
