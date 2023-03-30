Name: kernel-image-un-def
Release: alt1
epoch:1
%define kernel_base_version	6.2
%define kernel_sublevel	.9
%define kernel_extra_version	%nil
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	%__gcc_version_base

# Enable/disable docs formatting
%if "%sub_flavour" == "def" && %kgcc_version > 5
%def_enable docs
%else
%def_disable docs
%endif

%ifarch %ix86 x86_64
%def_enable domU
%else
%def_disable domU
%endif

#Remove oss
%def_disable oss
## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
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
%else
ExclusiveArch: i586 x86_64 ppc64le aarch64 armh
%endif

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

%define kvm_modules_dir arch/%arch_dir/kvm

ExclusiveOS: Linux

%if "%sub_flavour" == "def"
Provides: kernel = %kversion
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
BuildRequires: kernel-source-%kernel_base_version
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

# for check
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm-run >= 1.30 ltp >= 20210524-alt2 iproute2}}

%description
This package contains the Linux kernel %kernel_base_version that is used to boot and run
your system.

Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).

There are some other kernel variants in ALT systems:
* std-def: standard longterm kernel without preemption;
* un-def:  more modern then std-def and with preemption enabled.

%package -n kernel-image-domU-%flavour
Summary: Uncompressed linux kernel for XEN domU boot 
Group: System/Kernel and hardware
Requires(pre,postun): kmod

%description -n kernel-image-domU-%flavour
Most XEN virtualization system versions can not boot lzma-compressed
kernel images. This is an optional package with uncompressed linux
kernel image for this special case. If you do not know what is it XEN
it seems that you do not need this package.

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

%package -n kernel-modules-drm-ancient-%flavour
Summary: The Direct Rendering modules for ancient cards
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-ancient-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-ancient-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-ancient-%kversion-%flavour-%krelease > %version-%release
Requires(pre,post,postun): %name = %EVR

%description -n kernel-modules-drm-ancient-%flavour
The Direct Rendering Modules for ancient cards: mgag200.ko,
sis.ko, tdfx.ko, savage.ko, r128.ko, mga.ko, via.ko

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
%if "%sub_flavour" == "def"
Provides: kernel-headers = %version
%endif
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
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
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
CONFIGS="config config-%_target_cpu"
%if "%base_flavour" == "std"
CONFIGS="$CONFIGS config-std"
%endif
%if "%sub_flavour" == "pae"
CONFIGS="$CONFIGS config-pae"
%endif
%if "%sub_flavour" == "debug"
CONFIGS="$CONFIGS config-debug"
%endif
scripts/kconfig/merge_config.sh -m $CONFIGS

%make_build oldconfig
%make_build %make_target
%ifarch ppc64le
eu-strip --remove-comment -o %image_path vmlinux
%endif
%make_build modules
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
%if_enabled domU
install -Dp -m644 vmlinux %buildroot/boot/vmlinux-$KernelVer
%endif
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

%make_build modules_install INSTALL_MOD_PATH=%buildroot

install -d %buildroot%modules_dir/updates

# Move some modules to kernel-image package tree
# rmi2-core deps
install -d %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/common/videobuf2/ %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/mc/ %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/v4l2-core/videodev.ko %buildroot%modules_dir/kernel/drivers/media-core/
# other deps
mv %buildroot%modules_dir/kernel/drivers/media/rc/rc-core.ko %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/dvb-core/dvb-core.ko %buildroot%modules_dir/kernel/drivers/media-core/
mv %buildroot%modules_dir/kernel/drivers/media/radio/tea575x.ko %buildroot%modules_dir/kernel/drivers/media-core/

%ifarch aarch64 %arm
make dtbs_install INSTALL_DTBS_PATH=%buildroot/boot/devicetree/$KernelVer
%ifarch aarch64
pushd %buildroot/boot/devicetree/$KernelVer/
find . -mindepth 2 -type f | \
       while read f; do ln -srv "$f" "$(basename $f)"; done
popd
%endif
mkdir -p %buildroot/lib/devicetree
ln -s /boot/devicetree/$KernelVer %buildroot/lib/devicetree/$KernelVer
%endif

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

# remove *.bin files
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,devname,softdep,symbols}

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%base_flavour-%version/
cp -a Documentation/* %buildroot%_docdir/kernel-doc-%base_flavour-%version/
%endif

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist /boot/vmlinuz-*

%define _unpackaged_files_terminate_build 1
%ifnarch ppc64le
%define _stripped_files_terminate_build 1
%endif

%check
banner check
# First boot-test no matter have KVM or not.
timeout 300 vm-run uname -a
# Longer LTP tests only if there is KVM (which is present on all main arches).
if ! timeout 999 vm-run --kvm=cond \
        "/sbin/sysctl kernel.printk=8;
         runltp -f kernel-alt-vm -S skiplist-alt-vm -o out"; then
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
%dir %modules_dir/
%dir %modules_dir/updates
%defattr(0600,root,root,0700)
%modules_dir/*
%exclude %modules_dir/build
%exclude %modules_dir/kernel/drivers/media/
%exclude %modules_dir/kernel/drivers/staging/
%exclude %modules_dir/kernel/drivers/gpu/
%exclude %modules_dir/kernel/drivers/usb/typec/altmodes/typec_displayport.ko
%exclude %modules_dir/kernel/drivers/usb/typec/altmodes/typec_nvidia.ko
%ifarch %ix86 x86_64
# thinkpad_acpi now depends on drm causing "kernel image shouldn't require
# kernel modules" "sisyphus_check: check-kernel ERROR: kernel package
# violation".
%exclude %modules_dir/kernel/drivers/platform/x86/thinkpad_acpi.ko
%endif
%ghost %modules_dir/modules.alias.bin
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols.bin
%ghost %modules_dir/modules.builtin.bin
%ifarch aarch64 %arm
/boot/devicetree/%kversion-%flavour-%krelease
/lib/devicetree/%kversion-%flavour-%krelease
%endif

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

%files -n kernel-modules-drm-%flavour
%modules_dir/kernel/drivers/gpu/
%modules_dir/kernel/drivers/media/
%modules_dir/kernel/drivers/usb/typec/altmodes/typec_displayport.ko
%modules_dir/kernel/drivers/usb/typec/altmodes/typec_nvidia.ko
%ifarch %ix86 x86_64
%modules_dir/kernel/drivers/platform/x86/thinkpad_acpi.ko
%endif
%exclude %modules_dir/kernel/drivers/gpu/drm/nouveau
%exclude %modules_dir/kernel/drivers/gpu/drm/mgag200
%ifnarch aarch64 armh
%exclude %modules_dir/kernel/drivers/gpu/drm/sis
%exclude %modules_dir/kernel/drivers/gpu/drm/savage
%exclude %modules_dir/kernel/drivers/gpu/drm/tdfx
%exclude %modules_dir/kernel/drivers/gpu/drm/r128
%exclude %modules_dir/kernel/drivers/gpu/drm/mga
%exclude %modules_dir/kernel/drivers/gpu/drm/via
%endif

%files -n kernel-modules-drm-ancient-%flavour
%modules_dir/kernel/drivers/gpu/drm/mgag200
%ifnarch aarch64 armh
%modules_dir/kernel/drivers/gpu/drm/sis
%modules_dir/kernel/drivers/gpu/drm/savage
%modules_dir/kernel/drivers/gpu/drm/tdfx
%modules_dir/kernel/drivers/gpu/drm/r128
%modules_dir/kernel/drivers/gpu/drm/mga
%modules_dir/kernel/drivers/gpu/drm/via
%endif

%files -n kernel-modules-drm-nouveau-%flavour
%modules_dir/kernel/drivers/gpu/drm/nouveau

%files -n kernel-modules-staging-%flavour
%modules_dir/kernel/drivers/staging/

%files checkinstall

%changelog
* Thu Mar 30 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.2.9-alt1
- v6.2.9 (2023-03-30).

* Thu Mar 23 2023 Vitaly Chikunov <vt@altlinux.org> 1:6.2.8-alt1
- Rebase to v6.2.8 (2023-03-22).

* Wed Mar 22 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.21-alt1
- v6.1.21 (2023-03-22).

* Fri Mar 17 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.20-alt1
- v6.1.20 (2023-03-17).

* Mon Mar 13 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.19-alt1
- v6.1.19 (2023-03-13).

* Sat Mar 11 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.18-alt1
- v6.1.18 (2023-03-11).

* Sat Mar 11 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.17-alt1
- v6.1.17 (2023-03-11).

* Fri Mar 10 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.16-alt1
- v6.1.16 (2023-03-10).

* Fri Mar 03 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.15-alt1
- v6.1.15 (2023-03-03).

* Sat Feb 25 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.14-alt1
- v6.1.14 (2023-02-25).

* Wed Feb 22 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.13-alt1
- v6.1.13 (2023-02-22).

* Wed Feb 15 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.12-alt1
- v6.1.12 (2023-02-14).

* Thu Feb 09 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.11-alt1
- v6.1.11 (2023-02-09).

* Mon Feb 06 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.10-alt1
- v6.1.10 (2023-02-06).
- config-aarch64: Add Firefly Station P2 support.

* Thu Feb 02 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.9-alt1
- v6.1.9 (2023-02-01).
- config: Enable sfc-siena module (ALT#45079).
- Add kernel.unprivileged_io_uring_disabled sysctl.

* Tue Jan 24 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.8-alt1
- v6.1.8 (2023-01-24).
- config-aarch64: enable camera interface on Raspberry Pi.
- config-aarch64: fix for enable CONFIG_VIDEO_HANTRO=m.
- config-aarch64: update config for Rockchip rk3566|rk3568 SoC support.
- config-aarch64: fix outdated configs with new ones.

* Wed Jan 18 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.1.7-alt1
- v6.1.7 (2023-01-18).

* Tue Jan 17 2023 Vitaly Chikunov <vt@altlinux.org> 1:6.1.6-alt1
- v6.1.6 (2023-01-14).

* Thu Jan 12 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.0.19-alt1
- v6.0.19 (2023-01-12).
- config: Enable CONFIG_TXGBE=m (ALT#44895).

* Tue Jan 10 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.0.18-alt1
- v6.0.18 (2023-01-07).
- config-armh: Enable ROCKCHIP_IODOMAIN=m, CROS_EC_SPI=m (ALT#44813).

* Wed Jan 04 2023 Kernel Bot <kernelbot@altlinux.org> 1:6.0.17-alt1
- v6.0.17 (2023-01-04).

* Sat Dec 31 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.16-alt1
- v6.0.16 (2022-12-31).
- config: Enable CONFIG_BLK_DEV_UBLK=m.

* Thu Dec 22 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.15-alt1
- v6.0.15 (2022-12-21).

* Mon Dec 19 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.14-alt1
- v6.0.14 (2022-12-19).

* Thu Dec 15 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.13-alt1
- v6.0.13 (2022-12-14).

* Thu Dec 08 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.12-alt1
- v6.0.12 (2022-12-08).

* Sat Dec 03 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.11-alt1
- v6.0.11 (2022-12-02).
- config: Enable pvpanic modules.

* Sat Nov 26 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.10-alt1
- v6.0.10 (2022-11-26).

* Wed Nov 16 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.9-alt1
- v6.0.9 (2022-11-16).
- config: Enable CONFIG_CRASH_DUMP.

* Fri Nov 11 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.8-alt1
- v6.0.8 (2022-11-10).

* Fri Nov 04 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.7-alt1
- v6.0.7 (2022-11-04).

* Sat Oct 29 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.6-alt1
- v6.0.6 (2022-10-29).
- config: Disable DEBUG_INFO_BTF on aarch64.

* Wed Oct 26 2022 Kernel Bot <kernelbot@altlinux.org> 1:6.0.5-alt1
- v6.0.5 (2022-10-26).

* Mon Oct 24 2022 Vitaly Chikunov <vt@altlinux.org> 1:6.0.3-alt1
- Rebase to v6.0.3 (2022-10-21).
- Enable AMD ST support for ES8336 (ALT#43224).

* Mon Oct 24 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.17-alt1
- v5.19.17 (2022-10-24).

* Wed Oct 19 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.16-alt2
- ext4: fix check for block being out of directory size (Fixes:
  CVE-2022-1184).
- io_uring/af_unix: defer registered files gc to io_uring release
  (Fixes: CVE-2022-2602).

* Sat Oct 15 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.16-alt1
- v5.19.16 (2022-10-15).

* Wed Oct 12 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.15-alt1
- v5.19.15 (2022-10-12).

* Wed Oct 05 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.14-alt1
- v5.19.14 (2022-10-05).

* Wed Oct 05 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.13-alt1
- v5.19.13 (2022-10-04).
- config: Enable DRM_AMDGPU_SI, DRM_RADEON_USERPTR (ALT#43916).

* Wed Sep 28 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.12-alt1
- v5.19.12 (2022-09-28).

* Fri Sep 23 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.11-alt1
- v5.19.11 (2022-09-23).

* Tue Sep 20 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.10-alt1
- v5.19.10 (2022-09-20).

* Thu Sep 15 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.9-alt1
- v5.19.9 (2022-09-15).
- phy: rockchip-inno-usb2: Return zero after otg sync (ALT#43732).

* Thu Sep 08 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.8-alt1
- v5.19.8 (2022-09-08).
- Baikal-M: Support for Elpitech laptop.

* Tue Sep 06 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.19.7-alt1
- v5.19.7 (2022-09-05).

* Wed Aug 31 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.19.5-alt1
- v5.19.5 (2022-08-29).

* Fri Aug 26 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.19.4-alt1
- Rebase to v5.19.4 (2022-08-25).
- Apply baikalm-5.19.y patches (Alexey Sheplyakov).

* Sun Aug 21 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.19-alt1
- v5.18.19 (2022-08-21).

* Wed Aug 17 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.18-alt1
- v5.18.18 (2022-08-17).
- config: Make landlock, lockdown, and bpf LSMs available by default.
- ath11k: fix blocked for more than 120 seconds caused by reg update.
- Input: i8042 - enable dumbkbd quirk for HP 15-dy2xxx and 15s-fq2xxx.

* Thu Aug 11 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.17-alt1
- v5.18.17 (2022-08-11).

* Wed Aug 03 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.16-alt1
- v5.18.16 (2022-08-03).

* Sat Jul 30 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.15-alt1
- v5.18.15 (2022-07-29).

* Sat Jul 23 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.14-alt1
- v5.18.14 (2022-07-23).

* Fri Jul 22 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.13-alt1
- v5.18.13 (2022-07-22).

* Fri Jul 15 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.12-alt1
- v5.18.12 (2022-07-15).
- config: CONFIG_SND_SOC_AMD_ACP_PCI=m (ALT#43224).

* Wed Jul 13 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.11-alt1
- v5.18.11 (2022-07-12).

* Fri Jul 08 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.10-alt1
- v5.18.10 (2022-07-07).

* Sun Jul 03 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.9-alt1
- v5.18.9 (2022-07-02).

* Wed Jun 29 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.8-alt1
- v5.18.8 (2022-06-29).

* Mon Jun 27 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.18.7-alt1
- v5.18.7 (2022-06-25).

* Fri Jun 24 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.18.6-alt2
- Rebuild to fix loading of some kernel modules (particularly NAT).
  Note: This increases kernel-image package by ~20MB.

* Thu Jun 23 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.18.6-alt1
- Rebase to v5.18.6 (2022-06-22).
- Apply baikalm-5.18.y patches.
- Replace the fbdev drivers with simpledrm and the DRM fbdev emulation layer
  (excluding armh).

* Sat Jun 18 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.17.15-alt2
- Pick fixes of Intel-specific processor MMIO stale-data vulnerabilities.
 (Fixes: CVE-2022-21166, CVE-2022-21125, CVE-2022-21123).

* Wed Jun 15 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.17.15-alt1
- v5.17.15 (2022-06-14).

* Thu Jun 09 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.17.14-alt1
- v5.17.14 (2022-06-09).

* Tue Jun 07 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.17.13-alt1
- v5.17.13 (2022-06-06).
- altha: Restrict setcap binaries in nosuid mode.
- kernel.perf_event_paranoid=4 by default.

* Mon May 30 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.17.12-alt1
- v5.17.12 (2022-05-30).

* Wed May 25 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.17.11-alt1
- Update to v5.17.11 (2022-05-25).
- Applied Baikal-M patches. Supported boards: et101, aqbm1000, tf307.
  Supported firmware: based on SDK-M 5.3 (Alexey Sheplyakov)
- config: CONFIG_MICROCODE_OLD_INTERFACE=y which was off since 5.17.6-alt1.

* Wed May 18 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.17.9-alt1
- v5.17.9 (2022-05-18).

* Sun May 15 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.17.8-alt1
- v5.17.8 (2022-05-15).

* Thu May 12 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.17.7-alt1
- v5.17.7 (2022-05-12).

* Mon May 09 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.17.6-alt1
- Update to v5.17.6 (2022-05-09).
- spec: Provide: kernel-modules-ipset (closes: #42672).
- config: Enable CONFIG_NR_CPUS=8192 (closes: #42694).
- config: config: Enable KASLR (CONFIG_RANDOMIZE_BASE).
- config: Minor config update to add newest hardware and remove some legacy
  hardware support. Also, disable SHA1 (replace with SHA512), and
  set PANIC_TIMEOUT=600.

* Fri Apr 29 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.17.5-alt1
- v5.17.5 (2022-04-27).

* Wed Apr 20 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.17.4-alt1
- Rebase over next major stable release v5.17.4 (2022-04-20) due to v5.16
  branch being EOL. Duly contains multiple CVE fixes.
- Replace external kernel-modules-rtw89 with CONFIG_RTW89=m.
- Replace devicetree from /lib to /boot (Anton Midyukov)
- /lib/devicetree/<name.dtb> -> /lib/devicetree/<vendor>/<name.dtb> for
  aarch64 (Anton Midyukov).

* Thu Apr 14 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.20-alt1
- v5.16.20

* Sat Apr 09 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.19-alt1
- v5.16.19 (Fixes: CVE-2021-4034)

* Fri Apr 08 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.16.19-alt1
- Update to v5.16.19 (2022-04-08).

* Mon Mar 28 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.18-alt1
- v5.16.18

* Wed Mar 23 2022 Vitaly Chikunov <vt@altlinux.org> 1:5.16.17-alt1
- Update to v5.16.17 (2022-03-23).
- Use selected LTP tests in %%check.
- Do not build (redundant) htmldocs for kernel-doc package.
- CONFIG_SND_SOC_INTEL_SOF_ES8336_MACH=y (closes: #42075).
- CONFIG_BT_HCIBTUSB_MTK=y (closes: #42190).

* Sat Mar 19 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.16-alt1
- v5.16.16

* Wed Mar 16 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.15-alt1
- v5.16.15

* Mon Mar 14 2022 Nikolai Kostrigin <nickel@altlinux.org> 1:5.16.14-alt2
- config: enable Atheros ath11k PCI support
- Revert "Input: clear BTN_RIGHT/MIDDLE on buttonpads" to fix touchpad
  right button operation on ICL Si1516 laptop (closes: #42123)

* Fri Mar 11 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.14-alt1
- v5.16.14 (Fixes: CVE-2022-23036, CVE-2022-23037, CVE-2022-23038, CVE-2022-23039,
  CVE-2022-23040, CVE-2022-23041, CVE-2022-23042)

* Tue Mar 08 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.13-alt1
- v5.16.13

* Thu Mar 03 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.12-alt1
- v5.16.12

* Fri Feb 25 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.11-alt1
- v5.16.11

* Fri Feb 11 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.9-alt1
- v5.16.9  (Fixes: CVE-2022-0435)

* Wed Feb 09 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.8-alt1
- v5.16.8

* Mon Feb 07 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.7-alt1
- v5.16.7

* Wed Feb 02 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.5-alt1
- v5.16.5

* Sat Jan 29 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.4-alt1
- v5.16.4

* Fri Jan 28 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.3-alt1
- v5.16.3

* Thu Jan 20 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.2-alt1
- v5.16.2

* Wed Jan 19 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.1-alt1
- v5.16.1

* Tue Jan 11 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.16.0-alt1
- v5.16
- new gear repo scheme

* Sun Jan 09 2022 Kernel Bot <kernelbot@altlinux.org> 1:5.15.13-alt1
- v5.15.13

* Thu Dec 30 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.12-alt1
- v5.15.12

* Mon Dec 27 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.11-alt2
- CONFIG_FB_SIMPLE=y

* Wed Dec 22 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.11-alt1
- v5.15.11

* Fri Dec 17 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.10-alt1
- v5.15.10

* Tue Dec 14 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.8-alt1
- v5.15.8

* Wed Dec 08 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.7-alt1
- v5.15.7

* Wed Dec 01 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.6-alt1
- v5.15.6

* Mon Nov 29 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.5-alt3
- kernel.idmap_mounts sysctl introduced

* Fri Nov 26 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.5-alt2
- Add support for debian-specific kernel.unprivileged_userns_clone parameter

* Thu Nov 25 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.5-alt1
- v5.15.5

* Mon Nov 22 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.21-alt1
- v5.14.21

* Wed Nov 10 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.15.1-alt1
- v5.15.1

* Mon Nov 08 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.17-alt1
- v5.14.17

* Thu Nov 04 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.16-alt1
- v5.14.16  (Fixes: CVE-2021-42327)

* Wed Oct 27 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.15-alt1
- v5.14.15

* Wed Oct 20 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.14-alt1
- v5.14.14

* Sun Oct 17 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.13-alt1
- v5.14.13

* Wed Oct 13 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.12-alt1
- v5.14.12

* Sun Oct 10 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.11-alt1
- v5.14.11

* Thu Oct 07 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.10-alt1
- v5.14.10  (Fixes: CVE-2021-3653, CVE-2021-3656)

* Mon Oct 04 2021 Dmitry Terekhin <jqt4@altlinux.org> 1:5.14.9-alt2
- Disable all sleep states on BE-M1000 based boards.

* Thu Sep 30 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.9-alt1
- v5.14.9

* Wed Sep 29 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.8-alt1
- v5.14.8

* Thu Sep 23 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.13.19-alt1
- v5.13.19

* Wed Sep 01 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.14.0-alt1
- v5.14

* Fri Aug 27 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.13.13-alt1
- v5.13.13

* Thu Aug 19 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.13.12-alt1
- v5.13.12  (Fixes: CVE-2021-3653, CVE-2021-3656)

* Mon Aug 16 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.13.11-alt1
- v5.13.11  (Fixes: CVE-2021-3573)

* Thu Aug 12 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.13.10-alt1
- Updated to v5.13.10.

* Wed Aug 11 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.13.9-alt2
- Bumped release to pesign (alt1 was not pesigned, sorry).
- Added -checkinstall subpackage to verify EFI-stub signature.

* Wed Aug 11 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.13.9-alt1
- Updated to v5.13.9.

* Tue Aug 03 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.12.19-alt2
- Bumped release to pesign with new key.

* Wed Jul 21 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.19-alt1
- v5.12.19

* Mon Jul 19 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.18-alt1
- v5.12.18

* Fri Jul 16 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.17-alt1
- v5.12.17

* Mon Jul 12 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.16-alt1
- v5.12.16

* Fri Jul 09 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.15-alt1
- v5.12.15

* Wed Jun 30 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.14-alt1
- v5.12.14  (Fixes: CVE-2020-26541, CVE-2021-22543)

* Thu Jun 24 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.13-alt1
- v5.12.13

* Sat Jun 19 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.12-alt1
- v5.12.12

* Fri Jun 18 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.11-alt1
- v5.12.11

* Fri Jun 11 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.10-alt1
- v5.12.10  (Fixes: CVE-2020-24586, CVE-2020-24587, CVE-2020-24588, CVE-2020-26141,
  CVE-2020-26145, CVE-2020-26147, CVE-2021-20288, CVE-2021-23133,
  CVE-2021-23134, CVE-2021-28691, CVE-2021-3491, CVE-2021-3564)

* Fri May 14 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.12.0-alt1
- v5.12

* Fri May 14 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.21-alt1
- v5.11.21  (Fixes: CVE-2021-23133, CVE-2021-23134, CVE-2021-3491)

* Fri May 07 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.19-alt1
- v5.11.19

* Mon May 03 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.18-alt1
- v5.11.18

* Wed Apr 28 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.17-alt1
- v5.11.17

* Fri Apr 23 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.16-alt1
- v5.11.16  (Fixes: CVE-2021-23133)

* Fri Apr 16 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.15-alt1
- v5.11.15  (Fixes: CVE-2020-25670, CVE-2020-25671, CVE-2020-25672)

* Sat Apr 10 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.13-alt1
- v5.11.13

* Thu Apr 08 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.12-alt1
- v5.11.12  (Fixes: CVE-2021-29657)

* Thu Apr 01 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.11.11-alt2
- BE-M1000 partial support. PCI-E and sensors are NOT supported yet

* Wed Mar 31 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.11-alt1
- v5.11.11

* Sat Mar 27 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.10-alt1
- v5.11.10

* Tue Mar 23 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.8-alt1
- v5.11.8

* Thu Mar 18 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.7-alt1
- v5.11.7

* Fri Mar 12 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.23-alt1
- v5.10.23
- get rid of drm-radeon package (moved into drm)
- rmi2-core deps added to kernel-image

* Tue Mar 09 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.22-alt1
- v5.10.22

* Tue Mar 09 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.20-alt2
- get rid of v4l subpackage

* Fri Mar 05 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.20-alt1
- v5.10.20

* Mon Mar 01 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.19-alt1
- v5.10.19

* Fri Feb 19 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.11.0-alt1
- v5.11

* Thu Feb 18 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.17-alt1
- v5.10.17

* Wed Feb 17 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.16-alt1
- v5.10.16

* Wed Feb 10 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.15-alt1
- v5.10.15

* Tue Feb 09 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:5.10.14-alt2
- BE-M1000 (aka Baikal-M) support.  MBM1.0 boards with firmware from
  SDK-M version 4.4 and 4.3 are supported

* Mon Feb 08 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.14-alt1
- v5.10.14

* Thu Feb 04 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.13-alt1
- v5.10.13

* Mon Feb 01 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.12-alt1
- v5.10.12

* Thu Jan 28 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.11-alt1
- v5.10.11

* Sun Jan 24 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.10-alt1
- v5.10.10

* Wed Jan 20 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.9-alt2
- CONFIG_RMI4_* enabled

* Wed Jan 20 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.9-alt1
- v5.10.9

* Mon Jan 18 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.8-alt1
- v5.10.8

* Wed Jan 13 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.7-alt1
- v5.10.7  (Fixes: CVE-2020-28374)

* Sat Jan 09 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.6-alt1
- v5.10.6

* Thu Jan 07 2021 Kernel Bot <kernelbot@altlinux.org> 1:5.10.5-alt1
- v5.10.5

* Wed Dec 30 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.10.3-alt1
- v5.10.3

* Fri Dec 25 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.10.2-alt2
- ubuntu patch for NVIDIA drivers added

* Mon Dec 21 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.10.2-alt1
- v5.10.2

* Fri Dec 18 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.10.1-alt1
- v5.10.1

* Mon Dec 14 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.10.0-alt1
- v5.10

* Fri Dec 11 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.14-alt1
- v5.9.14  (Fixes: CVE-2020-28588)

* Tue Dec 08 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.13-alt1
- v5.9.13

* Wed Dec 02 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.12-alt1
- v5.9.12

* Tue Nov 24 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.11-alt1
- v5.9.11

* Sun Nov 22 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.10-alt1
- v5.9.10  (Fixes: CVE-2020-4788)

* Thu Nov 19 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.9-alt1
- v5.9.9

* Thu Nov 12 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.8-alt1
- v5.9.8

* Tue Nov 10 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.7-alt1
- v5.9.7

* Fri Nov 06 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.6-alt1
- v5.9.6  (Fixes: CVE-2020-25656)

* Mon Nov 02 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.3-alt1
- v5.9.3

* Thu Oct 29 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.2-alt1
- v5.9.2  (Fixes: CVE-2020-27152)

* Mon Oct 19 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.1-alt1
- v5.9.1

* Mon Oct 12 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.9.0-alt1
- v5.9

* Fri Oct 09 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.8.14-alt1
- v5.8.14

* Sat Oct 03 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.8.13-alt1
- v5.8.13

* Mon Sep 28 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.8.12-alt1
- v5.8.12

* Wed Sep 23 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.8.11-alt1
- v5.8.11

* Tue Sep 22 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.8.10-alt1
- v5.8.10

* Wed Sep 16 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.8.9-alt1
- v5.8.9

* Thu Sep 10 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.8.8-alt1
- v5.8.8

* Thu Aug 27 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.19-alt1
- v5.7.19

* Fri Aug 07 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.8.0-alt1
- v5.8

* Fri Aug 07 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.14-alt1
- v5.7.14

* Wed Aug 05 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.13-alt1
- v5.7.13

* Fri Jul 31 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.12-alt1
- v5.7.12

* Wed Jul 29 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.11-alt1
- v5.7.11

* Fri Jul 24 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.10-alt1
- v5.7.10

* Thu Jul 09 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.8-alt1
- v5.7.8

* Thu Jul 02 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.7-alt1
- v5.7.7

* Sat Jun 27 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.4.49-alt2
- Added armh support.
- Updated and cleaned up aarch64 and ppc64le configs.
- Built with numa balancing support (disabled by default).
- Disabled CONFIG_PAGE_OWNER.

* Thu Jun 25 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.6-alt1
- v5.7.6

* Tue Jun 23 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.5-alt1
- v5.7.5

* Thu Jun 18 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.4-alt1
- v5.7.4

* Tue Jun 16 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.2-alt2
- kiosk mode implemented by mcpain@

* Thu Jun 11 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.2-alt1
- v5.7.2

* Mon Jun 08 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.1-alt1
- v5.7.1  (Fixes: CVE-2020-10757)

* Tue Jun 03 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.7.0-alt1
- v5.7.0

* Wed Jun 03 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.6.16-alt1
- v5.6.16

* Wed May 27 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.6.15-alt1
- v5.6.15

* Fri May 15 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.6.13-alt1
- v5.6.13

* Sun May 10 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.6.12-alt1
- v5.6.12

* Wed May 06 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.6.11-alt1
- v5.6.11

* Thu Apr 30 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.6.8-alt1
- v5.6.8
- config changes from rider@

* Fri Apr 24 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.19-alt1
- v5.5.19  (Fixes: CVE-2019-19377)

* Thu Apr 02 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.6.0-alt1
- v5.6.0

* Wed Mar 25 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.13-alt1
- v5.5.13

* Wed Mar 25 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.12-alt1
- v5.5.12  (Fixes: CVE-2019-19769)

* Sat Mar 21 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.11-alt1
- v5.5.11

* Wed Mar 18 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.10-alt1
- v5.5.10

* Thu Mar 12 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.9-alt1
- v5.5.9  (Fixes: CVE-2020-8647, CVE-2020-8648, CVE-2020-8649)

* Fri Mar 06 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.8-alt1
- v5.5.8

* Fri Mar 06 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.24-alt1
- v5.4.24

* Sat Feb 29 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.7-alt1
- v5.5.7

* Sat Feb 29 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.23-alt1
- v5.4.23

* Tue Feb 25 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.6-alt1
- v5.5.6  (Fixes: CVE-2019-19076)

* Tue Feb 25 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.22-alt1
- v5.4.22  (Fixes: CVE-2019-19076)

* Thu Feb 20 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.5-alt1
- v5.5.5

* Thu Feb 13 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.3-alt1
- v5.5.3  (Fixes: CVE-2013-1798, CVE-2019-3016)

* Mon Feb 04 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.5.1-alt1
- v5.5.1

* Tue Feb 04 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.17-alt1
- v5.4.17(Fixes:_CVE-2019-14896,_CVE-2019-14897)

* Mon Jan 27 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.15-alt1
- v5.4.15

* Thu Jan 23 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.14-alt1
- v5.4.14

* Sat Jan 18 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.13-alt1
- v5.4.13

* Wed Jan 15 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.12-alt1
- v5.4.12(Fixes:_CVE-2019-14615,_CVE-2019-14895)

* Sun Jan 12 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.11-alt1
- v5.4.11

* Thu Jan 09 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.10-alt1
- v5.4.10

* Mon Jan 06 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.8-alt1
- v5.4.8

* Wed Jan 01 2020 Kernel Bot <kernelbot@altlinux.org> 1:5.4.7-alt1
- v5.4.7  (Fixes: CVE-2019-19037)

* Sat Dec 21 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.4.6-alt1
- v5.4.6

* Thu Dec 19 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.4.5-alt1
- v5.4.5

* Wed Dec 18 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.4.4-alt1
- v5.4.4

* Sat Dec 14 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.4.3-alt1
- v5.4.3  (Fixes: CVE-2019-18660, CVE-2019-19332)

* Sat Dec 14 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.4.0-alt1
- v5.4

* Thu Dec 05 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.15-alt1
- v5.3.15
* Sun Nov 24 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.13-alt1
- v5.3.13

* Thu Nov 21 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.12-alt1
- v5.3.12

* Wed Nov 13 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.11-alt1
- v5.3.11

* Sun Nov 10 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.10-alt1
- v5.3.10

* Thu Nov 07 2019 Vitaly Chikunov <vt@altlinux.org> 1:5.3.8-alt2
- Merge kernel-modules-kvm into kernel-image.

* Tue Oct 29 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.8-alt1
- v5.3.8

* Fri Oct 18 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.7-alt1
- v5.3.7

* Sun Oct 13 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.6-alt1
- v5.3.6

* Wed Oct 09 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.5-alt1
- v5.3.5  (Fixes: CVE-2019-14821)

* Wed Oct 09 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.3.0-alt1
- v5.3

* Mon Oct 07 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.20-alt1
- v5.2.20

* Sat Oct 05 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.19-alt1
- v5.2.19

* Mon Sep 16 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.15-alt1
- v5.2.15  (Fixes: CVE-2019-15030, CVE-2019-15031)

* Tue Sep 10 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.14-alt1
- v5.2.14

* Fri Sep 06 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.12-alt1
- v5.2.12

* Thu Aug 29 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.11-alt1
- v5.2.11

* Mon Aug 26 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.10-alt1
- v5.2.10

* Thu Aug 22 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.9-alt2
- aarch64 support added

* Fri Aug 16 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.9-alt1
- v5.2.9

* Sun Aug 11 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.8-alt1
- v5.2.8

* Tue Aug 06 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.21-alt1
- v5.1.21  (Fixes: CVE-2019-11478)

* Tue Aug 06 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.7-alt1
- v5.2.7

* Mon Aug 05 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.6-alt1
- v5.2.6  (Fixes: CVE-2019-10207, CVE-2019-11478, CVE-2019-13648)

* Thu Jul 18 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.1-alt1
- v5.2.1

* Tue Jul 16 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.18-alt1
- v5.1.18  (Fixes: CVE-2019-3846)

* Fri Jul 12 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.17-alt1
- v5.1.17

* Thu Jul 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.1.16-alt2
- Added ppc64le support.

* Wed Jul 03 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.16-alt1
- v5.1.16

* Tue Jun 25 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.15-alt1
- v5.1.15

* Mon Jun 24 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.14-alt1
- v5.1.14

* Thu Jun 20 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.12-alt1
- v5.1.12 (Fixes: CVE-2019-11477, CVE-2019-11478, CVE-2019-11479)

* Mon Jun 17 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.21-alt2
- multiple kernel remote denial of service issues fixed

* Mon Jun 03 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.9-alt1
- v5.1.9

* Sat May 11 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.15-alt1
- v5.0.15  (Fixes: CVE-2011-1079)

* Wed May 08 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.14-alt1
- v5.0.14

* Sun May 05 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.13-alt1
- v5.0.13

* Sat May 04 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.12-alt1
- v5.0.12  (Fixes: CVE-2019-3882)

* Mon Apr 22 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.9-alt1
- v5.0.9

* Wed Apr 17 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.8-alt2
- AltHa LSM added

* Wed Apr 17 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.8-alt1
- v5.0.8  (Fixes: CVE-2019-3887)

* Mon Apr 08 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.7-alt1
- v5.0.7

* Wed Apr 03 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.6-alt1
- v5.0.6

* Sat Mar 30 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.5-alt1
- v5.0.5

* Tue Mar 19 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.1-alt1
- v5.0.1

* Tue Mar 19 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.17-alt1
- v4.20.17

* Wed Mar 13 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.15-alt1
- v4.20.15

* Wed Mar 06 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.14-alt1
- 4.20.14

* Thu Feb 28 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.19.26-alt1
- v4.19.26

* Tue Feb 26 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.19.25-alt2
- SCSI_SMARTPQI set to m

* Tue Feb 26 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.12-alt1
- 4.20.12

* Thu Feb 07 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.7-alt1
- 4.20.7

* Fri Jan 11 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.1-alt1
- 4.20.1

* Mon Dec 24 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.20.0-alt1
- 4.20

* Sat Dec 22 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.12-alt1
- v4.19.12

* Mon Dec 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.10-alt1
- v4.19.10

* Thu Dec 13 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.9-alt1
- v4.19.9  (Fixes: CVE-2018-14625)

* Tue Dec 11 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.8-alt1
- v4.19.8

* Thu Dec 06 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.7-alt1
- v4.19.7

* Sun Dec 02 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.6-alt1
- v4.19.6

* Fri Nov 30 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.5-alt2
- build iin old branches fixed

* Tue Nov 27 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.5-alt1
- v4.19.5

* Fri Nov 23 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.4-alt1
- v4.19.4

* Thu Nov 22 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.3-alt1
- v4.19.3  (Fixes: CVE-2018-10940, CVE-2018-16658)

* Wed Nov 14 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.2-alt1
- v4.19.2  (Fixes: CVE-2018-18955)

* Fri Nov 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.1-alt1
- v4.19.1

* Mon Nov 05 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.17-alt1
- v4.18.17

* Mon Oct 29 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.0-alt1
- v4.19

* Sat Oct 20 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.16-alt1
- v4.18.16

* Thu Oct 18 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.15-alt1
- v4.18.15

* Mon Oct 15 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.14-alt1
- v4.18.14  (Fixes: CVE-2018-15471)

* Thu Oct 04 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.12-alt1
- v4.18.12  (Fixes: CVE-2018-7755)

* Mon Oct 01 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.11-alt1
- v4.18.11  (Fixes: CVE-2018-14633)

* Wed Sep 26 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.10-alt0.M80C.1
- v4.18.10

* Wed Sep 26 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.10-alt1
- v4.18.10

* Thu Sep 20 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.9-alt1
- v4.18.9

* Mon Sep 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.8-alt1
- v4.18.8

* Mon Sep 10 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.7-alt1
- v4.18.7

* Wed Sep 05 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.6-alt1
- v4.18.6

* Wed Aug 29 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.5-alt1
- v4.18.5

* Wed Aug 22 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.4-alt1
- v4.18.4

* Tue Aug 21 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.3-alt1
- v4.18.3  (Fixes: CVE-2018-9363)

* Fri Aug 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.1-alt1
- 4.18.1

* Thu Aug 16 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.15-alt1
- v4.17.15  (Fixes: CVE-2018-3620)

* Thu Aug 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.14-alt1
- v4.17.14

* Tue Aug 07 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.13-alt1
- v4.17.13

* Sat Aug 04 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.12-alt1
- v4.17.12

* Sun Jul 22 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.9-alt1
- v4.17.9

* Wed Jul 18 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.8-alt1
- v4.17.8

* Tue Jul 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.7-alt1
- v4.17.7

* Wed Jul 11 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.6-alt1
- v4.17.6  (Fixes: CVE-2018-10876, CVE-2018-10877, CVE-2018-10879, CVE-2018-10880,
  CVE-2018-10881, CVE-2018-10882, CVE-2018-10883)

* Mon Jul 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.5-alt1
- v4.17.5

* Tue Jul 03 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.4-alt1
- v4.17.4

* Tue Jun 26 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.18-alt1
- v4.16.18  (Fixes: CVE-2018-10840, CVE-2018-1118, CVE-2018-11412)

* Mon Jun 04 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.0-alt1
- v4.17

* Wed May 30 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.13-alt1
- v4.16.13

* Mon May 28 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.12-alt1
- v4.16.12
- external modules build fixed
- experimantal AltHa LSM added

* Wed May 23 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.11-alt1
- v4.16.11

* Mon May 21 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.10-alt1
- v4.16.10  (Fixes: CVE-2018-1120)

* Wed May 16 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.9-alt1
- v4.16.9  (Fixes: CVE-2018-1000200)

* Wed May 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.8-alt1
- v4.16.8

* Sun May 06 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.7-alt1
- v4.16.7  (Fixes: CVE-2018-1093, CVE-2018-1108)

* Thu Apr 26 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.5-alt1
- v4.16.5

* Tue Apr 24 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.4-alt1
- v4.16.4  (Fixes: CVE-2018-1092, CVE-2018-1094, CVE-2018-1095, CVE-2018-1108)

* Thu Apr 19 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.3-alt1
- v4.16.3

* Thu Apr 12 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.2-alt1
- v4.16.2

* Mon Apr 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.1-alt1
- v4.16.1

* Tue Apr 03 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.0-alt1
- v4.16.0

* Sun Apr 01 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.32-alt1
- v4.14.32  (Fixes: CVE-2017-8824)

* Mon Feb 19 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.15.4-alt1
- v4.15.4

* Mon Feb 05 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.17-alt1
- v4.14.17

* Wed Jan 31 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.16-alt1
- v4.14.16  (Fixes: CVE-2017-5715)

* Wed Jan 24 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.15-alt1
- v4.14.15

* Wed Jan 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.14-alt1
- v4.14.14  (Fixes: CVE-2017-1000410, CVE-2017-17741, CVE-2017-5753)

* Wed Jan 10 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.13-alt1
- v4.14.13

* Tue Jan 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.9.75-alt0.M80C.1
- v4.9.75

* Tue Jan 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.12-alt1
- v4.14.12

* Fri Dec 29 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.10-alt1
- v4.14.10

* Mon Dec 25 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.9-alt1
- v4.14.9  (Fixes: CVE-2017-16995, CVE-2017-16996)

* Mon Dec 25 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.8-alt1.1
- SMACK enabled
- kernel.unprivileged_bpf_disabled set by default  (Fixes: CVE-2017-16995, CVE-2017-16996)

* Wed Dec 20 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.8-alt1
- v4.14.8

* Sun Dec 17 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.7-alt1
- v4.14.7

* Fri Dec 15 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.6-alt1
- v4.14.6   (Fixes: CVE-2017-0861, CVE-2017-1000407)

* Mon Dec 11 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.5-alt1
- v4.14.5

* Wed Dec 06 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.4-alt1
- v4.14.4   (Fixes: CVE-2011-1161, CVE-2017-8824)

* Tue Dec 05 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.16-alt1.1
- temporary fix for HugeDirtyCowPOC (fixes CVE-2017-1000405)

* Mon Nov 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.0-alt1
- v4.14.0

* Wed Nov 08 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.12-alt1
- v4.13.12

* Thu Nov 02 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.11-alt1
- v4.13.11   (Fixes: CVE-2017-12193)

* Fri Oct 27 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.10-alt1.1
- v4.13.10

* Sun Oct 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.9-alt1.1
- v4.13.9

* Wed Oct 18 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.8-alt1.1
- v4.13.8   (Fixes: CVE-2017-12188, CVE-2017-15265)

* Tue Oct 17 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.7-alt1.1
- Local root in alsa fixed (Fixes: CVE-2017-15265)

* Sun Oct 15 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.7-alt1
- v4.13.7   (Fixes: CVE-2017-5123)

* Fri Oct 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.6-alt1
- v4.13.6   (Fixes: CVE-2017-0786, CVE-2017-1000255)

* Thu Oct 05 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.5-alt1
- v4.13.5   (Fixes: CVE-2017-1000252, CVE-2017-12153, CVE-2017-12154)

* Wed Sep 27 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.4-alt1
- v4.13.4 

* Wed Sep 20 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.3-alt1
- v4.13.3

* Thu Sep 14 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.2-alt1
- v4.13.2

* Thu Sep 14 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.0-alt1
- v4.13.0

* Tue Sep 12 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.12-alt1
- v4.12.12

* Wed Aug 30 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.10-alt1
- v4.12.10

* Fri Aug 25 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.9-alt1
- v4.12.9

* Wed Aug 16 2017 Dmitry V. Levin <ldv@altlinux.org> 1:4.12.8-alt1
- v4.12.7 -> v4.12.8.
- Synced %%check with std-def.
- Changed kernel-doc to a noarch subpackage.
- Restricted access to %%modules_dir/ (see #5969).

* Sun Aug 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.7-alt1
- v4.12.7

* Sat Aug 12 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.6-alt1
- v4.12.6

* Sun Aug 06 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.5-alt1
- v4.12.5

* Thu Jul 27 2017 Dmitry V. Levin <ldv@altlinux.org> 1:4.12.4-alt1
- v4.12.2 -> v4.12.4.

* Sat Jul 15 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.2-alt1
- v4.12.2

* Thu Jul 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.1-alt1
- v4.12.1

* Tue Jul 04 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.0-alt1
- v4.12

* Thu Jun 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.11.6-alt1
- 4.11.6

* Wed May 24 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.11.2-alt1
- v4.11.2

* Mon May 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.11.1-alt1
- v4.11.1

* Mon May 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.17-alt1
- v4.10.17

* Mon May 15 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.16-alt1
- v4.10.16

* Wed May 10 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.15-alt1
- v4.10.15

* Sat Apr 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.12-alt1
- v4.10.12

* Wed Apr 19 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.11-alt1
- v4.10.11

* Thu Apr 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.10-alt1
- v4.10.10

* Sun Apr 09 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.9-alt1
- v4.10.9

* Fri Mar 31 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.8-alt1
- v4.10.8

* Sun Mar 26 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.6-alt1
- v4.10.6

* Wed Mar 22 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.5-alt1
- v4.10.5

* Sun Mar 19 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.4-alt1
- v4.10.4

* Fri Mar 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.3-alt1
- 4.10.3
- in-kernel ipset returned

* Sun Mar 12 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.2-alt1
- 4.10.2

* Sun Mar 12 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.14-alt1
- v4.9.14

* Mon Feb 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.1-alt1
- 4.10.1

* Mon Feb 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.13-alt1
- v4.9.13

* Fri Feb 24 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.12-alt1
- v4.9.12

* Mon Feb 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.11-alt1
- v4.9.11

* Wed Feb 15 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.10-alt1
- v4.9.10

* Thu Feb 09 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.9-alt1
- v4.9.9

* Sun Feb 05 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.8-alt1
- v4.9.8

* Wed Feb 01 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.7-alt1
- v4.9.7

* Thu Jan 26 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.6-alt1
- v4.9.6

* Fri Jan 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.5-alt1
- v4.9.5

* Wed Jan 18 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.4-alt1
- v4.9.4

* Thu Jan 12 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.3-alt1
- v4.9.3

* Tue Jan 10 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.17-alt1
- v4.8.17

* Sat Jan 07 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.16-alt1
- v4.8.16

* Fri Dec 16 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.15-alt1
- v4.8.15

* Sun Dec 11 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.14-alt1
- v4.8.14

* Fri Dec 09 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.13-alt1
- v4.8.13

* Fri Dec 02 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.12-alt1
- v4.8.12

* Sat Nov 26 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.11-alt1
- v4.8.11

* Mon Nov 21 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.10-alt1
- v4.8.10

* Sun Nov 20 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.9-alt1
- v4.8.9

* Tue Nov 15 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.8-alt1
- v4.8.8

* Thu Nov 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.7-alt1
- v4.8.7

* Tue Nov 01 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.6-alt1
- v4.8.6

* Fri Oct 28 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.5-alt1
- v4.8.5
- secured /proc/interrupts

* Tue Oct 25 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.4-alt1
- v4.8.4

* Sat Oct 22 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.10-alt1
- v4.7.10

* Mon Oct 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.1-alt1
- v4.8.1

* Thu Oct 06 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.0-alt1
- v4.8
- gcc5 as kgcc
- gcc plugin activated (uses gcc-c++, libgmp-devel, mpc-devel)

* Fri Sep 30 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.6-alt1
- v4.7.6

* Sat Sep 24 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.5-alt1
- v4.7.5

* Thu Sep 15 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.4-alt1
- v4.7.4

* Wed Sep 07 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.3-alt1
- v4.7.3

* Sat Aug 20 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.2-alt1
- v4.7.2

* Thu Aug 18 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.1-alt1
- v4.7.1

* Wed Aug 17 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.7-alt1
- v4.6.7

* Mon Jul 25 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.0-alt1
- v4.7

* Mon Jul 11 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.4-alt1
- v4.6.4

* Sat Jun 25 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.3-alt1
- v4.6.3

* Fri Jun 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.2-alt1
- 4.6.2

* Wed Jun 08 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.7-alt1
- v4.5.7

* Thu May 19 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.0-alt1
- 4.6.0

* Thu May 12 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.4-alt1
- 4.5.4

* Fri May 06 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.3-alt1
- 4.5.3

* Wed Apr 20 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.2-alt1
- 4.5.2

* Wed Apr 13 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.1-alt1
- 4.5.1

* Tue Mar 15 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.0-alt1
- 4.5

* Thu Mar 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.5-alt1
- 4.4.5

* Fri Mar 04 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.4-alt1
- 4.4.4

* Fri Feb 26 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.3-alt1
- 4.4.3

* Thu Feb 18 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.2-alt1
- 4.4.2

* Tue Feb 02 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.1-alt1
- 4.4.1

* Tue Jan 19 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.0-alt2
- CVE-2016-0728 fixed

* Mon Jan 11 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.0-alt1
- 4.4.0

* Tue Dec 15 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.3.3-alt1
- 4.3.3

* Fri Dec 11 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.3.2-alt1
- 4.3.2

* Thu Dec 10 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.3.1-alt1
- 4.3.1

* Tue Nov 17 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.3.0-alt1
- 4.3.0

* Tue Nov 10 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.2.6-alt1
- 4.2.6

* Tue Oct 27 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.5-alt1
- 4.2.5

* Fri Oct 23 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.4-alt1
- 4.2.4

* Thu Oct 08 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.3-alt2
- CONFIG_NO_HZ_FULL disabled (closes: #31342)

* Mon Oct 05 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.3-alt1
- 4.2.3

* Tue Sep 29 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.1-alt1
- 4.2.1

* Tue Sep 08 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.0-alt1
- 4.2

* Mon Aug 17 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.1.6-alt1
- 4.1.6

* Tue Aug 11 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.1.5-alt1
- 4.1.5

* Wed Aug 05 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.1.4-alt1
- 4.1.4

* Tue Aug 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.9-alt1
- 4.0.9

* Mon Jul 13 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.8-alt1
- 4.0.8

* Tue Jun 23 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.6-alt1
- 4.0.6
- dependence on bootloader-utils upgraded

* Tue Jun 09 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.5-alt1
- 4.0.5

* Thu May 21 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.4-alt1
- 4.0.4

* Mon May 18 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.3-alt1
- 4.0.3

* Tue May 12 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.8-alt1
- 3.19.8

* Mon Apr 27 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.0-alt1
- 4.0.0

* Mon Apr 20 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.5-alt1
- 3.19.5

* Mon Apr 13 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.4-alt1
- 3.19.4

* Thu Mar 26 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.3-alt1
- 3.19.3

* Wed Mar 18 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.2-alt1
- 3.19.2

* Sun Mar 08 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.1-alt1
- 3.19.1

* Tue Feb 17 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.0-alt1
- 3.19

* Wed Feb 11 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.7-alt1
- 3.18.7
- adjtimex on 32-bit fixed
- in-kernel ipset excluded
- netlabel patch updated

* Sat Feb 07 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.6-alt1
- 3.18.6

* Fri Jan 30 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.5-alt1
- 3.18.5

* Wed Jan 28 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.4-alt1
- 3.18.4

* Sat Jan 17 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.3-alt1
- 3.18.3

* Fri Jan 09 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.2-alt1
- 3.18.2

* Wed Dec 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.1-alt1
- 3.18.1

* Mon Dec 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.0-alt1
- 3.18.0

* Mon Dec 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.6-alt1
- 3.17.6

* Sun Dec 07 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.5-alt1
- 3.17.5

* Sat Nov 22 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.4-alt1
- 3.17.4
- set HZ=1000 on x86_64

* Sun Nov 16 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.3-alt1
- 3.17.3

* Fri Oct 31 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.2-alt1
- 3.17.2

* Fri Oct 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.1-alt1
- 3.17.1

* Wed Oct 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.6-alt1
- 3.16.6

* Fri Oct 10 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.5-alt1
- 3.16.5

* Mon Oct 06 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.4-alt1
- 3.16.4

* Thu Oct 02 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.3-alt2
- ldv and sem patches added

* Thu Sep 18 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.3-alt1
- 3.16.3

* Mon Sep 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.2-alt1
- 3.16.2

* Wed Aug 20 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.1-alt1
- 3.16.1

* Mon Aug 18 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.0-alt1
- 3.16.0

* Mon Aug 18 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.10-alt1
- 3.15.10

* Fri Aug 01 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.8-alt1
- 3.15.8

* Thu Jul 31 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.7-alt1
- 3.15.7

* Wed Jul 16 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.5-alt2
- EFI_MIXED enabled

* Wed Jul 09 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.5-alt1
- 3.15.5

* Mon Jul 07 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.4-alt1
- 3.15.4

* Tue Jul 01 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.3-alt1
- 3.15.3

* Fri Jun 27 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.2-alt1
- 3.15.2
- LEGACY_PTYS disabled
- AUFS added

* Tue Jun 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.1-alt1
- 3.15.1

* Tue Jun 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.8-alt1
- 3.14.7

* Thu Jun 12 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.7-alt1
- 3.14.7

* Sun Jun 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.6-alt1
- 3.14.6

* Thu Jun 05 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.5-alt2
- Fixes CVE-2014-3153

* Sun Jun 01 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.5-alt1
- 3.14.5

* Wed May 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.4-alt1
- 3.14.4

* Wed May 07 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.3-alt1
- 3.14.3

* Mon Apr 28 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.2-alt1
- 3.14.2

* Wed Apr 23 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.11-alt1
- 3.13.11

* Tue Apr 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.1-alt1
- 3.14.1

* Mon Apr 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.0-alt1
- 3.14

* Fri Apr 04 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.9-alt1
- 3.13.9

* Tue Apr 01 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.8-alt1
- 3.13.8
- "usb: ehci: fix deadlock when threadirqs option is use" reverted

* Mon Mar 24 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.7-alt1
- 3.13.7

* Thu Mar 20 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.6-alt2
- CVE-2014-2523 fixed

* Tue Mar 11 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.6-alt1
- 3.13.6

* Mon Feb 24 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.5-alt1
- 3.13.5

* Fri Feb 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.4-alt1
- 3.13.4

* Fri Feb 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.3-alt1
- 3.13.3

* Fri Feb 07 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.2-alt1
- 3.13.2

* Thu Jan 30 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.1-alt1
- 3.13.1

* Wed Jan 22 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.0-alt1
- 3.13.0

* Thu Jan 16 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.8-alt1
- 3.12.8

* Fri Jan 10 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.7-alt1
- 3.12.7
- "drm/radeon: 0x9649 is SUMO2 not SUMO" patch applied

* Fri Dec 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.6-alt1
- 3.12.6

* Thu Dec 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.5-alt1
- 3.12.5

* Mon Dec 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.4-alt1
- 3.12.4

* Thu Dec 05 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.3-alt1
- 3.12.3

* Tue Dec 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.2-alt1
- 3.12.2

* Fri Nov 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.1-alt1
- 3.12.1

* Thu Nov 21 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.9-alt1
- 3.11.9

* Wed Nov 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.0-alt1
- 3.12.0

* Wed Nov 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.8-alt1
- 3.11.8

* Mon Nov 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.7-alt1
- 3.11.7

* Sat Oct 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.6-alt1
- 3.11.6

* Mon Oct 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.5-alt1
- 3.11.5

* Sun Oct 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.4-alt1
- 3.11.4

* Tue Oct 01 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.3-alt1
- 3.11.3

* Fri Sep 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.2-alt1
- 3.11.2

* Wed Sep 18 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.1-alt2
- CONFIG_DEBUG_ATOMIC_SLEEP disabled
- aufs fixed

* Sun Sep 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.1-alt1
- 3.11.1

* Fri Sep 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.0-alt1
- 3.11

* Tue Sep 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.11-alt1
- 3.10.11

* Thu Aug 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.10-alt1
- 3.10.10

* Tue Aug 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.8-alt1
- 3.10.8

* Fri Aug 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.7-alt1.1
- bpp hack from Ulf Winkelvos in hope to fix #29219
- memory sanitizing patch added
- exfat driver from Samsung added

* Thu Aug 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.7-alt1
- 3.10.7

* Mon Aug 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.6-alt1
- 3.10.6
- CONFIG_GOLDFISH_* disabled (mike@)

* Wed Aug 07 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.5-alt2
- "Add mark s0 flag for NetLabel subsystem" patch from stanv@ added

* Mon Aug 05 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.10.5-alt1
- 3.10.5

* Mon Jul 29 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.10.4-alt1
- 3.10.4

* Fri Jul 26 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.10.3-alt1
- 3.10.3

* Mon Jul 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.2-alt1
- 3.10.2

* Tue Jul 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.1-alt1
- 3.10.1

* Sun Jul 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.10-alt1
- 3.9.10

* Thu Jun 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.8-alt1
- 3.9.8
- ipset disabled for separate module

* Fri Jun 21 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.7-alt1
- 3.9.7
- SWIOTLB on i586 set to y (closes #28911)

* Fri Jun 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.6-alt1
- 3.9.6

* Mon Jun 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.5-alt1
- 3.9.5

* Tue Jun 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.4-alt2
- CVE-2013-2850 fixed

* Sat May 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.4-alt1
- 3.9.4

* Mon May 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.3-alt1
- 3.9.3

* Sun May 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.2-alt1
- 3.9.2

* Sun May 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.13-alt1
- 3.8.13

* Wed May 08 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.1-alt1
- 3.9.1

* Mon May 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.0-alt1
- 3.9.0

* Sun May 05 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.11-alt1
- 3.8.11

* Mon Apr 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.10-alt1
- 3.8.10

* Fri Apr 26 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.9-alt1
- 3.8.9

* Mon Apr 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.8-alt2
- EFI_VARS set back to m

* Wed Apr 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.8-alt1
- 3.8.8
- EFI_VARS set to y

* Tue Apr 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.7-alt2
- uefi boot record instalation fixed (closes #28827)

* Fri Apr 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.7-alt1
- 3.8.7

* Fri Apr 05 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.6-alt1
- 3.8.6
- evbug disabled

* Fri Mar 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.5-alt1
- 3.8.5
- RTC_CMOS changed ot y (closes #28513)

* Thu Mar 21 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.4-alt1
- 3.8.4

* Fri Mar 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.3-alt1
- 3.8.3
- obsoleted postinstall scripts calls removed

* Thu Mar 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.2-alt3
- Don't allow CLONE_NEWUSER | CLONE_FS (local root fixed)
- CVE-2013-1828 fixed

* Wed Mar 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.2-alt2
- lost rtl8192ce enabled on i586
- default bpp on cirrus/qemu set to 16

* Mon Mar 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.2-alt1
- 3.8.2

* Thu Feb 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.1-alt1
- 3.8.1

* Thu Feb 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.10-alt1
- 3.7.10

* Mon Feb 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.0-alt2
- CVE-2013-1763 fixed

* Tue Feb 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.0-alt1
- 3.8.0

* Mon Feb 18 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.9-alt1
- 3.7.9
- patches for correct /proc permissions from ldv@ applied

* Fri Feb 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.8-alt1
- 3.7.8

* Wed Feb 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.7-alt1.1
- REGULATOR_DUMMY disabled (closes #27798)

* Mon Feb 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.7-alt1
- 3.7.7

* Wed Feb 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.6-alt1.1
- no OSS and some other config changes (closes: #28358) (closes: #28359)

* Mon Feb 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.6-alt1
- 3.7.6

* Tue Jan 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.5-alt1
- 3.7.5
- FANOTIFY and MMC_RICOH_MMC enabled

* Tue Jan 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.4-alt1
- 3.7.4

* Thu Jan 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.3-alt1
- 3.7.3

* Mon Jan 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.2-alt1.2
- conditional docs building

* Mon Jan 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.2-alt1.1
- changelog entries for std-def and std-pae added (hackaround)

* Mon Jan 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.2-alt1
- std-def, std-pae and un-def from one tree via specsubst
- 3.7.2
- gcc 4.7

* Sat Dec 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.1-alt2.1
- really do as written below

* Fri Dec 28 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.1-alt2
- make sha256 module on i586

* Thu Dec 20 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.6.11-alt1
- 3.6.11 (closes: 28138)
- Build using std-def config with config diff from 3.5.7.

* Tue Dec 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.1-alt1
- 3.7.1

* Tue Dec 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.11-alt1
- 3.6.11

* Tue Dec 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.0-alt1
- 3.7 release

* Tue Dec 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.0-alt0.8
- 3.7-rc8

* Tue Nov 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.0-alt0.7
- 3.7-rc7

* Tue Nov 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.8-alt1
- 3.6.8

* Wed Nov 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.7-alt2
- 32 bpp framebuffer on kvm's cirrus disabled back
- link-vmlinux.sh packaged (closes: #28016)

* Mon Nov 19 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.7-alt1
- 3.6.7

* Thu Nov 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.6-alt2
- some cirrus-related patches applied, 32 bpp mode enabled

* Tue Nov 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.6-alt1
- 3.6.6

* Thu Nov 01 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.5-alt1
- 3.6.5
- FB_EFI enabled

* Mon Oct 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.4-alt2
- 3.6.4

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.3-alt2
- fixed possible ex4 corruption (https://lkml.org/lkml/2012/10/23/690)
- ldv@ patchs to mountinfo added
- CONFIG_DEBUG_PREEMPT disabled

* Mon Oct 22 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.3-alt1
- 3.6.3
- Borislav Petkovs test fix fo boot crash on nvidia ide

* Sat Oct 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.2-alt1
- 3.6.2

* Thu Oct 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.1-alt2.1
- POWER_AVS disabled

* Mon Oct 08 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.1-alt2
- 3.6.1

* Thu Oct 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.0-alt2
- wrong default hostname on x86_64 fixed
- drm-vgem driver added
- some config changes from std-def

* Mon Oct 01 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.0-alt1
- 3.6

* Sat Sep 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.4-alt1
- 3.5.4

* Sun Aug 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.3-alt1
- 3.5.3
- kmod: pass -b option to /sbin/modprobe (by ldv@)

* Wed Aug 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.2-alt1
- 3.5.2
- Applyed: fs: push rcu_barrier() from deactivate_locked_super()

* Fri Aug 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.1-alt1
- 3.5.1

* Thu Aug 02 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.0-alt2
- rebuild with right kernel-source

* Thu Jul 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.0-alt1
- 3.5

* Fri Jul 20 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.4.6-alt1
- 3.4.6

* Tue Jul 17 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.4.5-alt1
- 3.4.5

* Mon Jun 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.4.4-alt1
- 3.4.4
