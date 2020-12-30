# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define ktarget  native
%define kflavour clr-%ktarget
%define kernel_source_version 5.9
%define kernel_base_version 5.9.16

Name:		kernel-image-%kflavour
Version:	%kernel_base_version
Release:	alt1.clr1009
%define flavour         %( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour    %( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour     %( s='%flavour'; printf %%s "${s#*-}" )
License:	GPL-2.0
Summary:	Intel optimized Clear Linux %sub_flavour kernel
Url:		http://www.kernel.org/
Vcs:		https://github.com/clearlinux-pkgs/linux
Group:		System/Kernel and hardware
Packager:	Kernel Maintainers Team <kernel@packages.altlinux.org>

%define kversion %version-%kflavour-%release
%add_verify_elf_skiplist /lib/modules/%kversion/*

Source1:	config
Source2:	cmdline
Patch0:		%name-%version-%release.patch

ExclusiveOS:	Linux
ExclusiveArch:	x86_64

BuildRequires(pre): rpm-build-kernel
BuildRequires: bc
BuildRequires: flex
BuildRequires: kernel-source-%kernel_source_version = 1.0.0
BuildRequires: kmod
BuildRequires: libdb4-devel
BuildRequires: libelf-devel
BuildRequires: lz4
BuildRequires: lzma-utils
BuildRequires: module-init-tools >= 3.16
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: rsync

AutoReqProv:	no

#cve.start cve patches from 0001 to 050
#cve.end

#mainline: Mainline patches, upstream backport and fixes from 0051 to 0099
Patch0051: 0051-sched-fair-Ignore-cache-hotness-for-SMT-migration.patch
#mainline.end

#Serie.clr 01XX: Clear Linux patches
Patch0101: 0101-i8042-decrease-debug-message-level-to-info.patch
Patch0102: 0102-increase-the-ext4-default-commit-age.patch
Patch0103: 0103-silence-rapl.patch
Patch0104: 0104-pci-pme-wakeups.patch
Patch0105: 0105-ksm-wakeups.patch
Patch0106: 0106-intel_idle-tweak-cpuidle-cstates.patch
Patch0107: 0107-bootstats-add-printk-s-to-measure-boot-time-in-more-.patch
Patch0108: 0108-smpboot-reuse-timer-calibration.patch
Patch0109: 0109-initialize-ata-before-graphics.patch
Patch0110: 0110-give-rdrand-some-credit.patch
Patch0111: 0111-ipv4-tcp-allow-the-memory-tuning-for-tcp-to-go-a-lit.patch
Patch0112: 0112-kernel-time-reduce-ntp-wakeups.patch
Patch0113: 0113-init-wait-for-partition-and-retry-scan.patch
Patch0114: 0114-print-fsync-count-for-bootchart.patch
Patch0115: 0115-add-boot-option-to-allow-unsigned-modules.patch
Patch0116: 0116-enable-stateless-firmware-loading.patch
Patch0117: 0117-migrate-some-systemd-defaults-to-the-kernel-defaults.patch
Patch0118: 0118-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0119: 0119-add-scheduler-turbo3-patch.patch
Patch0120: 0120-use-lfence-instead-of-rep-and-nop.patch
Patch0121: 0121-do-accept-in-LIFO-order-for-cache-efficiency.patch
Patch0122: 0122-locking-rwsem-spin-faster.patch
Patch0123: 0123-ata-libahci-ignore-staggered-spin-up.patch
Patch0124: 0124-print-CPU-that-faults.patch
Patch0125: 0125-x86-microcode-Force-update-a-uCode-even-if-the-rev-i.patch
Patch0126: 0126-x86-microcode-echo-2-reload-to-force-load-ucode.patch
Patch0127: 0127-fix-bug-in-ucode-force-reload-revision-check.patch
Patch0128: 0128-nvme-workaround.patch
Patch0129: 0129-don-t-report-an-error-if-PowerClamp-run-on-other-CPU.patch
#Serie.end

# https://docs.01.org/clearlinux/latest/guides/clear/compatible-kernels.html
%description
Our build of the Linux kernel from Clear Linux Project is highly tuned
for x86_64 platform.

%package -n kernel-headers-%flavour
License:	GPL-2.0
Summary:	The Linux kernel header files
Group:		Development/Kernel
AutoReqProv:	no

%description -n kernel-headers-%flavour
Linux kernel headers files

%package -n kernel-headers-modules-%flavour
License:	GPL-2.0
Summary:	The Linux kernel development files
Group:		Development/Kernel
AutoReqProv:	no

%description -n kernel-headers-modules-%flavour
Linux kernel build files

%prep
%setup -cT -n kernel-image-%kflavour
rm -rf kernel-source-%kernel_source_version
tar xf %kernel_src/kernel-source-%kernel_source_version.tar
%setup -D -T -n kernel-image-%kflavour/kernel-source-%kernel_source_version
%patch0 -p1

#cve.patch.start cve patches
#cve.patch.end

#mainline.patch.start Mainline patches, upstream backport and fixes
%patch0051 -p1
#mainline.patch.end

#Serie.patch.start Clear Linux patches
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1
%patch0119 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1
%patch0127 -p1
%patch0128 -p1
%patch0129 -p1
#Serie.patch.end

cp %{SOURCE1} .

%build
BuildKernel() {

    Target=$1
    Arch=x86_64
    ExtraVer="-%kflavour-%release"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make O=${Target} -s mrproper
    cp config ${Target}/.config
    scripts/config --file ${Target}/.config -e DEBUG_INFO

    make O=${Target} -s ARCH=${Arch} olddefconfig
    make O=${Target} ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} %{?sparse_mflags}
}

BuildKernel %{ktarget}

%install

InstallKernel() {

    Target=$1
    Kversion=$2
    Arch=x86_64
    KernelDir=%{buildroot}/boot
    DevDir=%{buildroot}/usr/src/linux-${Kversion}

    mkdir   -p ${KernelDir}
    install -m 644 ${Target}/.config	${KernelDir}/config-${Kversion}
    install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
    install -m 644 %{SOURCE2}		${KernelDir}/cmdline-${Kversion}
    cp	${Target}/arch/x86/boot/bzImage ${KernelDir}/vmlinuz-${Kversion}
    chmod 755 ${KernelDir}/vmlinuz-${Kversion}

    mkdir -p %{buildroot}/lib/modules
    make O=${Target} -s ARCH=${Arch} INSTALL_MOD_PATH=%buildroot modules_install %{?_smp_mflags}

    rm -f %{buildroot}/lib/modules/${Kversion}/build
    rm -f %{buildroot}/lib/modules/${Kversion}/source

    mkdir -p ${DevDir}
    find . -type f -a '(' -name 'Makefile*' -o -name 'Kbuild*' -o -name 'Kconfig*' ')' -exec cp -t ${DevDir} --parents -pr {} +
    find . -type f -a '(' -name '*.sh' -o -name '*.pl' ')' -exec cp -t ${DevDir} --parents -pr {} +
    cp -t ${DevDir} -pr ${Target}/{Module.symvers,tools}
    ln -s ../../../boot/config-${Kversion} ${DevDir}/.config
    ln -s ../../../boot/System.map-${Kversion} ${DevDir}/System.map
    cp -t ${DevDir} --parents -pr arch/x86/include
    cp -t ${DevDir}/arch/x86/include -pr ${Target}/arch/x86/include/*
    cp -t ${DevDir}/include -pr include/*
    cp -t ${DevDir}/include -pr ${Target}/include/*
    cp -t ${DevDir} --parents -pr scripts/*
    cp -t ${DevDir}/scripts -pr ${Target}/scripts/*
    find  ${DevDir}/scripts -type f -name '*.[cho]' -exec rm -v {} +
    find  ${DevDir} -type f -name '*.cmd' -exec rm -v {} +
    # Cleanup any dangling links
    find ${DevDir} -type l -follow -exec rm -v {} +

    make headers_install INSTALL_HDR_PATH=%buildroot%_prefix/include/linux-%version-%flavour
    ln -s /usr/src/linux-${Kversion} %buildroot/lib/modules/${Kversion}/build
}

InstallKernel %{ktarget} %{kversion}

%files
/boot/config-%{kversion}
/boot/cmdline-%{kversion}
/boot/System.map-%{kversion}
/boot/vmlinuz-%{kversion}
%dir /lib/modules/%{kversion}
/lib/modules/%{kversion}/kernel
/lib/modules/%{kversion}/modules.*

%files -n kernel-headers-%flavour
%_prefix/include/linux-%version-%flavour

%files -n kernel-headers-modules-%flavour
/lib/modules/%{kversion}/build
/usr/src/linux-%{kversion}

%changelog
* Wed Dec 30 2020 Vitaly Chikunov <vt@altlinux.org> 5.9.16-alt1.clr1009
- Update to 5.9.16-1009 (2020-12-21).
- Fixed module signing (by rpm-build 4.0.4-alt152).
- Fix kernel-headers-modules package (add absent .config and System.map).

* Sat Oct 31 2020 Vitaly Chikunov <vt@altlinux.org> 5.9.1-alt1.clr992
- First import of version 5.9.1-992 (2020-10-17).
