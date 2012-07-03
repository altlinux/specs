Name: MAKEDEV
Version: 3.3.1
Release: alt20

%define revision 3

Summary: A program used for creating the device files in /dev
License: GPL
Group: System/Kernel and hardware

Url: http://www.lanana.org/docs/device-list/
Source: %name-%version-%revision.tar.bz2
Patch: MAKEDEV-3.3.1-alt.patch.bz2
Patch1: MAKEDEV-3.3.1-alsa-alt.patch
Patch2: MAKEDEV-3.3.1-dvb-alt.patch
Patch3: MAKEDEV-3.3.1-alt-pack.patch
Patch4: MAKEDEV-3.3.1-alt-zaptel.patch
Patch5: MAKEDEV-3.3.1-alt-microcode-ACM.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildPreReq: rpm >= 0:4.0.3-alt1
Requires: dev = %version-%release

%define dev_minimal_re null|full|zero|console|ptmx|tty0?|fb0|u?random|std(in|out|err)|fd|(hd[a-d]|sd[a-h])([1-9]|1[0-5]|)|ttyS[0-3]

%define udev_test(r:i:) \
if [ -r /proc/mounts ]; then \
	(while read dev mountpoint rest ; do \
		[ "$mountpoint" != /dev ] || exit 1 \
	done \
	exit 0 ) < /proc/mounts || { \
		echo \
		echo '** Cannot %{-r:remove %{-r*}}%{-i:install %{-i*}}: mounted udev detected.' \
		echo '** This is no problem, but to avoid side-effects with' \
		echo '** stopping and starting it automatically, please do:' \
		echo 'service udevd umount' \
		echo '%{-r:rpm -e %{-r*}}%{-i:apt-get install %{-i*}}' \
		echo 'service udevd restart' \
		echo '** Note that some services like syslogd or gpm might need' \
		echo '** restart after this, too; dcop (KDE) might have problems.' \
		exit 1 \
	} \
fi

%package -n dev-minimal
Group: System/Kernel and hardware
Summary: Base entries in the /dev directory
Conflicts: dev < 3.3.1-alt19
Provides: /dev, /dev/pts
PreReq: sh, grep, mktemp, sed, setup >= 2.1.9-ipl15mdk, coreutils
AutoReqProv: no

%package -n dev
Group: System/Kernel and hardware
Summary: Commonly used entries in the /dev directory
Requires: dev-minimal = %version-%release
AutoReqProv: no

%description
This package contains the %name script, which makes it easier to create
and maintain the files in the /dev directory.  /dev directory files
correspond to a particular device supported by Linux (USB, parallel
or serial ports, scanners, sound cards, hard/optical/tape drives, etc.)
and interface with the drivers in the kernel.

%description -n dev-minimal
This package contains the very basic set of /dev entries; it is suited
for bare chroots or installed systems which should be minimally equipped
with /dev even if/when udev is not running.  You should consider full
dev package if for some reason you would like any other devices there.

%description -n dev
ALT Linux operating system uses file system entries to represent
devices (CD-ROMs, floppy drives, etc.) attached to the machine. All of
these entries are in the /dev tree (although they don't have to be).

This package contains commonly used /dev entries.

%prep
%setup -q
%patch -p1
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1

subst 's/-g -Wall/%optflags/;s/install /\$(INSTALL) /g' Makefile
find -type f -name \*.orig -print0 | xargs -r0 rm -vf

%build
make

%install
makedev() {
	# Note that we need RPM 4.0.3-0.71 or higher for this to be of any use,
	# but otherwise we could screw up ownerships if the destination account
	# doesn't exist when we run MAKEDEV.
	%buildroot/dev/MAKEDEV \
	-c %buildroot%_sysconfdir/makedev.d \
	-d %buildroot/dev -M $@ | sed "s|%buildroot||g" >> manifest
}

rm -f manifest

%makeinstall devdir=%buildroot/dev
mkdir -p %buildroot/sbin
mv -f %buildroot/dev/MAKEDEV %buildroot/sbin
ln -s ../sbin/MAKEDEV %buildroot/dev/MAKEDEV

makedev adb -m 56
makedev agpgart
makedev alsa
makedev ataraid
makedev apm_bios
makedev audioctl
makedev beep
makedev capi20
makedev cdrom
makedev cfs
makedev compaq
makedev console -m 32
makedev cpu
makedev cua -m 4
makedev cui -m 16
makedev dasd
makedev dac960
makedev dri
makedev dvb
makedev dv1394r
makedev dv1394w
makedev efirtc
makedev em8300
makedev enskip
makedev fujitsu/apanel
makedev fb
makedev fd
makedev fd0
makedev fd1
makedev ftape
makedev ht -m 2
makedev i2c -m 2
makedev i2o
makedev ibcs
makedev ida
makedev ide -m 33
makedev initrd
makedev input -m 32
makedev ip -m 16
makedev ipfilter -m 16
makedev ir
makedev iscc -m 2
makedev isdn -m 16
makedev ixj
makedev kbd
makedev js -m 4
makedev kpoll
makedev lirc
makedev log -m 1
makedev loop -m 32
makedev lp -m 8
makedev mandrake
makedev mbuf
makedev md
makedev microcode
makedev mouse
makedev nb -m 32
makedev net/tun
makedev netlink
makedev nht -m 2
makedev nst -m 16
makedev openprom
makedev osst -m 4
makedev nvidia
makedev par -m 8
makedev pcd -m 4
makedev pd
makedev pf -m 4
makedev pg -m 4
makedev pktcdvd -m 4
makedev ppp -m 4
makedev pt
makedev ptmx
makedev pty
makedev qng
makedev raid
makedev ram -m 20
makedev random
makedev raw
makedev rd
makedev rmt
makedev rtc
makedev rtf -m 64
makedev rtsock -m 6
makedev scd -m 8
makedev scramdisk -m 16
makedev sd
makedev sg -m 32
makedev shm
makedev slamr -m 4
makedev smpt
makedev sound
makedev sr -m 8
makedev st -m 16
makedev staliomem -m 4
makedev std
makedev systty
makedev tlk
makedev toshiba
makedev thinkpad
makedev tty -m 32
makedev urandom
makedev usb -m 32
makedev v4l -m 4
makedev vcs
makedev video1394
makedev vmmon
makedev vnet -m 4
makedev winradio -m 4
makedev xda
makedev xdb
makedev vhci
makedev rfcomm
makedev nvram
makedev rtf -m 16
# makedev xpram
makedev zap
makedev kqemu
makedev qvm86
makedev vzctl
makedev sonypi
makedev ham
makedev fuse

# Put some base entries aside for dev-minimal package.
egrep '/dev/(%dev_minimal_re)$' manifest \
| sort -ub -t/ -k2 \
> dev-minimal.list

# Skip /dev/log for the sake of upgrades to really old dev packages.
grep -v '/dev/log$' manifest \
| egrep -v '/dev/(%dev_minimal_re)$' \
| sort -ub -t/ -k2 \
> dev.list

# Make subdirectories we otherwise would have nothing to do with.
install -d -m755 %buildroot/dev/{pts,shm}

%pre -n dev-minimal
%udev_test -i dev-minimal

%post -n dev-minimal
if [ -f %_sysconfdir/fstab ]; then
	# Add /dev/pts to fstab if fstab exists (install2 does it during install).
	if grep -F -qs devpts %_sysconfdir/fstab; then
		if grep -qs 'devpts.*mode=0622' /etc/fstab; then
			# Correct permissions from broken dev packages.
			TMP=$(mktemp /tmp/fstab.XXXXXX) &&
			sed -e 's/devpts.*mode=0622/devpts	gid=5,mode=0620/' <%_sysconfdir/fstab >"$TMP" &&
				cat "$TMP" >%_sysconfdir/fstab ||
				echo "failed to correct devpts permissions in %_sysconfdir/fstab" 1>&2
			rm -f "$TMP"
		fi
	else
		echo 'devpts		/dev/pts		devpts	gid=5,mode=0620	0 0' >>%_sysconfdir/fstab
	fi
fi
PCA=/sbin/pam_console_apply
[ -x "$PCA" ] && "$PCA" ||:

%preun -n dev-minimal
%udev_test -r dev-minimal ||:

# RPM would let dev-minimal installation break
# but install dev (which requires the same dev-minimal)
# during that transaction; so need to check here too
%pre -n dev
%udev_test -i dev
[ -L /dev/snd ] && rm -f /dev/snd ||:
[ -d /dev/video ] && rm -rf /dev/video ||:

%post -n dev
PCA=/sbin/pam_console_apply
[ -x "$PCA" ] && "$PCA" ||:

%preun -n dev
%udev_test -r dev ||:

%files
/dev/MAKEDEV
/sbin/*
%_sbindir/*
%_mandir/man?/*
%config(noreplace) %_sysconfdir/makedev.d/*
%doc devices.txt

%files -n dev-minimal -f dev-minimal.list
%dir /dev
%ghost /dev/log
%dir /dev/pts
%dir /dev/shm

%files -n dev -f dev.list

# - if anything can be done with udevd autostop/start
#   (there are known problems at least with syslog, gpm and dcop/kde)
# - remove (failing) attempts to makedev dac960, ixj, microcode
# - add ttyUSB (think USB UPS) and/or USB HID to dev-minimal?
# - (led@) add ram#, loop#, tty# to dev-minimal? (bare+0..3/1..15)
# - (led@) /dev/mapper/control -> ../device-mapper
# - (lakostis@) NB: /dev/mem for xorg
# - (led@) NB: /dev/tty7, 12 for xorg (at least in ALTSP)
# - add dev-asterisk (=> no more nonexistant group spam :)

%changelog
* Mon Mar 31 2008 Michael Shigorin <mike@altlinux.org> 3.3.1-alt20
- whoops, unfinished re-re-making of preinstall script
  (alt19 didn't really test for udev due to wrong src.rpm
  being uploaded)
- forgot re-adding dev package as well
- thus rebuilt
- don't break package uninstallation either
  (bug introduced in 3.3.1-alt19)

* Thu Mar 13 2008 Michael Shigorin <mike@altlinux.org> 3.3.1-alt19
- split dev package into dev and dev-minimal (#14887)
- the following /dev entries were moved from dev to dev-minimal
  + /dev, /dev/pts, /dev/shm directories
  + /dev/fd, /dev/stdin, /dev/stdout, /dev/stderr symlinks
  + /dev/log (ghost file)
  + /dev/null, /dev/full, /dev/zero
  + /dev/random, /dev/urandom
  + /dev/console, /dev/tty, /dev/tty0, /dev/ptmx, /dev/fb0
  + /dev/hda..hdd, sda..sdh (including partition devices up to 15)
  + /dev/ttyS0..ttyS3 (see also #11888)
- added preun scripts to guard against package removal
  while udevd is actually running
- minor spec cleanup
- re-added an Url:

* Sat Mar 10 2007 Michael Shigorin <mike@altlinux.org> 3.3.1-alt18
- updated message upon detecting udev ("umount", not "stop")

* Sat Mar 03 2007 Michael Shigorin <mike@altlinux.org> 3.3.1-alt17
- updated patch2 (changed dvb major from 250 to 212, fixes #10926)
  + thanks Sergey Vlasov (vsu@) for detailed bugreport

* Sun Nov 12 2006 Michael Shigorin <mike@altlinux.org> 3.3.1-alt16
- changed:
  + /dev/slamr*: major from 212 to 242 (#10234)

* Sat Oct 28 2006 Michael Shigorin <mike@altlinux.org> 3.3.1-alt15
- added:
  + /dev/fuse (#10048)
- changed:
  + /dev/cpu/%%d/microcode -> /dev/cpu/microcode (#6854)
  + /dev/input/ttyACM%%d -> /dev/ttyACM%%d (#6854)

* Sun Sep 24 2006 Michael Shigorin <mike@altlinux.org> 3.3.1-alt14
- package takeover
- added:
  + /dev/sonypi (#4927)
  + /dev/zap/ (#5745)
  + /dev/ham (#7885)
  + /dev/kqemu, /dev/qvm86, /dev/vzctl (#8618)
- spec macro abuse cleanup

* Wed Jan 05 2005 Dmitry V. Levin <ldv@altlinux.org> 3.3.1-alt13.1
- dev: added /dev and /dev/pts to package provides.

* Mon Jul 26 2004 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt13
- added /dev/sr* (#4870)
- added /dev/fujitsu/apanel (#4778)

* Tue Jun 29 2004 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt12
- added /dev/dv1394(r,w) (#3965)
- added /dev/toshiba (#3664)
- added /dev/thinkpad/thinkpad (#4224)

* Fri Jan 23 2004 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt11
- added /dev/slamr*, ttySL0 now is link to /dev/slamr0
- added /dev/rtf*, /dev/rtsock*, /dev/mbuff
- added /dev/dvb/* for DVB devices (#3469)

* Wed Dec 10 2003 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt10
- added /dev/pctINT (Intel modem)

* Sun Nov 02 2003 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt9
- added /dev/pktcdvd* (#3225)

* Thu Sep 25 2003 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt8
- removed /dev/video directory

* Thu Sep 11 2003 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt7
- added /dev/nvram
- added /dev/ttyLT0 (#2899)

* Mon Jul 28 2003 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt6
- Added /dev/snd/* for new ALSA

* Tue Jul 08 2003 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt5
- Added device for PCTEL modem

* Wed Jun 25 2003 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt4
- Updated EM8300 devices
- Added aloadC* symlinks for aload* (#0002297)

* Thu Mar 27 2003 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt3
- Added bluetooth devices

* Mon Jan 20 2003 Konstantin Volckov <goldhead@altlinux.ru> 3.3.1-alt2
- Added slmdm device

* Thu Nov 21 2002 Kachalov Anton <mouse@altlinux.ru> 3.3.1-alt1
- 3.3.1
- include the /dev/iseries devices on ppc64
- build nosst devices (#72914)
- build the tunnelling device (/dev/net/tun)
- add configuration for libraw1394 (#67203)
- build 32 scsi generic devices
- add cfs device used by coda
- resync with current LANANA updates, remove ibcs config file
- resync with usb device list
- create kpoll and 16 scramdisk devices
- handle a step of 0 when creating multiple nodes
- add /dev/cpu/*/microcode (perms 0600) to the dev package
- up the limit on ide devices (hda through hdt) back up from 17 to 33
- actually create the vsys device

* Mon Apr 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.2-alt3
- Added pam_console_apply call to %%post.

* Mon Jan 21 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.2-alt2
- Moved em8300 devices from /dev/video/ to /dev/.
- Resurrected /dev/video symlink to /dev/video0.
- Added /dev/lirc device.

* Wed Jan 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.2-alt1
- Upgraded to 3.2-6 (added a lot of new devices).
- Moved MAKEDEV to /sbin (symlink kept for compatibility).
- Enable unprivileged packaging!

* Thu Nov  8 2001 Grigory Milev <week@altlinux.ru> 3.2-5-alt1
- New version released

* Tue Jan 23 2001 Dmitry V. Levin <ldv@fandra.org> 3.0.6-ipl5mdk
- Fixed defattr for dev subpackage.
- Upgraded to -8 release of RH.
- Added more devices.

* Tue Dec 26 2000 Dmitry V. Levin <ldv@fandra.org> 3.0.6-ipl4mdk
- RE adaptions.
- Added ibcs devices.

* Tue Nov 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.6-4mdk
- Put config files as noreplace.

* Wed Nov 15 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.6-3mdk
- Add toshiba devices.
- Upgrade to -7 release of rh.

* Wed Sep 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.6-2mdk
- Make pg* as cdwriter group (thanks till).

* Wed Aug 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.6-1mdk
- add an rm -f $TMP in %%post (pixel).
- Correct alsa link.
- Merge with RH 3.0.6

* Mon Jul 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.2-5mdk
- Correct usbmouse link to input/mouse0.

* Wed Jul 26 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.2-4mdk
- Create ppp devices.

* Tue Jul 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.2-3mdk
- Don't remove isdnctl (remove it from the isdn package instead).
- Correct micrcode in the right way (titi sucks).

* Tue Jul 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.0.2-2mdk
- remove RH microcode entry and reput the entires i add to dev before
  lord chmoue destroy it : cpu/{mircrocode,?/{cpuid,msr} for 2cpuid,msr} for
  2.4.x
- remove also conflicting /dev/isdnctrl

* Mon Jul 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.2-1mdk
- Mandrake adaptation of the new dev system.
- Merge dev system of Red Hat.
- Merge MAKEDEV and dev package.

