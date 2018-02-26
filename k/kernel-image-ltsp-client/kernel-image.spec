Name: kernel-image-ltsp-client
Version: 2.6.32
Release: alt4

%define kernel_stable_version 59
%define kernel_base_version	%version
%define kernel_extra_version	%nil
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
%define kgcc_version	4.5

%def_disable docs
%def_disable v4l

## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware

Url: http://www.altlinux.org/LTSP
Packager: Michael Shigorin <mike@altlinux.org>

Source1: config-i586
Patch0: linux-%kernel_base_version.%kernel_stable_version.patch
# from led@'s opensuse-based 2.6.32
Patch10: linux-%kernel_base_version.13-fix-mm--page.patch
Patch11: linux-%kernel_base_version.45-feat-net-swap.patch
Patch20: linux-%kernel_base_version.13-feat-mm-swapfile--notify.patch
Patch21: linux-%kernel_base_version.13-feat-drivers-block--ramzswap.patch
Patch30: linux-%kernel_base_version.58-feat-drivers-gpu--35.patch
Patch31: linux-%kernel_base_version.11-feat-lib--list_sort.patch
Patch32: linux-%kernel_base_version.26-fix-mm--pageattr.patch

# x86_64 thin clients should use std-def or whatever suits
ExclusiveArch: i586
ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric
BuildRequires: module-init-tools >= 3.1

%if_enabled docs
BuildRequires: xmlto transfig ghostscript
%endif

%if_enabled ccache
BuildRequires: ccache
%endif

%ifdef use_ccache
BuildRequires: ccache
%endif

Requires: bootloader-utils >= 0.4.9-alt1
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.8.3-alt1

Provides: kernel = %kversion

Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: mkinitrd >= 1:2.9.9-alt1

%description
This package contains the Linux kernel that is used to boot and run
your system.

Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).

The "ltsp-client" flavour of kernel packages is almost vanilla kernel
adding swap-over-net patch by Peter Zijlstra to fix networked swap
issues.

It's trimmed down towards diskless network-bootable thin clients
(e.g. ALTSP) and is rather unsuitable for anything else.

See also http://www.altlinux.org/LTSP

%package -n kernel-modules-alsa-%flavour
Summary: The Advanced Linux Sound Architecture modules
Group: System/Kernel and hardware
Provides:  kernel-modules-alsa-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-alsa-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-alsa-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %version-%release
Requires(postun): %name = %version-%release

%description -n kernel-modules-alsa-%flavour
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system. ALSA has the following
significant features:
1. Efficient support for all types of audio interfaces, from consumer
soundcards to professional multichannel audio interfaces.
2. Fully modularized sound drivers.
3. SMP and thread-safe design.
4. User space library (alsa-lib) to simplify application programming
and provide higher level functionality.
5. Support for the older OSS API, providing binary compatibility for
most OSS programs.

These are sound drivers for your ALT Linux system.

%package -n kernel-modules-drm-%flavour
Summary: The Direct Rendering Infrastructure modules
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %version-%release
Requires(postun): %name = %version-%release

%description -n kernel-modules-drm-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.

These are DRM modules for your ALT Linux system.

%package -n kernel-modules-v4l-%flavour
Summary: Video4Linux driver modules (obsolete)
Group: System/Kernel and hardware
Provides:  kernel-modules-v4l-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-v4l-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-v4l-%kversion-%flavour-%krelease > %version-%release
Provides:  kernel-modules-uvcvideo-%kversion-%flavour-%krelease = %version-%release
Provides:  kernel-modules-gspca-%kversion-%flavour-%krelease = %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %version-%release
Requires(postun): %name = %version-%release

%description -n kernel-modules-v4l-%flavour
Video for linux drivers

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).

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
tar -jxf %kernel_src/kernel-source-%kernel_base_version.tar.bz2
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -p1
%patch10 -p1
%patch11 -p1
%patch20 -p1
%patch21 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1

install -m644 %SOURCE1 .

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

%build
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

echo "Building kernel $KernelVer"

%make_build mrproper

cp -vf config-%_target_cpu .config

%make_build oldconfig
%make_build include/linux/version.h
%make_build bzImage
%make_build modules

echo "Kernel built $KernelVer"

%if_enabled docs
# psdocs, pdfdocs don't work yet
%make_build htmldocs
%endif

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 arch/%base_arch/boot/bzImage \
	%buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

make modules_install INSTALL_MOD_PATH=%buildroot INSTALL_FW_PATH=%buildroot/lib/firmware/$KernelVer

install -d %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir/include

# remove asm-* include files for other architectures
pushd %buildroot%kbuild_dir/include
for dir in asm-*; do
	[ "$dir" = "asm-generic" ] && continue
	[ "$dir" = "asm-x86" ] && continue
	rm -rf -- "$dir"
done
%ifarch x86_64
ln -s asm-x86 asm-x86_64
%else
%ifarch i586
ln -s asm-x86 asm-i386
%endif
%endif
popd

# drivers-headers install
install -d %buildroot%kbuild_dir/drivers/scsi
install -d %buildroot%kbuild_dir/drivers/md
install -d %buildroot%kbuild_dir/drivers/usb/core
install -d %buildroot%kbuild_dir/drivers/net/wireless
install -d %buildroot%kbuild_dir/net/mac80211
install -d %buildroot%kbuild_dir/kernel
install -d %buildroot%kbuild_dir/lib
cp -a drivers/scsi/{{scsi,scsi_typedefs}.h,scsi_module.c} \
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
	arch/x86/Makefile
	arch/x86/Makefile_32
	arch/x86/Makefile_32.cpu
%ifarch x86_64
	arch/x86/Makefile_64
%endif

	scripts/pnmtologo
	scripts/mod/modpost
	scripts/mkmakefile
	scripts/mkversion
	scripts/mod/mk_elfconfig
	scripts/kconfig/conf
	scripts/mkcompile_h
	scripts/makelst
	scripts/Makefile.modpost
	scripts/Makefile.modinst
	scripts/Makefile.lib
	scripts/Makefile.host
	scripts/Makefile.clean
	scripts/Makefile.build
	scripts/Makefile
	scripts/Kbuild.include
	scripts/kallsyms
	scripts/genksyms/genksyms
	scripts/basic/fixdep
	scripts/extract-ikconfig
	scripts/conmakehash
	scripts/checkversion.pl
	scripts/checkincludes.pl
	scripts/checkconfig.pl
	scripts/bin2c
	scripts/gcc-version.sh

	.config
	.kernelrelease
	gcc_version.inc
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

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%base_flavour-%version/
cp -a Documentation/* %buildroot%_docdir/kernel-doc-%base_flavour-%version/
find %buildroot%_docdir/kernel-doc-%base_flavour-%version/DocBook \
	-maxdepth 1 -type f -not -name '*.html' -delete
%endif # if_enabled docs

# drop firmware
rm -rf %buildroot/lib/firmware
rm -rf %buildroot%kbuild_dir/include/media

%post -n kernel-modules-drm-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-drm-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease

%post -n kernel-modules-v4l-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-v4l-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease

%post -n kernel-modules-alsa-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-alsa-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease

%post -n kernel-headers-%flavour
%post_kernel_headers %kversion-%flavour-%krelease

%postun -n kernel-headers-%flavour
%postun_kernel_headers %kversion-%flavour-%krelease

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
%modules_dir
%exclude %modules_dir/build
%exclude %modules_dir/kernel/sound
%exclude %modules_dir/kernel/drivers/gpu/drm
%if_enabled v4l
%exclude %modules_dir/kernel/drivers/media/
%endif

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build

%if_enabled docs
%files -n kernel-doc-%base_flavour
%doc %_docdir/kernel-doc-%base_flavour-%version
%endif

%files -n kernel-modules-alsa-%flavour
%modules_dir/kernel/sound/

%files -n kernel-modules-drm-%flavour
%modules_dir/kernel/drivers/gpu/drm

%if_enabled v4l
%files -n kernel-modules-v4l-%flavour
%modules_dir/kernel/drivers/media/
%endif

%changelog
* Tue Mar 20 2012 Michael Shigorin <mike@altlinux.org> 2.6.32-alt4
- 2.6.32.59 (thanks, Willy)
- patches:
  + replaced drm33 with 2.6.35 code backport by led@
    with an additional nouveau fixup from 2.6.38
    and a few more useful bits

* Mon Mar 05 2012 Michael Shigorin <mike@altlinux.org> 2.6.32-alt3
- 2.6.32.58
- config-i586:
  + CONFIG_FB_*:
    - dropped all specific drivers
    - enabled uvesafb just in case
    - disabled firmware EDID
  + CONFIG_DRM_*:
    - enabled KMS for radeon by default
    - enabled nouveau and vmwgfx (drm33 staging)
  + a few more staging drivers (usbip, et131x, slicoss)
  + disabled USB HID Boot Protocol drivers (not recommended)
- thanks led@ as usual

* Sun Jan 22 2012 Michael Shigorin <mike@altlinux.org> 2.6.32-alt2
- patches:
  + feat-drivers-block--ramzswap (and feat-mm-swapfile--notify)
- config-i586:
  + io scheduler switched from deadline to noop
  + switch back from CONFIG_PREEMPT to CONFIG_PREEMPT_VOLUNTARY
    (looks like the former doesn't play nice with net-swap
    while the latter does)
- mostly led@'s advice again

* Sat Jan 21 2012 Michael Shigorin <mike@altlinux.org> 2.6.32-alt1
- 2.6.32.54
  + KMS enabled
  + OSS dropped (was disabled by default ever since)
  + patches (huge thanks to led@):
    - swap-over-net
    - drm33
  + built with gcc4.5
- spec based on kernel-image-tmc-tc-2.6.27-alt12 one
