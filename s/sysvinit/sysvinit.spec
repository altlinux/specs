Name: sysvinit
Version: 3.00
Release: alt2

%def_enable selinux
%def_enable initramfs

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Summary: Programs which control basic system processes
License: GPLv2+
Group: System/Configuration/Boot and Init
Url: http://savannah.nongnu.org/projects/%name

# ftp://ftp.twaren.net/Unix/NonGNU/%name/%name-%version.tar.bz2
Source: %name-%version.tar

Patch0001: 0001-ALT-Use-program_invocation_short_name-as-progname.patch
Patch0002: 0002-ALT-Mark-usage-functions-as-noreturn.patch
Patch0003: 0003-ALT-Do-not-try-a-few-binaries.patch
Patch0004: 0004-OWL-initcmd_setenv-exclude-INIT_VERSION.patch
Patch0005: 0005-OWL-Fixes.patch
Patch0006: 0006-ALT-Fix-some-build-warnings.patch
Patch0007: 0007-ALT-Add-DISTRO-ALT-to-makefile.patch
Patch0008: 0008-ALT-Change-the-error-message-when-the-getuid-check-f.patch
Patch0009: 0009-ALT-wall-line-size.patch
Patch0010: 0010-ALT-halt-poweroff.patch
Patch0011: 0011-GENTOO-halt-do-kexec-instead-of-reboot-if-another-ke.patch
Patch0012: 0012-Fix-FTBFS-with-glibc-2.28.patch

Provides: SysVinit = %version-%release
Obsoletes: SysVinit < %version-%release

Requires: /sbin/sulogin
Requires: %name-utils = %version-%release
Conflicts: glibc < 6:2.2.1-ipl0.2mdk,
BuildConflicts: openssl-devel < 0.9.6a
# Required for SELinux support.
%{?_enable_selinux:BuildRequires: libselinux-devel}

Conflicts: systemd
Conflicts: systemd-sysvinit

%description
This package contains a group of programs that control the
very basic functions of your system.  sysvinit includes the init
program, the first program started by the Linux kernel when the
system boots.  init then controls the startup, running and shutdown
of all other programs.

%package utils
Summary: Commonly used utilites from sysvinit
Group: System/Base
Conflicts: SysVinit < 2.86-alt2

%description utils
The package contains commonly used non-boot-specific utilities from sysvinit:
bootlogd, killall5, last, lastb, mesg, mountpoint, pidof, pidof, wall.

%if_enabled initramfs
%package initramfs
Summary: Init for initramfs
Group: System/Base

%description initramfs
Simplified version of init (used in initfamfs).
%endif

%prep
%setup
%autopatch -p1

pushd src
find -type f -print0 |
	xargs -r0 grep -FZl '"paths.h"' -- |
	xargs -r0 sed -i 's/"paths\.h"/"paths_init.h"/g' --
mv paths.h paths_init.h
echo '#include <paths.h>' >>paths_init.h
sed -i 's/\<paths\.h\>/paths_init.h/g' -- Makefile
popd

find -type f -name \*.orig -delete

sed -i 's,/run/initctl,/dev/initctl,g' -- man/initctl.5

%build
%if_enabled initramfs
%make_build -C src init \
	DISTRO=ALT \
	CFLAGS='%optflags -fomit-frame-pointer' \
	LDFLAGS= \
	LCRYPT= \
	WITH_SELINUX= \
	#
mv -f src/init{,.initrd}

%make_build -C src clean
%endif

%make_build -C src \
	DISTRO=ALT \
	CFLAGS='%optflags -fomit-frame-pointer' \
	LDFLAGS= \
	LCRYPT= \
	%{?_enable_selinux:WITH_SELINUX=yes} \
	#
%install
mkdir -p %buildroot{/{s,}bin,%_sysconfdir/inittab.d,/dev,/run,%_bindir,%_includedir,%_mandir/man{1,3,5,8}}
%make_install install -C src \
	ROOT=%buildroot \
	DISTRO=ALT \
	#

install -pm755 src/bootlogd src/init.initrd %buildroot/sbin/

mkfifo -m600 %buildroot/dev/initctl
touch %buildroot/run/initctl

# Remove e2fsprogs utility.
rm -f -- %buildroot/sbin/logsave
rm -f -- %buildroot%_man8dir/logsave.*

%pre
# This is tricky.  We don't want to let RPM remove the only link to the
# old init as that would actually leave it pending for delete on process
# termination.  That delete is a filesystem write operation meaning that
# the root filesystem would need to stay mounted read/write.  But we
# absolutely want to be able to remount it read-only during shutdown,
# possibly with the old init still alive!
if [ -e /sbin/init ] && [ ! -e /sbin/.init-working ]; then
	ln /sbin/init /sbin/.init-working
fi

%post
# If /proc is mounted and /sbin/.init-working is running, tell init to
# invoke the replaced version of itself.
if pidof /sbin/.init-working >/dev/null 2>&1; then
	/sbin/telinit u
	sleep 1
fi

# If /proc is not mounted or /sbin/.init-working is no longer running,
# remove it.
if ! pidof /sbin/.init-working >/dev/null 2>&1; then
	rm -f /sbin/.init-working
fi

# Transition to avoid non-rebootable system after upgrade from 2.88
if [ -e /dev/initctl ] && [ -d /run ] && [ ! -e /run/initctl ]; then
	ln -srf /dev/initctl /run/initctl
fi

%files
%attr(700,root,root) /sbin/init
%attr(700,root,root) /sbin/shutdown
%dir %_sysconfdir/inittab.d
/sbin/halt
/sbin/fstab-decode
/sbin/poweroff
/sbin/reboot
/sbin/runlevel
/sbin/telinit
%_man5dir/initscript.*
%_man5dir/inittab.*
%_man5dir/initctl.*
%_man8dir/halt.*
%_man8dir/fstab-decode.*
%_man8dir/init.*
%_man8dir/poweroff.*
%_man8dir/reboot.*
%_man8dir/runlevel.*
%_man8dir/shutdown.*
%_man8dir/telinit.*
%_includedir/*
%ghost /dev/initctl
%ghost /run/initctl

%if_enabled initramfs
%files initramfs
%attr(700,root,root) /sbin/init.initrd
%endif

%files utils
%attr(700,root,root) /sbin/bootlogd
/sbin/killall5
/sbin/pidof
/bin/mountpoint
/bin/pidof
%_bindir/last
%_bindir/lastb
%_bindir/mesg
%_bindir/readbootlog
%attr(2711,root,tty) %_bindir/wall
%_man1dir/last.*
%_man1dir/lastb.*
%_man1dir/mesg.*
%_man1dir/mountpoint.*
%_man1dir/wall.*
%_man1dir/readbootlog.*
%_man8dir/bootlogd.*
%_man8dir/killall5.*
%_man8dir/pidof.*

%changelog
* Thu May 19 2022 Alexey Gladkov <legion@altlinux.ru> 3.00-alt2
- Create /run/initctl as a symlink to /dev/initctl to help with migration
  without reboot (ALT#42789).

* Thu Dec 16 2021 Alexey Gladkov <legion@altlinux.ru> 3.00-alt1
- Updated to 3.00.
- Reviewed patches.

* Thu Dec 16 2021 Alexey Gladkov <legion@altlinux.ru> 2.88-alt7
- Add conflict to systemd to make it impossible to install systemd on a system
  with sysvinit (ALT#41579).

* Mon Nov 11 2019 Dmitry V. Levin <ldv@altlinux.org> 2.88-alt6
- Fixed build with glibc >= 2.28.
- Removed explicit "PreReq: coreutils".

* Thu Feb 19 2015 Alexey Gladkov <legion@altlinux.ru> 2.88-alt5
- Add subpackage for initramfs (closes: #30738).

* Wed Jun 13 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.88-alt4
- halt: do kexec instead of reboot if another kernel is loaded

* Wed Oct 05 2011 Dmitry V. Levin <ldv@altlinux.org> 2.88-alt3
- poweroff: pass "-P" option to shutdown (closes: #26391).
- halt: pass "-H" option to shutdown.

* Tue Apr 05 2011 Dmitry V. Levin <ldv@altlinux.org> 2.88-alt2
- Renamed SysVinit to sysvinit.

* Thu Aug 05 2010 Dmitry V. Levin <ldv@altlinux.org> 2.88-alt1
- Updated to 2.88-11.
- Enabled SELinux support.
- sysvinit-utils: added controversial Conflict (closes: #15625).
- Fixed wall(1) output.

* Fri Apr 25 2008 Dmitry V. Levin <ldv@altlinux.org> 2.86-alt2
- Moved commonly used non-boot-specific utilities to sysvinit-utils
  subpackage, based on work made by Dmitry M. Maslennikov.

* Sat Jan 06 2007 Dmitry V. Levin <ldv@altlinux.org> 2.86-alt1
- Updated to 2.85-36.
- Reviewed patches.

* Mon May 15 2006 Dmitry V. Levin <ldv@altlinux.org> 2.85-alt9
- Fixed build with gcc-4.1.0.

* Tue May 24 2005 Dmitry V. Levin <ldv@altlinux.org> 2.85-alt8
- Fixed 64bit compilation issues.

* Sat Jan 03 2004 Dmitry V. Levin <ldv@altlinux.org> 2.85-alt7
- Updated to 2.85-9.
  + Merged upstream patches:
    owl-wall-longjmp-clobbering
    owl-format
    alt-owl-bootlogd
    owl-mount-proc
    owl-typos
    rh-alt-owl-shutdown-log
    owl-alt-makefile
  + Updated patches:
    alt-progname-umask
    rh-alt-pidof
    alt-doc
- Do not try to exec /sbin/mount.
- Fixed three potential problems introduced in 2.85-9.
- Fixed few signedness (harmless though) issues.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.85-alt6
- Fixed build.
- Build with -Werror.
- Fixed annoying 'must be superuser' error messages.

* Mon May 12 2003 Dmitry V. Levin <ldv@altlinux.org> 2.85-alt5
- Removed rh-alt-halt patch,
  install startup >= 0.1-alt1 package is recommended.
- Do not package start-stop-daemon by default,
  moved to service >= 0.1-alt1 package.

* Tue May 06 2003 Dmitry V. Levin <ldv@altlinux.org> 2.85-alt4
- PreReq: coreutils (#0002562).

* Sun Apr 27 2003 Dmitry V. Levin <ldv@altlinux.org> 2.85-alt3
- Synced with 2.85-owl4:
  + Don't build sulogin, use new implementation from msulogin package.
  + Don't mount /proc in pidof, and mount it as "proc" rather than "none"
    in killall5 such that umount and others can reasonably refer to it in
    error messages.
- Do not package utmpdump.

* Wed Apr 23 2003 Dmitry V. Levin <ldv@altlinux.org> 2.85-alt2
- Synced with 2.85-owl1:
  + New/updated patches:
    owl-wall-longjmp-clobbering
    owl-format
    owl-alt-sulogin
    alt-owl-start-stop-daemon
    alt-owl-bootlogd
    owl-mount-path
    owl-typos
    rh-alt-owl-shutdown-log

* Sun Apr 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.85-alt1
- Updated to 2.85.
  + Following patches are merged upstream:
    alt-wall-alarm
    alt-init-spawn
    alt-sulogin-notty
    rh-alt-wait
    owl-alt-bound
    owl-alt-format
    alt-wall-tty
    alt-man-wall
  + Updated patches:
    owl-alt-sulogin
- /sbin/start-stop-daemon:
  + various safety fixes;
  + changed pid_is_exec check.
- Provides: /sbin/start-stop-daemon.

* Tue Apr 15 2003 Dmitry V. Levin <ldv@altlinux.org> 2.84-alt8
- Reworked patches: following patches are going upstream:
  alt-wall-alarm
  alt-init-spawn
  alt-sulogin-notty
  rh-alt-wait
  owl-alt-bound
  owl-alt-format
  alt-wall-tty
  alt-man-wall

* Fri Apr 04 2003 Dmitry V. Levin <ldv@altlinux.org> 2.84-alt7
- Updated to 2.84-3.
- wall: fixed alarm handling (#0002460).

* Sat Mar 01 2003 Dmitry V. Levin <ldv@altlinux.org> 2.84-alt6
- Fixed build in system without /dev/initctl available.
- pidof: honor full pathname.
- wall: avoid writing to non-tty devices.
- last: added '-t' option for checking state at certain times (rh).
- shutdown: added logging on shutdown/reboot (rh).
- shutdown: spawn: fixed child process handling and program execution (rh).

* Tue Dec 10 2002 Dmitry V. Levin <ldv@altlinux.org> 2.84-alt5
- src/init.c(spawn): fixed bug reported by Vladimir N. Oleynik.
- Packaged /sbin/bootlogd and /sbin/start-stop-daemon.

* Tue Sep 17 2002 Dmitry V. Levin <ldv@altlinux.org> 2.84-alt4
- Revert back /sbin/halt permissions (to reenable -usermode).
- Use subst instead of perl in build scripts.

* Tue Aug 06 2002 Dmitry V. Levin <ldv@altlinux.org> 2.84-alt3
- Marked /dev/initctl socket as %%ghost (#0001125).

* Sat Jul 13 2002 Dmitry V. Levin <ldv@altlinux.org> 2.84-alt2
- Reviewed patches, dropped obsolete ones.
- Added building of bootlogd and start-stop-daemon.
- Restricted permissions on root-only programs.

* Thu Feb 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.84-alt1
- 2.84
- Added initreq.h

* Wed Nov 14 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.83-alt1
- 2.83
- Moved usermode stuff to separate package.

* Tue Sep 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.82-alt2
- usermode: fixed pam config.

* Wed Aug 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.82-alt1
- 2.82

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.81-alt2
- Fixed version display info.
- Changed usermode subpackage requirements.

* Wed Aug 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.81-alt1
- 2.81
- Added usermode subpackage with consolehelpr bindings.

* Fri Jun 01 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.78-ipl5mdk
- Progname patch.
- Various bound and format checks from Owl project.
- Ensure the umask is no less restrictive than 022 (owl).
- Use getpass(3) in sulogin - the old code was unreliable (owl).

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.78-ipl4mdk
- Fixed umask (rh).

* Fri Feb 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.78-ipl3mdk
- Merged RH patches:
  + document '-n' option to wall, make it root-only (rh).
  + don't open files in sulogin unless they're really ttys (rh).

* Wed Jan 10 2001 Dmitry V. Levin <ldv@fandra.org> 2.78-ipl2mdk
- Added blowfish crypt support (from libcrypt).

* Wed Oct 18 2000 Dmitry V. Levin <ldv@fandra.org> 2.78-ipl1mdk
- Merged MDK, RH and BCL patches.
- Re-execute /sbin/init in %post.

* Sun Feb 20 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Wed Jan  5 2000 Dmitry V. Levin <ldv@fandra.org>
- Merge with mdk

* Fri Oct 22 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with redhat changes.

* Tue Sep 28 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- nologin patch isn't needed

* Tue Sep 14 1999 Daouda LO <daouda@mandrakesoft.com>
- 2.77

* Wed May 19 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- We can't hardlink /bin/pidof anywhere, because it's a symlink itself.
  Fix...

* Tue May 18 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Linking /bin/pidof to /sbin/pidof for RH compatibilities.

* Mon Apr 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- The normal source doen't work, we need to remove the orphan link to rebuild.

* Fri Apr  9 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- update to 2.76
- bzip2 man pages
- handle RPM_OPT_FLAGS
- remove some RH patches because they're not required with 2.76
- add de, fr, tr locales
- Move pidof from /sbin to /bin - can't hurt.

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- glibc 2.1

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- poweroff symlink not included (problem #762)

* Thu Jul 09 1998 Chris Evans <chris@ferret.lmh.ox.ac.uk>
- Fix a securelevel releated security hole. Go on, try and break append
  only files + securelevel now ;-)

* Wed Jul  8 1998 Jeff Johnson <jbj@redhat.com>
- remove /etc/nologin at end of shutdown.
- compile around missing SIGPWR on sparc

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.74
- fixed the package source url... (yeah, it was wrong !)

* Wed Oct 1 1997 Cristian Gafton <gafton@redhat.com>
- fixed the MD5 check in sulogin (128 hash bits encoded with base64 gives
  22 bytes, not 24...). Fix in -md5.patch

* Thu Sep 11 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- /etc/initrunlvl gets linked to /tmp/init-root/var/run/initrunlvl which is
  just plain wrong..
- /usr/bin/utmpdump was missing in the files section, although it was
  explicitly patched into PROGS.
- added attr's to the files section.
- various small fixes.

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- updated to 2.71
- built against glibc 2.0.4

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added sulogin.8 man page to file list.
