# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define kflavour		rt
Name: kernel-image-%kflavour
%define kernel_base_version	5.10
%define kernel_sublevel	.152
%define kernel_rt_release	rt75
%define kernel_extra_version	%nil
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
Release: alt1.%kernel_rt_release

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; printf %%s "${s#*-}" )

#Remove oss
%def_disable oss
## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*

Summary: The Linux kernel with PREEMPT_RT patches (Real-Time Linux)
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://wiki.linuxfoundation.org/realtime/
Vcs: git://git.kernel.org/pub/scm/linux/kernel/git/rt/linux-stable-rt.git
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: %name-%version-%release.patch

ExclusiveArch: x86_64

%define make_target bzImage
%ifarch ppc64le
%define make_target vmlinux
%endif
%ifarch aarch64
%define make_target Image
%endif

%define image_path arch/%base_arch/boot/%make_target
%ifarch ppc64le
%define image_path %make_target
%endif

%define arch_dir %base_arch
%ifarch %ix86 x86_64
%define arch_dir x86
%endif

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: bc
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kernel-source-%kernel_base_version = 1.0.0
BuildRequires: kmod
BuildRequires: libdb4-devel
BuildRequires: libelf-devel
BuildRequires: libgmp-devel
BuildRequires: libmpc-devel
BuildRequires: lzma-utils
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: rsync
# for check
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm-run >= 1.30 ltp >= 20210524-alt2 iproute2}}

Requires: bootloader-utils
Requires: coreutils
Requires: kmod
Requires: mkinitrd

Provides: kernel = %kversion

AutoReqProv: no

%description
This package contains the Linux kernel %kernel_base_version%kernel_sublevel \
with PREEMPT_RT patches (%kernel_extra_version) with some OSADL patches.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common
Provides: kernel-headers = %version
AutoReqProv: nocpp
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
This package contains documentation files for ALT Linux kernel packages:
 * kernel-image-%base_flavour-up-%kversion-%krelease
 * kernel-image-%base_flavour-smp-%kversion-%krelease

The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.

%package checkinstall
Summary: Verify presence of pesign
Group: System/Kernel and hardware
Requires: %name = %EVR
Requires: rpm-pesign-checkinstall

%description checkinstall
%summary.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -p1 -s

# OSADL patches: https://www.osadl.org/OSADL-Linux-Add-on-Patches.kernelpatches.0.html
## https://www.osadl.org/NMI-SysRq.sysysrequest-via-nmi-polling.0.html
patch -p1 -s < add-nmi-callback-and-raw-parport-driver.patch # SETPARPORT_RAW
## https://www.osadl.org/Latency-histograms.latencyhist.0.html
patch -p1 -s < latency-histograms.patch # PREEMPTIRQ_EVENTS *_HIST
## https://www.osadl.org/Ping-SysRq.sysysrequest-via-ping.0.html
patch -p1 -s < net-ipv4-icmp-ping-sysrq.patch
## https://www.osadl.org/Precise-load-measurement.precise-system-load.0.html
patch -p1 -s < sched-add-per-cpu-load-measurement.patch # CPU_IDLERUNTIME

# fix -rt suffix
rm -f localversion*

# Set GCC version for gcc-wrapper.
echo 'export GCC_VERSION=%__gcc_version_base' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

chmod +x tools/objtool/sync-check.sh

%build
export ARCH=%base_arch
export NPROCS=%__nprocs
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper

# Configuration construction
CONFIGS=config-x86_64
%if "%base_flavour" == "rt"
CONFIGS="$CONFIGS config-rt"
%endif

scripts/kconfig/merge_config.sh -m $CONFIGS

# Options not recommended by
# https://wiki.linuxfoundation.org/realtime/documentation/known_limitations
FORBID="TRANSPARENT_HUGEPAGE
	OPROFILE
	X86_POWERNOW_K8
	BCACHE
	RT_GROUP_SCHED
	CPUMASK_OFFSTACK"

# Clean up and settle everything
%make_build olddefconfig

# Panic if forbidden options are enabled
for opt in $FORBID; do
	grep CONFIG_$opt= .config && exit 1
done

grep ^CONFIG_PREEMPT_RT=y .config

# Check options from OSADL patches are enabled.
grep SETPARPORT_RAW .config
grep CONFIG_MISSED_TIMER_OFFSETS_HIST .config
grep CONFIG_WAKEUP_LATENCY_HIST .config
grep CONFIG_SWITCHTIME_HIST .config
grep CPU_IDLERUNTIME .config

%make_build %make_target
%make_build modules
%ifarch aarch64
%make_build dtbs
%endif

echo "Kernel built $KernelVer"

%install
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

%ifarch aarch64
mkdir -p %buildroot/lib/devicetree/$KernelVer
find arch/%arch_dir/boot/dts -type f -name \*.dtb | xargs -iz install -pm0644 z %buildroot/lib/devicetree/$KernelVer
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
cp -a drivers/scsi/scsi.h \
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
	scripts/module.lds
	scripts/subarch.include
	scripts/depmod.sh
	scripts/gcc-plugins/*.so
	scripts/ld-version.sh
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

find %buildroot%kheaders_dir -name ..install.cmd -delete

#provide symlink to autoconf.h for back compat
pushd %buildroot%old_kbuild_dir/include/linux
ln -s ../generated/autoconf.h
ln -s ../generated/utsrelease.h
ln -s ../generated/uapi/linux/version.h
popd

# Remove *.bin files, they will be packaged as ghosts.
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,devname,softdep,symbols}

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist /boot/vmlinuz-*

# Fix: eu-elflint failed for modules
%add_verify_elf_skiplist %modules_dir/*

%check
vm-run cat /sys/kernel/realtime

if ! timeout 999 vm-run --kvm=cond \
	"/sbin/sysctl kernel.printk=8;
	 runltp -f kernel-alt-vm -S skiplist-alt-vm -o out"; then
	cat /usr/lib/ltp/output/LTP_RUN_ON-out.failed >&2
	sed '/TINFO/i\\' /usr/lib/ltp/output/out | awk '/TFAIL/' RS= >&2
	exit 1
fi

%pre checkinstall
set -ex
check-pesign-helper /boot/vmlinuz-%kversion-%flavour-%krelease

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
%dir %modules_dir
%defattr(0600,root,root,0700)
%modules_dir/kernel
%modules_dir/modules.order
%modules_dir/modules.builtin*
%exclude %modules_dir/build
%ghost %modules_dir/modules.alias
%ghost %modules_dir/modules.dep
%ghost %modules_dir/modules.devname
%ghost %modules_dir/modules.softdep
%ghost %modules_dir/modules.symbols
%ghost %modules_dir/modules.alias.bin
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols.bin
%ghost %modules_dir/modules.builtin.bin
%ifarch aarch64
/lib/devicetree/%kversion-%flavour-%krelease
%endif

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build

%files checkinstall

%changelog
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
