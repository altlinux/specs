Name: bootloader-utils
Version: 0.4.14
Release: alt1

Summary: Bootloader utilities
License: GPL
Group: System/Base
BuildArch: noarch

Source: %name-%version-%release.tar

PreReq: getopt, make-initrd >= 0.4.3-alt2
Conflicts: grub2 < 1.98-alt13

# Automatically added by buildreq on Thu Feb 22 2007
BuildRequires: perl-devel

%description
This package contains utilities used to manipulate bootloaders.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%makeinstall perl_libdir=%buildroot%perl_vendor_privlib
ln -s `relative %perl_vendor_privlib/bootloader_utils.pm %_datadir/loader/bootloader_utils.pm` \
	%buildroot%_datadir/loader/bootloader_utils.pm
mkdir -p %buildroot/%_rpmlibdir
install -pD -m755 kernel.filetrigger %buildroot/%_rpmlibdir/boot_kernel.filetrigger

mkdir -p %buildroot/%_sysconfdir/sysconfig

cat > %buildroot/%_sysconfdir/sysconfig/installkernel <<-EOF
INITRD_GENERATOR=make-initrd
MKINITRD=%_sbindir/mkinitrd-make-initrd
#INITRD_AUTOUPDATE=all
EOF

%check
make test

%pre
[ $1 -gt 1 ] || exit 0
f=/etc/sysconfig/installkernel
rm -f $f.install
[ ! -f $f ] || exit 0
if [ -f $f.rpmsave ]; then
  cp -a $f.rpmsave $f.install
else
  cat >&2 <<EOF
Neither $f nor $f.rpmsave
exits, no way to find out whether this system was configured to use make-initrd
or mkinitrd by default.  This update implements the first scenario.  If this is
not the case, please edit $f after update.
EOF
fi

%post
[ $1 -gt 1 ] || exit 0
f=/etc/sysconfig/installkernel
[ -f $f.install ] || exit 0
cp -a $f $f.rpmnew 2> /dev/null ||:
mv $f.install $f

%files
%config(noreplace) %_sysconfdir/sysconfig/installkernel
/sbin/installkernel
%_sbindir/detectloader.sh
%_sbindir/detectliloboot.sh
%_sbindir/convertdev.sh
%_sbindir/rebootin
%_datadir/loader/
%perl_vendor_privlib/*.pm
%_man8dir/*.*
%_rpmlibdir/*.filetrigger

%changelog
* Thu Oct 20 2011 Anton Protopopov <aspsk@altlinux.org> 0.4.14-alt1
- installkernel: run depmod before creating initrd

* Wed Jul 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.13-alt1
- support for 3.x kernels added

* Sun Dec 12 2010 Dmitry V. Levin <ldv@altlinux.org> 0.4.12-alt1
- %%pre: when neither /etc/sysconfig/installkernel nor
  /etc/sysconfig/installkernel.rpmsave exists, assume that
  system was configured to use make-initrd (closes: #24739),
  and issue a warning for mkinitrd users.

* Fri Dec 10 2010 Dmitry V. Levin <ldv@altlinux.org> 0.4.11-alt1
- boot_kernel.filetrigger: cleanup,
  do nothing when either /proc or /sys is not mounted.

* Wed Dec 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.10-alt3
- fix options handling bug in installkernel introduced in 0.4.10-alt1
- implement INITRD_AUTOUPDATE={all,default,none} option for automatic
  ramdisks update on kernel install/removal
- set default INITRD_AUTOUPDATE value to 'none'

* Tue Dec 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.10-alt2
- Fixed /etc/sysconfig/installkernel migration issues (ALT #24709):
  + do not switch from mkinitrd to make-initrd if
    make-initrd was not enabled before the update;
  + inherit locally modified config left after make-initrd update

* Tue Dec 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.10-alt1
- introduce NODEFAULT,NOFLAVOUR and KEEPINITRD options for installkernel
- add make-initrd dependency
- add /etc/sysconfig/installkernel from make-initrd

* Mon Nov 29 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.9-alt2
- ldv@: minor filetrigger patch

* Thu Nov 25 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.9-alt1
- implement filetrigger for kernel update

* Mon Nov 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.8-alt4
- rider@: add grub2 support to detectloader.sh

* Thu Sep 30 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.8-alt3
- Remove redundant vmlinuz-smp,vmlinuz-up,initrd-smp.img,initrd-up.img
  links creation
- raorn@: add EXTLINUX support (ALT #24154)
- zerg@: create /boot/vmlinuz-{kflavour} links (ALT #24145)

* Fri Jun 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.8-alt2
- Remove grub-mkconfig call from installkernel (moved to filetrigger)
- (ALT #23333)

* Wed Feb 24 2010 Alexey Gladkov <legion@altlinux.ru> 0.4.8-alt1
- Add make-initrd support.

* Mon Jan 18 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.7-alt1
- grub2 support

* Sat Jan 09 2010 Vladislav Zavjalov <slazav@altlinux.org> 0.4.6-alt1
- lilo:
  - protect quotes in lilo.conf values (closes: #22705);
  - remove spaces from labels
- bootloader_utils.pm: cleanup code of getroot()

* Fri Dec 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4.5-alt1
- detectliloboot.sh: return real boot device when raid-extra-boot
  is set to mbr-only

* Tue Oct 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4.4-alt1
- installkernel: improve error messages (closes: #21914)

* Mon Oct 05 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4.3-alt1
- add convertdev.sh script to convert UUID=.. or LABEL=.. to device names
  use it in detectliloboot.sh and grub scripts (closes #18127)
- bootloader_utils.pm: mnt2dev(): don't use mtab to convert device names

* Mon Sep 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4.2-alt1
- add --label option to installkernel, lilo and grub scripts

* Wed Sep 16 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4.1-alt1
- installkernel:
  - change lilo restarting logic (closes #1014, #1015, #20695):
    old behaviour: restart lilo if first bootloader found in
      devices from /proc/partitions is lilo
    new one: restart lilo when lilo bootloader is found in
      device from boot= setting in lilo.conf
  - when detectliloboot.sh fails to find device, there are no
    need to run detectloader.sh (thx Dmitry V. Levin)
      (closes: #21106)
  - suppress unwanted output from cd -
- detectloader: replace by two shell scripts:
    detectliloboot.sh -- to get boot device from lilo.conf
    detectloader.sh -- to get bootloader type on the given device or file
- bootloader_utils.pm:
  - (getroot): recognize UUID and LABEL
      (thx Dmitry V. Levin) (closes: #2194, #18127)
  - remove unused functions (partitions, typeOfMBR) used in
      removed detectloader program
- rebootin
  - remove GRUB support
  - fix working with quoted labels in lilo.conf (closes: #11446).
  - cleanup code, improve error and help messages
  - add long options, add -l option for listing available labels.
  - update manpage
- remove URL and Packager tags (thx Dmitry V. Levin).

* Fri Mar 07 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt1
- grub: Fixed memtest removal (Alexey Tourbin).
- installkernel:
  + Do not discard /sbin/lilo stdout (Alexey Tourbin).
  + Do not run detectloader in nolaunch mode.
  + Do not invoke "cp" by absolute pathname.
  + Do not touch files in DURING_INSTALL mode,
    thus reverting the change made in 0.3.1-alt2.
  + Replaced non-portable "realpath" with "readlink -e".
  + Fixed xen kernels install (Aleksey Avdeev, #13672).

* Thu Feb 22 2007 Alexey Tourbin <at@altlinux.ru> 0.3.2-alt1
- fixed accidental Windows(tm) removal from lilo.conf (#6102)
- fixed lilo.conf quoting issues (#10903)

* Mon Feb 12 2007 Alexey Gladkov <legion@altlinux.ru> 0.3.1-alt2
- Update symlinks in /boot if DURING_INSTALL specified.

* Fri Feb 09 2007 Alexey Gladkov <legion@altlinux.ru> 0.3.1-alt1.1.1
- NMU:
    - quote lilo parameters.

* Thu Feb 09 2006 Anton Farygin <rider@altlinux.ru> 0.3.1-alt1.1
- NMU:
    - fstab parser fixes (#3318, #8615)
    - installkernel fixes (#4811, #7386)

* Tue Aug 17 2004 Alexey Tourbin <at@altlinux.ru> 0.3.1-alt1
- fixed skiplist processing (Sergey Vlasov, #4254)
- create backup (.old) copies of lilo.conf and grub/menu.lst (#4395)
- installkernel: run mkinitrd(8) without --ifneeded (should hopefully fix #4234 and #4643)

* Fri Jun 11 2004 Alexey Tourbin <at@altlinux.ru> 0.3-alt1
- added support for LABEL and UUID volumes (via /etc/mtab)
- installkernel: save entry for /boot/vmlinuz before upgrade
- installkernel: added support for memtest86
- grub: fix for separate /boot partition, by Sergey Vlasov (#4234)
- started test suite (test.pl)

* Fri May 07 2004 Alexey Tourbin <at@altlinux.ru> 0.2-alt1
- here goes my first major revision; highlights:
  + common.pm -> bootloader_utils.pm, reworked
  + detectloader(1) reworked
  + helpers for lilo(1) and grub(1) configuration files reworked
  + installkernel reworked, /etc/sysconfig/installkernel disappeared

* Wed Mar 19 2003 Peter Novodvorsky <nidd@altlinux.com> 0.1-alt7
- Updated label shorten algorithm in lilo installer script.

* Mon Dec 09 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt6
- Fixed perl dependencies (#0001679).

* Fri Nov 15 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt5
- rebuild
- more features:
    + skiplist for mhz (#0001015)
    + advanced skiping of cdroms (#0001014)

* Fri Mar 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.1-alt4
- Fixed configuration options parsing (imz, #0000507).

* Thu Feb 14 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt3
- added new signature for the GRUB

* Fri Nov 23 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.1-alt2
- Added %%build section, autogenerated buildrequires.

* Wed Nov 14 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.1-alt1
- Imported MDK code (to be rewritten).
