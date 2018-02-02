Name: kernel-image-ovz-el
Epoch: 1
Version: 2.6.32
Release: alt162

%define kernel_base_version	%version
%define kernel_real_version	2.6.32
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
%define nprocs 12

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

%{?brp_strip_none:%brp_strip_none /boot/*}

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware
Url: http://wiki.openvz.org/Download/kernel/
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Source11: config-x86
Source12: config-x86_64
Patch0: patch-042stab126.2-combined
Patch1: %name-%version-%release.patch

ExclusiveArch: i586 i686 x86_64

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version
BuildRequires: kernel-source-%kernel_real_version = %kernel_extra_version_numeric
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

%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system glibc-devel-static}}

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
Prereq: %name = %EVR
Requires(postun): %name = %EVR

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
Prereq: %name = %EVR
Requires(postun): %name = %EVR

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
Prereq: %name = %EVR
Requires(postun): %name = %EVR

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
Provides:  kernel-modules-drm-nouveau-%flavour = %version-%release
Provides:  kernel-modules-drm-nouveau-%kversion-%flavour-%krelease = %version-%release
Provides:  kernel-modules-drm-radeon-%flavour = %version-%release
Provides:  kernel-modules-drm-radeon-%kversion-%flavour-%krelease = %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %EVR
Requires(postun): %name = %EVR

%description -n kernel-modules-drm-%flavour
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
Prereq: %name = %EVR
Requires(postun): %name = %EVR

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
Prereq: %name = %EVR
Requires(postun): %name = %EVR

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
Prereq: %name = %EVR
Requires(postun): %name = %EVR

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
rm -rf kernel-source-%kernel_real_version
tar -xf %kernel_src/kernel-source-%kernel_real_version.tar.*
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_real_version
%patch0 -p1
%patch1 -p1

install -m 0644 %SOURCE11 %SOURCE12 ./

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

%build
[ "%__nprocs" -gt "%nprocs" ] || export NPROCS=%nprocs
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper

cp -vf \
%ifarch %ix86
	config-x86 \
%else
	config-%_target_cpu \
%endif
	.config

%make_build oldconfig

diff -u \
%ifarch %ix86
	config-x86 \
%else
	config-%_target_cpu \
%endif
	.config ||:

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
%ifarch %ix86
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
%ifarch %ix86
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
timeout 600 qemu -no-kvm -kernel %buildroot/boot/vmlinuz-$KernelVer -nographic -append console=ttyS0 -initrd initrd.img > boot.log
grep -q "^$msg" boot.log &&
grep -qE '^(\[ *[0-9]+\.[0-9]+\] *)?(reboot: )?Power down' boot.log || {
	cat >&2 boot.log
	echo >&2 'Marker not found'
	exit 1
}


%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
/lib/firmware/*
%dir %modules_dir/
%defattr(0600,root,root,0700)
%modules_dir/*
%exclude %modules_dir/build
%exclude %modules_dir/kernel/sound/
%if_enabled v4l
%exclude %modules_dir/kernel/drivers/media/
%endif
%if_enabled staging
%exclude %modules_dir/kernel/drivers/staging/
%endif
%exclude %modules_dir/kernel/drivers/gpu/drm/
%if_enabled kvm
%exclude %modules_dir/kernel/arch/x86/kvm/
%endif
%exclude %modules_dir/kernel/drivers/ide/

%files -n kernel-image-domU-%flavour
/boot/vmlinux-%kversion-%flavour-%krelease

%if_enabled oss
%files -n kernel-modules-oss-%flavour
%defattr(0600,root,root,0700)
%modules_dir/kernel/sound/oss/
%endif #oss

%files -n kernel-modules-ide-%flavour
%defattr(0600,root,root,0700)
%modules_dir/kernel/drivers/ide/

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
%files -n kernel-modules-alsa-%flavour
%defattr(0600,root,root,0700)
%modules_dir/kernel/sound/
%if_enabled oss
%exclude %modules_dir/kernel/sound/oss/
%endif

%files -n kernel-modules-drm-%flavour
%defattr(0600,root,root,0700)
%modules_dir/kernel/drivers/gpu/drm/

%if_enabled kvm
%files -n kernel-modules-kvm-%flavour
%defattr(0600,root,root,0700)
%modules_dir/kernel/arch/x86/kvm/
%endif # kvm

%if_enabled v4l
%files -n kernel-modules-v4l-%flavour
%defattr(0600,root,root,0700)
%modules_dir/kernel/drivers/media/
%endif # v4l

%if_enabled staging
%files -n kernel-modules-staging-%flavour
%defattr(0600,root,root,0700)
%modules_dir/kernel/drivers/staging/
%endif # staging

%changelog
* Thu Feb 01 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.6.32-alt162
- Updated to 042stab127.2.
- Changed kernel version back to 2.6.32 and changed version visible
  through vdso(7) to 3.2.0 (ALT#34433).

* Tue Dec 26 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.2.0-alt160
- Backported support of prlimit64 syscall.
- Faked version reported by kernel to fix work of glibc 2.26
  with openvz kernel.

* Thu Dec 21 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt159
- Updated to 042stab126.2.

* Tue Nov 21 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt158
- Updated to 042stab126.1.

* Mon Oct 30 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt157
- Updated to 042stab125.5.

* Tue Sep 26 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt156
- Updated to 042stab125.1.

* Tue Aug 22 2017 Dmitry V. Levin <ldv@altlinux.org> 2.6.32-alt155
- Added %%check like one found in std-def kernels.
- Restricted access to %%modules_dir/ (see #5969).

* Tue Jul 04 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt154
- Updated to 042stab123.9 (Updated fix for CVE-2017-1000364).

* Tue Jun 27 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt153
- Updated to 042stab123.8 (Fixes: CVE-2017-9077 CVE-2017-9076 CVE-2017-9075
  CVE-2017-9074 CVE-2017-8890 CVE-2017-1000364).

* Thu May 18 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt152
- Updated to 042stab123.3.

* Mon Mar 27 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt151
- Updated to 042stab120.20.

* Tue Mar 07 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt150
- Updated to 042stab120.19.

* Thu Feb 09 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt149
- Updated to 042stab120.18.

* Wed Nov 23 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt148
- Updated to 042stab120.11.

* Fri Oct 28 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt147
- Updated to 042stab120.6.

* Wed Oct 26 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt146
- Updated to 042stab120.5.

* Mon Oct 24 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt145
- Updated to 042stab120.3.

* Fri Oct 21 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt144
- Added fix for CVE-2016-5195.

* Tue Oct 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt143
- Updated to 042stab117.16.

* Thu Jun 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt142
- Backported direct firmware loading for compatibility with udev >= 217.

* Fri May 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt141
- Updated to 042stab116.1.

* Wed Mar 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt140
- Updated to 042stab113.21.

* Tue Dec 29 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt139
- Updated to 042stab113.11.

* Wed Dec 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt138
- Updated to 042stab112.15.

* Fri Jul 24 2015 Dmitry V. Levin <ldv@altlinux.org> 2.6.32-alt137
- Backported AT_EMPTY_PATH fixes from 042stab111.1 (closes: #31136).

* Thu Jul 23 2015 Dmitry V. Levin <ldv@altlinux.org> 2.6.32-alt136
- Updated to 042stab108.8 (fixes multiple CVEs).

* Tue Jul 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt135
- Updated to 042stab108.6.

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt134
- Updated to 042stab108.3 (CVE-2015-2925).

* Thu May 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt133
- Updated to 042stab108.2.

* Tue May 05 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt132
- Updated to 042stab108.1.

* Fri Apr 24 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt131
- Updated to 042stab106.6.

* Sat Mar 21 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt130
- Updated to 042stab105.14.
- nfs: backported options support: 'v4.0', 'v4.1', 'vers=4.0',
  'vers=4.1' (ALT#30845).

* Tue Feb 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt129
- Updated to 042stab104.1.

* Thu Jan 29 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt128
- Updated to 042stab103.6.

* Wed Dec 24 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt127
- Updated to 042stab102.9 (ALT#30599).

* Tue Dec 16 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.32-alt126
- Updated to 042stab094.8 (multiple CVEs) (ALT#30487).

* Sun Aug 17 2014 Led <led@altlinux.ru> 2.6.32-alt125
- Update to 042stab093.4

* Thu Jul 24 2014 Led <led@altlinux.ru> 2.6.32-alt124
- Update to 042stab092.3

* Thu Jul 10 2014 Led <led@altlinux.ru> 2.6.32-alt123
- Update to 042stab092.2:
  + CVE-2014-4699

* Wed Jun 25 2014 Led <led@altlinux.ru> 2.6.32-alt122
- Update to 042stab090.5:
  + CVE-2014-3519

* Fri Jun 20 2014 Led <led@altlinux.ru> 2.6.32-alt121
- Update to 042stab090.4

* Sat Jun 07 2014 Led <led@altlinux.ru> 2.6.32-alt120
- Update to 042stab090.3 (CVE-2014-3153)

* Sat May 31 2014 Led <led@altlinux.ru> 2.6.32-alt119
- Update to 042stab090.2

* Sat Apr 19 2014 Led <led@altlinux.ru> 2.6.32-alt118
- Update to 042stab088.4

* Sun Mar 23 2014 Led <led@altlinux.ru> 2.6.32-alt117
- fix a bug in the VFS lookup code could cause a kernel panic

* Sat Mar 22 2014 Led <led@altlinux.ru> 2.6.32-alt116
- netfilter: nf_conntrack_dccp: fix skb_header_pointer API usages (CVE-2014-2523)

* Fri Mar 14 2014 Led <led@altlinux.ru> 2.6.32-alt115
- Update to 042stab085.17

* Thu Feb 20 2014 Led <led@altlinux.ru> 2.6.32-alt114
- mmap: call mmap prep only for regular files

* Fri Feb 14 2014 Led <led@altlinux.ru> 2.6.32-alt113
- Update to 042stab084.25:
  + ploop: roll back alloc_head on ENOSPC
  + mmap: do not call mmap for directories
  + ploop: unlock plo->lock in ploop_entry_reloc_a_req

* Fri Feb 07 2014 Led <led@altlinux.ru> 2.6.32-alt112
- updated ipt_NETFLOW to 1.8.2

* Wed Feb 05 2014 Led <led@altlinux.ru> 2.6.32-alt111
- Update to 042stab084.20:
  + Fixes in conntracks
  + Rework ext4_file_mmap locking to avoid extending struct file_operations
  + ploop: fix a race condition on relocation of blocks

* Fri Jan 17 2014 Led <led@altlinux.ru> 2.6.32-alt110
- Update to 042stab084.17

* Wed Jan 08 2014 Led <led@altlinux.ru> 2.6.32-alt109
- Update to 042stab084.14
- CVE-2013-2141
- CVE-2013-4470

* Thu Dec 12 2013 Led <led@altlinux.ru> 2.6.32-alt108
- Update to 042stab084.12

* Thu Nov 14 2013 Led <led@altlinux.ru> 2.6.32-alt107
- Update to 042stab082.3

* Tue Oct 29 2013 Led <led@altlinux.ru> 2.6.32-alt106
- Update to 042stab081.8

* Wed Oct 16 2013 Led <led@altlinux.ru> 2.6.32-alt105
- Update to 042stab081.5

* Fri Sep 27 2013 Led <led@altlinux.ru> 2.6.32-alt104
- fixed spec

* Sun Sep 22 2013 Led <led@altlinux.ru> 2.6.32-alt103
- Update to 042stab081.3

* Thu Aug 29 2013 Led <led@altlinux.ru> 2.6.32-alt102
- Update to 042stab079.6

* Tue Aug 06 2013 Led <led@altlinux.ru> 2.6.32-alt101
- Update to 042stab079.5

* Fri Aug 02 2013 Led <led@altlinux.ru> 2.6.32-alt100
- Update to 042stab079.4

* Mon Jul 15 2013 Led <led@altlinux.ru> 2.6.32-alt99
- fs: defer do_filp_open() access checks to may_open()

* Fri Jul 12 2013 Led <led@altlinux.ru> 2.6.32-alt98
- Update to 042stab078.28

* Tue Jul 02 2013 Led <led@altlinux.ru> 2.6.32-alt97
- fixed freeing RCU-protected IP-options (CVE-2013-2224)
- enabled OCFS2_FS

* Fri Jun 21 2013 Led <led@altlinux.ru> 2.6.32-alt96
- Update to 042stab078.26

* Fri Jun 14 2013 Led <led@altlinux.ru> 2.6.32-alt95
- Update to 042stab078.22

* Sat Jun 08 2013 Led <led@altlinux.ru> 2.6.32-alt94
- Update to 042stab078.21

* Tue Jun 04 2013 Led <led@altlinux.ru> 2.6.32-alt93
- Update to 042stab078.20

* Wed May 22 2013 Led <led@altlinux.ru> 2.6.32-alt92
- Update to 042stab078.16
- moved nouveau and radeon DRM modules to kernel-modules-drm-* subpackage
- removed kernel-modules-drm-nouveau-* and kernel-modules-drm-radeon-*
  subpackages

* Sun May 19 2013 Led <led@altlinux.ru> 2.6.32-alt91
- Update to 042stab078.13

* Fri May 17 2013 Led <led@altlinux.ru> 2.6.32-alt90
- Update to 042stab078.11
- disabled:
  + DRM_I810 (broken)
  + ATH9K_HTC (broken)

* Wed May 15 2013 Led <led@altlinux.ru> 2.6.32-alt89
- updated to 042stab076.8
- restored Requires version of bootloader-utils

* Tue May 14 2013 Led <led@altlinux.ru> 2.6.32-alt88
- perf: Treat attr.config as u64 in perf_swevent_init() (CVE-2013-2094)

* Tue May 07 2013 Led <led@altlinux.ru> 2.6.32-alt87
- Update to 042stab076.7
- usb-storage: add unusual_devs entry for Casio EX-N1 digital camera
- gspca_pac7302: add support for Genuis Look 317 WebCam
- updated Requires
- enabled JFS_FS
- upstream fixes:
  + jfs
  + reiserfs

* Wed Apr 03 2013 Led <led@altlinux.ru> 2.6.32-alt86
- Update to 042stab076.5

* Sun Mar 31 2013 Led <led@altlinux.ru> 2.6.32-alt85
- fuse: fix stat call on 32 bit platforms (ALT#28767)

* Wed Mar 13 2013 Led <led@altlinux.ru> 2.6.32-alt84
- Update to 042stab075.2

* Mon Mar 11 2013 Led <led@altlinux.ru> 2.6.32-alt83
- Update to 042stab074.10

* Fri Mar 01 2013 Led <led@altlinux.ru> 2.6.32-alt82
- Update to 042stab074.9

* Tue Feb 19 2013 Led <led@altlinux.ru> 2.6.32-alt81
- Update to 042stab074.4
- enabled FB_UVESA
- added ipt_NETFLOW 1.8

* Fri Feb 08 2013 Led <led@altlinux.ru> 2.6.32-alt80
- Update to 042stab072.10
- removed obsoleted %%post[un]_kernel_modules macros
- kbuild: generate modules.builtin (ALT#28491)
- disabled:
  + OCFS2 (broken by OpenVZ)
  + FUNCTION_TRACER
  + FRAME_POINTER
  + DEBUG_FORCE_WEAK_PER_CPU
  + DEBUG_DEVRES
- enabled:
  + CIFS_ACL
  + PRAMCACHE
  + DRM_I2C_CH7006
  + MMC_RICOH_MMC
  + SND_CMIPCI
  + SMS_SIANO_MDTV
  + USB_PWC
  + HP_WATCHDOG
  + WL12XX
  + DM_RAID
  + BLK_DEV_NBD
  + NETPRIO_CGROUP
  + IP_SET
  + USB_NET_AX8817X
  + E1000E
- RTC_DRV_CMOS=y

* Sat Oct 27 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt79
- Update to 042stab063.2

* Sat Oct 13 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt78
- Update to 042stab062.2

* Sun Sep 30 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt77
- mm: add numa node symlink for cpu devices in sysfs (ALT 27782)

* Fri Sep 28 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt76
- Update to 042stab062.1

* Thu Sep 13 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt75
- Update to 042stab061.9

* Tue Sep 04 2012 Anton Protopopov <aspsk@altlinux.org> 2.6.32-alt74
- Update to 042stab061.8

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
