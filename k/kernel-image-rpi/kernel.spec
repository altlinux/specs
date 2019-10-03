# must be the same as in .config
%define flavour -rpi

%define prerelease .4
#%%define prerelease %nil

%define kgcc_version 8
%brp_strip_none /boot/*

Name: kernel-image-rpi
Version: 4.19.71
Release: alt0%prerelease
# Release: alt1
Summary: The Linux kernel
License: GPL
Group: System/Kernel and hardware
URL: https://www.kernel.org/
# https://github.com/raspberrypi/linux/ not yet merged to upstream
ExclusiveArch: aarch64

%define karch arm64

Source0: linux-%version.tar
#.xz

BuildRequires: gcc%kgcc_version
BuildRequires: bc coreutils flex
BuildRequires: openssl
BuildRequires: libelf-devel libssl-devel

Provides: kernel = %version-%release
Provides: kernel-image = %version-%release

%description
%summary for network and embedded ARM devices

%define KernelVer %version%flavour-%release
%define dts_dir /lib/devicetree/%KernelVer
%define modules_dir /lib/modules/%KernelVer
%define kheaders_dir /usr/src/linux-%version-headers

%add_verify_elf_skiplist %dts_dir/*
%add_findreq_skiplist %dts_dir/*

%package -n kernel-headers%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Provides: kernel-headers = %version-%release
%description -n kernel-headers%flavour
This package contains Linux kernel headers for building userspace programs

%prep
%setup -n linux-%version
# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc


%build
%make_build mrproper
cp kernel-%_arch.config .config
sed -i -re '/-Wredundant-decls/d' tools/scripts/Makefile.include
%make_build KERNELRELEASE=%KernelVer all modules
%make_build dtbs
# overlays are built in arch/arm directory; move them to arch/arm64
rm -f arch/%karch/boot/dts/overlays \
	&& mv arch/arm/boot/dts/overlays arch/%karch/boot/dts/overlays
# wipe symlinks and other garbage
find arch/%karch/boot/dts -not -type d -not -type f -delete
find arch/%karch/boot/dts -type f \
	-not -name '*.dtb' \
	-not -name '*.dtbo' \
	-delete
# remove empty directories
find arch/%karch/boot/dts -type d -empty -delete

%install
rm -rf %buildroot
umask 022
mkdir -p %buildroot
# the kernel image
install -Dp -m644 arch/%karch/boot/Image \
	%buildroot/boot/linux-%version

install -Dp -m644 System.map %buildroot/boot/System.map-%KernelVer
install -Dp -m644 .config %buildroot/boot/config-%KernelVer

# modules directory
mkdir -p %buildroot%modules_dir/kernel
# %make INSTALL_MOD_PATH=%buildroot INSTALL_MOD_STRIP=1 modules_install
# circumvent broken modules_install
mkdir -p `find . -type f -name '*.ko' -exec dirname '{}' '+' | sort | uniq | sed -re 's,^.,%buildroot%modules_dir/kernel,g'`
find . -type f -name '*.ko' | sed -re 's,^..,,g' | cpio -p %buildroot%modules_dir/kernel

rm -f %buildroot%modules_dir/{build,source}

# may be used by bootloaders like extlinux
ln -sf linux-%version %buildroot/boot/linux

# avoid depmod complaints on boot
touch %buildroot%modules_dir/modules.{builtin,dep,order}
touch %buildroot%modules_dir/modules.{alias,builtin,dep,symbols}.bin

# headers directories
mkdir -pm755 %buildroot%kheaders_dir/include
cp -ra include/asm-generic include/linux %buildroot%kheaders_dir/include/
mkdir -pm755 %buildroot%kheaders_dir/arch/%karch/include
cp -ra arch/%karch/include/asm %buildroot%kheaders_dir/arch/%karch/include/

# devicetree directory
mkdir -p %buildroot%dts_dir
# cp -ra arch/%karch/boot/dts/* %buildroot%dts_dir/
find arch/%karch/boot/dts -type f -name \*.dtb |xargs -iz install -pm0644 z %buildroot%dts_dir

%clean
rm -rf %buildroot


%post -n kernel-image%flavour
# avoid complaints from depmod
test -f %modules_dir/modules.builtin || touch %modules_dir/modules.builtin
test -f %modules_dir/modules.dep || touch %modules_dir/modules.dep
test -f %modules_dir/modules.order || touch %modules_dir/modules.order


%post -n kernel-headers%flavour
# there may be different kernel sources and headers
test -d /usr/src/linux \
|| ln -sf linux-%version-headers /usr/src/linux
# in general, this should work for all other kernel sources and headers
test -d /usr/include/asm \
|| ln -sf ../src/linux/arch/%karch/include/asm /usr/include/asm
test -d /usr/include/asm-generic \
|| ln -sf ../src/linux/include/asm-generic /usr/include/asm-generic
test -d /usr/include/linux \
|| ln -sf ../src/linux/include/linux /usr/include/linux

%preun -n kernel-image%flavour
# keep old kernel images; this may require manual cleanup on occasion
ln /boot/linux-%version /boot/linux-%version-old
rm -f /boot/linux-old
ln -sf linux-%version-old /boot/linux-old

%files
%defattr(0600,root,root,0700)
/boot/linux
/boot/linux-%version
/boot/System.map-%KernelVer
/boot/config-%KernelVer
%dir %dts_dir
%dts_dir/*
%dir %modules_dir/
%modules_dir
%modules_dir/kernel/*
%ghost %config(noreplace) %modules_dir/modules.*

%files -n kernel-headers%flavour
%defattr(0644,root,root,0755)
%dir %kheaders_dir
%kheaders_dir/*

%changelog
* Tue Oct 01 2019 Dmitry Terekhin <jqt4@altlinux.org> 4.19.71-alt0.4
- add System.map
- add config
- only one devicetree directory
- fix flavour
- fix KERNELRELEASE to %version%flavour-%release

* Tue Oct 01 2019 Dmitry Terekhin <jqt4@altlinux.org> 4.19.71-alt0.3
- install devicetree

* Tue Oct 01 2019 Dmitry Terekhin <jqt4@altlinux.org> 4.19.71-alt0.2
- simplify spec
- add devicetree
- add modules_dir

* Tue Oct 01 2019 Dmitry Terekhin <jqt4@altlinux.org> 4.19.71-alt0.1
- spec and config changed - first test

* Fri Aug 30 2019 Gremlin from Kremlin <gremlin@altlinux.org> 4.19.71-alt1
- first build with RPi 4 support (arm64 a.k.a. aarch64)
