Name: make-initrd-bootloader
Version: 0.5
Release: alt1

Summary: Bootloader based on make-initrd
License: GPL-2
Group: System/Base

ExclusiveArch: x86_64

Source0: %name-%version.tar

BuildRequires: make sed bc flex
BuildRequires: libssl-devel
BuildRequires: libelf-devel
BuildRequires: kmod

Requires: make-initrd-boot

%description
%summary.

%prep
%setup
%make_build

%install
%makeinstall_std

kver="`cat "%buildroot/lib/bootloader/boot/version"`"

[ -e "%buildroot/lib/bootloader/boot/System.map-$kver" ] ||
	mv -f -- \
		"%buildroot/lib/bootloader/boot/System.map" \
		"%buildroot/lib/bootloader/boot/System.map-$kver"

[ -e "%buildroot/lib/bootloader/boot/config-$kver" ] ||
	mv -f -- \
		"%buildroot/lib/bootloader/boot/config" \
		"%buildroot/lib/bootloader/boot/config-$kver"

modules_dir="$(ls -1d %buildroot/lib/modules/*)"

# No external modules outside of this package.
rm -f -- "$modules_dir"/build
rm -f -- "$modules_dir"/source

rm -f -- "$modules_dir"/modules.{alias,dep,symbols,builtin}.bin
touch -- "$modules_dir"/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot/lib/bootloader/boot/bootloader.img

mkdir -p -- %buildroot/boot
touch %buildroot/boot/bootloader.conf

%add_verify_elf_skiplist /lib/bootloader/boot/vmlinuz-*
%brp_strip_none /lib/bootloader/boot/*

%files
/sbin/make-bootloader
/lib/bootloader
%ghost /lib/bootloader/boot/bootloader.img
/lib/modules/*
%ghost /lib/modules/*/modules.alias.bin
%ghost /lib/modules/*/modules.dep.bin
%ghost /lib/modules/*/modules.symbols.bin
%ghost /lib/modules/*/modules.builtin.bin
%ghost %config(noreplace) /boot/bootloader.conf
%config(noreplace) %_sysconfdir/bootloader.mk

%changelog
* Sat Sep 11 2021 Alexey Gladkov <legion@altlinux.ru> 0.5-alt1
- Move feature to make-initrd package.

* Thu Apr 09 2020 Alexey Gladkov <legion@altlinux.ru> 0.4-alt1
- Built package only for x86_64.

* Sun Apr 05 2020 Alexey Gladkov <legion@altlinux.ru> 0.3-alt1
- Rename loader.

* Sat Apr 04 2020 Alexey Gladkov <legion@altlinux.ru> 0.2-alt1
- Update files.

* Wed Apr 01 2020 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- First build.

