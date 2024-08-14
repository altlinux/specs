%define _unpackaged_files_terminate_build 1
%define efi_arches %ix86 x86_64 aarch64 riscv64

# SBAT generation number for ALT
# Refer to https://github.com/rhboot/shim/blob/main/SBAT.md
%global alt_gen_number 1

# grub modules' architecture is heavily dependent on custom ELF sections.
# LTO crashes that fragile house of cards, so should be disabled.
%global optflags_lto %nil

%global gnulib_version 9f48fb992a3d7e96610c4ce8be969cff2d61a01b

# No need for post-processing GRUB modules and their helpers
%add_findreq_skiplist %_libdir/grub/*/*
%add_verify_elf_skiplist %_libdir/grub/*/*
%add_debuginfo_skiplist %_libdir/grub/*/*
%add_python3_path %_libdir/grub
%add_python3_compile_exclude %_libdir/grub
%add_python3_req_skip %_libdir/grub/*/gdb_helper.py

# NB: not a fashion but the critical need to fit into 62 sectors
%define _optlevel s

Name: grub
Version: 2.12
Release: alt3

Summary: GRand Unified Bootloader
License: GPL-3
Group: System/Kernel and hardware

Url: http://www.gnu.org/software/grub

ExclusiveArch: %ix86 x86_64 aarch64 ppc64le riscv64

Source0: %name-%version.tar
Source1: grub2-sysconfig

Source2: gnulib-%version.tar

Source3: 39_memtest
Source4: grub.filetrigger

Source6: grub-autoupdate

Source8: update-grub
Source9: update-grub.8

Source10: grub-efi-autoupdate
Source11: embedded_grub.cfg

Source12: grub-entries
Source13: grub-entries.8

Source14: grub-efi.filetrigger

Source15: sbat.csv.in

Source16: grub-dumpsbat.c

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-uefi
BuildRequires(pre): rpm-build-python3

BuildRequires: flex
BuildRequires: ruby
BuildRequires: autogen
BuildRequires: texinfo
BuildRequires: help2man
BuildRequires: squashfs-tools

BuildRequires: zlib-devel
BuildRequires: libfuse-devel
BuildRequires: liblzma-devel
BuildRequires: libfreetype-devel
BuildRequires: libdevmapper-devel

BuildRequires: fonts-bitmap-misc
BuildRequires: fonts-bitmap-univga
# Default font
%define font /usr/share/fonts/bitmap/univga/u_vga16_9.pcf.gz

Requires: gettext

%ifarch %ix86
%global grubefiarch i386-efi
%global linux_module_name linux
%global efi_suff ia32
%endif
%ifarch x86_64
%global grubefiarch x86_64-efi
%global linux_module_name linux
%global efi_suff x64
%endif
%ifarch aarch64
%global grubefiarch arm64-efi
%global linux_module_name linux
%global efi_suff aa64
%endif
%ifarch riscv64
%global grubefiarch riscv64-efi
%global linux_module_name linux
%global efi_suff riscv64
%endif

%package common
Summary: GRand Unified Bootloader (common part)
Group: System/Kernel and hardware
Provides: grub2-common = %EVR
Obsoletes: grub2-common < %EVR

%package pc
Summary: GRand Unified Bootloader (PC BIOS variant)
Group: System/Kernel and hardware
Requires: %name-common = %version-%release
%ifarch %ix86 x86_64
Provides: grub2 = %EVR
Provides: grub = %EVR
%endif
Provides: grub2-pc = %EVR
Obsoletes: grub2-pc < %EVR

%package ieee1275
Summary: GRand Unified Bootloader (IEEE1275 variant)
Group: System/Kernel and hardware
Requires: %name-common = %version-%release
%ifarch ppc64le
Requires: powerpc-utils
Provides: grub2 = %EVR
Provides: grub = %EVR
%endif

%package efi
Summary: GRand Unified Bootloader (UEFI variant)
Group: System/Kernel and hardware
Requires: %name-common = %EVR
Provides: grub2-efi = %EVR
Obsoletes: grub2-efi < %EVR
Requires(pre): efibootmgr >= 15
%ifarch aarch64
Provides: grub2 = %EVR
Provides: grub = %EVR
%endif

%package efi-checkinstall
Summary: Verify EFI-stub signature
Group: System/Kernel and hardware
Requires: %name-efi = %EVR
Requires(post): rpm-pesign-checkinstall

%define desc_generic \
GNU GRUB is a multiboot boot loader. It was derived from GRUB. It is an \
attempt to produce a boot loader for IBM PC-compatible machines that \
has both the ability to be friendly to beginning or otherwise \
nontechnically interested users and the flexibility to help experts in \
diverse environments. It is compatible with Free/Net/OpenBSD and Linux. \
It supports Win 9x/NT and OS/2 via chainloaders. It has a menu \
interface and a command line interface. \
It implements the Multiboot standard, which allows for flexible loading \
of multiple boot images (needed for modular kernels such as the GNU Hurd).

%description
%desc_generic

%description common
%desc_generic

This package carries the shared code and data.

%description pc
%desc_generic

This package provides PC BIOS support.

%description ieee1275
%desc_generic

This package provides Open Firmware (IEEE 1275) support.

%description efi
%desc_generic

This package provides UEFI systems support.

Please note that the official build is signed; this shouldn't
intervene in any way but rather provides means to cope with
UEFI SecureBoot (better described as Restricted Boot) firmware
when one can't disable it easily, doesn't want to, or needs not to.

%description efi-checkinstall
%desc_generic

This package enables EFI signature verification.

%prep
%setup -b 2

%patch0 -p1

sed -i "/^AC_INIT(\[GRUB\]/ s/%version[^]]\+/%version-%release/" configure.ac

# append ALT data to SBAT section
# make sure upstream data is set appropriately in sbat.csv.in too
cat %SOURCE15 > sbat.csv
echo "grub.altlinux,%alt_gen_number,ALT Linux,grub,%version-%release,http://git.altlinux.org/gears/g/grub.git" >> sbat.csv

# Check gnulib version
grep '^GNULIB_REVISION=%gnulib_version$' bootstrap.conf || exit 1

%build
./bootstrap --no-git --gnulib-srcdir=../gnulib-%version
./autogen.sh
build_grub() {
	local dir="$1"; shift
	mkdir -p "$dir"
	pushd "$dir"
	%define _configure_script ../configure
	%configure \
		TARGET_LDFLAGS=-static \
		--disable-werror \
		"$@"
	%make_build
	popd
}

build_efi_image() {
	local mkimage="$1"; shift
	local dir="$1"; shift
	local format="$1"; shift
	"$mkimage" -O "$format" -o "$dir"/grub.efi -d "$dir"/grub-core \
		-m memdisk.squashfs -p "" --sbat sbat.csv \
		part_gpt part_apple part_msdos hfsplus fat ext2 btrfs xfs \
		squash4 normal chain boot configfile diskfilter \
		minicmd reboot halt search search_fs_uuid search_fs_file \
		search_label sleep test syslinuxcfg all_video video font \
		gfxmenu gfxterm gfxterm_background lvm lsefi efifwsetup cat \
		gzio iso9660 loadenv loopback mdraid09 mdraid1x png jpeg \
		extcmd keystatus procfs cryptodisk gcry_rijndael gcry_sha1 \
		gcry_sha256 luks luks2 gcry_sha512 gcry_serpent gcry_twofish \
		crypto pbkdf2 password_pbkdf2 echo regexp tftp \
		f2fs exfat ntfs ntfscomp memdisk \
		"$@"
}

%ifarch %ix86 x86_64
build_grub build-pc \
	--with-platform=pc \
#
%endif

%ifarch ppc64le
build_grub build-ieee1275 \
	--with-platform=ieee1275 \
#
%endif

%ifarch %efi_arches
build_grub build-efi \
	--with-platform=efi \
#

# create memdisk with fonts
workdir="$(mktemp -d)"
mkdir -p "$workdir/fonts"
./build-efi/grub-mkfont -o "$workdir/fonts/unicode.pf2" %font
mksquashfs "$workdir" memdisk.squashfs -comp xz
rm -rf "$workdir"

build_efi_image build-efi/grub-mkimage build-efi %grubefiarch %linux_module_name

#add forced ia32 version build to be bundled with x86_64 EFI
%ifarch x86_64
build_grub build-efi-ia32 \
	--with-platform=efi \
	--target=i386 \
#
# use 64bit mkimage to build i386-efi image
build_efi_image build-efi/grub-mkimage build-efi-ia32 i386-efi linux
%endif
%endif

# build grub-dumpsbat utility used in grub-efi-autoupdate
gcc %optflags -D_FILE_OFFSET_BITS=64 %SOURCE16 -o grub-dumpsbat

%install
%ifarch %ix86 x86_64
%makeinstall_std -C build-pc
%ifarch x86_64
#"cherry pick" only i386 executable
install -pDm644 build-efi-ia32/grub.efi %buildroot%_efi_bindir/grubia32.efi

#install ia32 version in parallel with x64 for x86_64 platforms with ia32 EFI
%makeinstall_std -C build-efi-ia32
%endif
%endif

%makeinstall_std -C \
%ifarch ppc64le
	build-ieee1275
%else
	build-efi
%endif

install -pDm644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/grub2

%find_lang grub

mkdir -p %buildroot/boot/grub/fonts

install -pD -m755 %SOURCE8 %buildroot%_sbindir/
install -pD -m644 %SOURCE9 %buildroot%_man8dir/update-grub.8
install -pD -m644 %SOURCE13 %buildroot%_man8dir/grub-entries.8

# TODO: drop the obsolete one (unifont.pf2)
%buildroot%_bindir/grub-mkfont -o %buildroot/boot/grub/unifont.pf2 \
                               %_datadir/fonts/bitmap/misc/8x13.pcf.gz
%buildroot%_bindir/grub-mkfont -o %buildroot/boot/grub/fonts/unicode.pf2 %font
install -pDm644 %buildroot/boot/grub/fonts/unicode.pf2 \
        %buildroot%_datadir/grub/unicode.pf2

mkdir -p %buildroot/boot/grub/themes

install -pDm755 %SOURCE3 %buildroot%_sysconfdir/grub.d/
sed -i 's,^libdir=,libdir=%_libdir,g' %buildroot%_sysconfdir/grub.d/39_memtest
sed -i 's,@LOCALEDIR@,%_datadir/locale,g' %buildroot%_sysconfdir/grub.d/*

install -pDm755 %SOURCE4 %buildroot%_rpmlibdir/grub.filetrigger
%ifarch %ix86 x86_64 ppc64le
install -pDm755 %SOURCE6 %buildroot%_sbindir/grub-autoupdate
%endif

%ifarch %efi_arches
install -pDm755 %SOURCE10 %buildroot%_sbindir/grub-efi-autoupdate
install -pDm755 %SOURCE14 %buildroot%_rpmlibdir/grub-efi.filetrigger
%endif
install -pDm755 %SOURCE12 %buildroot%_sbindir/grub-entries

# install grub-dumpsbat utility used in grub-efi-autoupdate
install -pDm755 grub-dumpsbat %buildroot%_bindir/grub-dumpsbat

# Ghost config file
install -d %buildroot/boot/grub
touch %buildroot/boot/grub/grub.cfg
ln -s ../boot/grub/grub.cfg %buildroot%_sysconfdir/grub.cfg

# Docs/habits compat symlink
mkdir -p %buildroot%_sysconfdir/default
ln -s ../sysconfig/grub2 %buildroot%_sysconfdir/default/grub

# Ghost file generated by grub-install
touch %buildroot/boot/grub/grubenv

# These tools are only for efi and x86_64
%ifnarch x86_64
rm -vf %buildroot%_bindir/grub-render-label
rm -vf %buildroot%_sbindir/grub-bios-setup
rm -vf %buildroot%_sbindir/grub-macbless

rm -vf %buildroot%_man1dir/grub-render-label*
rm -vf %buildroot%_man8dir/grub-bios-setup*
rm -vf %buildroot%_man8dir/grub-macbless*
%endif

%ifarch %efi_arches
install -pDm644 build-efi/grub.efi %buildroot%_efi_bindir/grub%{efi_suff}.efi

# Remove headers
rm -f %buildroot%_libdir/grub-efi/*/*.h
%endif

%files common -f grub.lang
%dir %_sysconfdir/grub.d
%dir %_datadir/grub
%dir %_libdir/grub
%dir /boot/grub
/boot/grub/*.pf2
/boot/grub/fonts/
/boot/grub/themes/
%_sysconfdir/grub.d/00_header
%_sysconfdir/grub.d/05_altlinux_theme
%_sysconfdir/grub.d/10_linux
%_sysconfdir/grub.d/20_linux_xen
%_sysconfdir/grub.d/25_bli
%_sysconfdir/grub.d/30_os-prober
%_sysconfdir/grub.d/30_uefi-firmware
%_sysconfdir/grub.d/39_memtest
%config(noreplace) %_sysconfdir/grub.d/40_custom
%config(noreplace) %_sysconfdir/grub.d/41_custom
%_sysconfdir/grub.d/README
%config(noreplace) %_sysconfdir/sysconfig/grub2
%ghost %config(noreplace) /boot/grub/grub.cfg
%ghost %attr(644,root,root) /boot/grub/grubenv
%_sysconfdir/grub.cfg
%_sysconfdir/default/grub
%_datadir/bash-completion/completions/*
%_rpmlibdir/grub.filetrigger
# these tools are only for efi and x86_64
%ifarch x86_64
%_bindir/grub-render-label
%_sbindir/grub-bios-setup
%_sbindir/grub-macbless
%endif
%_sbindir/grub-install
%_sbindir/grub-mkconfig
%_sbindir/grub-ofpathname
%_sbindir/grub-probe
%_sbindir/grub-reboot
%_sbindir/grub-set-default
%_sbindir/grub-sparc64-setup
%_sbindir/grub-entries
%_sbindir/update-grub
%_bindir/grub-editenv
%_bindir/grub-file
%_bindir/grub-fstest
%_bindir/grub-glue-efi
%_bindir/grub-kbdcomp
%_bindir/grub-menulst2cfg
%_bindir/grub-mknetdir
%_bindir/grub-mkstandalone
%_bindir/grub-mkfont
%_bindir/grub-mklayout
%_bindir/grub-mkimage
%_bindir/grub-mkpasswd-pbkdf2
%_bindir/grub-mkrelpath
%_bindir/grub-mkrescue
%_bindir/grub-mount
%_bindir/grub-script-check
%_bindir/grub-syslinux2cfg
%_bindir/grub-dumpsbat
%_datadir/grub/grub-mkconfig_lib
%_datadir/grub/unicode.pf2
%_man1dir/*
%_man8dir/*
%_infodir/grub.info.*
%_infodir/grub-dev.info.*

%ifarch %ix86 x86_64
%files pc
%_sbindir/grub-autoupdate
%_libdir/grub/*-pc/
%endif

%ifarch ppc64le
%files ieee1275
%_sbindir/grub-autoupdate
%_libdir/grub/*-ieee1275/
%endif

%ifarch %efi_arches
%files efi
%_efi_bindir/grub%{efi_suff}.efi
%ifarch x86_64
%_efi_bindir/grubia32.efi
%_libdir/grub/i386-efi
%endif
%_sbindir/grub-efi-autoupdate
%_libdir/grub/%grubefiarch
%_rpmlibdir/grub-efi.filetrigger

%files efi-checkinstall
%endif

%ifarch %ix86 x86_64 ppc64le
%ifarch %ix86 x86_64
%post pc
%endif
%ifarch ppc64le
%post ieee1275
%endif
grub-autoupdate || {
	echo "** WARNING: grub-autoupdate failed, NEXT BOOT WILL LIKELY FAIL NOW"
	echo "** WARNING: please run it by hand, record the output offline,"
	echo "** WARNING: make sure you have bootable rescue CD/flash media handy"
	echo "** WARNING: and try \`grub-install /dev/sdX' manually"
} >&2
%endif

%post efi
[ -z "$DURING_INSTALL" ] || exit 0
modprobe -q efivars ||:
modprobe -q efivarfs ||:
grep -q '^GRUB_DISTRIBUTOR=' %_sysconfdir/sysconfig/grub2 ||
	echo 'GRUB_DISTRIBUTOR="ALT Linux"' >> %_sysconfdir/sysconfig/grub2

grep -q '^GRUB_BOOTLOADER_ID=' %_sysconfdir/sysconfig/grub2 ||
	echo 'GRUB_BOOTLOADER_ID="altlinux"' >> %_sysconfdir/sysconfig/grub2

grub-efi-autoupdate || {
	echo "** WARNING: grub-efi-autoupdate failed, NEXT BOOT WILL LIKELY FAIL NOW"
	echo "** WARNING: please run grub-efi-autoupdate by hand, record the output offline,"
	echo "** WARNING: make sure you have recovery bootable media handy."
} >&2

%changelog
* Tue Aug 13 2024 Egor Ignatov <egori@altlinux.org> 2.12-alt3
- fix boot from encrypted partition in Legacy install
- fix error in bash-completion script
- use default value if GRUB_TOP_LEVEL is not set (closes: #48681)

* Thu Aug 08 2024 Egor Ignatov <egori@altlinux.org> 2.12-alt2
- revert _optlevel back to 's' (closes: #51107)

* Tue Jul 23 2024 Egor Ignatov <egori@altlinux.org> 2.12-alt1
- 2.12
- grub-efi-autoupdate: update only ALT Linux GRUB efi images (closes: #41959)
- grub-install: validate grub root volume in efi boot (fixes: CVE-2023-4001)
- grub-install: install efi grub.cfg for removable (closes: #39745)
- grub-mkconfig: add --class altlinux for menuentries (closes: #39609)
- support xfsprogs >= 6.5.0 (closes: #49891)
- add sysconfig option GRUB_TOP_LEVEL set to /boot/vmlinuz (closes: #48681)
- package unicode.pf2 to the datadir also (closes: #39616)

* Wed May 15 2024 Egor Ignatov <egori@altlinux.org> 2.06-alt19
- bumped release to pesign with the new key

* Thu Mar 07 2024 Egor Ignatov <egori@altlinux.org> 2.06-alt18
- EFI image: embed memdisk with default font

* Fri Oct 06 2023 Egor Ignatov <egori@altlinux.org> 2.06-alt17
- backport upstream NTFS patch set (fixes: CVE-2023-4692, CVE-2023-4693)
  + bump grub SBAT level to 4 and reset grub.altlinux
- backport upstream ext2 fs patches (closes: #48343)
- backport: Fix md array device enumeration (closes #47850)
- return backward compatibility for grub config (closes: #48056)

* Wed Sep 06 2023 Egor Ignatov <egori@altlinux.org> 2.06-alt16
- 39_memtest: fix grub.cfg generation on i586 (closes: #47471)

* Tue Aug 22 2023 Egor Ignatov <egori@altlinux.org> 2.06-alt15
- 39_memtest: add uefi support (closes: #47244)

* Wed Aug 16 2023 Egor Ignatov <egori@altlinux.org> 2.06-alt14
- add f2fs, exfat, ntfs, ntfscomp modules to efi image (closes: #47257)

* Wed Jul 19 2023 Egor Ignatov <egori@altlinux.org> 2.06-alt13
- change repo structure
 + get rid of git subtree
 + keep patches in a separate git branch
 + move alt-specific files to the 'altlinux' directory
- post efi: probe quietly both efivars and efivarfs (closes: #46660)

* Fri Jun 23 2023 Egor Ignatov <egori@altlinux.org> 2.06-alt12
- switch to the vendored gnulib of the required version
  + this makes it easier to port grub to other branches

* Fri Mar 24 2023 Egor Ignatov <egori@altlinux.org> 2.06-alt11
- os-alt patch: change GRUB_VMLINUZ_SYMLINKS default behavior to yes (closes: #44406)
- Introduced the grub-efi-checkinstall subpackage for automatic EFI
  signature verification (glebfm@)

* Tue Mar 14 2023 Egor Ignatov <egori@altlinux.org> 2.06-alt10
- grub2-sysconfig: change default option to GRUB_VMLINUZ_SYMLINKS=yes (closes: #44406)
- add upstream-0061-net-ip-Do-IP-fragment-maths-safely patch (fixes: CVE-2022-28733)
- bump grub.altlinux SBAT level to 2 after closing CVE missed in the previous release

* Sun Jan 22 2023 Egor Ignatov <egori@altlinux.org> 2.06-alt9
- fix os-alt patch: replace obsolete variable gone long ago (nickel@) (closes: #44387)
- remove translation for 'Change language (press F2)' (closes: #45437)
- remove rhboot SecureBoot patches; use upstream shim_lock and lockdown verifiers
- update fedora-Rework-how-the-fdt-command-builds patch
- add upstream security patch set 2022-06-07:
  (fixes: CVE-2021-3695, CVE-2021-3696, CVE-2021-3697, CVE-2022-28734)
  (fixes: CVE-2022-28734, CVE-2022-28735, CVE-2022-28736)
- add upstream security patch set 2022-11-15:
  (fixes: CVE-2022-2601, CVE-2022-3775)
- bump sbat global generation number from 1 to 3

* Mon Aug 15 2022 Nikolai Kostrigin <nickel@altlinux.org> 2.06-alt8
- fix FTBFS with new gnulib (upstream patchset)
- grub(-efi): switch from 'egrep' to 'grep -E' in filetriggers (closes: #43329)
- update os-alt patch: switch from 'fgrep' to 'grep -F'
- add alt-util-grub.d-switch-from-fgrep-to-grep-F patch

* Thu Feb 24 2022 Nikolai Kostrigin <nickel@altlinux.org> 2.06-alt7
- grub-efi: improve RPM filetrigger and post install script to skip all
  actions in case of being invoked at package installing stage by OS installer
  (closes: #42025)
- 30_uefi-firmware.in: Fix for zero supported indications (closes: #41970)
- pack 41_custom as there appear to be users of it (closes: #41832)

* Thu Jan 27 2022 Nikolai Kostrigin <nickel@altlinux.org> 2.06-alt6
- add basic clean looking, blinkless boot support based on fedora patch set

* Wed Jan 26 2022 Nikolai Kostrigin <nickel@altlinux.org> 2.06-alt5
- add upstream-grub-mkconfig-Restore-umask-for-the-grub.cfg patch
  (fixes: CVE-2021-3981)

* Fri Oct 01 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.06-alt4
- add upstream-fs-xfs-Fix-unreadable-filesystem-with-v4-superblock patch
  (closes: #40878)

* Wed Aug 18 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.06-alt3
- new version
- update debian-install_signed patch
- update debian-grub-install-extra-removable patch
- update debian-grub-install-removable-shim patch
- update fedora-Revert-templates-Properly-disable-the-os-prober-by-d patch
- spec: disable LTO due to modules' build system incompatibility

* Sat Aug 14 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.06-alt2.rc1
- add fedora patch to add blscfg command (keremet@) (closes: #40512)
- add alt-gfxterm-backspace-workaround patch (egori@)

* Wed May 19 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.06-alt1.rc1
- new version
  + includes fixes for BootHole vulnerabilities so drop corresponding patches
  + includes fixes for SB Bypass 2021 vulnerabilities
    (fixes: CVE-2020-14372, CVE-2020-25632, CVE-2020-25647, CVE-2020-27749)
    (fixes: CVE-2020-27779, CVE-2021-20225, CVE-2021-20233, CVE-2021-3418)
- update os-alt-xen patch
- remove upstreamed ubuntu-efi-setup patch
- update fedora SB patch set
- update fedora-Rework-how-the-fdt-command-builds patch
- add fedora patches to revert os-prober disabling in SB
- switch default graphics mode from "800x600" to "auto" (closes: #39948)
- grub-efi-autoupdate: fix --removable installations were not updated
- update alt-add-strings-and-translation-for-OS-ALT patch (antohami@)
- add alt-fix-build-with-new-gnulib patch (egori@)

* Tue Feb 16 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.04-alt3
- grub-efi-autoupdate: fix grub update rendering system unbootable
- grub-efi.filetrigger: add to ensure grub reinstall during shim-signed update
- provide OS ALT installer messages Russian translation
  + add add-strings-and-translation-for-OS-ALT patch (underwit@, antohami@)
- update grub messages Russian translation
  + add alt-update-russian-translation patch (underwit@)
- spec: prepare grub-efi to be buildable on RISCV64 (arei@)
- spec: fix AARCH64 EFI binary suffix

* Fri Dec 25 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.04-alt2
- grub-install: add workaround for malformed EFI-firmware implementations
  (closes: #39432)
  + add debian-grub-install-removable-shim patch
  + add debian-grub-install-extra-removable patch
  + add alt-grub-install-no-fallback-for-removable patch
- grub-efi-autoupdate: use grub-install --force-extra-removable by default

* Fri Nov 13 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.04-alt1
- new version
  + update and thin out ALT patches
  + replace fedora SB patch set
  + spec: add gnulib to BR:
  + spec: don't use linuxefi module name while assembling a EFI binary
- add upstream patch set and adapt it to fix BootHole & Co. vulnerabilities
  + (fixes: CVE-2020-10713, CVE-2020-14308, CVE-2020-14309, CVE-2020-14310)
  + (fixes: CVE-2020-14311, CVE-2020-15705, CVE-2020-15706, CVE-2020-15707)

* Fri Oct 02 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt30
- disallow kernels with unsigned EFI stub to be run by grub in SB mode
  + remove alt-relaxed-kernel-sign-check patch

* Wed Aug 19 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt29
- spec: add tftp module into EFI image (closes: #38681)
- sort kernels by mtime instead of ctime (ptrnine@)

* Fri Jul 17 2020 Oleg Solovyov <mcpain@altlinux.org> 2.02-alt28
- apply subvol option substitution into GRUB_CMDLINE_LINUX_DEFAULT

* Thu May 21 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt27
- add fedora-efi-chainloader-truncate-relocation patch (closes: #37112)

* Wed Apr 08 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt26
- spec: add echo and regexp modules into EFI image
  + echo fixes env vars passing to kernel cmdline in SB mode

* Tue Mar 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt25
- improve grub-2.02-alt-os-prober-compat patch

* Thu Feb 20 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt24
- introduce compatibility with os-prober 1.77 (closes: #36624)
  + remove grub-2.00-debian-uefi-os-prober patch
  + add alt-os-prober-compat patch
  + spec: add libfuse-devel to BR to support grub-mount feature
- spec: replace deprecated PreReq with Requires(pre) for efibootmgr

* Thu Feb 06 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt23
- spec: add even more crypto modules to enable boot time encrypted
  password feature operation in SB mode on some UEFI firmwares

* Thu Jan 23 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt22
- fix debian-install_signed patch (closes: #37664)
- spec: remove useless pesigning from install section
  + fix license
  + move rpm-macros-uefi to BR(pre):

* Mon Jan 20 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt21
- spec: add crypto modules into EFI binary images to support LUKS encrypted
  partition booting without dedicated unenctypted /boot partition alongside
  (closes: #37663)

* Fri Nov 29 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt20
- improve third-party customizer programs compatibility
  + grub2-sysconfig: add GRUB_BACKGROUND definition
  + rework altlinux-theme patch for conditional default colors application
- spec: sed autogen.sh to choose python3 interpreter explicitly

* Tue Oct 29 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt19
- grub-ieee1275: added R: powerpc-utils. (glebfm@)
- add xfs-sparse-inodes patch (closes: #37394)

* Tue Aug 13 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt18
- add extcmd and keystatus modules to EFI images (closes: #36722)

* Fri Jun 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.02-alt17
- Refactored %%build and %%install sections;
- Added grub-ieee1275 support for ppc64le architecture;
- %%ix86: renamed efi image files to grubia32{,sb}.efi ;
- spec:
  + removed unpackaged files;
  + added ExclusiveArch tag to skip build on unsupported architectures.

* Tue Mar 19 2019 Leonid Krivoshein <klark@altlinux.org> 2.02-alt16
- grub-entries script: variables initialization added

* Tue Feb 12 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt15
- add rhboot/grub2 SB patch set to prevent unauthorized code execution at boot time when SB is enabled
- add grub-entries script by klark@ for list grub menu (closes: #36048)
- add patch preventing boot failure for unsigned kernel in SB environment
  + add an optional patch application flag for convenience

* Mon Dec 10 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt14
- added patch from upstream with changes for default pit time source to ptimer

* Thu Nov 29 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt13
- fix FTBFS by adding suse-fix-build-with-gcc8 patch
- fix FTBFS by adding fix-binutils-break-grub-efi-build patch
- remove ubt

* Mon Jun 25 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt12
- add ia32 EFI binary to x86_64 package
- add a patch adopted from fedora one introducing linuxefi/initrdefi commands
- add ia32 grub modules to package
  + add embedded config into ia32 EFI coreimage
  + rename x64 EFI binary to grubx64.efi
  + add grub-efi-autoupdate ia32 EFI compatibility

* Wed May 30 2018 Oleg Solovyov <mcpain@altlinux.org> 2.02-alt11
- LVM+LUKS fixes:
  + write UUID to grub.cfg after installation
  + don't skip devices under /dev/mapper/

* Fri May 25 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt10
- removed xxd requires from efi firmware setup script

* Mon May 21 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt9
- fixed config generation errors on EFI platform (closes: #34852)

* Sun May 13 2018 Leonid Krivoshein <klark@altlinux.org> 2.02-alt8
- write to read-only grub device problem fixed.

* Mon Apr 16 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt7
- revert back the LVM+LUKS fixes from alt6

* Mon Apr 16 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt6
- add ubt for backporting

* Mon Apr 16 2018 Oleg Solovyov <mcpain@altlinux.org> 2.02-alt6
- LVM+LUKS fixes:
  + write UUID to grub.cfg after installation
  + fix empty root parameter after update-grub

* Thu Mar 29 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt5
- more grub-efi modules enabled by default:
  part_apple part_msdos xfs squash4 search_fs_file search_label sleep  test syslinuxcfg video 
  gfxterm_background lvm lsefi efifwsetup cat gzio iso9660 loadenv loopback mdraid09 mdraid1x 
  png jpeg
- added patch from ubuntu for efi setup menu entry (closes: #34467)
- filetrigger and configs moved from pc/efi packages to common part

* Sat Dec 02 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt4
- interaction between the user and the shift key at boot time interrupts the grub wait timeout (closes: #33655)

* Thu Nov 30 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt3
- fixed sysconfig/grub2 usage in grub-efi post script (closes: #34258)
- fixed Xen menu entry  (closes: #32811)

* Tue Jul 18 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt2
- renamed from grub2 to grub
- added strong requires to efibootmgr >= 15

* Sat Jun 17 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt1
- add ubt for backporting process

* Mon Jun 05 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.02-alt1
- 2.02 released

* Tue May 10 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.02-alt0.3
- 2.02 beta3

* Wed Dec 02 2015 Michael Shigorin <mike@altlinux.org> 2.00-alt21
- CVE-2015-8370: those who have set up GRUB passwords MUST
  upgrade or find their use of this "protection" inefficient:
  http://hmarco.org/bugs/CVE-2015-8370-Grub2-authentication-bypass.html
  (closes: #31631)
- added fedora patch to piggyback --unrestricted through CLASS
  thus changing the default for password-protected menuentry items
  to request password only when an attempt to change boot parameters
  is made (but to let the system boot by default); see also
  http://altlinux.org/grub#password
- added upstream texinfo patch to fix FTBFS
- explicit BR: texinfo

* Tue Dec 17 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt20
- updated pesign macros use, reworked binaries installation
- prepare for production signing

* Wed Nov 27 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt19
- rebuilt with current gnu-efi
- pesign with ALT key

* Tue Nov 26 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt18
- adapted debian patch to accept os-prober output for EFI binaries
  (see also RH#972355, RH#873207, deb#698914)

* Sat Nov 16 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt17
- updated grub-2.00-os-alt.patch for 2.00 (closes: #29583)

* Thu Oct 31 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt16
- 39_memtest: warning goes to stderr now and not into grub.cfg

* Thu Oct 24 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt15
- 39_memtest: support separate /boot properly (closes: #29460)

* Wed Jul 24 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt14
- efi: try loading efivars.ko just in case, no harm and no use otherwise

* Thu May 23 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt13
- firsttime: dropped (closes: #28966)

* Mon Mar 04 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt12
- better UEFI boot label support (mind the sysconfig fixes)
- dropped patch8 (irrelevant)

* Mon Feb 18 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt11.2
- revert patch suggested in #28218 (results in black-on-black text menu)

* Thu Feb 07 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt11.1
- firsttime: i18n support

* Thu Jan 31 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt11
- make grub less bold with its noisy opinions (closes: #25778)
- cas@: updated 05_altlinux_theme (closes: #28218)
- skip memtest in EFI mode
- changed default font from dejavu sans mono to univga

* Thu Jan 31 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt10
- whoops, actually added grub-efi-autoupdate script (closes: #28485)
- tweaked both grub-autoupdate and posttrans filetrigger
  to be almost quiet in EFI case

* Wed Jan 23 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt9
- efi subpackage is signed by default on x86_64
- introduced efi-unsigned subpackage with a clean copy
- initial grub-2.00-install-uefi-signed.patch based on
  ubuntu_install_signed.patch from 2.00-11ubuntu1 package
- initial efi postinstall update script

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt8
- introduced efi-signed subpackage (x86_64 only)
- use rpm-macros-uefi

* Thu Dec 06 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt7
- dropped patch4 (see also #28181)

* Tue Dec 04 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt6
- cas@ fixed wrong path in theme patch (closes: #28176)
- introduced /etc/default/grub "compat" symlink
- dropped /boot/efi/* due to complete lack of applicability

* Thu Nov 22 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt5
- maintenance release:
  + fixed filetrigger lapse (thanks crux@, see also #27916)
  + grub2-common is now aware of grub-0.9x symlink (closes: #27935)

* Tue Nov 13 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt4
- initial EFI support merge
- NB: grub2-pc package got split into -pc and -common,
  please double-check that things went well

* Mon Nov 05 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt3
- try harder to warn that the configuration is not complete
  for automated grub upgrades thus needs to be updated manually
  (closes: #27916)
- adapted update-grub(8) from debian

* Sun Nov 04 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt2
- applied upstream patch to revert broken fix resulting in wrong
  assessment of core.img size and a failure to install grub:
  http://bzr.savannah.gnu.org/lh/grub/trunk/grub/revision/4586
  (closes: #25666)

* Fri Oct 26 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt1
- 2.00 (closes: #27803)
- updated patches
  + fixed 05_altlinux_theme (closes: #27642)
- built with devmapper support
  + alterator-grub needs one-line fix to work again on mdraid though
- updated an Url: (closes: #26901)
- added a redundant but compatible unicode.pf2 font file
  (might be split off to a separate subpackage soonish)

* Fri May 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt9
- fix build with automake >= 1.11.2

* Mon Aug 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt8
- rename to grub2-pc
- fix build

* Fri Jul 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt7
- force grub config update on grub update

* Tue Jun 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt6
- increase probability of race winning during install on evms device
  (ALT #25628) again

* Wed Jun 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt5
- shaba@ (ALT #25666):
  build with -Os optimization
  add LZMA support
- shaba@: add man pages

* Tue May 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt4
- remove 'with Linux' within linux-only entries

* Fri May 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt3
- fix adding failsafe options to non-failsave cmdline (ALT #25676)
- change 'splash=silent' to 'splash' in default sysconfig

* Thu May 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt2
- disable floppies handling (ALT #24974)

* Fri May 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt1
- 1.99
- fix absolute pathnames during install (ALT #25444)

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt24.20100804
- fix grub-1.98-evms-crap-alt.patch for /dev/vd* devices (ALT #25497)

* Wed Feb 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt23.20100804
- remove buggy brain which sets gfxpayload=keep in 10_linux
- mention timeout features in sysconfig
- mention GRUB_PRELOAD_MODULES in sysconfig

* Mon Jan 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt22.20100804
- add options to /ets/sysconfig/grub2:
  GRUB_AUTOUPDATE_CFG,GRUB_AUTOUPDATE_CFGNAME to control automatic config
   update
  GRUB_VMLINUZ_SYMLINKS to control symlinks handling in /boot/vmlinuz*
  GRUB_VMLINUZ_FAILSAFE to control failsafe entries
- temporary remove ntldr-img from grub-extras

* Fri Oct 29 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt21.20100804
- place default font in /boot/grub (ALT #24446)
- fix initrd finding (ALT #24442)

* Thu Oct 28 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.98-alt20.20100804
- fix this unhappy firsttime script
- use UUIDs for flavoured entries

* Wed Oct 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.98-alt19.20100804
- firsttime script added

* Mon Oct 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt18.20100804
- add GRUB_AUTOUPDATE_DEVICE and GRUB_AUTOUPDATE_FORCE options for
  automatic grub update (ALT #24114)

* Mon Sep 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt17.20100804
- update grub-1.98-evms-crap-alt.patch (evms/lvm2)

* Wed Sep 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt16.20100804
- make grub menu look tuneable with /etc/sysconfig/grub2

* Wed Sep 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt15.20100804
- hackaround: update evms-crap-alt.patch (strip devmapper for el-smp kernel)

* Wed Aug 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt14.20100804
- 20100804 snapshot
- add gettext to Requires (ALT #23845)

* Fri Jun 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt13
- update grub menu in filetrigger (ALT #23332)
- fix memtest finding

* Wed Apr 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt12
- add space before (failsafe mode) (ALT #23361)
- fix default xen initrd name

* Mon Apr 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt11
- add memtest and xen detection
- set localedir

* Fri Apr 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt10
- do not provide grub
- fix for evms/lvm device probing

* Mon Apr 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt9
- add 904_disable_floppies.patch from debian
- mark %_sysconfdir/grub.d/40_custom as config(noreplace)
- add Provides/Obsoletes for grub

* Tue Mar 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt8
- add 950-quick-boot.patch from debian
- enable savedefault feature by default

* Mon Mar 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt7
- remove evms crap in one more place

* Fri Mar 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt6
- make evms-crap-alt patch more common

* Fri Mar 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt5
- rewrite stupid evms-crap-alt patch

* Thu Mar 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt4
- remove evms crap (for installer)

* Tue Mar 09 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt3
- fix bug in default menuentries

* Mon Mar 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt2
- boot default (/boot/vmlinuz) kernel first
- change default font to 8x13

* Sat Mar 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt1
- 1.98

* Sat Jan 30 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.97-alt3
- 1.97.2

* Thu Jan 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.97-alt2
- add patches from fedora (initramfs,os name)
- remove buggy grub2-helper-10_altlinux
- make /etc/sysconfig/grub2 useful

* Mon Jan 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.97-alt1
- 1.97

* Fri Jun 19 2009 Denis Kuznetsov <dek@altlinux.ru> 1.96-alt2
- Fixed #20475

* Thu Jun 11 2009 Denis Kuznetsov <dek@altlinux.ru> 1.96-alt1
- Initial build for Sisyphus

