Name: grub
Version: 2.02
Release: alt3

Summary: GRand Unified Bootloader
License: GPL
Group: System/Kernel and hardware

Url: http://www.gnu.org/software/grub

Source0: %name-%version.tar
Source1: grub2-sysconfig

Source3: 39_memtest
Source4: grub.filetrigger

Source5: grub-extras-%version.tar

Source6: grub-autoupdate

Source8: update-grub
Source9: update-grub.8

Source10: grub-efi-autoupdate

Patch0: grub-2.02-os-alt.patch
Patch1: grub-2.00-sysconfig-path-alt.patch
Patch2: grub-2.02-altlinux-theme.patch
Patch3: grub-2.00-debian-uefi-os-prober.patch
Patch4: grub-2.02-os-alt-xen.patch
Patch5: grub-2.02-debian-disable_floppies.patch
Patch6: grub-2.02-add-fw_path-variable.patch
Patch7: grub-2.02-efibootmgr-check.patch
Patch8: grub-2.02-debian-install_signed.patch
Patch9: grub-2.00-fedora-unrestricted.patch
Patch10: grub2-stfu.patch

BuildRequires: flex fonts-bitmap-misc fonts-ttf-dejavu libfreetype-devel python-modules ruby autogen
BuildRequires: liblzma-devel help2man zlib-devel
BuildRequires: libdevmapper-devel
BuildRequires: texinfo
BuildRequires: pesign >= 0.109-alt4
BuildRequires: rpm-macros-uefi
BuildRequires(pre): rpm-build-ubt

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
%global grubefiname grubia32.efi
%endif
%ifarch x86_64
%global grubefiarch x86_64-efi
%global grubefiname grubx64.efi
%endif
%ifarch aarch64
%global grubefiarch arm64-efi
%global grubefiname grubaa64.efi
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

%package efi
Summary: GRand Unified Bootloader (UEFI variant)
Group: System/Kernel and hardware
Requires: %name-common = %EVR
Provides: grub2-efi = %EVR
Obsoletes: grub2-efi < %EVR
PreReq: efibootmgr >= 15
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
%patch3 -p1
%patch4 -p2
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

sed -i 's,@GRUB_EFI_NAME@,%grubefiname,' %SOURCE10
sed -i "/^AC_INIT(\[GRUB\]/ s/%version[^]]\+/%version-%release/" configure.ac

%ifarch %ix86 x86_64
cd ..
rm -rf %name-pc-%version
cp -a %name-%version %name-pc-%version
%endif

%build
%ifarch %ix86 x86_64
pushd ../%name-pc-%version
./autogen.sh
%configure \
	TARGET_LDFLAGS=-static \
	--with-platform=pc \
	--disable-werror

%make_build
popd
%endif

./autogen.sh
%configure \
	TARGET_LDFLAGS=-static \
	--with-platform=efi \
	--disable-werror

%make_build

./grub-mkimage -O %grubefiarch -o grub.efi -d grub-core -p "" \
	part_gpt hfsplus fat ext2 btrfs normal chain boot configfile linux \
	minicmd reboot halt search search_fs_uuid all_video font gfxmenu gfxterm

%install
%ifarch %ix86 x86_64
%makeinstall_std -C ../%name-pc-%version
%endif
%makeinstall_std

install -pDm644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/grub2

%find_lang grub

mkdir -p %buildroot/boot/grub/fonts

install -pD -m755 %SOURCE8 %buildroot%_sbindir/
install -pD -m644 %SOURCE9 %buildroot%_man8dir/update-grub.8

# TODO: drop the obsolete one (unifont.pf2)
%buildroot%_bindir/grub-mkfont -o %buildroot/boot/grub/unifont.pf2 %_datadir/fonts/bitmap/misc/8x13.pcf.gz
%buildroot%_bindir/grub-mkfont -o %buildroot/boot/grub/fonts/unicode.pf2 %font

mkdir -p %buildroot/boot/grub/themes

install -pDm755 %SOURCE3 %buildroot%_sysconfdir/grub.d/
sed -i 's,^libdir=,libdir=%_libdir,g' %buildroot%_sysconfdir/grub.d/39_memtest
sed -i 's,@LOCALEDIR@,%_datadir/locale,g' %buildroot%_sysconfdir/grub.d/*

install -pDm755 %SOURCE4  %buildroot%_rpmlibdir/grub.filetrigger
install -pDm755 %SOURCE6  %buildroot%_sbindir/grub-autoupdate
install -pDm755 %SOURCE10 %buildroot%_sbindir/grub-efi-autoupdate

# Ghost config file
install -d %buildroot/boot/grub
touch %buildroot/boot/grub/grub.cfg
ln -s ../boot/grub/grub.cfg %buildroot%_sysconfdir/grub.cfg

# Docs/habits compat symlink
mkdir -p %buildroot%_sysconfdir/default
ln -s ../sysconfig/grub2 %buildroot%_sysconfdir/default/grub

install -pDm644 grub.efi %buildroot%_efi_bindir/grub.efi

# NB: UEFI GRUB2 image gets signed when build environment is set up that way
%ifarch x86_64
%pesign -s -i %buildroot%_efi_bindir/grub.efi
%endif

# Remove headers
rm -f %buildroot%_libdir/grub-efi/*/*.h

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
%_sysconfdir/grub.d/39_memtest
%config(noreplace) %_sysconfdir/grub.d/40_custom
%config(noreplace) %_sysconfdir/sysconfig/grub2
%_sysconfdir/default/grub
%_sysconfdir/bash_completion.d/grub
%_sbindir/grub-bios-setup
%_sbindir/grub-install
%_sbindir/grub-mkconfig
%_sbindir/grub-ofpathname
%_sbindir/grub-probe
%_sbindir/grub-reboot
%_sbindir/grub-set-default
%_sbindir/grub-sparc64-setup
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
%_bindir/grub-render-label
%_bindir/grub-script-check
%_bindir/grub-syslinux2cfg
%_datadir/grub/grub-mkconfig_lib
%_man1dir/*
%_man8dir/*
%_infodir/grub.info.*
%_infodir/grub-dev.info.*

%ifarch %ix86 x86_64
%files pc
%ghost %config(noreplace) /boot/grub/grub.cfg
%_sysconfdir/grub.cfg
%_sbindir/grub-autoupdate
%_rpmlibdir/%name.filetrigger
%_libdir/grub/*-pc/
%endif

%files efi
%ghost %config(noreplace) /boot/grub/grub.cfg
%_sysconfdir/grub.cfg
%_sbindir/grub-efi-autoupdate
%_rpmlibdir/%name.filetrigger
%_efi_bindir/grub.efi
%_libdir/grub/%grubefiarch

%ifarch %ix86 x86_64
%post pc
grub-autoupdate || {
	echo "** WARNING: grub-autoupdate failed, NEXT BOOT WILL LIKELY FAIL NOW"
	echo "** WARNING: please run it by hand, record the output offline,"
	echo "** WARNING: make sure you have bootable rescue CD/flash media handy"
	echo "** WARNING: and try \`grub-install /dev/sdX' manually"
} >&2
%endif

%post efi
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
* Thu Nov 30 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt3
- fixed sysconfig/grub2 usage in grub-efi post script (closes: #34258)
- fixed Xen menu entry  (closes: #32811)

* Tue Jul 18 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt2
- renamed from grub2 to grub
- added strong requires to efibootmgr >= 15

* Sat Jun 17 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt1%ubt
- add %%ubt for backporting process

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

