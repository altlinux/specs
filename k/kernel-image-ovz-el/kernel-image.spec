Name: kernel-image-ovz-el
Version: 2.6.32
Release: alt73

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
%define kgcc_version	4.4

# Enable/disable several parts of kernel
%def_disable docs
%def_disable oss
%def_enable kvm
%def_enable v4l
%def_enable staging

## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware
Url: http://wiki.openvz.org/Download/kernel/
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: %name-%version-%release.patch

ExclusiveArch: i586 x86_64

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric
BuildRequires: module-init-tools >= 3.1
BuildRequires: lzma-utils
Provides: kernel-modules-eeepc-%flavour

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

The "ovz-el" variant of kernel packages is a RHEL6 based OpenVZ kernel.
OpenVZ is container-based virtualization for Linux that creates multiple
secure, isolated containers on a single physical server enabling better
server utilization and ensuring that applications do not conflict.

%package -n kernel-image-domU-%flavour
Summary: Uncompressed linux kernel for XEN domU boot
Group: System/Kernel and hardware
Prereq: coreutils
Prereq: module-init-tools >= 3.1

%description -n kernel-image-domU-%flavour
Most XEN virtualization system versions can not boot lzma-compressed
kernel images. This is an optional package with uncompressed linux
kernel image for this special case. If you do not know what is it XEN
it seems that you do not need this package.

%package -n kernel-modules-oss-%flavour
Summary: OSS sound driver modules (obsolete)
Group: System/Kernel and hardware
Provides:  kernel-modules-oss-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-oss-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-oss-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %version-%release
Requires(postun): %name = %version-%release

%description -n kernel-modules-oss-%flavour
This package contains OSS sound driver modules for the Linux kernel
package %name-%version-%release.

These drivers are declared obsolete by the kernel maintainers; ALSA
drivers should be used instead.  However, the older OSS drivers may be
still useful for some hardware, if the corresponding ALSA drivers do
not work well.

Install this package only if you really need it.

%package -n kernel-modules-ide-%flavour
Summary: IDE  driver modules (obsolete by PATA)
Group: System/Kernel and hardware
Provides:  kernel-modules-ide-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-ide-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-ide-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %version-%release
Requires(postun): %name = %version-%release

%description -n kernel-modules-ide-%flavour
This package contains  IDE driver modules for the Linux kernel
package %name-%version-%release.

These drivers are declared obsolete by the kernel maintainers; PATA
drivers should be used instead.  However, the older IDE drivers may be
still useful for some hardware, if the corresponding PATA drivers do
not work well.

Install this package only if you really need it.

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

%package -n kernel-modules-drm-nouveau-%flavour
Summary: The Direct Rendering Infrastructure modules for NVIDIA cards
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-nouveau-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-nouveau-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-nouveau-%kversion-%flavour-%krelease > %version-%release
Requires: kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %version-%release
Requires(postun): %name = %version-%release

%package -n kernel-modules-drm-radeon-%flavour
Summary: The Direct Rendering Infrastructure modules for ATI cards
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-radeon-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-radeon-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-radeon-%kversion-%flavour-%krelease > %version-%release
Requires: kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
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

These are modules for your ALT Linux system

%description -n kernel-modules-drm-nouveau-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.

These are modules for your ALT Linux system

%description -n kernel-modules-drm-radeon-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.

These are modules for your ALT Linux system

%if_enabled kvm
%package -n kernel-modules-kvm-%flavour
Summary: Linux KVM (Kernel Virtual Machine) modules
Group: System/Kernel and hardware
Provides:  kernel-modules-kvm-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-kvm-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-kvm-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %version-%release
Requires(postun): %name = %version-%release

%description -n kernel-modules-kvm-%flavour
Linux kernel module for Kernel Virtual Machine virtualization
environment.
%endif

%if_enabled v4l
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
%endif

%if_enabled staging
%package -n kernel-modules-staging-%flavour
Summary:  Kernel modules under development
Group: System/Kernel and hardware
Provides:  kernel-modules-staging-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-staging-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-staging-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %version-%release
Requires(postun): %name = %version-%release

%description -n kernel-modules-staging-%flavour
Drivers and filesystems that are not ready to be merged into the main
portion of the Linux kernel tree at this point in time for various
technical reasons.
%endif

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
#Requires: kernel-headers-alsa

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
tar -jxf %kernel_src/kernel-source-%kernel_base_version.tar.bz2
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -p1

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

echo "Building Kernel $KernelVer"

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
install -Dp -m644 vmlinux %buildroot/boot/vmlinux-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

make modules_install INSTALL_MOD_PATH=%buildroot INSTALL_FW_PATH=%buildroot/lib/firmware/$KernelVer


mkdir -p %buildroot%kbuild_dir/arch/x86
install -d %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir/include
cp -a arch/x86/include %buildroot%kbuild_dir/arch/x86

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
	scripts/basic/hash
	scripts/extract-ikconfig
	scripts/conmakehash
	scripts/checkversion.pl
	scripts/checkincludes.pl
	scripts/checkconfig.pl
	scripts/bin2c
	scripts/gcc-version.sh
	scripts/recordmcount.pl
%ifarch i586
	scripts/gcc-x86_32-has-stack-protector.sh
%else
%ifarch x86_64
	scripts/gcc-x86_64-has-stack-protector.sh
%endif
%endif
	scripts/module-common.lds

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
make headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir
find %buildroot%kheaders_dir -name '.*.cmd' -o -name '.install' | xargs rm -f

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%base_flavour-%version/
cp -a Documentation/* %buildroot%_docdir/kernel-doc-%base_flavour-%version/
find %buildroot%_docdir/kernel-doc-%base_flavour-%version/DocBook \
	-maxdepth 1 -type f -not -name '*.html' -delete
%endif # if_enabled docs

#remove video headers
#rm -rf %buildroot%kbuild_dir/include/media
#rm -rf %buildroot%kbuild_dir/drivers/media
#rm -fr %buildroot%kbuild_dir/include/linux/video{_decoder,dev,dev2}.h

%post -n kernel-modules-oss-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-oss-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease

%post -n kernel-modules-ide-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-ide-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease

%post -n kernel-modules-drm-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-drm-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease

%post -n kernel-modules-drm-nouveau-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-drm-nouveau-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease

%post -n kernel-modules-drm-radeon-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-drm-radeon-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease

%if_enabled kvm
%post -n kernel-modules-kvm-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-kvm-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease
%endif

%if_enabled v4l
%post -n kernel-modules-v4l-%flavour
%post_kernel_modules %kversion-%flavour-%krelease

%postun -n kernel-modules-v4l-%flavour
%postun_kernel_modules %kversion-%flavour-%krelease
%endif

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
%if_enabled v4l
%exclude %modules_dir/kernel/drivers/media/
%endif
%if_enabled staging
%exclude %modules_dir/kernel/drivers/staging/
%endif
%exclude %modules_dir/kernel/drivers/gpu/drm
%if_enabled kvm
%exclude %modules_dir/kernel/arch/x86/kvm
%endif
%exclude %modules_dir/kernel/drivers/ide/
/lib/firmware/*

%files -n kernel-image-domU-%flavour
/boot/vmlinux-%kversion-%flavour-%krelease

%if_enabled oss
%exclude %modules_dir/kernel/sound/oss

%files -n kernel-modules-oss-%flavour
%modules_dir/kernel/sound/oss
%endif #oss

%files -n kernel-modules-ide-%flavour
%modules_dir/kernel/drivers/ide/

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
%if_enabled oss
%exclude %modules_dir/kernel/sound/oss
%endif

%files -n kernel-modules-drm-%flavour
%modules_dir/kernel/drivers/gpu/drm
%exclude %modules_dir/kernel/drivers/gpu/drm/nouveau
%exclude %modules_dir/kernel/drivers/gpu/drm/radeon

%files -n kernel-modules-drm-nouveau-%flavour
%modules_dir/kernel/drivers/gpu/drm/nouveau

%files -n kernel-modules-drm-radeon-%flavour
%modules_dir/kernel/drivers/gpu/drm/radeon

%if_enabled kvm
%files -n kernel-modules-kvm-%flavour
%modules_dir/kernel/arch/x86/kvm
%endif # kvm

%if_enabled v4l
%files -n kernel-modules-v4l-%flavour
%modules_dir/kernel/drivers/media/
%endif # v4l

%if_enabled staging
%files -n kernel-modules-staging-%flavour
%modules_dir/kernel/drivers/staging/
%endif # staging

%changelog
* Sun Jul 29 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt73
- Update to 042stab059.7

* Tue Jul 24 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt72
- Update to 042stab059.4

* Wed Jun 27 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt71
- Update to 042stab057.1

* Mon Jun 11 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt70
- Update to 042stab056.11
- Disable CONFIG_MULTICORE_RAID456 (ALT 27399)

* Sun Jun 03 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt69
- Update to 042stab056.8
- Change URL to a more appropriate (ALT 27389)
- Remove xtables-addons from modules list

* Tue May 29 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt68
- Update to 042stab056.5

* Thu May 24 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt67
- Enable devtmpfs

* Thu May 24 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt66
- Update to 042stab056.2

* Mon May 21 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt65
- Update to 042stab055.11

* Mon May 14 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt64
- Update to 042stab055.10

* Fri May 04 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt63
- Update to 042stab055.7

* Thu May 03 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt62
- Update to 042stab055.6

* Wed May 02 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt61
- Update to 042stab055.4

* Thu Apr 12 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt60
- Update to 042stab054.3

* Thu Apr 05 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt59
- Update to 042stab054.2

* Thu Apr 05 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt58
- Update to 042stab054.1

* Tue Mar 27 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt57
- Update to 042stab053.4

* Fri Mar 23 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt56
- Update to 042stab053.3

* Thu Mar 15 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt55
- Update to 042stab052.8
- new ploop block device

* Mon Feb 27 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt54
- Update to 042stab051.3

* Mon Feb 20 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt53
- Update to 042stab051.2

* Mon Feb 13 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt52
- Update to 042stab051.1

* Fri Feb 03 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt51
- Update to 042stab049.5

* Thu Jan 26 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt50
- Update to 042stab049.2

* Mon Jan 23 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt49
- Update to 042stab048.1

* Fri Jan 20 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt48
- proc: clean up and fix /proc/<pid>/mem handling (CVE-2012-0056)

* Fri Jan 13 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt47
- Update to 042stab046.1

* Sun Dec 18 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt46
- Update to 042stab045.1

* Tue Dec 13 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt45
- Update to 042stab044.9

* Mon Dec 05 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt44
- Update to 042stab044.5

* Thu Nov 24 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt43
- Update to 042stab044.1

* Fri Nov 11 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt42
- Update to 042stab042.1
- Triple Answer to the Ultimate Question of Life, the Universe,
  and Everything

* Thu Nov 10 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt41
- Update to 042stab040.1

* Thu Nov 03 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt40
- Update to 042stab039.10

* Thu Oct 20 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt39
- Update to 042stab039.5

* Wed Oct 12 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt38
- Update to 042stab039.3

* Fri Oct 07 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt37
- Update to 042stab039.2

* Thu Oct 06 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt36
- Update to 042stab039.1

* Mon Sep 19 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt35
- Update to 042stab037.1
- Add support to ipset version 6

* Thu Sep 15 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt34
- Update to 042stab036.6
- Enable several ide chipsets (ALT 26229)

* Wed Sep 14 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt33
- Build ocfs2 filesystem

* Mon Sep 05 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt32
- Update to stable 042stab036.1 kernel
- Remove ipset

* Thu Aug 04 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt31
- Update to 042stab025.1 kernel
- Enable several scsi drivers (ALT 25978)

* Wed Jul 27 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt30
- Update to 042stab024.1 kernel

* Mon Jul 25 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt29
- Update to 042stab023.1 kernel

* Fri Jul 22 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt28
- Update to 042stab022.1 kernel

* Thu Jul 14 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt27
- Update to 042stab021.1 kernel
- Build staging drivers

* Fri Jul 08 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt26
- Update to 042stab020.1 kernel
- Enable BLK_DEV_THROTTLING (ALT 25836)
- Add ipt-netflow to modules.build

* Mon Jun 20 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt25
- Apply 042stab018.1 patches

* Fri Jun 10 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt24
- Apply 042stab017.1 patches

* Tue Jun 07 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt23
- Apply 042stab016.1 patches

* Thu Jun 02 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt22
- Apply 042stab015.1 patches

* Fri May 27 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt21
- Apply 042stab014.1 patches

* Thu May 26 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt20
- Apply 042stab013.1 patches

* Thu May 19 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt19
- Apply 042test012.1 patches
- Fixed description for kernel-modules-drm-radeon (ALT 25557)

* Thu May 12 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt18
- Apply 042test012.1 patches

* Tue May 10 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt17
- Apply 042test011.1 patches

* Thu Apr 21 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt16
- VZDQUOTA: downgrade quota revision from 1 to 0 for quota version 2
  (ALT #25432, #25056)

* Mon Apr 11 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt15
- Build reiserfs module (ALT 25390)
- Build dm-multipath.ko

* Thu Mar 31 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt14
- don't pack unnecessary files in kernel-headers-*
- Build kernel-doc-* as noarch package [but actually we don't build docs]
- Pack radeon.ko and nouveau.ko into separate packages (ALT 25299)
- Enable xen support, build kernel-image-domU-ovz-el (ALT 25288)
- Enable MOXA_INTELLIO and MOXA_SMARTIO (ALT 25287)
- Apply lost (due to merge conflicts) part of ALT syslog patch
- Compile schedulers in
- Enable PRINTK_TIME

* Sun Mar 06 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt13
- Enable suspend and hibernate
- Enable /dev/psaux
- Apply 042test008.1 patches

* Mon Feb 28 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt12
- Build e1000e as an external module
- Change package description
- apply patch from 1778 vz bug

* Sat Feb 12 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt11
- VE: shutrown environment only if pid ns child reaper is VE init
  (by Stanislav Kinsbursky, see vz bug #1773)
- Apply 042test007.1 patches
- Backport 729a6a30 from mainline, see ALT #25055

* Thu Feb 03 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt10
- mm: check mm in __vm_enough_memory() (ALT #25000)
- Check return value of crypto_alloc_shash() right
- fix jiffies location
- Fix some differences between i586 and x86_64 configs
- build a lot of stuff as modules
- Do not build snd_pcsp.ko
- Add drbd83 to modules.build
- Remove KALLSYMS_{ALL,EXTRA_PASS}
- Enable IKCONFIG and IKCONFIG_PROC

* Fri Jan 21 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt9
- Apply 042test006.1 patches
- Build kernel-modules-v4l-ovz-el as a separate package

* Mon Jan 17 2011 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt8
- Changes to configs
- ptrace: return virtual pid in events by Andrey Vagin (ALT 24829)
- fix NULL dereference in nfsd_statfs (ALT 24873)

* Thu Dec 30 2010 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt7
- Switch to new scheme of merging with the latest kernel
- Apply 042test005.1 patches

* Fri Dec 24 2010 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt6
- ALT and ovz specific syslog patch (ALT 24807)
- cgroupfs: create /sys/fs/cgroup to mount cgroupfs on (ALT 24809)

* Fri Dec 17 2010 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt5
- The Return Of The i586

* Tue Dec 07 2010 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt4
- Apply 042test003.1 patches
- Fix build without CONFIG_VZ_FAIRSCHED
- Remove xen from config
- Run oldconfig on x86_64
- Add modules.build
- Don't build i586 kernel anymore

* Mon Nov 29 2010 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt3
- Remove %post and %preun scripts for kernel-image
- Apply 042test002.1 patches
- Replace config files with el ones

* Mon Nov 01 2010 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt2
- Build with gcc4.4
- Don't panic when booting on i586 (OpenVZ bug 1681)

* Tue Oct 19 2010 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt1
- Build for Sysiphus
