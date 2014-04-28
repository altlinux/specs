%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_with() %{expand:%%force_with %{1}} %{expand:%%undefine _without_%{1}}
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}

%define intel_64 nocona core2 corei7 nehalem
%define intel_32 pentium pentiumpro pentium_mmx pentium2 pentium3 pentium_m pentium4 prescott atom
%define amd_32 5x86 k5 k6 k6_2 k6_3 geode k7 athlon athlon_xp
%define amd_64 opteron k8 k9 k10 barcelona phenom
%define via_64 nano
%define via_32 c3 c3_2
%define x86_64 x86_64 %intel_64 %amd_64 %via_64

%define extra_modules %nil
%define Extra_modules() BuildRequires: kernel-src-%1 = %2 \
%global extra_modules %extra_modules %1=%2

%define base_flavour led
%define default_sub_flavour ws
%if "xws" == "x"
%define sub_flavour %default_sub_flavour
%else
%define sub_flavour ws
%endif
%define flavour %base_flavour-%sub_flavour

Name: kernel-image-%flavour
Version: 3.13.11
Release: alt5

%define kernel_req %nil
%define kernel_prov %nil
%define kernel_branch 3.13
%define kernel_stable_version 11
%define kernel_extra_version .%kernel_stable_version
#define kernel_extra_version %nil

%define krelease %release

%define kmandir %{_man9dir}l
# Build options
# You can change compiler version by editing this line:
%define kgcc_version 4.8

%def_enable smp
%def_disable optimize_for_size
%def_disable verbose
%def_disable debug
%def_enable modversions
%def_enable kallsyms
%def_with src
%def_enable docs
%def_enable htmldocs
%def_enable man
%def_disable compat
%def_enable lto
%def_disable lto_slim
%def_enable relocatable
%def_enable x32
%def_enable cr
%def_enable bld
%def_disable mptcp
%def_enable debugfs
%def_enable coredump
%def_enable olpc
%def_enable numa
%def_disable hotplug_memory
%def_enable acpi
%def_enable pci
%def_disable vme
%def_disable math_emu
%def_disable pae
%def_disable x86_extended_platform
%def_enable pcmcia
%def_enable isdn
%def_enable telephony
%def_enable atm
%def_enable fddi
%def_enable w1
%def_enable hamradio
%def_enable arcnet
%def_enable caif
%def_enable can
%def_enable hippi
%def_enable fusion
%def_enable drm
%def_enable ipv6
%def_disable apei
%def_enable edac
%def_enable ide
%def_enable pata
%def_enable firewire
%def_enable bluetooth
%def_enable irda
%def_enable joystick
%def_enable gameport
%def_enable usb_gadget
%def_enable tablet
%def_enable touchscreen
%def_enable lirc
%def_enable iio
%def_enable watchdog
%def_enable regulator
%def_enable mfd
%def_enable spi
%def_enable mtd
%def_disable rapidio
%def_enable mmc
%def_enable media
%def_enable sound
%def_disable oss
%def_enable alsa
%def_disable pcsp
%def_enable video
%def_enable guest
%def_enable simple_ext2
%def_disable ext4_for_ext2
%def_enable ext4_for_ext3
%def_enable bootsplash
%def_disable fbcondecor
%def_disable crasher
%def_disable logo
%def_enable taskstats
%def_enable security
%def_enable audit
%def_enable selinux
%def_enable tomoyo
%def_enable apparmor
%def_enable smack
%def_enable yama
%def_enable thp
%def_enable kvm
%def_disable hyperv
%def_disable hypervisor_guest
%def_disable kvm_guest
%def_disable nfs_swap
%def_enable fatelf
%def_enable lnfs
%def_enable oprofile
%def_enable secrm
%def_with firmware
%def_with tools
%def_with perf
%def_with lkvm

%def_disable debug_section_mismatch

#define allocator SLAB

%def_enable remove_unused_exports

#Extra_modules spl 0.6.2
%Extra_modules zfs 0.6.2
#Extra_modules kvm 3.10.1
%Extra_modules vboxhost 4.3.10
%Extra_modules vboxguest 4.3.10
#Extra_modules nvidia 331.20
%Extra_modules fglrx 14.10
#Extra_modules knem 1.1.1
#Extra_modules exfat 1.2.7
#Extra_modules ipt_NETFLOW 1.8.2
#Extra_modules netatop 0.3
#Extra_modules omnibook 20110911

%define strip_mod_opts --strip-unneeded -R .comment

## Don't edit below this line ##################################

%define kversion	%kernel_branch%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease
%define firmware_dir	/lib/firmware/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kernel_branch-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware
Url: http://www.kernel.org/

Source0: linux-%version.tar
Source1: %flavour-%kernel_branch.x86_64.config
Source2: %flavour-%kernel_branch.x86.config
Source5: fixes.inc
Source6: features.inc
Source7: fixes-apply.inc
Source8: features-apply.inc
Source10: Makefile.external

#Patch0000: patch-%kernel_branch.%kernel_stable_version

%include %_sourcedir/fixes.inc

%include %_sourcedir/features.inc

ExclusiveOS: Linux
ExclusiveArch: %x86_64 %ix86
ExcludeArch: i386

%ifarch %x86_64 %ix86
%define kernel_arch x86
%else
%define kernel_arch %_target_cpu
%endif

%ifarch %x86_64
%define base_arch x86_64
%endif
%ifarch %ix86
%define base_arch x86
%endif

%ifnarch x86_64 i486 i586
%set_disable docs
%set_without src
%endif

%if_disabled docs
%set_disable htmldocs
%set_disable man
%endif

%ifnarch i486
%set_disable math_emu
%endif

%if "%sub_flavour" == "vs"
%def_enable vserver
%set_enable hypervisor_guest
%else
%def_disable vserver
%endif

%{?_disable_lto:%set_disable lto_slim}

%{?_disable_pci:%set_disable drm}

%{?_disable_media:%set_disable lirc}

%if_disabled sound
%set_disable oss
%set_disable alsa
%endif

%{?_disable_alsa:%set_disable pcsp}

%{?_disable_video:%set_disable bootsplash}

%{?_disable_hypervisor_guest:%set_disable hyperv}

%{?_enable_debug:%set_enable debugfs}

%{!?allocator:#define allocator SLAB}

%if "%sub_flavour" != "%default_sub_flavour"
%set_without tools
%endif

%ifnarch x86_64 i486 i586 i686
%set_without tools
%endif

%if_without tools
%set_without perf
%set_without lkvm
%endif

%if "%sub_flavour" == "ws"
%set_disable numa
%endif

%if "%sub_flavour" != "ws"
%set_disable bootsplash
%set_disable bld
%ifarch %ix86
%ifnarch i486 i586 pentium_m pentium pmmx pentium_mmx m1 6x86 crusoe m2 6x86mx mp6 k6_3 k6_2 k6 cyrix3 geode c3 nx586 gxm gx1 gx2 gx 55x 5x86 winchip winchip2
#set_enable pae
%endif
%endif
%endif

%if "%sub_flavour" == "vs"
%def_enable vserver
%else
%def_disable vserver
%endif

%ifarch %x86_64
%define kernel_base_cpu	GENERIC_CPU
%ifarch k8
%define kernel_cpu	K8
%endif
%ifarch k9
%define kernel_cpu	K9
%endif
%ifarch k10
%define kernel_cpu	K10
%endif
%ifarch nocona
%define kernel_cpu	PSC
%endif
%ifarch core2
%define kernel_cpu	CORE2
%endif
%ifarch corei7 nehalem
%define kernel_cpu	COREI7
%endif
%endif

%ifarch %ix86
%define kernel_base_cpu	M386
%ifarch i486
%define kernel_cpu	486
%endif
%ifarch i586
%define kernel_cpu	586
%endif
%ifarch i686
%define kernel_cpu	686
%endif
%ifarch k6
%define kernel_cpu	K6
%endif
%ifarch athlon
%define kernel_cpu	K7
%endif
%ifarch pentium4
%define kernel_cpu	PENTIUM4
%endif
%ifarch k8_32
%define kernel_cpu	K8
%endif
%ifarch k9_32
%define kernel_cpu	K9
%endif
%ifarch k10_32
%define kernel_cpu	K10
%endif
%ifarch core2_32
%define kernel_cpu	CORE2
%endif
%ifarch atom
%define kernel_cpu	ATOM
%endif
%ifarch corei7_32 nehalem_32
%define kernel_cpu	COREI7
%endif
%endif

%define perf_make_opts %{?_enable_verbose:V=1} JOBS=%__nprocs prefix=%_prefix perfexecdir=%_libexecdir/perf WERROR=0 EXTRA_CFLAGS="%optflags %{?_disable_debug:-g0}"
%define lkvm_make_opts %{?_enable_verbose:V=1} LTO=1 prefix=%_prefix EXTRA_CFLAGS="%optflags %{?_disable_debug:-g0}"

%if "x%extra_modules" != "x"
%define extra_mods %(echo "%extra_modules" | sed 's/=[^ ]*//g')
%endif

%if %(echo "%extra_mods" | grep -q '\bkvm\b' && echo 1 || echo 0)
%def_enable kvm_ext
%endif

BuildPreReq: rpm-build-kernel >= 0.103
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
%{?kgcc_version:BuildRequires: gcc%kgcc_version}
BuildRequires: module-init-tools >= 3.1
BuildRequires: patch >= 2.6.1-alt1
%{?_with_src:BuildRequires: pxz}

%{?_with_firmware:BuildRequires: hardlink}
%{?_enable_htmldocs:BuildRequires: xmlto transfig ghostscript}
%{?_enable_man:BuildRequires: xmlto}
%{?_with_perf:BuildRequires: binutils-devel libelf-devel asciidoc elfutils-devel >= 0.138 pkgconfig(gtk+-2.0) libnewt-devel perl-devel python-dev libunwind-devel libaudit-devel libnuma-devel}
%{?_with_lkvm:BuildRequires: binutils-devel libvncserver-devel libSDL-devel zlib-devel libaio-devel libgtk+3-devel}

Requires: bootloader-utils >= 0.4.21
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.9.8.24.1

Provides: kernel = %kversion
Provides: kernel-modules-md-%flavour = %version-%release
%{?_enable_w1:Provides: kernel-modules-w1-%flavour = %version-%release}

PreReq: coreutils
PreReq: module-init-tools >= 3.1
PreReq: mkinitrd >= 1:2.9.9-alt1
AutoProv: no, %kernel_prov
AutoReq: no, %kernel_req

%description
This package contains the Linux kernel that is used to boot and run your system.
Most hardware drivers for this kernel are built as modules. Some of these drivers
are built separately from the kernel; they are available in separate packages
(kernel-modules-*-%flavour).
%if "%sub_flavour" == "ws"
The "ws" flavour of kernel packages is kernels for using on workstations.
%endif
%if "%sub_flavour" == "vs"
The "vs" flavour of kernel packages is VServer kernels http://linux-vserver.org.
It allows to run multiple virtual units at once. Those units are sufficiently
isolated to guarantee the required security, but utilize available resources
efficiently, as they run on the same kernel.
%endif

%define kernel_modules_package_add_provides() \
Provides: kernel-modules-%{1}-%flavour = %version-%release \
Provides: kernel-modules-%{1}-%kversion-%flavour-%krelease = %version-%release

%define kernel_modules_package_std_body() \
Group: System/Kernel and hardware \
Provides: kernel-modules-%{1}-%kversion-%flavour-%krelease = %kversion-%release \
Conflicts: kernel-modules-%{1}-%kversion-%flavour-%krelease < %kversion-%release \
Conflicts: kernel-modules-%{1}-%kversion-%flavour-%krelease > %kversion-%release \
Requires: %name = %kversion-%release \
AutoProv: no, %kernel_prov \
AutoReq: no, %kernel_req \
PreReq: coreutils module-init-tools >= 3.1 %name = %kversion-%release

%define kernel_doc_package_std_body() \
Group: Documentation \
%{?base_flavour:Provides: kernel-%{1}-%base_flavour = %version-%release} \
Obsoletes: kernel-%{1}-%flavour-%kernel_branch \
Provides: kernel-%{1}-%flavour-%kernel_branch = %version-%release \
BuildArch: noarch \
AutoProv: no \
AutoReq: no

%if 0
%define kernel_modules_package_post() \
%post -n kernel-modules-%{1}-%flavour \
%post_kernel_modules %kversion-%flavour-%krelease \
\
%postun -n kernel-modules-%{1}-%flavour \
%postun_kernel_modules %kversion-%flavour-%krelease

%define kernel_extmods_package_post() \
%post -n kernel-modules-%{1}-%flavour \
%post_kernel_modules %kversion-%flavour-%krelease \
\
%postun -n kernel-modules-%{1}-%flavour \
%postun_kernel_modules %kversion-%flavour-%krelease
%else
%define kernel_modules_package_post() \
%nil

%define kernel_extmods_package_post() \
%nil
%nil
%endif

%define kernel_modules_package_files() \
%files -n kernel-modules-%{1}-%flavour -f %{1}.rpmmodlist

%package -n kernel-modules-scsi-%flavour
Summary: SCSI driver modules
%kernel_modules_package_std_body scsi

%description -n kernel-modules-scsi-%flavour
This package contains SCSI modules for the Linux kernel package
%name-%version-%release.


%package -n kernel-modules-infiniband-%flavour
Summary: InfiniBand core and support driver modules
%kernel_modules_package_std_body infiniband
%kernel_modules_package_add_provides ib

%description -n kernel-modules-infiniband-%flavour
This package contains InfiniBand core and support driver modules for the Linux
kernel package %name-%version-%release.


%package -n kernel-modules-ipmi-%flavour
Summary: IPMI core and support driver modules
%kernel_modules_package_std_body ipmi

%description -n kernel-modules-ipmi-%flavour
This package contains IPMI core and support driver modules for the Linux kernel
package %name-%version-%release.


%if_enabled edac
%package -n kernel-modules-edac-%flavour
Summary: EDAC (Error Detection And Correction) driver modules
%kernel_modules_package_std_body ipmi

%description -n kernel-modules-edac-%flavour
This package contains EDAC (Error Detection And Correction) driver modules for
the Linux kernel package %name-%version-%release.
%endif


%if_enabled video
%package -n kernel-modules-video-%flavour
Summary: Video graphics driver modules
%kernel_modules_package_std_body video
%kernel_modules_package_add_provides fb
%kernel_modules_package_add_provides framebuffer

%description -n kernel-modules-video-%flavour
This package contains Video graphics modules for the Linux kernel package
%name-%version-%release.
%endif


%package -n kernel-modules-input-extra-%flavour
Summary: Linux extra input drivers modules
%kernel_modules_package_std_body input-extra
%{?_enable_joystick:%kernel_modules_package_add_provides joystick}
%{?_enable_joystick:%kernel_modules_package_add_provides gamepad}
%{?_enable_tablet:%kernel_modules_package_add_provides tablet}
%{?_enable_touchscreen:%kernel_modules_package_add_provides touchscreen}

%description -n kernel-modules-input-extra-%flavour
This package contains extra input drivers modules modules for the Linux
kernel package %name-%version-%release.


%if_enabled usb_gadget
%package -n kernel-modules-usb-gadget-%flavour
Summary: Linux USB Gadget driver modules
%kernel_modules_package_std_body usb-gadget

%description -n kernel-modules-usb-gadget-%flavour
USB Gadget support on a system involves a peripheral controller,
and the gadget driver using it.
This package contains Linux USB Gadget driver modules for the kernel
package %name-%version-%release.
%endif


%if_enabled watchdog
%package -n kernel-modules-watchdog-%flavour
Summary: Linux Watchdog Timer driver modules
%kernel_modules_package_std_body watchdog

%description -n kernel-modules-watchdog-%flavour
This package contains Watchdog Timer driver modules for the Linux kernel
package %name-%version-%release.
%endif


%if_enabled mtd
%package -n kernel-modules-mtd-%flavour
Summary: Linux Memory Technology Devices driver and fs modules
%kernel_modules_package_std_body mtd

%description -n kernel-modules-mtd-%flavour
Memory Technology Devices are flash, RAM and similar chips, often used
for solid state file systems on embedded devices.
This package contains Memory Technology Devices driver and fs modules for
the Linux kernel package %name-%version-%release.
%endif


%package -n kernel-modules-fs-extra-%flavour
Summary: Linux extra filesystems drivers modules
%kernel_modules_package_std_body fs-extra

%description -n kernel-modules-fs-extra-%flavour
This package contains extra filesystems drivers modules modules for the
Linux kernel package %name-%version-%release.


%package -n kernel-modules-net-extra-%flavour
Summary: Linux extra net drivers modules
%kernel_modules_package_std_body net-extra
%{?_enable_atm:%kernel_modules_package_add_provides atm}
%{?_enable_hamradio:%kernel_modules_package_add_provides hamradio}
%{?_enable_irda:%kernel_modules_package_add_provides irda}
%{?_enable_isdn:%kernel_modules_package_add_provides isdn}

%description -n kernel-modules-net-extra-%flavour
This package contains extra net drivers modules modules for the Linux
kernel package %name-%version-%release.


%if_enabled oss
%package -n kernel-modules-oss-%flavour
Summary: OSS sound driver modules (obsolete)
%kernel_modules_package_std_body oss

%description -n kernel-modules-oss-%flavour
This package contains OSS sound driver modules for the Linux kernel
package %name-%version-%release.
These drivers are declared obsolete by the kernel maintainers; ALSA
drivers should be used instead.  However, the older OSS drivers may be
still useful for some hardware, if the corresponding ALSA drivers do
not work well.
Install this package only if you really need it.
%endif


%if_enabled alsa
%package -n kernel-modules-sound-%flavour
Summary: The Advanced Linux Sound Architecture modules
%kernel_modules_package_std_body sound
%kernel_modules_package_add_provides alsa
%kernel_modules_package_add_provides sound-ext

%description -n kernel-modules-sound-%flavour
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.
%endif


%if_enabled ide
%package -n kernel-modules-ide-%flavour
Summary: The IDE modules (old)
%kernel_modules_package_std_body ide

%description -n kernel-modules-ide-%flavour
Integrated Disk Electronics (IDE aka ATA-1) is a connecting standard for
mass storage units such as hard disks.
These are old IDE modules for your Linux system.
%endif


%if_enabled drm
%package -n kernel-modules-drm-%flavour
Summary: The Direct Rendering Infrastructure modules
%kernel_modules_package_std_body drm

%description -n kernel-modules-drm-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.
These are DRM modules for your Linux system.
%endif


%if_enabled media
%package -n kernel-modules-media-%flavour
Summary: Linux media driver modules
# Needed for webcams
Requires: kernel-modules-alsa-%flavour = %kversion-%release
%kernel_modules_package_std_body media

%description -n kernel-modules-media-%flavour
V4L kernel modules support for video capture and overlay devices,
webcams and AM/FM radio cards.
DVB kernel modules for DVB/ATSC device handling, software fallbacks etc.
%endif


%if_enabled guest
%if "%sub_flavour" != "guest"
%package -n kernel-modules-guest-%flavour
Summary: Linux guest driver modules
%kernel_modules_package_std_body guest

%description -n kernel-modules-guest-%flavour
This package contains Linux guest driver modules for the kernel package
%name-%version-%release.
%endif
%endif


%if_enabled kvm
%package -n kernel-modules-kvm-%flavour
Summary: Kernel-based Virtual Machine (KVM) modules
%kernel_modules_package_std_body kvm

%description -n kernel-modules-kvm-%flavour
Support hosting fully virtualized guest machines using hardware
virtualization extensions. You will need a fairly recent processor
equipped with virtualization extensions.
These are KVM modules for your Linux system.
%endif


%if_enabled oprofile
%package -n kernel-modules-oprofile-%flavour
Summary: OProfile system profiling module
%kernel_modules_package_std_body oprofile

%description -n kernel-modules-oprofile-%flavour
OProfile is a profiling system capable of profiling the whole system,
include the kernel, kernel modules, libraries, and applications.
These are OProfile module and vmlinux file for your Linux system.
%endif


%package -n kernel-headers-modules-%flavour
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel
%{?kgcc_version:Requires: gcc%kgcc_version}
Obsoletes: kernel-headers-modules-%flavour-%kernel_branch
Provides: kernel-headers-modules-%flavour-%kernel_branch = %version-%release
Provides: kernel-devel-%flavour = %version-%release
%{?base_flavour:Provides: kernel-devel-%base_flavour = %version-%release}
Provides: kernel-devel = %version-%release
#Obsoletes: kernel-headers-modules-%flavour = %version
AutoProv: no

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source directory.


%if_with firmware
%package -n firmware-kernel-%flavour
Summary: Firmware for drivers from %name
Group: System/Kernel and hardware
License: GPLv2, Redistributable
Requires: %name = %kversion-%release
AutoProv: no
AutoReq: no

%description -n firmware-kernel-%flavour
Firmware for drivers from %name.
%endif


%if_with perf
%package -n perf
Summary: Performance analysis tools for Linux
Group: Development/Tools
AutoReq: yes,noperl,nopython
AutoProv: yes,noperl,nopython

%description -n perf
Performance counters for Linux are are a new kernel-based subsystem that provide
a framework for all things performance analysis. It covers hardware level
(CPU/PMU, Performance Monitoring Unit) features and software features (software
counters, tracepoints) as well.
This package contains performance analysis tools for Linux
%endif

%if_with lkvm
%package -n lkvm
Summary: Native Linux KVM tool
Group: Emulators
Provides: linux-kvm = %version-%release
Provides: kvm-tool = %version-%release

%description -n lkvm
The goal of this tool is to provide a clean, from-scratch, lightweight KVM host
tool implementation that can boot Linux guest images with no BIOS dependencies
and with only the minimal amount of legacy device emulation.
%endif


%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version
%{?base_flavour:Provides: kernel-headers-%base_flavour = %version}
Obsoletes: kernel-headers-%flavour-%kernel_branch
Provides: kernel-headers-%flavour-%kernel_branch = %version-%release
#Obsoletes: kernel-headers-%flavour = %version
Provides: %kheaders_dir/include
AutoProv: no

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).


%if_enabled docs
%package -n kernel-doc-%flavour
Summary: Linux kernel %kversion-%flavour documentation
%kernel_doc_package_std_body doc

%description -n kernel-doc-%flavour
This package contains documentation files for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.


%if_enabled htmldocs
%package -n kernel-docbook-%flavour
Summary: Linux kernel %kversion-%flavour HTML API documentation
%kernel_doc_package_std_body docbook

%description -n kernel-docbook-%flavour
This package contains API documentation HTML files for Linux kernel
package kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.
%endif


%if_enabled man
%package -n kernel-man-%flavour
Summary: Linux kernel %kversion-%flavour man pages
%kernel_doc_package_std_body man
Provides: kernel-man = %version-%release
Conflicts: kernel-man > %version-%release
Conflicts: kernel-man < %version-%release

%description -n kernel-man-%flavour
This package contains man pages for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The man pages contained in this package may be different from the similar
files in upstream kernel distributions, because some patches applied to
the corresponding kernel packages may change things in the kernel and
update the documentation to reflect these changes.
%endif
%endif


%if_with src
%package -n kernel-src-%flavour
Summary: Linux kernel %kversion-%flavour sources
Group: Development/Kernel
%{?base_flavour:Provides: kernel-src-%base_flavour = %version-%release}
Obsoletes: kernel-src-%flavour-%kernel_branch
Provides: kernel-src-%flavour-%kernel_branch = %version-%release
BuildArch: noarch
AutoProv: no
AutoReq: no

%description -n kernel-src-%flavour
This package contains sources for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
%endif


%ifdef extra_mods
%(for M in %extra_modules; do
m="${M%%=*}"
v="${M#*=}"
for p in $(rpmquery --whatprovides kernel-src-$m 2>/dev/null); do
	rpmquery --provides $p | grep -q "^kernel-src-$m = $v-"'*' && break || p=;
done
[ -n "$p" ] || p="kernel-src-$m-$v"
License="$(rpmquery --qf '%%{LICENSE}\n' $p 2>/dev/null)"
[ -n "$License" -a "$License" != "(none)" ] && License="License: $License" || License=
S="$(rpmquery --qf '%%{SUMMARY}\n' $p 2>/dev/null | sed -n 's/\( modules*\) sources/\1/p')"
[ -n "$S" ] || S="$m kernel modules v$v"
Desc="$(rpmquery --qf '%%{DESCRIPTION}\n' $p 2>/dev/null | sed -n -z 's/\( modules*\) sources/\1/gp')"
[ -n "$Desc" ] || Desc="$S."
cat <<__PACKAGE__
%%package -n kernel-modules-$m-%flavour
Version: ${v}_%kversion
Summary: $S
$License
%kernel_modules_package_std_body $m
Provides: kernel-extmods-$m-%flavour = %version-%release
Provides: kernel-modules-$m-%flavour = %kversion-%release

%%description -n kernel-modules-$m-%flavour
$Desc

__PACKAGE__
done)
%define version %kversion
%endif


%prep
%setup -c -n kernel-image-%flavour-%kversion-%krelease
cd linux-%version
#patch0000 -p1

%include %_sourcedir/fixes-apply.inc

%include %_sourcedir/features-apply.inc

# get rid of unwanted files resulting from patch fuzz
#find . -name "*.orig" -delete -or -name "*~" -delete

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
%ifdef kgcc_version
GCC_VERSION="%kgcc_version"
%else
GCC_VERSION="$(%__cc -dumpversion | cut -d. -f1-2)"
%endif
echo -n "export GCC_VERSION=$GCC_VERSION" > gcc_version.inc

sed -i -r \
	-e '/^CC[[:blank:]]*=/s/(gcc)[[:blank:]]*$/\1-'$GCC_VERSION/ \
	-e '/^AR[[:blank:]]*=/s/(gcc-ar)[[:blank:]]*$/\1-'$GCC_VERSION/ \
	-e '/^NM[[:blank:]]*=/s/(gcc-nm)[[:blank:]]*$/\1-'$GCC_VERSION/ \
	Makefile

%if_with src
cd ..
find linux-%kversion -type f -or -type l -not -name '*.orig' -not -name '*~' -not -name '.git*' > kernel-src-%flavour.list
cd -
%endif

install -m644 %SOURCE1 %SOURCE2 .

%ifdef extra_mods
install -m 0644 %SOURCE10 ./Makefile.external
install -d -m 0755 external
for m in $(echo " %extra_modules " | sed 's/ zfs\(=.* \)/ spl\1&/'); do
	tar -C external -xf %kernel_src/${m%%=*}-${m#*=}.tar*
done
%endif


%build
%define make_kernel %make_build %{?_enable_verbose:V=1} %{?_enable_lto_slim:AR=gcc-ar-$GCC_VERSION NM=gcc-nm-$GCC_VERSION LTO_JOBS=%__nprocs}

cd linux-%version

config_fix()
{
	local a
	local e
	a=$1
	shift
	while [ -n "$1" ]; do
		e="$e -$a $1"
		shift
	done
	scripts/config $e
}

config_disable()
{
	echo "DISABLE=<$@>"
	config_fix d $@
}

config_enable()
{
	config_fix e $@
}

config_module()
{
	config_fix m $@
}

config_val()
{
	scripts/config --set-val $@
}

config_str()
{
	scripts/config --set-str $@
}

if [ -f %flavour-%kernel_branch.%_target_cpu.config ]; then
	cp -vf %flavour-%kernel_branch.%_target_cpu.config .config
else
	cp -vf %flavour-%kernel_branch.%base_arch.config .config
%ifdef kernel_cpu
%if "%base_arch" != "%_target_cpu"
	config_disable %kernel_base_cpu
	config_enable m%kernel_cpu
%endif
%endif
fi

config_str localversion -%flavour-%krelease

%ifarch atom
config_val nr_cpus 4
%endif

%ifarch %intel_64 %intel_32
config_disable cpu_sup_{amd,centaur,{cyrix,transmeta,umc}_32}
config_enable cpu_sup_intel
%endif

%ifarch %amd_64 %amd_32
config_disable cpu_sup_{centaur,intel,{cyrix,transmeta,umc}_32}
config_enable cpu_sup_amd
%endif

%ifarch %via_64 %via_32
config_disable cpu_sup_{amd,intel,{cyrix,transmeta,umc}_32}
config_enable cpu_sup_centaur
%endif

%ifarch %ix86
%ifnarch i486 i586
config_disable eisa
%endif
%endif

config_disable \
%if_disabled sound
	sound usb_emi{26,62} \
%else
	%{?_disable_oss:sound_prime} %{?_disable_alsa:snd} \
%endif
	%{?_disable_smp:smp} \
	%{?_disable_modversions:modversions} \
	%{?_disable_compat:sysctl_syscall acpi_proc_event compat_vdso i2c_compat proc_pid_cpuset sysfs_deprecated usb_devicefs isb_device_class edac_legacy_sysfs x86_acpi_cpufreq_cpb} \
	%{?_disable_x32:x86_x32} \
	%{?_disable_pae:highmem64g} %{?_enable_pae:highmem4g} \
	%{?_disable_bld:bld} \
	%{?_disable_coredump:coredump} \
	%{?_disable_olpc:olpc} \
	%{?_disable_numa:numa} \
	%{?_disable_video:fb video_output_control backlight_lcd_support} \
	%{?_disable_drm:drm vga_switcheroo} \
	%{?_disable_ipv6:ipv6} \
	%{?_disable_apei:acpi_apei} \
	%{?_disable_edac:edac} \
	%{?_disable_arcnet:arcnet} \
	%{?_disable_caif:caif} \
	%{?_disable_can:can} \
	%{?_disable_hippi:hippi} \
	%{?_disable_fusion:fusion} \
	%{?_disable_ide:ide} \
	%{?_disable_firewire:firmware} \
	%{?_disable_irda:irda} \
	%{?_disable_joystick:input_joystick} \
	%{?_disable_tablet:input_tablet} \
	%{?_disable_touchscreen:input_touchscreen} \
	%{?_disable_lirc:lirc} \
	%{?_disable_gameport:gameport} \
	%{?_disable_usb_gadget:usb_gadget} \
	%{?_disable_pcmcia:pccard pcmcia} \
	%{?_disable_atm:atm} \
	%{?_disable_fddi:fddi} \
	%{?_disable_hamradio:hamradio} \
	%{?_disable_w1:w1} \
	%{?_disable_iio:iio} \
	%{?_disable_watchdog:watchdog} \
	%{?_disable_spi:spi} \
	%{?_disable_regulator:regulator} \
	%{?_disable_mtd:mtd} \
	%{?_disable_rapidio:rapidio} \
	%{?_disable_media:media_support} \
	%{?_disable_mmc:mmc} \
	%{?_disable_isdn:isdn} \
	%{?_disable_telephony:phone} \
	%{?_disable_taskstats:taskstats} \
	%{?_disable_security:security} \
	%{?_disable_audit:audir} \
	%{?_disable_selinux:security_selinux} \
	%{?_disable_tomoyo:securyty_tomoyo} \
	%{?_disable_apparmor:security_apparmor} \
	%{?_disable_smack:security_smack} \
	%{?_disable_yama:securyty_yama} \
	%{?_disable_thp:transparent_hugepage} \
	%{?_disable_guest:virtio drm_{cirrus_qemu,vmwgfx} vmware_balloon} \
	%{?_disable_kvm:kvm} \
	%{?_disable_hypervisor_guest:hypervisor_guest} \
	%{?_disable_hyperv:hyperv} \
	%{?_disable_kvm_guest:kvm_guest} \
	%{?_disable_bootsplash:bootsplash} \
	%{?_disable_crasher:crasher} \
	%{?_disable_logo:logo} \
	%{?_disable_pci:pci} \
	%{?_disable_vme:vme_bus} \
	%{?_disable_acpi:acpi} \
	%{?_disable_pcsp:snd_pcsp} \
	%{?_disable_nfs_swap:nfs_swap} \
	%{?_disable_hotplug_memory:memory_hotplug} \
	%{?_disable_math_emu:math_emulation} \
	%{?_disable_kallsyms:kallsyms} \
	%{?_disable_oprofile:profiling oprofile} \
	%{?_disable_fatelf:binfmt_fatelf} \
	%{?_enable_simple_ext2:ext2_fs_{xattr,posix_acl,security}} \
	%{?_enable_ext4_for_ext2:ext2_fs} %{?_enable_ext4_for_ext3:ext3_fs}

%{?_disable_pata:config_disable $(sed -n '/^CONFIG_PATA_/s/^CONFIG_\(PATA_.*\)=.*$/\1/p' .config | tr '[[:upper:]]\n' '[[:lower:]] ')}
# FIXME MFD_* may be selected with other options
%{?_disable_mfd:config_disable $(sed -n '/^config[[:blank:]]/s/^config[[:blank:]]*\(.*\)[[:blank:]]*$/\1/p' drivers/mfd/Kconfig | tr '[[:upper:]]\n' '[[:lower:]] ')}

config_enable \
	%{?_disable_lto:lto_disable} \
	%{?_enable_lto_slim:lto_slim} \
	%{?_enable_relocatable:relocatable} \
%ifarch i486 i586 i686
	x86_generic \
	%{?_enable_optimize_for_size:cc_optimize_for_size} \
%endif
	%{?_enable_debug_section_mismatch:debug_section_mismatch} \
	%{?_enable_modversions:modversions} \
	%{?_enable_pae:highmem64g} \
	%{?_enable_bld:bld} \
	%{?_enable_mptcp:mptcp} \
	%{?_enable_x86_extended_platform:x86_extended_platform} \
	%{?_enable_ext4_for_ext2:ext4_use_for_ext2} %{?_enable_ext4_for_ext3:ext4_use_for_ext3} \
	%{?_enable_debugfs:debug_fs} \
	%{?_enable_secrm:{ext{2,3,4},fat}_secrm} \
	%{?_enable_kvm_ext:kvm_external} \
	%{?_enable_lnfs:nfs{,d}_v4_security_label} \
	%{?_enable_kallsyms:kallsyms} \
%ifarch %x86_64
	%{?_enable_cr:checkpoint_restore proc_page_monitor} \
%endif
	%{?allocator:%allocator}

# arch-specific
%ifarch corei7 nehalem
config_disable crypto_crc32c
%endif
%ifarch i486
config_module crypto_{aes,twofish,salsa20}
%endif

%ifarch %intel_64 %via_64 %via_32
config_disable usb_ohci_hcd
%endif
%ifarch K9 K10 barcelona phenom
config_disable usb_uhci_hcd
%endif
%ifarch %amd_64 %amd_32 %via_64 %via_32
config_disable sched_smt net_dma pch_dma
%endif

# FIXME
config_disable iscsi_ibft_find firmware_memmap
# Timberdale is a companion chip for Atom CPUs in embedded in-car infotainment systems. Are we need that?
config_disable {mfd,serial,video}_timberdale
# I2C access to the SI470X radio chip is only needed on embedded systems
config_disable i2c_si470x
%ifarch %ix86 %x86_64
# Nokia Retu and Tahvo multi-function device found on Nokia Internet Tablets (770, N800 and N810).
config_disable mfd_retu
# Maxim 1586/1587 voltage regulator is suitable for PXA27x chips.
config_disable regulator_max1586
# non-x86 devices
config_disable mfd_ti_am335x_tscadc twl6040_core ucb1400_core mfd_wm8994
# Cadence devices only for ARM?
config_disable net_cadence
%endif
# non-modularized mfd drivers
config_disable olpc

%if_enabled debug
config_enable \
	kallsyms_all \
	slub_{debug,stats} \
	lockup{,_{detector,support}} \
	debug_{lockdep,kernel,mutexes,bugverbose,info,writecount,slab{,_leak}} \
	crash_dump proc_vmcore \
	kgdb
config_val bootparam_softlockup_panic_value 0
%endif

. gcc_version.inc
export CC="gcc-$GCC_VERSION"

echo "Building kernel %kversion-%flavour-%krelease"

%make_build oldconfig
%make_kernel bzImage modules

# psdocs, pdfdocs don't work yet
%{?_enable_htmldocs:%def_enable builddocs}
%{?_enable_man:%def_enable builddocs}
%if_enabled builddocs
%{?_enable_htmldocs:%make_build htmldocs}
%{?_enable_man:%make_build mandocs 2>&1 | tee mandocs.log | grep -E --line-buffered '^  (MAN|GEN)[[:blank:]]'}
echo "Kernel docs built %kversion-%flavour-%krelease"
%endif

%if_enabled remove_unused_exports
(grep -v '^#' | sort -u) > Module.symvers.enabled <<__EOF__
# FGLRX
acpi_get_next_object
acpi_lid_notifier_register
acpi_lid_notifier_unregister
amd_iommu_bind_pasid
amd_iommu_device_info
amd_iommu_enable_device_erratum
amd_iommu_free_device
amd_iommu_init_device
amd_iommu_unbind_pasid
amd_iommu_set_invalid_ppr_cb
amd_iommu_set_invalidate_ctx_cb
pm_vt_switch_register
pm_vt_switch_required
pm_vt_switch_unregister
set_memory_array_uc
set_memory_array_wb
smp_call_function
# VBox
__get_vm_area
map_vm_area
schedule_hrtimeout_range
set_pages_nx
set_pages_x
smp_call_function
# ZFS
check_disk_size_change
do_exit
elevator_change
get_gendisk
lock_may_read
lock_may_write
next_online_pgdat
__EOF__

sort -u -k2 Module.symvers.unused |
join -v2 -t'	' -11 -22 -o 2.4,2.2 Module.symvers.enabled - |
sed 's/	/\\(/;s/$/\\)/;s/^/^(|ACPI_)/' |
grep -E -o -f - $(find . -type f -name '*.c'; find ./kernel -type f -name '*.h') | tr ':' ' ' |
while read f p; do
	[ "${f%%.c}" = "$f" -o -f ${f%%.c}.o ] || continue
	sed -i "/^$p/s/^.*\(EXPORT\)\(_SYMBOL\)/\1_UNUSED\2/" $f >&2
	s="${p%%)}"
	echo "${s#*\(}	${f#./}"
done > Module.symvers.disabled

%make_kernel bzImage modules
%endif

%if_with perf
sed -i 's|\(perfexecdir[[:blank:]]*=[[:blank:]]*\).*$|\1%_libexecdir/perf|' tools/perf/config/Makefile
%make_build -C tools/perf %{?_enable_verbose:V=1} %perf_make_opts all man
%endif

%{?_with_lkvm:%make_build -C tools/kvm %lkvm_make_opts}

%{?extra_mods:%make_kernel -f Makefile.external %extra_mods && echo "External modules built"}


%install
cd linux-%version

. gcc_version.inc
export CC=gcc-$GCC_VERSION

install -Dp -m644 System.map %buildroot/boot/System.map-%kversion-%flavour-%krelease
install -Dp -m644 arch/%base_arch/boot/bzImage %buildroot/boot/vmlinuz-%kversion-%flavour-%krelease
install -Dp -m644 .config %buildroot/boot/config-%kversion-%flavour-%krelease

%make_install \
	INSTALL_MOD_PATH=%buildroot \
	INSTALL_FW_PATH=%buildroot%firmware_dir \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}} \
	modules_install
cp %buildroot%modules_dir/modules.dep{,.inkernel}

%ifdef extra_mods
make -f Makefile.external DESTDIR=%buildroot \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}} \
	INSTALL_MOD_PATH=%modules_dir \
	$(echo " %extra_mods " | sed 's/ zfs / zfs_spl /')
%endif

%{?_enable_oprofile:install -m 0644 vmlinux %buildroot%modules_dir/}

install -d -m 0755 %buildroot%kbuild_dir
cp -aL include %buildroot%kbuild_dir/
find %buildroot%kbuild_dir/include/config -type f -empty -delete
find %buildroot%kbuild_dir/include/config -type d -empty -delete
for d in arch/%kernel_arch/include; do
	a="$(dirname "$d")"
	install -d -m 0755 %buildroot%kbuild_dir/$a
	cp -a $d %buildroot%kbuild_dir/$a/
	install -p -m 0644 $a/Makefile* %buildroot%kbuild_dir/$a/
done
find %buildroot%kbuild_dir/{include,arch} -type f \( -name Kbuild -or -name '.*.cmd' \) -delete

%if 0
# drivers-headers install
install -d -m 0755 %buildroot%kbuild_dir/{drivers/{scsi,md,usb/core,net/wireless},net/mac80211,kernel,lib}
install -m 0644 drivers/scsi/scsi{{,_typedefs}.h,_module.c} %buildroot%kbuild_dir/drivers/scsi/
install -m 0644 drivers/md/dm*.h %buildroot%kbuild_dir/drivers/md/
install -m 0644 drivers/usb/core/*.h %buildroot%kbuild_dir/drivers/usb/core/
install -m 0644 drivers/net/wireless/Kconfig %buildroot%kbuild_dir/drivers/net/wireless/
install -m 0644 lib/hexdump.c %buildroot%kbuild_dir/lib/
install -m 0644 kernel/workqueue.c %buildroot%kbuild_dir/kernel/
install -m 0644 net/mac80211/{ieee80211_i,sta_info}.h %buildroot%kbuild_dir/net/mac80211/
%endif

# Install files required for building external modules (in addition to headers)
for f in \
	.config \
	Makefile \
	Module.symvers* \
	scripts/Kbuild.include \
	scripts/Makefile{,.{build,clean,host,lib,lto,mod*}} \
	scripts/bin2c \
	scripts/check{includes,version}.pl \
	scripts/conmakehash \
	scripts/depmod.sh \
	scripts/extract-ikconfig \
	scripts/gcc-* \
	scripts/kallsyms \
	scripts/ld-*.sh \
	scripts/makelst \
	scripts/mk{compile_h,makefile,version} \
	scripts/module-common.lds \
	scripts/pnmtologo \
	scripts/recordmcount.pl \
	scripts/basic/fixdep \
	scripts/genksyms/genksyms \
	scripts/kconfig/conf \
	scripts/mod/{modpost,mk_elfconfig} \
	gcc_version.inc
do
	if [ -f "$f" ]; then
		[ -x "$f" ] && mode=0755 || mode=0644
		install -Dp -m $mode {,%buildroot%kbuild_dir/}$f
	fi
done

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
make -j%__nprocs headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir
find %buildroot%kheaders_dir -type f -a \( -name .install -o -name ..install.cmd \) -delete

# Fix symlinks to kernel sources in /lib/modules
rm -f %buildroot%modules_dir/{build,source}
ln -s %kbuild_dir %buildroot%modules_dir/build

%if_with perf
%makeinstall_std -C tools/perf %perf_make_opts install-man
install -d -m 0755 %buildroot%_docdir/perf-%version
install -m 0644 tools/perf/{CREDITS,design.txt,Documentation/examples.txt} %buildroot%_docdir/perf-%version/
%endif

%if_with lkvm
%makeinstall_std -C tools/kvm %lkvm_make_opts
install -d -m 0755 %buildroot%_docdir/lkvm-%version
install -m 0644 tools/kvm/{CREDITS*,README,Documentation/*} %buildroot%_docdir/lkvm-%version/
%endif

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%flavour/
for I in Documentation/*; do
	case "$(basename "$I")" in
		DocBook)
%if_enabled htmldocs
			for J in "$I"/*.tmpl; do
				j=$(basename "$J" .tmpl)
				[ -d "$I/$j" ] || continue
				install -d -m 0755 %buildroot%_docdir/kernel-doc-%flavour/DocBook/"$j"
				install -m 0644 "$I/$j"/*.html %buildroot%_docdir/kernel-doc-%flavour/DocBook/"$j"/
				install -m 0644 "$I/$j.html" %buildroot%_docdir/kernel-doc-%flavour/DocBook/
			done
%endif
			;;
		[a-z][a-z]_[A-Z][A-Z]|Makefile|dontdiff) ;;
		*) cp -aL "$I" %buildroot%_docdir/kernel-doc-%flavour/ ;;
	esac
done
find %buildroot%_docdir/kernel-doc-%flavour -type f -name Makefile -delete
%if_enabled man
install -d %buildroot%kmandir
install -m 0644 Documentation/DocBook/man/* %buildroot%kmandir/
%endif
%endif

cd -

%if_with src
install -d -m 0755 %kernel_srcdir
t="%__nprocs"
XZ="xz"
[ $t = 1 ] || XZ=p$XZ
tar	--transform='s/^linux-%kversion/&-%flavour-%krelease/' \
	--owner=root --group=root --mode=u+w,go-w,go+rX \
	-T kernel-src-%flavour.list \
	-cf - | \
	$XZ -T$t -8e > %kernel_srcdir/linux-%kversion-%flavour-%krelease.tar.xz
%endif

rm -rf *.rpmmodlist{,~}
gen_rpmmodlist() {
	ls -d $@ | sed 's|^%buildroot||'
}
gen_rpmmodfile() {
	local F=$1.rpmmodlist
	shift
	gen_rpmmodlist $@ > $F
}
gen_rpmmodfile scsi-base \
%if "%sub_flavour" == "guest"
	%buildroot%modules_dir/kernel/drivers/scsi/{virtio*,{,lib}iscsi*,scsi_transport_iscsi.ko} \
%endif
	%buildroot%modules_dir/kernel/drivers/{scsi/{{*_mod,scsi_{tgt,transport_srp},vhba}.ko,osd,device_handler{,/scsi_dh.ko}},target/{iscsi,target_core_mod.ko}}
gen_rpmmodfile infiniband %buildroot%modules_dir/kernel/{drivers/{infiniband,scsi/scsi_transport_srp.ko},net/{9p/9pnet_rdma.ko,rds,sunrpc/xprtrdma}}
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/{message/fusion,scsi{,/device_handler}/*,target/*,vhost/vhost_scsi.ko} | \
	grep -Fxv -f scsi-base.rpmmodlist | \
	grep -Fxv -f infiniband.rpmmodlist | \
	grep -v '^%modules_dir/kernel/drivers/scsi/virtio.*' > scsi.rpmmodlist
mv scsi-base.rpmmodlist scsi-base.rpmmodlist~
gen_rpmmodfile ipmi %buildroot%modules_dir/kernel/drivers/{acpi/acpi_ipmi,char/ipmi,{acpi/acpi_ipmi,hwmon/i{bm,pmi}*}.ko}
%{?_enable_drm:gen_rpmmodfile drm %buildroot%modules_dir/kernel/drivers/gpu}
%{?_enable_fddi:gen_rpmmodfile fddi %buildroot%modules_dir/kernel/{drivers/net,net/802}/fddi*}
%{?_enable_usb_gadget:gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/usb/gadget/* | grep -xv '%modules_dir/kernel/drivers/usb/gadget/udc-core.ko' > usb-gadget.rpmmodlist}
%{?_enable_watchdog:gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/watchdog/* | grep -Ev '^%modules_dir/kernel/drivers/watchdog/(watch|soft)dog.ko$' > watchdog.rpmmodlist}
%if_enabled video
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/video/* | \
	grep -xv '%modules_dir/kernel/drivers/video/uvesafb.ko' | \
	grep -xv '%modules_dir/kernel/drivers/video/console' | \
	grep -xv '%modules_dir/kernel/drivers/video/sis' | \
	grep -xv '%modules_dir/kernel/drivers/video/backlight' | \
	grep -v '^%modules_dir/kernel/drivers/video/.*sys.*\.ko$' > video.rpmmodlist
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/video/backlight/* | grep -Ev '%modules_dir/kernel/drivers/video/(backlight/(apple_bl|lcd).ko$)' >> video.rpmmodlist
%endif
%if_enabled media
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/media/* | grep -xv '%modules_dir/kernel/drivers/media/media.ko' | grep -xv '%modules_dir/kernel/drivers/media/v4l2-core' > media.rpmmodlist
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/media/v4l2-core/* | grep -xv '%modules_dir/kernel/drivers/media/v4l2-core/videodev.ko' >> media.rpmmodlist
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/hid/hid-picolcd.ko >> media.rpmmodlist
%endif
%{?_enable_ide:gen_rpmmodfile ide %buildroot%modules_dir/kernel/drivers/{ide,leds/ledtrig-ide-disk.ko}}
%{?_enable_edac:gen_rpmmodfile edac %buildroot%modules_dir/kernel/drivers/edac}
%{?_enable_mtd:gen_rpmmodfile mtd %buildroot%modules_dir/kernel/{drivers/mtd,lib/bch.ko}}
gen_rpmmodfile input-extra \
	%{?_enable_joystick:%buildroot%modules_dir/kernel/drivers/input/joystick} \
	%{?_enable_tablet:%buildroot%modules_dir/kernel/drivers/input/tablet} \
	%{?_enable_touchscreen:%buildroot%modules_dir/kernel/drivers/input/touchscreen}
%if "%sub_flavour" != "guest"
%{?_enable_guest:gen_rpmmodfile guest %buildroot%modules_dir/kernel/{drivers/{virtio/virtio_{balloon,mmio,pci}.ko,{char{,/hw_random},net,block,scsi}/virtio*%{?_enable_drm:,gpu/drm/{cirrus,qxl,vmwgfx}}%{?_enable_hypervisor_guest:,misc/vmw_balloon.ko}%{?_enable_hyperv:,hv,input/serio/hyperv-*,hid/hid-hyperv.ko,net/hyperv,scsi/hv_storvsc.ko},platform/x86/pvpanic.ko},net/{9p/*_virtio.ko,vmw*}}}
%{?_enable_drm:grep -F -f drm.rpmmodlist guest.rpmmodlist | sed 's/^/%%exclude &/' >> drm.rpmmodlist}
%endif
sed -n '/^\//s/^/%%exclude &/p' *.rpmmodlist > exclude-drivers.rpmmodlist

%{?_enable_oprofile:%add_verify_elf_skiplist %modules_dir/vmlinux}

%if_with firmware
hardlink -c %buildroot%firmware_dir
%ifdef brp_strip_none
%brp_strip_none %firmware_dir/*
%else
%add_strip_skiplist %firmware_dir/*
%endif
%add_verify_elf_skiplist %firmware_dir/*
%endif

%{?_with_perf: %add_verify_elf_skiplist %_libdir/libperf-gtk.so}


%kernel_modules_package_post scsi

%kernel_modules_package_post infiniband

%kernel_modules_package_post ipmi

%{?_enable_edac:%kernel_modules_package_post edac}

%{?_enable_video:%kernel_modules_package_post video}

%{?_enable_usb_gadget:%kernel_modules_package_post usb-gadget}

%{?_enable_watchdog:%kernel_modules_package_post watchdog}

%{?_enable_mtd:%kernel_modules_package_post mtd}

%kernel_modules_package_post fs-extra

%kernel_modules_package_post input-extra

%kernel_modules_package_post net-extra

%{?_enable_oss:%kernel_modules_package_post oss}

%{?_enable_ide:%kernel_modules_package_post ide}

%{?_enable_drm:%kernel_modules_package_post drm}

%{?_enable_media:%kernel_modules_package_post media}

%{?_enable_alsa:%kernel_modules_package_post sound}

%if "%sub_flavour" != "guest"
%{?_enable_guest:%kernel_modules_package_post guest}
%endif

%{?_enable_kvm:%kernel_modules_package_post kvm}

%{?_enable_oprofile:%kernel_modules_package_post oprofile}

%ifdef extra_mods
%(for m in %extra_mods; do
cat <<__PACKAGE__
%kernel_extmods_package_post $m

__PACKAGE__
done)
%endif


%files -f exclude-drivers.rpmmodlist
/boot/*
%dir %modules_dir
%modules_dir/modules.order
%modules_dir/modules.builtin
%modules_dir/modules.softdep
%ghost %modules_dir/modules.alias*
%ghost %modules_dir/modules.dep
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols*
%ghost %modules_dir/modules.builtin.bin
%ghost %modules_dir/modules.devname
%modules_dir/modules.dep.inkernel
%dir %modules_dir/kernel
%modules_dir/kernel/arch
%modules_dir/kernel/block
%modules_dir/kernel/crypto
%modules_dir/kernel/drivers
%modules_dir/kernel/fs
%modules_dir/kernel/kernel
%modules_dir/kernel/lib
%modules_dir/kernel/mm
%modules_dir/kernel/net
%modules_dir/kernel/security
%if_enabled sound
%dir %modules_dir/kernel/sound
%{?_enable_pci:%modules_dir/kernel/sound/ac97_bus.ko}
%dir %modules_dir/kernel/sound/core
%modules_dir/kernel/sound/core/snd.ko
%modules_dir/kernel/sound/soundcore.ko
%exclude %modules_dir/kernel/drivers/usb/misc/emi*
%exclude %modules_dir/kernel/drivers/hid/hid-prodikeys.ko
%endif
%{?_enable_kvm:%exclude %modules_dir/kernel/arch/*/kvm}
%if_enabled oprofile
%exclude %modules_dir/vmlinux
%exclude %modules_dir/kernel/arch/*/oprofile
%endif
# extra fs
%exclude %modules_dir/kernel/fs/afs
%exclude %modules_dir/kernel/fs/adfs
%exclude %modules_dir/kernel/fs/affs
%exclude %modules_dir/kernel/fs/befs
%exclude %modules_dir/kernel/fs/bfs
%exclude %modules_dir/kernel/fs/coda
%exclude %modules_dir/kernel/fs/dlm
%exclude %modules_dir/kernel/fs/efs
%exclude %modules_dir/kernel/fs/freevxfs
%exclude %modules_dir/kernel/fs/gfs2
%exclude %modules_dir/kernel/fs/hpfs
%exclude %modules_dir/kernel/fs/lustre
%exclude %modules_dir/kernel/fs/minix
%exclude %modules_dir/kernel/fs/ncpfs
%exclude %modules_dir/kernel/fs/ocfs2
%exclude %modules_dir/kernel/fs/omfs
%exclude %modules_dir/kernel/fs/qnx?
%exclude %modules_dir/kernel/fs/sysv
%if_enabled mtd
%exclude %modules_dir/kernel/fs/jffs2
%exclude %modules_dir/kernel/fs/romfs
%exclude %modules_dir/kernel/fs/ubifs
%endif
# extra net
%exclude %modules_dir/kernel/net/802/p8023.ko
%{?_enable_arcnet:%exclude %modules_dir/kernel/drivers/net/arcnet}
%exclude %modules_dir/kernel/net/appletalk
%exclude %modules_dir/kernel/drivers/net/appletalk
%if_enabled atm
%exclude %modules_dir/kernel/net/atm
%exclude %modules_dir/kernel/drivers/atm
%exclude %modules_dir/kernel/drivers/usb/atm
%endif
%{?_enable_can:%exclude %modules_dir/kernel/net/can}
%{?_enable_can:%exclude %modules_dir/kernel/drivers/net/can}
%exclude %modules_dir/kernel/net/batman-adv
%{?_enable_caif:%exclude %modules_dir/kernel/net/caif}
%{?_enable_caif:%exclude %modules_dir/kernel/drivers/net/caif}
%if_enabled hamradio
%exclude %modules_dir/kernel/net/ax25
%exclude %modules_dir/kernel/net/netrom
%exclude %modules_dir/kernel/net/rose
%exclude %modules_dir/kernel/drivers/net/hamradio
%endif
%{?_enable_hippi:%exclude %modules_dir/kernel/drivers/net/hippi}
%exclude %modules_dir/kernel/drivers/net/dsa
%exclude %modules_dir/kernel/drivers/net/ieee802154
%exclude %modules_dir/kernel/drivers/net/plip
%exclude %modules_dir/kernel/drivers/net/slip/slip.ko
%exclude %modules_dir/kernel/net/dccp
%exclude %modules_dir/kernel/net/decnet
%exclude %modules_dir/kernel/net/dsa
%exclude %modules_dir/kernel/net/ieee802154
%exclude %modules_dir/kernel/net/ipx
%if_enabled irda
%exclude %modules_dir/kernel/net/irda
%exclude %modules_dir/kernel/drivers/net/irda
%endif
%if_enabled isdn
%exclude %modules_dir/kernel/net/bluetooth/cmtp
%exclude %modules_dir/kernel/drivers/isdn
%endif
%exclude %modules_dir/kernel/net/wimax
%exclude %modules_dir/kernel/drivers/net/wimax
%exclude %modules_dir/kernel/net/lapb
%exclude %modules_dir/kernel/net/llc/llc2.ko
%exclude %modules_dir/kernel/net/mac802154
%exclude %modules_dir/kernel/net/phonet
%exclude %modules_dir/kernel/drivers/net/usb/cdc-phonet.ko
%exclude %modules_dir/kernel/net/rxrpc
%exclude %modules_dir/kernel/net/sctp
%exclude %modules_dir/kernel/net/tipc
%exclude %modules_dir/kernel/drivers/net/wan
%exclude %modules_dir/kernel/drivers/tty/synclink*
%{?_enable_pcmcia:%exclude %modules_dir/kernel/drivers/char/pcmcia/synclink*}
%exclude %modules_dir/kernel/net/x25


%kernel_modules_package_files scsi
%{?_enable_hyperv:%exclude %modules_dir/kernel/drivers/scsi/hv_storvsc.ko}


%kernel_modules_package_files infiniband

%kernel_modules_package_files ipmi

%kernel_modules_package_files input-extra

%{?_enable_edac:%kernel_modules_package_files edac}

%{?_enable_video:%kernel_modules_package_files video}

%{?_enable_usb_gadget:%kernel_modules_package_files usb-gadget}

%{?_enable_mtd:%kernel_modules_package_files mtd}

%{?_enable_watchdog:%kernel_modules_package_files watchdog}


%files -n kernel-modules-fs-extra-%flavour
%modules_dir/kernel/fs/afs
%modules_dir/kernel/fs/adfs
%modules_dir/kernel/fs/affs
%modules_dir/kernel/fs/befs
%modules_dir/kernel/fs/bfs
#modules_dir/kernel/fs/ceph
%modules_dir/kernel/fs/coda
%modules_dir/kernel/fs/dlm
%modules_dir/kernel/fs/efs
%modules_dir/kernel/fs/freevxfs
%modules_dir/kernel/fs/gfs2
%modules_dir/kernel/fs/hpfs
%modules_dir/kernel/fs/lustre
%modules_dir/kernel/fs/minix
%modules_dir/kernel/fs/ncpfs
%modules_dir/kernel/fs/ocfs2
%modules_dir/kernel/fs/omfs
%modules_dir/kernel/fs/qnx?
%modules_dir/kernel/fs/sysv
%if_enabled mtd
%modules_dir/kernel/fs/jffs2
%modules_dir/kernel/fs/romfs
%modules_dir/kernel/fs/ubifs
%endif


%files -n kernel-modules-net-extra-%flavour
%modules_dir/kernel/net/802/p8023.ko
%{?_enable_arcnet:%modules_dir/kernel/drivers/net/arcnet}
%modules_dir/kernel/net/appletalk
%modules_dir/kernel/drivers/net/appletalk
%modules_dir/kernel/net/batman-adv
%if_enabled atm
%modules_dir/kernel/net/atm
%modules_dir/kernel/drivers/atm
%modules_dir/kernel/drivers/usb/atm
%endif
%if_enabled caif
%modules_dir/kernel/net/caif
%modules_dir/kernel/drivers/net/caif
%endif
%if_enabled can
%modules_dir/kernel/net/can
%modules_dir/kernel/drivers/net/can
%endif
%if_enabled fddi
%modules_dir/kernel/net/802/fddi.ko
%modules_dir/kernel/drivers/net/fddi
%endif
%if_enabled hamradio
%modules_dir/kernel/net/ax25
%modules_dir/kernel/net/netrom
%modules_dir/kernel/net/rose
%modules_dir/kernel/drivers/net/hamradio
%endif
%{?_enable_hippi:%modules_dir/kernel/drivers/net/hippi}
%modules_dir/kernel/drivers/net/dsa
%modules_dir/kernel/drivers/net/ieee802154
%modules_dir/kernel/drivers/net/plip
%modules_dir/kernel/drivers/net/slip/slip.ko
#modules_dir/kernel/net/ceph
%modules_dir/kernel/net/dccp
%modules_dir/kernel/net/decnet
%modules_dir/kernel/net/dsa
%modules_dir/kernel/net/ieee802154
%modules_dir/kernel/net/ipx
%if_enabled irda
%modules_dir/kernel/net/irda
%modules_dir/kernel/drivers/net/irda
%endif
%if_enabled isdn
%modules_dir/kernel/net/bluetooth/cmtp
%modules_dir/kernel/drivers/isdn
%endif
%modules_dir/kernel/net/wimax
%modules_dir/kernel/drivers/net/wimax
%modules_dir/kernel/net/lapb
%modules_dir/kernel/net/llc/llc2.ko
%modules_dir/kernel/net/mac802154
%modules_dir/kernel/net/phonet
%modules_dir/kernel/drivers/net/usb/cdc-phonet.ko
%modules_dir/kernel/net/rxrpc
%modules_dir/kernel/net/sctp
%modules_dir/kernel/net/tipc
%modules_dir/kernel/drivers/net/wan
%modules_dir/kernel/drivers/tty/synclink*
%{?_enable_pcmcia:%modules_dir/kernel/drivers/char/pcmcia/synclink*}
%modules_dir/kernel/net/x25


%if_enabled oss
%files -n kernel-modules-oss-%flavour
%modules_dir/kernel/sound/oss
%modules_dir/kernel/sound/sound_firmware.ko
%endif


%if_enabled alsa
%files -n kernel-modules-sound-%flavour
%modules_dir/kernel/sound
%modules_dir/kernel/drivers/usb/misc/emi*
%modules_dir/kernel/drivers/hid/hid-prodikeys.ko
%{?_enable_oss:%exclude %modules_dir/kernel/sound/oss}
%exclude %modules_dir/kernel/sound/*.ko
%exclude %modules_dir/kernel/sound/core/snd.ko
%endif


%if "%sub_flavour" != "guest"
%{?_enable_guest:%kernel_modules_package_files guest}
%if_enabled drm
%dir %modules_dir/kernel/drivers/gpu
%dir %modules_dir/kernel/drivers/gpu/drm
%endif
%endif


%if_enabled kvm
%files -n kernel-modules-kvm-%flavour
%modules_dir/kernel/arch/*/kvm
%endif


%files -n kernel-headers-%flavour
%kheaders_dir


%{?_enable_ide:%kernel_modules_package_files ide}

%{?_enable_drm:%kernel_modules_package_files drm}

%{?_enable_media:%kernel_modules_package_files media}


%if_enabled oprofile
%files -n kernel-modules-oprofile-%flavour
%modules_dir/vmlinux
%modules_dir/kernel/arch/*/oprofile
%endif


%if_with firmware
%files -n firmware-kernel-%flavour
%dir /lib/firmware
%firmware_dir
%endif


%if_with perf
%files -n perf
%doc %_docdir/perf-%version
%_sysconfdir/bash_completion.d
%_bindir/perf
%_bindir/trace
%_libexecdir/perf
%_libdir/libperf*
%_man1dir/*
%endif


%if_with lkvm
%files -n lkvm
%doc %_docdir/lkvm-%version
%_bindir/lkvm
%endif


%ifdef extra_mods
%(for m in %extra_mods; do
cat <<__PACKAGE__
%%files -n kernel-modules-$m-%flavour -f linux-%kversion/external/$m.rpmmodlist

__PACKAGE__
done)
%endif


%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build


%if_enabled docs
%files -n kernel-doc-%flavour
%doc %_docdir/kernel-doc-%flavour
%{?_enable_htmldocs:%exclude %_docdir/kernel-doc-%flavour/DocBook}


%if_enabled htmldocs
%files -n kernel-docbook-%flavour
%doc %dir %_docdir/kernel-doc-%flavour
%doc %_docdir/kernel-doc-%flavour/DocBook
%endif


%if_enabled man
%files -n kernel-man-%flavour
%kmandir
%endif
%endif


%if_with src
%files -n kernel-src-%flavour
%_usrsrc/kernel
%endif


%changelog
* Sun Apr 27 2014 Led <led@altlinux.ru> 3.13.11-alt5
- updated:
  + fix-mm--zswap
  + fix-scripts-mod--modpost
  + feat-block--bfq-iosched
  + feat-mm--zcache
- enabled remove_unused_exports

* Sat Apr 26 2014 Led <led@altlinux.ru> 3.13.11-alt4
- updated:
  + feat-kernel-vserver
  + feat-tools--kvm
- disabled remove_unused_exports

* Fri Apr 25 2014 Led <led@altlinux.ru> 3.13.11-alt3
- updated:
  + feat-kernel-vserver

* Thu Apr 24 2014 Led <led@altlinux.ru> 3.13.11-alt2
- added:
  + fix-scripts-mod--modpost
- added optional removing unused exports
- enabled remove_unused_exports
- fglrx 14.10

* Wed Apr 23 2014 Led <led@altlinux.ru> 3.13.11-alt1
- 3.13.11
- removed:
  + fix-kernel--user_namespace
- updated:
  + feat-tools--kvm

* Tue Apr 22 2014 Led <led@altlinux.ru> 3.13.10-alt8
- added:
  + fix-kernel--user_namespace
- enabled lto

* Sun Apr 20 2014 Led <led@altlinux.ru> 3.13.10-alt7
- updated:
  + fix-tools-lib--traceevent
  + feat-drivers-block--btier
  + feat-drivers-platform--omnibook
- added:
  + fix-drivers-isdn--icn
  + fix-drivers-md--bcache
  + fix-fs-f2fs

* Sun Apr 20 2014 Led <led@altlinux.ru> 3.13.10-alt6
- updated:
  + fix-virt-kvm--kvm
  + feat-drivers-block--btier
  + feat-scripts--lto
- added:
  + fix-drivers-cpufreq--speedstep-smi
  + fix-tools-lib--traceevent

* Sun Apr 20 2014 Led <led@altlinux.ru> 3.13.10-alt5
- updated:
  + feat-lib--unwind
  + feat-fs-squashfs--write
- added:
  + fix-fs-ramfs
  + feat-scripts--lto

* Fri Apr 18 2014 Led <led@altlinux.ru> 3.13.10-alt4
- added:
  + feat-fs-squashfs--write

* Thu Apr 17 2014 Led <led@altlinux.ru> 3.13.10-alt3
- updated:
  + fix-drivers-base
  + fix-drivers-spi
  + fix-net-core
  + feat-kernel-vserver
- added:
  + fix-drivers-char-ipmi--ipmi_si
  + fix-drivers-mtd-nand
  + fix-drivers-regulator
  + fix-drivers-scsi--scsi_transport_srp
  + fix-kernel-rcu
  + fix-include-linux
  + fix-mm--slab

* Tue Apr 15 2014 Led <led@altlinux.ru> 3.13.10-alt2
- added:
  + fix-drivers-infiniband-hw--ocrdma
  + fix-kernel-apic--apic
- fixed spec

* Tue Apr 15 2014 Led <led@altlinux.ru> 3.13.10-alt1
- 3.13.10
- updated:
  + fix-drivers-scsi--scsi_mod
  + feat-drivers-hwmon--ipmisensors
  + feat-drivers-block--btier
  + feat-fs-tux3
  + feat-tools--kvm
- added:
  + fix-drivers-gpu-drm--drm_kms_helper
  + fix-drivers-leds--leds-pwm
  + fix-drivers-net-can--janz-ican3
  + fix-drivers-net-wireless--wl3501_cs
  + fix-drivers-scsi--advansys
  + fix-drivers-scsi--ch
  + fix-drivers-virtio--virtio_balloon
  + fix-drivers-watchdog--sbc8360
  + fix-net-ipv4-netfilter--ip_tables
  + fix-net-ipv6--ipv6
  + fix-net-ipv6-netfilter--ip6_tables
- disabled I2C_SI470X

* Sun Apr 06 2014 Led <led@altlinux.ru> 3.13.9-alt2
- removed:
  + fix-drivers-mfd--arizona-core
- updated:
  + fix-mm--zswap
  + feat-mm--zcache
- added:
  + fix-drivers-gpio--gpio-sx150x
  + fix-drivers-mfd--arizona
  + fix-drivers-regulator--88pm8607

* Sun Apr 06 2014 Led <led@altlinux.ru> 3.13.9-alt1
- updated:
  + feat-firmware--bfa
  + feat-firmware--bna
  + feat-firmware--brcmfmac
  + feat-firmware--wl1251
- added:
  + fix-drivers-gpio--gpio-tps6586x
  + fix-drivers-gpio--gpio-tps65910
  + fix-drivers-mfd--max776xx
  + fix-drivers-mfd--max8925
  + fix-drivers-mfd--max899x
  + fix-drivers-mfd--tps65090
  + fix-drivers-mfd--tps6586x
  + fix-drivers-mfd--tps65910
  + feat-firmware--wcn36xx

* Sat Apr 05 2014 Led <led@altlinux.ru> 3.13.9-alt0
- 3.13.9
- updated:
  + fix-fs-pstore--pstore
  + fix-net-netfilter--nf_conntrack_proto_dccp
  + feat-kernel-vserver
  + feat-mm--uksm
- added:
  + fix-drivers-bluetooth--hci_vhci
  + fix-drivers-gpio--gpio-palmas
  + fix-drivers-gpio--gpio-rc5t583
  + fix-drivers-gpio--gpio-stmpe
  + fix-drivers-gpio--gpio-tc3589x
  + fix-drivers-iio-adc--lp8788-adc
  + fix-drivers-mfd
  + fix-drivers-mfd--88pm860x
  + fix-drivers-mfd--ab3100
  + fix-drivers-mfd--abx500
  + fix-drivers-mfd--lp8788
  + fix-drivers-mfd--palmas
  + fix-drivers-mfd--stmpe
  + fix-drivers-mfd--stmpe-i2c
  + fix-drivers-mfd--stmpe-spi
  + fix-drivers-mfd--tc3589x
  + fix-drivers-mfd--wm831x
  + fix-drivers-mfd--wm831x-i2c
  + fix-drivers-mfd--wm831x-spi
  + fix-drivers-mfd--wm8350
  + fix-drivers-mfd--wm8350-i2c
  + fix-drivers-mfd--wm8400
  + fix-drivers-net-ethernet-oki-semi--pch_gbe
- disabled:
  + DPM_WATCHDOG
  + SECURITY_APPARMOR_HASH
- enabled:
  + DOUBLEFAULT

* Fri Apr 04 2014 Led <led@altlinux.ru> 3.13.8-alt0
- initial build based on kernel-image-led-ws-3.10.35-alt6
