# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
#%%def_without check

%define ktarget std-kvm
#%%define ktarget vm
#%%define ktarget virtual

%define kflavour %ktarget
%define krelease %release

%define kernel_base_version     5.10
%define kernel_sublevel .176
%define kernel_extra_version    %nil

%define kernel_extra_version_numeric 1.0.0

# ClearLinux kvm: https://raw.githubusercontent.com/clearlinux-pkgs/linux-kvm/master/config
# FireCracker: https://raw.githubusercontent.com/firecracker-microvm/firecracker/master/resources/microvm-kernel-x86_64.config
# Ubuntu virtual: https://kernel.ubuntu.com/~kernel-ppa/configs/natty/amd64-config.flavour.virtual

Name: kernel-image-%kflavour
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
Release: alt1

%define flavour         %( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour    %( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour     %( s='%flavour'; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version    %__gcc_version_base

License: GPL-2.0
Summary: Linux kernel with Clear Linux KVM config for running inside KVM
Url: http://www.kernel.org/
Group: System/Kernel and hardware
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: %name-%version-%release.patch

%define kversion %kernel_base_version%kernel_sublevel%kernel_extra_version
%define modules_dir      /lib/modules/%kversion-%flavour-%krelease
%add_verify_elf_skiplist %modules_dir/*

Source1: config
#Source2: cmdline

ExclusiveOS:	Linux
ExclusiveArch:	x86_64

Provides: kernel-image-clr-kvm = %EVR
Obsoletes: kernel-image-clr-kvm < %version

BuildRequires(pre): rpm-build-kernel
BuildRequires: bc
BuildRequires: flex
BuildRequires: gcc%kgcc_version gcc%kgcc_version-c++
BuildRequires: gcc%kgcc_version-plugin-devel libgmp-devel libmpc-devel
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric
BuildRequires: kmod
BuildRequires: libdb4-devel
BuildRequires: libelf-devel
BuildRequires: lz4
BuildRequires: lzma-utils
BuildRequires: module-init-tools >= 3.16
BuildRequires: openssl
BuildRequires: openssl-devel
%if 0%{?!_without_check:1}
%define qemu_pkg x86
BuildRequires: qemu-system-%qemu_pkg-core ipxe-roms-qemu glibc-devel-static
%endif

AutoReqProv: no

%description
This Linux kernel flavour is intended to be run as a guest in a virtual environment.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -p1

cp %{SOURCE1} .

%build
export NPROCS=%__nprocs
export ARCH=%base_arch
Target=%{ktarget}
Arch=%base_arch
ExtraVer="-%kflavour-%release"

perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

make O=${Target} -s mrproper
cp config ${Target}/.config

make O=${Target} -s ARCH=${Arch} olddefconfig
#make O=${Target} -s ARCH=${Arch} tinyconfig
make O=${Target} -s ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} %{?sparse_mflags} vmlinux bzImage

make O=${Target} -s ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} %{?sparse_mflags} modules

%install

Target=%{ktarget}
Kversion=%kversion-%flavour-%krelease
Arch=%base_arch
KernelDir=%{buildroot}/boot
ModulesDir=%buildroot%modules_dir
DevDir=%{buildroot}/usr/src/linux-${Kversion}

mkdir   -p ${KernelDir}
install -m 644 ${Target}/.config	${KernelDir}/config-${Kversion}
install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
# install -m 644 %%{SOURCE2}		${KernelDir}/cmdline-${Kversion}
install -m 755 ${Target}/arch/%base_arch/boot/bzImage ${KernelDir}/vmlinuz-${Kversion}
install -m 755 ${Target}/vmlinux ${KernelDir}/vmlinux-${Kversion}
# mkdir   -p ${ModulesDir}/kernel
make O=${Target} -s ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y modules_install INSTALL_MOD_PATH=%buildroot
rm -f ${ModulesDir}/{build,source}

%check
KernelVer=%kversion-%flavour-%krelease
mkdir -p test
cd test
msg='Booted successfully'
gcc -static -xc -o init - <<__EOF__
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

echo "init" | cpio -H newc -o | gzip > initrd.img

qemu_arch=%base_arch
qemu_opts=""
timeout --foreground 600 qemu-system-"$qemu_arch" $qemu_opts \
	-bios bios.bin \
        -nographic -no-reboot -m 256M \
	-kernel %buildroot/boot/vmlinuz-$KernelVer \
        -append "console=ttyS0 panic=-1 no_timer_check debug" \
	-initrd initrd.img > boot.log &&
grep -q "^$msg" boot.log &&
grep -qE '^(\[ *[0-9]+\.[0-9]+\] *)?reboot: Power down' boot.log || {
        cat >&2 boot.log
        echo >&2 'Marker not found'
        exit 1
}

%files
/boot/config-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/vmlinux-%kversion-%flavour-%krelease
/boot/vmlinuz-%kversion-%flavour-%krelease
%dir %modules_dir/
%defattr(0600,root,root,0700)
%modules_dir/*

%changelog
* Wed Mar 29 2023 Andrew A. Vasilyev <andy@altlinux.org> 5.10.176-alt1
- 5.10.176

* Fri Mar 10 2023 Andrew A. Vasilyev <andy@altlinux.org> 5.10.172-alt1
- 5.10.172

* Fri Feb 17 2023 Andrew A. Vasilyev <andy@altlinux.org> 5.10.168-alt1
- 5.10.168

* Mon Jan 16 2023 Andrew A. Vasilyev <andy@altlinux.org> 5.10.163-alt1
- 5.10.163

* Wed Dec 14 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.158-alt1
- 5.10.158

* Tue Dec 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.157-alt1
- 5.10.157

* Fri Nov 11 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.154-alt1
- 5.10.154

* Mon Oct 10 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.147-alt1
- 5.10.147

* Fri Sep 23 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.144-alt1
- 5.10.144

* Tue Aug 09 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.135-alt1
- 5.10.135

* Sun Jul 17 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.130-alt1
- 5.10.130

* Sat Jul 09 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.128-alt1
- 5.10.128

* Tue Jun 28 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.125-alt1
- 5.10.125

* Tue Jun 21 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.123-alt1
- 5.10.123

* Fri May 20 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.117-alt1
- 5.10.117

* Mon Apr 04 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.109-alt1
- 5.10.109

* Fri Mar 04 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.102-alt1
- 5.10.102

* Tue Feb 01 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.95-alt1
- 5.10.95

* Fri Jan 14 2022 Andrew A. Vasilyev <andy@altlinux.org> 5.10.91-alt1
- 5.10.91

* Fri Dec 17 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.85-alt1
- 5.10.85

* Fri Nov 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.80-alt1
- 5.10.80

* Thu Nov 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.77-alt1
- 5.10.77

* Thu Oct 07 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.71-alt1
- 5.10.71

* Tue Sep 28 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.69-alt1
- 5.10.69

* Sun Sep 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.66-alt1
- 5.10.66

* Wed Sep 15 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.64-alt1
- 5.10.64
- %%check vmlinuz kernel, not vmlinux one

* Wed Sep 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.62-alt1
- 5.10.62

* Sat Aug 14 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.58-alt1
- 5.10.58

* Mon Jul 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.53-alt1
- 5.10.53

* Thu Jun 03 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.42-alt1
- 5.10.42

* Sat Apr 24 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.32-alt1
- 5.10.32

* Tue Apr 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.10.29-alt1
- 5.10.29

* Sun Apr 11 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.4.111-alt1
- 5.4.111
- change kernel name to kernel-image-std-kvm (Closes: #39908)

* Fri Apr 09 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.4.109-alt1
- 5.4.109

* Fri Mar 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.4.107-alt1
- 5.4.107

* Mon Mar 22 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.4.105-alt1
- 5.4.105

* Fri Mar 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.4.102-alt1
- 5.4.102

* Wed Jan 20 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.4.91-alt1
- 5.4.91

* Mon Dec 21 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.4.85-alt1
- 5.4.85

* Wed Dec 16 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.4.84-alt1
- 5.4.84

* Wed Dec 16 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.4.83-alt1
- 5.4.83

* Fri Dec 04 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.4.81-alt1
- 5.4.81

* Wed Nov 11 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.4.80-alt1
- initial build for ALT

