%define efi_arches %ix86 x86_64 aarch64 riscv64

# SBAT generation number for ALT
# Refer to https://github.com/rhboot/shim/blob/main/SBAT.md
%global alt_gen_number 1

# grub modules' architecture is heavily dependent on custom ELF sections.
# LTO crashes that fragile house of cards, so should be disabled.
%global optflags_lto %nil

Name: grub
Version: 2.06
Release: alt9

Summary: GRand Unified Bootloader
License: GPL-3
Group: System/Kernel and hardware

Url: http://www.gnu.org/software/grub

ExclusiveArch: %ix86 x86_64 aarch64 ppc64le riscv64

Source0: %name-%version.tar
Source1: grub2-sysconfig

Source3: 39_memtest
Source4: grub.filetrigger

Source5: grub-extras-%version.tar

Source6: grub-autoupdate

Source8: update-grub
Source9: update-grub.8

Source10: grub-efi-autoupdate
Source11: embedded_grub.cfg

Source12: grub-entries
Source13: grub-entries.8

Source14: grub-efi.filetrigger

Source15: sbat.csv.in

Patch0: grub-2.04-os-alt.patch
Patch1: grub-2.00-sysconfig-path-alt.patch
Patch2: grub-2.02-altlinux-theme.patch
Patch4: grub-2.04-os-alt-xen.patch
Patch5: grub-2.02-debian-disable_floppies.patch
Patch6: grub-2.04-add-fw_path-variable.patch
Patch8: grub-2.06-debian-install_signed.patch
Patch9: grub-2.00-fedora-unrestricted.patch
Patch10: grub2-stfu.patch
Patch11: grub-2.02-shift-interrupt-timeout.patch
Patch13: grub-2.02-check_writes-alt.patch
Patch14: grub-2.04-alt-luks-use-uuid.patch
Patch20: grub-2.02-alt-os-prober-compat.patch
Patch21: grub-2.04-alt-set-default-bootloader_id.patch
Patch22: grub-2.06-debian-grub-install-extra-removable.patch
Patch23: grub-2.06-debian-grub-install-removable-shim.patch
Patch24: grub-2.04-alt-grub-install-no-fallback-for-removable.patch
Patch25: grub-2.04-alt-add-file-with-Russian-translation.patch
Patch26: grub-2.04-alt-add-strings-and-translation-for-OS-ALT.patch
Patch28: grub-2.06-alt-gfxterm-backspace-workaround.patch
Patch29: grub-2.06-upstream-fs-xfs-Fix-unreadable-filesystem-with-v4-superblock.patch
Patch30: grub-2.06-upstream-grub-mkconfig-Restore-umask-for-the-grub.cfg.patch

# gnulib adoption
# see: https://lists.gnu.org/archive/html/grub-devel/2022-03/msg00125.html
Patch31: grub-2.06-upstream-0001-config.h.in-Use-visual-indentation.patch
Patch32: grub-2.06-upstream-0002-config-Where-present-ensure-config-util.h-precedes-c.patch
Patch33: grub-2.06-upstream-0003-gnulib-Drop-fix-base64.patch.patch
Patch34: grub-2.06-upstream-0004-gnulib-Drop-no-abort.patch.patch
Patch35: grub-2.06-upstream-0005-gnulib-Update-gnulib-version-and-drop-most-gnulib-pa.patch
Patch36: grub-2.06-upstream-0006-gnulib-Handle-warnings-introduced-by-updated-gnulib.patch
Patch37: grub-2.06-upstream-0007-configure-Fix-various-new-autotools-warnings.patch
Patch38: grub-2.06-upstream-0008-lib-posix_wrap-errno.h-Add-__set_errno-macro.patch

Patch39: grub-2.06-alt-util-grub.d-switch-from-fgrep-to-grep-F.patch

Patch190: grub-2.06-fedora-Rework-how-the-fdt-command-builds.patch
Patch191: grub-2.06-fedora-Revert-templates-Properly-disable-the-os-prober-by-d.patch
Patch192: grub-2.06-fedora-Revert-templates-Disable-the-os-prober-by-default.patch
Patch193: grub-2.06-fedora-blscfg-add-blscfg-module-to-parse-Boot-Loader-Specif.patch

# upstream security patch set 2022-06-07
# see: https://lists.gnu.org/archive/html/grub-devel/2022-06/msg00035.html
Patch200: grub-2.06-upstream-0001-loader-efi-chainloader-Simplify-the-loader-state.patch
Patch201: grub-2.06-upstream-0002-commands-boot-Add-API-to-pass-context-to-loader.patch
Patch202: grub-2.06-upstream-0003-loader-efi-chainloader-Use-grub_loader_set_ex.patch

Patch203: grub-2.06-upstream-0011-kern-efi-sb-Reject-non-kernel-files-in-the-shim_lock.patch
Patch204: grub-2.06-upstream-0012-kern-file-Do-not-leak-device_name-on-error-in-grub_f.patch

Patch205: grub-2.06-upstream-0021-video-readers-png-Refuse-to-handle-multiple-image-he.patch
Patch206: grub-2.06-upstream-0022-video-readers-png-Drop-greyscale-support-to-fix-heap.patch
Patch207: grub-2.06-upstream-0023-video-readers-png-Avoid-heap-OOB-R-W-inserting-huff-.patch
Patch208: grub-2.06-upstream-0024-video-readers-png-Sanity-check-some-huffman-codes.patch
Patch209: grub-2.06-upstream-0025-video-readers-jpeg-Abort-sooner-if-a-read-operation-.patch
Patch210: grub-2.06-upstream-0026-video-readers-jpeg-Do-not-reallocate-a-given-huff-ta.patch
Patch211: grub-2.06-upstream-0027-video-readers-jpeg-Refuse-to-handle-multiple-start-o.patch
Patch212: grub-2.06-upstream-0028-video-readers-jpeg-Block-int-underflow-wild-pointer-.patch

Patch213: grub-2.06-upstream-0031-normal-charset-Fix-array-out-of-bounds-formatting-un.patch

Patch214: grub-2.06-upstream-0041-net-netbuff-Block-overly-large-netbuff-allocs.patch
Patch215: grub-2.06-upstream-0042-net-dns-Fix-double-free-addresses-on-corrupt-DNS-res.patch
Patch216: grub-2.06-upstream-0043-net-dns-Don-t-read-past-the-end-of-the-string-we-re-.patch
Patch217: grub-2.06-upstream-0044-net-tftp-Prevent-a-UAF-and-double-free-from-a-failed.patch
Patch218: grub-2.06-upstream-0045-net-tftp-Avoid-a-trivial-UAF.patch
Patch219: grub-2.06-upstream-0046-net-http-Do-not-tear-down-socket-if-it-s-already-bee.patch
Patch220: grub-2.06-upstream-0047-net-http-Fix-OOB-write-for-split-http-headers.patch
Patch221: grub-2.06-upstream-0048-net-http-Error-out-on-headers-with-LF-without-CR.patch

Patch222: grub-2.06-upstream-0051-fs-f2fs-Do-not-read-past-the-end-of-nat-bitmap.patch
Patch223: grub-2.06-upstream-0052-fs-f2fs-Do-not-copy-file-names-that-are-too-long.patch
Patch224: grub-2.06-upstream-0053-fs-btrfs-Fix-several-fuzz-issues-with-invalid-dir-it.patch
Patch225: grub-2.06-upstream-0054-fs-btrfs-Fix-more-ASAN-and-SEGV-issues-found-with-fu.patch
Patch226: grub-2.06-upstream-0055-fs-btrfs-Fix-more-fuzz-issues-related-to-chunks.patch

# upstream security patch set 2022-11-15
# see: https://lists.gnu.org/archive/html/grub-devel/2022-11/msg00059.html
Patch230: grub-2.06-upstream-font-fixes-0001-font-Fix-size-overflow-in-grub_font_get_glyph_intern.patch
Patch231: grub-2.06-upstream-font-fixes-0002-font-Fix-several-integer-overflows-in-grub_font_cons.patch
Patch232: grub-2.06-upstream-font-fixes-0003-font-Remove-grub_font_dup_glyph.patch
Patch233: grub-2.06-upstream-font-fixes-0004-font-Fix-integer-overflow-in-ensure_comb_space.patch
Patch234: grub-2.06-upstream-font-fixes-0005-font-Fix-integer-overflow-in-BMP-index.patch
Patch235: grub-2.06-upstream-font-fixes-0006-font-Fix-integer-underflow-in-binary-search-of-char-.patch
# Do not apply the following patch as it forbids loading fonts not embedded in the efi image
# if Secure Boot  enabled.  This patch  only reduces the attack  surface [1], but  no actual
# vulnerabilities have been discovered.
# Come  back to this  when there  will be ability to sign and load external fonts (ex. [2]).
# [1] https://lists.gnu.org/archive/html/grub-devel/2022-11/msg00067.html
# [2] https://lists.gnu.org/archive/html/grub-devel/2022-12/msg00070.html
#
# Patch236: grub-2.06-upstream-font-fixes-0007-kern-efi-sb-Enforce-verification-of-font-files.patch
Patch237: grub-2.06-upstream-font-fixes-0008-fbutil-Fix-integer-overflow.patch
Patch238: grub-2.06-upstream-font-fixes-0009-font-Fix-an-integer-underflow-in-blit_comb.patch
Patch239: grub-2.06-upstream-font-fixes-0010-font-Harden-grub_font_blit_glyph-and-grub_font_blit_.patch
Patch240: grub-2.06-upstream-font-fixes-0011-font-Assign-null_font-to-glyphs-in-ascii_font_glyph.patch
Patch241: grub-2.06-upstream-font-fixes-0012-normal-charset-Fix-an-integer-overflow-in-grub_unico.patch

# clean boot patch set
Patch1000: grub-2.06-fedora-0023-Don-t-write-messages-to-the-screen.patch
Patch1001: grub-2.06-fedora-0024-Don-t-print-GNU-GRUB-header.patch
Patch1002: grub-2.06-fedora-0039-Don-t-emit-Booting-.-message.patch

BuildRequires(pre): rpm-macros-uefi
BuildRequires: flex fonts-bitmap-misc fonts-ttf-dejavu libfreetype-devel python-modules ruby autogen
BuildRequires: liblzma-devel help2man zlib-devel
BuildRequires: libdevmapper-devel
BuildRequires: texinfo
BuildRequires: libfuse-devel
BuildRequires: gnulib

# fonts: choose one

## dejavu
#BuildRequires: fonts-ttf-dejavu
#define font /usr/share/fonts/ttf/dejavu/DejaVuSansMono.ttf

## terminus
#BuildRequires: fonts-bitmap-terminus
#define font /usr/share/fonts/bitmap/terminus/ter-x16n.pcf.gz

## univga
BuildRequires: fonts-bitmap-univga
%define font /usr/share/fonts/bitmap/univga/u_vga16_9.pcf.gz

## see also fonts-bitmap-ucs-miscfixed; efont-unicode doesn't fit

Requires: gettext

# NB: not a fashion but the critical need to fit into 62 sectors
%define _optlevel s

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

%prep
%setup -b 5
%patch0 -p2
%patch1 -p1
%patch2 -p2
%patch4 -p2
%patch5 -p1
%patch6 -p1
%patch8 -p2
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch13 -p2
%patch14 -p2
%patch20 -p2
%patch21 -p2
%patch22 -p1
%patch23 -p1
%patch24 -p2
%patch25 -p2
%patch26 -p2
%patch28 -p1
%patch29 -p1
%patch30 -p1

# gnulib adoption
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1

%patch39 -p1

%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1

%patch200 -p1
%patch201 -p1
%patch202 -p1

%patch203 -p1
%patch204 -p1

%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1

%patch213 -p1

%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch218 -p1
%patch219 -p1
%patch220 -p1
%patch221 -p1

%patch222 -p1
%patch223 -p1
%patch224 -p1
%patch225 -p1
%patch226 -p1

%patch230 -p1
%patch231 -p1
%patch232 -p1
%patch233 -p1
%patch234 -p1
%patch235 -p1
#%patch236 -p1
%patch237 -p1
%patch238 -p1
%patch239 -p1
%patch240 -p1
%patch241 -p1

%patch1000 -p1
%patch1001 -p1
%patch1002 -p1

sed -i "/^AC_INIT(\[GRUB\]/ s/%version[^]]\+/%version-%release/" configure.ac
sed -i "/^AC_PREREQ/ s/2\.63/2.64/" configure.ac
sed -i "s/PYTHON:=python/PYTHON:=python3/" autogen.sh

# append ALT data to SBAT section
# make sure upstream data is set appropriately in sbat.csv.in too
cat %SOURCE15 > sbat.csv
echo "grub.altlinux,%alt_gen_number,ALT Linux,grub,%version-%release,http://git.altlinux.org/gears/g/grub.git" >> sbat.csv

%build
./bootstrap --no-git --gnulib-srcdir=%_datadir/gnulib
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
	"$mkimage" -O "$format" -o "$dir"/grub.efi -d "$dir"/grub-core -p "" \
		--sbat sbat.csv \
		part_gpt part_apple part_msdos hfsplus fat ext2 btrfs xfs \
		squash4 normal chain boot configfile diskfilter \
		minicmd reboot halt search search_fs_uuid search_fs_file \
		search_label sleep test syslinuxcfg all_video video font \
		gfxmenu gfxterm gfxterm_background lvm lsefi efifwsetup cat \
		gzio iso9660 loadenv loopback mdraid09 mdraid1x png jpeg \
		extcmd keystatus procfs cryptodisk gcry_rijndael gcry_sha1 \
		gcry_sha256 luks gcry_sha512 gcry_serpent gcry_twofish \
		crypto pbkdf2 password_pbkdf2 echo regexp tftp \
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
%buildroot%_bindir/grub-mkfont -o %buildroot/boot/grub/unifont.pf2 %_datadir/fonts/bitmap/misc/8x13.pcf.gz
%buildroot%_bindir/grub-mkfont -o %buildroot/boot/grub/fonts/unicode.pf2 %font

mkdir -p %buildroot/boot/grub/themes

install -pDm755 %SOURCE3 %buildroot%_sysconfdir/grub.d/
sed -i 's,^libdir=,libdir=%_libdir,g' %buildroot%_sysconfdir/grub.d/39_memtest
sed -i 's,@LOCALEDIR@,%_datadir/locale,g' %buildroot%_sysconfdir/grub.d/*

install -pDm755 %SOURCE4  %buildroot%_rpmlibdir/grub.filetrigger
install -pDm755 %SOURCE6  %buildroot%_sbindir/grub-autoupdate
%ifarch %efi_arches
install -pDm755 %SOURCE10 %buildroot%_sbindir/grub-efi-autoupdate
install -pDm755 %SOURCE14 %buildroot%_rpmlibdir/grub-efi.filetrigger
%endif
install -pDm755 %SOURCE12 %buildroot%_sbindir/grub-entries

# Ghost config file
install -d %buildroot/boot/grub
touch %buildroot/boot/grub/grub.cfg
ln -s ../boot/grub/grub.cfg %buildroot%_sysconfdir/grub.cfg

# Docs/habits compat symlink
mkdir -p %buildroot%_sysconfdir/default
ln -s ../sysconfig/grub2 %buildroot%_sysconfdir/default/grub

%ifarch %efi_arches
install -pDm644 build-efi/grub.efi %buildroot%_efi_bindir/grub%{efi_suff}.efi

# Remove headers
rm -f %buildroot%_libdir/grub-efi/*/*.h
%endif

%files common -f grub.lang
%dir %_sysconfdir/grub.d
%dir %_libdir/grub
%dir /boot/grub
/boot/grub/*.pf2
/boot/grub/fonts/
/boot/grub/themes/
%_sysconfdir/grub.d/00_header
%_sysconfdir/grub.d/05_altlinux_theme
%_sysconfdir/grub.d/10_linux
%_sysconfdir/grub.d/20_linux_xen
%_sysconfdir/grub.d/30_os-prober
%_sysconfdir/grub.d/30_uefi-firmware
%_sysconfdir/grub.d/39_memtest
%config(noreplace) %_sysconfdir/grub.d/40_custom
%config(noreplace) %_sysconfdir/grub.d/41_custom
%_sysconfdir/grub.d/README
%config(noreplace) %_sysconfdir/sysconfig/grub2
%ghost %config(noreplace) /boot/grub/grub.cfg
%_sysconfdir/grub.cfg
%_sysconfdir/default/grub
%_sysconfdir/bash_completion.d/grub
%_rpmlibdir/%name.filetrigger
# these tools are only for efi and x86_64
%ifarch x86_64 ppc64le
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
%_datadir/grub/grub-mkconfig_lib
%_man1dir/*
%ifarch x86_64
%exclude %_man1dir/grub-render-label*
%exclude %_man8dir/grub-bios-setup*
%exclude %_man8dir/grub-macbless*
%endif
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
%_rpmlibdir/%name-efi.filetrigger
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
modprobe efivars
grep -q '^GRUB_DISTRIBUTOR=' %_sysconfdir/sysconfig/grub2 ||
	echo 'GRUB_DISTRIBUTOR="ALT Linux"' >> %_sysconfdir/sysconfig/grub2

grep -q '^GRUB_BOOTLOADER_ID=' %_sysconfdir/sysconfig/grub2 ||
	echo 'GRUB_BOOTLOADER_ID="altlinux"' >> %_sysconfdir/sysconfig/grub2

grub-efi-autoupdate || {
	echo "** WARNING: grub-efi-autoupdate failed, NEXT BOOT WILL LIKELY FAIL NOW"
	echo "** WARNING: please run grub-efi-autoupdate by hand, record the output offline,"
	echo "** WARNING: make sure you have e.g. rEFInd bootable media handy."
} >&2

%changelog
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

