Name: basesystem
Version: sisyphus
Release: alt21
Epoch: 1

Summary: The skeleton package which defines a basic %distribution chroot
License: GPLv2+
Group: System/Base
BuildArch: noarch

Requires: altlinux-release
Requires: bash
Requires: bzip2
Requires: common-licenses
Requires: coreutils >= 6.12
Requires: diffutils
Requires: etcskel
Requires: filesystem
Requires: findutils
Requires: gawk
Requires: getopt
Requires: grep
Requires: gzip
Requires: perl-base
Requires: rootfiles
Requires: rpm
Requires: sed
Requires: setup
Requires: shadow-utils
Requires: tar
Requires: util-linux
Requires: vitmp
Requires: xz

%package -n interactivesystem
Summary: The skeleton package which defines an interactive %distribution system
Group: System/Base
Requires: %name = %epoch:%version-%release
Requires: chkconfig
Requires: console-common-scripts
Requires: crontabs
Requires: e2fsprogs
Requires: info
Requires: less
Requires: losetup
Requires: man
Requires: mingetty
Requires: network-config-subsystem
Requires: termutils
Requires: passwd
Requires: sash
Requires: service
Requires: startup
Requires: stmpclean
Requires: syslogd-daemon
Requires: SysVinit
Requires: time
Requires: which

%description
This package defines the components of a basic %distribution system
(for example, the package installation order to use during bootstrapping).

%description -n interactivesystem
This package defines the components of an interactive %distribution system
(for example, the package installation order to use during bootstrapping).

%files
%files -n interactivesystem

%changelog
* Wed Apr 06 2011 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt21
- Merged /bin/hostname, mktemp and stat into versioned coreutils.
- Moved from basesystem to interactivesystem:
  SysVinit, e2fsprogs, losetup, service, which;
- Added to basesystem: xz.

* Sun Nov 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt20
- Moved chkconfig and startup from basesystem to interactivesystem.

* Fri Aug 14 2009 Alexey Tourbin <at@altlinux.ru> 1:sisyphus-alt19
- basesystem: Added which.

* Wed Jul 29 2009 Alexey Tourbin <at@altlinux.ru> 1:sisyphus-alt18
- basesystem: Removed info-install.
- interactivesystem: Added syslogd-daemon.

* Wed Apr 11 2007 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt17
- interactivesystem: Removed sound-scripts.

* Sun Mar 11 2007 Alexey Tourbin <at@altlinux.ru> 1:sisyphus-alt16
- basesystem: Added mktemp.

* Tue Nov 21 2006 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt15
- basesystem: Added bzip2.

* Wed Feb 01 2006 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt14
- basesystem:
  + removed dev;
  + replaced vim-minimal with vitmp.

* Sun Apr 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt13
- basesystem:
  + replaced net-tools with /bin/hostname (#6360).
- interactivesystem:
  + replaced tmpwatch with stmpclean;
  + removed mkbootdisk (#5717);
  + removed bdflush (#6485).

* Mon Apr  4 2005 Ivan Zakharyaschev <imz@altlinux.ru> 1:sisyphus-alt12
- interactivesystem: substituted "console-common-scripts" for
  "console-tools_or_kbd console-data".

* Wed Nov 17 2004 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt11
- s/net-scripts/network-config-subsystem/ (#5490).

* Mon Apr  5 2004 Ivan Zakharyaschev <imz@altlinux.ru> 1:sisyphus-alt10
- interactivesystem: 
  + added console-data (due to splitted console-tools-0.2.3-ipl24mdk), 
  + substituted console-tools_or_kbd for console-tools.

* Mon Sep 22 2003 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt9
- basesystem: added bash (#3018).

* Thu Apr 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt8
- basesystem: replaced initscripts with service + startup.
- interactivesystem: added packages: sound-scripts net-scripts.

* Wed Feb 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt7
- Added getopt to basesystem list.

* Fri Feb 07 2003 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt6
- Removed kernel and bash from basesystem list.

* Tue Sep 17 2002 Stanislav Ievlev <inger@altlinux.ru> 1:sisyphus-alt5
- Merged sh-utils, textutils and fileutils into coreutils.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt4
- interactivesystem:
  + removed from requires: ncurses.
  + added to requires: termutils.

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt3
- interactivesystem: removed from requires: termcap, ntsysv.

* Sun Jun 02 2002 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt2
- basesystem: removed from requires: crontabs, ncurses.
- interactivesystem: added to requires: bdflush, crontabs, mingetty, ncurses.

* Sat Nov 17 2001 Dmitry V. Levin <ldv@altlinux.org> 1:sisyphus-alt1
- Split into two packages.
- Cleanup requires.

* Sat Mar 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 7.2-ipl4mdk
- Changed kernel to kernel-up.

* Wed Jan 31 2001 Dmitry V. Levin <ldv@fandra.org> 7.2-ipl3mdk
- Added require on common-licenses.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 7.2-ipl2mdk
- Removed sysklogd from requires.

* Fri Oct 27 2000 Francis Galiegue <fg@mandrakesoft.com> 7.2-2mdk
- ia64: does not require ldconfig nor procmail for now - KLUDGE - see spec file
  for details
- ia64: requires eli

* Mon Oct  9 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 7.2-1mdk
- 7.2

* Fri Mar 24 2000 Pixel <pixel@mandrakesoft.com> 7.1-4mdk
- remove the BuildArchitectures: noarch
 (otherwise can't have arch dependent Requires, silly me)

* Wed Mar 22 2000 Pixel <pixel@mandrakesoft.com> 7.1-3mdk
- changed require vim-minimal to vim (thanks Quel Qun)

* Tue Mar 21 2000 Pixel <pixel@mandrakesoft.com> 7.1-2mdk
- added a *lot* of requires. Now *is* the base

* Mon Mar 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 7.1-1mdk
- Upgrade version.
- Update groups.

* Thu Dec  2 1999 Pixel <pixel@linux-mandrake.com>
- changed back Requires to preReq :(

* Wed Dec  1 1999 Pixel <pixel@linux-mandrake.com>
- changed preReq to Requires

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build Release.

* Tue Jul 06 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build in the new environement (VER: 6mdk).

* Fri Apr  9 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- add de locale

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- don't require rpm (breaks dependency chain)

* Tue Mar 16 1999 Erik Troan <ewt@redhat.com>
- require rpm

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
