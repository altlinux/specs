%def_disable check

Name: kernel-image-rocknix
Release: alt1
epoch:1
%define kernel_need_version	6.18
# Used when kernel-source-x.y does not currently exist in repository.
%define kernel_base_version	6.18
%define kernel_sublevel .35
%define kernel_extra_version	%nil
# kernel version is need version
Version: %kernel_need_version%kernel_sublevel%kernel_extra_version
# Numeric extra version scheme developed by Alexander Bokovoy:
# 0.0.X -- preX
# 0.X.0 -- rcX
# 1.0.0 -- release
%define kernel_extra_version_numeric 0

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	%__gcc_version_base

%def_disable docs

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
# https://xff.cz/git/linux
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

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
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric
BuildRequires: module-init-tools >= 3.16
BuildRequires: lzma-utils
BuildRequires: libelf-devel
BuildRequires: bc
BuildRequires: rsync
BuildRequires: openssl openssl-devel
BuildRequires: python3
# for check
%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system-%qemu_pkg-core ipxe-roms-qemu glibc-devel-static}}

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
Requires(pre): u-boot-tools

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
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -p1

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

chmod +x tools/objtool/sync-check.sh

%build
mkdir .bin
ln -s /bin/true .bin/git
export PATH="$PWD/.bin:$PATH"
export ARCH=%base_arch
export NPROCS=%__nprocs
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper

#configuration construction

CONFIGS="config-%_target_cpu"

scripts/kconfig/merge_config.sh -m $CONFIGS

%make_build oldconfig
%make_build %make_target V=1
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

install -Dp -m644 .config %buildroot/boot/config-$KernelVer

make modules_install INSTALL_MOD_PATH=%buildroot

make dtbs_install INSTALL_DTBS_PATH=%buildroot/boot/devicetree/$KernelVer
mkdir -p %buildroot/lib/devicetree
ln -s /boot/devicetree/$KernelVer %buildroot/lib/devicetree/$KernelVer

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
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin,builtin.alias}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin,builtin.alias}.bin
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
/boot/devicetree/%kversion-%flavour-%krelease
%dir %modules_dir/
%defattr(0600,root,root,0700)
%modules_dir/*
%exclude %modules_dir/build
%ghost %modules_dir/modules.alias.bin
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols.bin
%ghost %modules_dir/modules.builtin.bin
%ghost %modules_dir/modules.builtin.alias.bin
/lib/devicetree/%kversion-%flavour-%krelease

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
* Wed Jun 10 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.35-alt1
- 6.18.35

* Tue Jun 02 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.34-alt1
- 6.18.34

* Mon May 25 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.33-alt1
- 6.18.33

* Mon May 18 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.32-alt1
- 6.18.32

* Thu May 14 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.30-alt1
- 6.18.30

* Tue May 12 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.29-alt1
- 6.18.29

* Fri May 08 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.27-alt1
- 6.18.27
- config-aarch64: CONFIG_DRM_PANEL_SAMSUNG_SOFEF00=y, CONFIG_DRM_PANEL_SAMSUNG_S6E3FC2X01=y, CONFIG_RMI4_I2C=m

* Tue Apr 28 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.25-alt1
- 6.18.25

* Thu Apr 23 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.24-alt1
- 6.18.24

* Sun Apr 19 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.23-alt1
- 6.18.23

* Sat Apr 11 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.22-alt1
- 6.18.22

* Fri Apr 03 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.21-alt1
- 6.18.21

* Thu Mar 26 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.20-alt1
- 6.18.20

* Fri Mar 20 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.19-alt1
- 6.18.19

* Mon Mar 16 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.18-alt1
- 6.18.18

* Thu Mar 05 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.16-alt1
- 6.18.16

* Mon Mar 02 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.15-alt1
- 6.18.15

* Fri Feb 27 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.14-alt1
- 6.18.14

* Fri Feb 20 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.13-alt1
- 6.18.13

* Thu Feb 19 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.12-alt2
- config-aarch64: CONFIG_DRM_PANEL_RAYDIUM_RM692E5=y

* Tue Feb 17 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.12-alt1
- 6.18.12

* Thu Feb 12 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.10-alt1
- 6.18.10

* Mon Feb 09 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.9-alt1
- 6.18.9

* Mon Feb 02 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.8-alt1
- 6.18.8

* Sun Jan 25 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.7-alt1
- 6.18.7

* Mon Jan 19 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.6-alt1
- 6.18.6

* Mon Jan 12 2026 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.5-alt1
- 6.18.5

* Fri Dec 19 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.2-alt1
- 6.18.2

* Mon Dec 15 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.1-alt1
- 6.18.1

* Mon Dec 01 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.18.0-alt1
- 6.18

* Mon Nov 24 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.17.9-alt1
- 6.17.9

* Fri Nov 14 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.17.8-alt1
- 6.17.8

* Wed Nov 05 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.17.7-alt1
- 6.17.7

* Tue Oct 21 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.17.4-alt1
- 6.17.4

* Mon Oct 13 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.12-alt1
- 6.16.12

* Mon Oct 06 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.11-alt1
- 6.16.11

* Sun Oct 05 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.10-alt1
- 6.16.10

* Thu Sep 25 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.9-alt1
- 6.16.9

* Tue Sep 23 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.8-alt1
- 6.16.8

* Fri Sep 12 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.7-alt1
- 6.16.7

* Wed Sep 10 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.6-alt1
- 6.16.6

* Fri Sep 05 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.5-alt1
- 6.16.5

* Tue Sep 02 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.4-alt1
- 6.16.4

* Tue Sep 02 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.16.3-alt1
- 6.16.3

* Thu Aug 28 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.11-alt2
- fixed wifi on retroid pocket

* Thu Aug 21 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.11-alt1
- 6.15.11

* Mon Aug 18 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.10-alt1
- 6.15.10

* Mon Aug 04 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.9-alt1
- 6.15.9

* Wed Jul 30 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.8-alt4
- config-aarch64: CONFIG_JOYSTICK_ROCKNIX=m

* Mon Jul 28 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.8-alt3
- config-aarch64: CONFIG_JOYSTICK_RETROID=y

* Mon Jul 28 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.8-alt2
- update config for SM8250

* Thu Jul 24 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.8-alt1
- 6.15.8

* Wed Jul 23 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.7-alt1
- 6.15.7

* Tue Jul 15 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.6-alt1
- 6.15.6

* Mon Jul 07 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.5-alt1
- 6.15.5

* Mon Jun 30 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.4-alt1
- 6.15.4

* Fri Jun 20 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.3-alt1
- 6.15.3

* Wed Jun 11 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.2-alt2
- dts: rk3399: fixed dmc opp table

* Wed Jun 11 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.2-alt1
- 6.15.2

* Thu Jun 05 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.1-alt1
- 6.15.1

* Tue May 27 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.15.0-alt1
- 6.15

* Mon Apr 07 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:6.12.22-alt1
- 6.12.22

* Wed Nov 06 2024 Valery Inozemtsev <shrek@altlinux.ru> 1:6.8.12-alt2
- add chassis type in DTS of Anbernic and Powkiddy (closes: #51967)

* Thu Oct 03 2024 Valery Inozemtsev <shrek@altlinux.ru> 1:6.8.12-alt1
- 6.8.12

* Wed May 29 2024 Valery Inozemtsev <shrek@altlinux.ru> 1:6.8.11-alt1
- 6.8.11

* Wed May 22 2024 Valery Inozemtsev <shrek@altlinux.ru> 1:6.8.10-alt1
- 6.8.10
