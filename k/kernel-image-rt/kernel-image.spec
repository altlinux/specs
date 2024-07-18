Name: kernel-image-rt
%define kernel_base_version	6.1
%define kernel_sublevel	.99
%define kernel_rt_release	rt36
%define kernel_extra_version	%nil
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
Release: alt1.%kernel_rt_release

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

Summary: The Linux kernel with PREEMPT_RT patches (Real-Time Linux)
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://wiki.linuxfoundation.org/realtime/
Vcs: git://git.kernel.org/pub/scm/linux/kernel/git/rt/linux-stable-rt.git
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: %name-%version-%release.patch

%if "%sub_flavour" == "pae"
ExclusiveArch: i586
%else
ExclusiveArch: aarch64 x86_64
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
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm-run >= 1.30 ltp >= 20210524-alt2 iproute2 rtcheck}}

%description
This package contains the Linux kernel %kernel_base_version%kernel_sublevel \
with Real-Time Linux project PREEMPT_RT patches.

Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).

There are some other kernel variants in ALT systems:
* std-def: latest longterm (LTS) kernel;
* un-def:  latest stable kernel, usually higher version than std-def.

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
Provides:  kernel-modules-v4l-%flavour = %version-%release
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
Requires(pre,post,postun): %name = %EVR

%description -n kernel-modules-drm-ancient-%flavour
The Direct Rendering Modules for ancient cards:
sis.ko, tdfx.ko, savage.ko, r128.ko, mga.ko, via.ko

These are modules for your ALT Linux system

%package -n kernel-modules-drm-nouveau-%flavour
Summary: The Direct Rendering Infrastructure modules for NVIDIA cards
Group: System/Kernel and hardware
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
%define _default_patch_flags -s
%autopatch -p1

# fix -rt suffix
rm -f localversion*

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
%if "%base_flavour" == "rt"
CONFIGS="$CONFIGS config-rt"
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
# Boot-test and check for Real-Time properties.
timeout 300 vm-run --tcg --mem=1G --cpu=1 --qemu="-rtc clock=vm -icount 0,sleep=on" rtcheck -v
# Longer LTP tests only if there is KVM (which is present on all main arches).
if ! timeout 999 vm-run --kvm=cond \
        "/sbin/sysctl kernel.printk=8;
         runltp -f kernel-alt-vm -S skiplist-alt-vm -o out"; then
        cat /usr/lib/ltp/output/LTP_RUN_ON-out.failed >&2
        sed '/TINFO/i\\' /usr/lib/ltp/output/out | awk '/TFAIL/' RS= >&2
        exit 1
fi
# Verify fchmodat2 backport.
make -C tools/testing/selftests/fchmodat2
timeout 300 vm-run tools/testing/selftests/fchmodat2/fchmodat2_test

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
%ifnarch aarch64 armh
%exclude %modules_dir/kernel/drivers/gpu/drm/sis
%exclude %modules_dir/kernel/drivers/gpu/drm/savage
%exclude %modules_dir/kernel/drivers/gpu/drm/tdfx
%exclude %modules_dir/kernel/drivers/gpu/drm/r128
%exclude %modules_dir/kernel/drivers/gpu/drm/mga
%exclude %modules_dir/kernel/drivers/gpu/drm/via
%endif

%files -n kernel-modules-drm-ancient-%flavour
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
* Thu Jul 18 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.99-alt1.rt36
- v6.1.99-rt36 (2024-07-17).

* Thu Jul 04 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.96-alt1.rt35
- v6.1.96-rt35 (2024-07-02).

* Fri Jun 28 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.95-alt1.rt34
- v6.1.95-rt34 (2024-06-26).

* Fri Jun 21 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.94-alt1.rt33
- v6.1.94-rt33 (2024-06-20).

* Mon May 27 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.92-alt1.rt32
- v6.1.92-rt32 (2024-05-26).

* Sat May 25 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.91-alt1.rt31
- v6.1.91-rt31 (2024-05-24).

* Wed May 15 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.1.90-alt2.rt30
- Bumped release to pesign with the new key.

* Fri May 10 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.90-alt1.rt30
- v6.1.90-rt30 (2024-05-03).

* Thu Apr 04 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.83-alt1.rt28
- v6.1.83-rt28 (2024-03-28).

* Thu Mar 21 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.82-alt1.rt27
- v6.1.82-rt27 (2024-03-21).

* Sat Mar 02 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.80-alt1.rt26
- v6.1.80-rt26 (2024-03-01).

* Wed Feb 28 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.79-alt1.rt25
- v6.1.79-rt25 (2024-02-27).

* Fri Feb 09 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.77-alt1.rt24
- v6.1.77-rt24 (2024-02-08).

* Wed Jan 31 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.75-alt1.rt23
- v6.1.75-rt23 (2024-01-30).

* Fri Jan 19 2024 Kernel Bot <kernelbot@altlinux.org> 6.1.73-alt1.rt22
- v6.1.73-rt22 (2024-01-18).

* Fri Dec 29 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.69-alt1.rt21
- v6.1.69-rt21 (2023-12-28).

* Thu Dec 14 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.67-alt1.rt20
- v6.1.67-rt20 (2023-12-13).

* Sat Dec 09 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.66-alt1.rt19
- v6.1.66-rt19 (2023-12-08).

* Mon Dec 04 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.65-alt1.rt18
- v6.1.65-rt18 (2023-12-03).

* Sat Dec 02 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.64-alt1.rt17
- v6.1.64-rt17 (2023-12-01).
- config: Enable HID_REDRAGON module (ALT#48182).
- Remove symlinking to /lib/devicetree (ALT#48055).

* Sat Oct 21 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.59-alt1.rt16
- v6.1.59-rt16 (2023-10-20).

* Wed Sep 20 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.54-alt1.rt15
- v6.1.54-rt15 (2023-09-19).

* Mon Sep 18 2023 Vitaly Chikunov <vt@altlinux.org> 6.1.46-alt2.rt14
- Synchronize source with std-def/sisyphus.

* Mon Sep 18 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.46-alt1.rt14
- v6.1.46-rt14 (2023-09-17).

* Fri Aug 18 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.46-alt1.rt13
- v6.1.46-rt13 (2023-08-18).

* Sat Jul 08 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.38-alt1.rt12
- v6.1.38-rt12 (2023-07-07).

* Thu Jun 15 2023 Kernel Bot <kernelbot@altlinux.org> 6.1.33-alt1.rt11
- v6.1.33-rt11 (2023-06-12).

* Tue May 16 2023 Vitaly Chikunov <vt@altlinux.org> 6.1.28-alt1.rt10
- Rebase onto v6.1.28-rt10 (2023-05-15) with std-def configs.

* Sat Mar 25 2023 Kernel Bot <kernelbot@altlinux.org> 5.10.176-alt1.rt86
- v5.10.176-rt86 (2023-03-24).

* Mon Mar 20 2023 Kernel Bot <kernelbot@altlinux.org> 5.10.175-alt1.rt84
- v5.10.175-rt84 (2023-03-19).

* Sun Feb 19 2023 Kernel Bot <kernelbot@altlinux.org> 5.10.168-alt1.rt83
- v5.10.168-rt83 (2023-02-18).

* Tue Jan 31 2023 Kernel Bot <kernelbot@altlinux.org> 5.10.165-alt1.rt81
- v5.10.165-rt81 (2023-01-30).

* Thu Jan 26 2023 Kernel Bot <kernelbot@altlinux.org> 5.10.162-alt1.rt79
- v5.10.162-rt79 (2023-01-26).
- Enable xtables modules (ALT#44829).

* Mon Jan 16 2023 Kernel Bot <kernelbot@altlinux.org> 5.10.162-alt1.rt78
- v5.10.162-rt78 (2023-01-04).

* Fri Dec 09 2022 Kernel Bot <kernelbot@altlinux.org> 5.10.158-alt1.rt77
- v5.10.158-rt77 (2022-12-08).

* Sat Nov 05 2022 Kernel Bot <kernelbot@altlinux.org> 5.10.153-alt1.rt76
- v5.10.153-rt76 (2022-11-04).

* Mon Oct 31 2022 Kernel Bot <kernelbot@altlinux.org> 5.10.152-alt1.rt75
- v5.10.152-rt75 (2022-10-30).
- config-rt: Enable ZRAM=m (ALT#40762).

* Tue Sep 27 2022 Kernel Bot <kernelbot@altlinux.org> 5.10.145-alt1.rt74
- v5.10.145-rt74 (2022-09-23).

* Mon Sep 19 2022 Kernel Bot <kernelbot@altlinux.org> 5.10.140-alt1.rt73
- v5.10.140-rt73 (2022-09-03).

* Fri Aug 12 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.131-alt2.rt72
- config: CONFIG_R8188EU=m.

* Sun Jul 17 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.131-alt1.rt72
- Update to v5.10.131-rt72 (2022-07-15).

* Sun Jun 12 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.120-alt1.rt70
- Update to v5.10.120-rt70 (2022-06-10).

* Tue May 17 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.115-alt1.rt67
- Update to v5.10.115-rt67 (2022-05-12).

* Fri Apr 08 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.109-alt1.rt65
- Update to v5.10.109-rt65 (2022-04-07).

* Thu Mar 17 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.106-alt1.rt64
- Update to v5.10.106-rt64 (2022-03-16).

* Fri Mar 11 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.104-alt1.rt63
- Update to v5.10.104-rt63 (2022-03-09). (Fixes CVE-2022-0847).

* Sun Feb 13 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.100-alt1.rt62
- Update to v5.10.100-rt62 (2022-02-11).

* Fri Feb 11 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.90-alt1.rt61
- Update to v5.10.90-rt61 (2022-02-11).

* Sun Jan 09 2022 Vitaly Chikunov <vt@altlinux.org> 5.10.90-alt1.rt60
- Updated to v5.10.90-rt60 (2022-01-05).
- spec: Disable GCC plugins and GCC version dependence. Remove dependence
  on gcc and libelf-devel for kernel-headers-modules.

* Fri Dec 24 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.87-alt1.rt59
- Updated to v5.10.87-rt59 (2021-12-19).

* Thu Dec 02 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.78-alt1.rt56
- Update to v5.10.78-rt56 (2021-11-29).

* Sun Oct 17 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.73-alt1.rt54
- Update to v5.10.73-rt54 (2021-10-15).

* Mon Sep 20 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.65-alt1.rt53
- Update to v5.10.65-rt53 (2021-09-17).

* Thu Sep 02 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.59-alt1.rt52
- Update to v5.10.59-rt52 (2021-08-25).

* Mon Aug 09 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.56-alt1.rt48
- Update to v5.10.56-rt48 (2021-08-06).
- Enable modules signing.

* Tue Aug 03 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.10.52-alt2.rt47
- Bumped release to pesign with new key.

* Wed Jul 28 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.52-alt1.rt47
- Update to v5.10.52-rt47 (2021-07-23).

* Sun Jul 18 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.47-alt1.rt46
- Update to v5.10.47-rt46 (16 Jul 2021).
- spec: Remove BuildRequires: dev86.

* Wed Jul 07 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.47-alt1.rt45
- Update to v5.10.47-rt45 (02 Jul 2021).
- Remove startup from Requires.
- spec: Change way LTP is run.

* Thu Jun 10 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.41-alt1.rt42
- Update to v5.10.41-rt42 (04 Jun 2021)
- spec: Run LTP tests in %%check.

* Wed May 26 2021 Vitaly Chikunov <vt@altlinux.org> 5.10.35-alt1.rt39
- Update to v5.10.35-rt39 (12 May 2021).

* Thu May 06 2021 Vitaly Chikunov <vt@altlinux.org> 4.19.189-alt1.rt78
- Update to v4.19.189-rt78 (28 Apr 2021).

* Tue Apr 06 2021 Vitaly Chikunov <vt@altlinux.org> 4.19.184-alt1.rt75
- Update to v4.19.184-rt75 (02 Apr 2021).

* Sat Mar 13 2021 Vitaly Chikunov <vt@altlinux.org> 4.19.180-alt1.rt73
- Update to v4.19.180-rt73 (12 Mar 2021).

* Wed Feb 10 2021 Vitaly Chikunov <vt@altlinux.org> 4.19.173-alt1.rt72
- Update to v4.19.173-rt72 (08 Feb 2021).

* Mon Jan 25 2021 Vitaly Chikunov <vt@altlinux.org> 4.19.165-alt1.rt70
- Update to v4.19.165-rt70 (08 Jan 2021).

* Fri Nov 27 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.160-alt1.rt69
- Update to v4.19.160-rt69 (25 Nov 2020).

* Sun Nov 08 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.152-alt1.rt65
- Update to v4.19.152-rt65 (30 Oct 2020).

* Sun Oct 04 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.148-alt1.rt64
- Update to v4.19.148-rt64 (02 Oct 2020).
- config: Enable some options.

* Sun Sep 06 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.142-alt1.rt63
- Update to v4.19.142-rt63 (03 Sep 2020).

* Sat Aug 29 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.135-alt1.rt61
- Update to v4.19.135-rt61 (28 Aug 2020).

* Fri Aug 07 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.135-alt1.rt60
- Update to v4.19.135-rt60 (03 Aug 2020).

* Wed Jul 15 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.132-alt1.rt59
- Update to v4.19.132-rt59 (14 Jul 2020).

* Tue Jul 07 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.127-alt2.rt55
- Rebuild with debuginfo package.

* Wed Jul 01 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.127-alt1.rt55
- Update to v4.19.127-rt55 (22 Jun 2020).

* Mon Jun 15 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.127-alt1.rt54
- Update to 4.19.127-rt54 (08 Jun 2020).

* Sat May 23 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.124-alt1.rt53
- Update to 4.19.124-rt53.

* Thu May 07 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.120-alt1.rt52
- Update to 4.19.120-rt52.

* Tue May 05 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.115-alt1.rt50
- Update to 4.19.115-rt50.

* Tue Apr 28 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.115-alt1.rt49
- Update to 4.19.115-rt49.

* Fri Apr 17 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.115-alt1.rt48
- Update to 4.19.115-rt48.
- Add more BPF options, enable IKCONFIG, IKHEADERS.

* Tue Apr 07 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.106-alt1.rt46
- Update to 4.19.106-rt46.

* Sat Mar 28 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.106-alt1.rt45
- Update to 4.19.106-rt45.

* Mon Mar 02 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.106-alt1.rt44
- Update to 4.19.106-rt44.

* Wed Feb 26 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.103-alt1.rt42
- Update to v4.19.103-rt42.
- Make ATA modules built-in (for qemu -hda).

* Tue Feb 11 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.100-alt1.rt41
- Update to v4.19.100-rt41.

* Thu Jan 09 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.90-alt1.rt35
- Update to v4.19.90-rt35.

* Sun Nov 24 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt8.rt24
- Add some more std-def =y options.

* Mon Nov 18 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt7.rt24
- Add CONFIG_USER_NS=y.

* Mon Oct 14 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt6.rt24
- Add xz support squashfs (for propagator).

* Thu Sep 19 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt5.rt24
- Enable virtio_scsi module.

* Sun Sep 08 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt4.rt24
- Add two OSADL patches for debug purposes:
  + tracing: Add latency histograms
  + Provide individual CPU usage measurement based on idle time
- Enable performance scaling governor by default and disable powersave.
- Disable multiple debug options.

* Sat Sep 07 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt3.rt24
- Add more performance (disable NO HZ) and tracing options.

* Fri Sep 06 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt2.rt24
- Enable EFI handover support.

* Thu Sep 05 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt1.rt24
- Initial build of PREEMPT_RT kernel.
