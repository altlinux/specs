Name: gpm
Version: 1.20.1
Release: alt18

Summary: A mouse server for the Linux console
License: GPLv2+
Group: System/Servers

# ftp://arcana.linux.it/pub/gpm/gpm-%version.tar.bz2
Source: gpm-%version.tar
Source1: gpm.init
Source2: gpm.service

Patch1: gpm-1.20.1-alt-texinfo.patch
Patch2: gpm-1.20.1-owl-gpm-root.patch
Patch3: gpm-1.20.1-owl-liblow.patch
Patch4: gpm-1.20.1-owl-warnings.patch
Patch5: gpm-1.20.1-alt-daemonize.patch
Patch6: gpm-1.20.1-alt-get_console.patch
Patch7: gpm-1.20.1-alt-syslog.patch
Patch8: gpm-1.20.1-alt-nodebug.patch
Patch9: gpm-1.20.1-alt-log.patch
Patch10: gpm-1.20.1-alt-progname.patch
Patch11: gpm-1.20.1-alt-pam_console_apply.patch
Patch12: gpm-1.20.1-alt-rh-shlib.patch
Patch13: gpm-1.20.1-deb-alt-xterm_mouse_support.patch
Patch14: gpm-1.20.1-mdk-alt-consolename.patch
Patch15: gpm-1.20.1-alt-netmouse.patch
Patch16: gpm-1.20.1-deb-stack-fix.patch
Patch17: gpm-1.20.1-alt-gpm_open-shutup.patch
Patch18: gpm-1.20.1-alt-libm.patch
Patch19: gpm-1.20.1-alt-AC_GNU_SOURCE.patch
Patch20: gpm-1.20.1-alt-mice.patch
Patch21: 0001-Un-nest-wacom-helpers-in-src-mice.c-for-Clang-compat.patch
Patch22: 0002-Un-nest-summa-helpers-in-src-mice.c-for-Clang-compat.patch
Patch23: gpm-1.20.1-alt-sigemptyset.patch

Requires: lib%name = %version-%release

# Automatically added by buildreq on Sat Mar 10 2007
BuildRequires: libncurses-devel
BuildRequires: makeinfo

%package -n lib%name
Summary: Shared library for running mouse driven programs
Group: System/Libraries
Provides: %name-lib = %version
Obsoletes: %name-lib

%package -n lib%name-devel
Summary: Include files for developing mouse driven programs
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel

%package -n lib%name-devel-static
Summary: Static library for developing static mouse driven programs
Group: Development/C
Requires: lib%name-devel = %version-%release
Requires: libtinfo-devel-static

%package root
Summary: A mouse server add-on which draws pop-up menus on the console
Group: System/Servers
Requires: %name = %version-%release

%description
gpm provides mouse support to text-based Linux applications
as well as console cut-and-paste operations using the mouse.

%description -n lib%name
This package contains the shared library needed for running of
mouse driven programs for the console.

%description -n lib%name-devel
This package contains the libraries and header files needed
for the development of mouse driven programs for the console.

%description -n lib%name-devel-static
This package contains the static library needed for the development
of statically linked mouse driven programs for the console.

%description root
The gpm-root program allows pop-up menus to appear on a text console
at the click of a mouse button.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p2

find -type f -name \*.orig -delete

%build
find -type f -name \*.y |while read f; do
	rm -fv "${f%%.y}.c"
done

export ac_cv_path_emacs=no
%autoreconf
%configure
# SMP-incompatible build.
%make

%install
mkdir -p %buildroot/dev

%makeinstall
mv %buildroot%_bindir/gpm-root %buildroot%_sbindir/
chmod 644 %buildroot%_libdir/*.so*

install -p -m644 doc/gpm-root.1 %buildroot%_man1dir/
install -p -m644 conf/gpm-root.conf %buildroot%_sysconfdir/

install -pD -m755 %_sourcedir/gpm.init %buildroot%_initdir/gpm
install -pD -m644 %_sourcedir/gpm.service %buildroot%_unitdir/gpm.service

mksock %buildroot/dev/gpmctl

bzip2 -9 Changelog ||:

%post
%post_service gpm

%preun
%preun_service gpm

%triggerpostun -- gpm < 0:1.20.1-alt2
/sbin/chkconfig --add gpm ||:

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files
%_initdir/gpm
%_unitdir/gpm.service
%ghost %attr(600,root,root) %verify(not user) /dev/gpmctl
%_bindir/*
%_sbindir/gpm
%_man1dir/mev.1*
%_man1dir/mouse-test.1*
%_man7dir/*
%_man8dir/*
%_infodir/*.info*
%doc Change* doc/FAQ README TODO BUGS doc/README.* doc/Announce

%files root
%config(noreplace) %_sysconfdir/gpm-root.conf
%_sbindir/gpm-root
%_man1dir/gpm-root.1*

%changelog
* Mon Jan 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.20.1-alt18
- Fixed build.

* Thu Apr 27 2017 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt17
- Replaced the patch introduced in 1.20.1-alt15 with upstream patches.
- Fixed a bug uncovered by gcc -Wmisleading-indentation.

* Sat Feb 06 2016 Michael Shigorin <mike@altlinux.org> 1.20.1-alt16
- Fixed FTBFS (BR: makeinfo).

* Tue Jan 19 2016 Michael Shigorin <mike@altlinux.org> 1.20.1-alt15
- E2K: added clang support patch by Alexander Kolesen:
  http://lists.linux.it/pipermail/gpm/2011-April/001122.html

* Tue Sep 09 2014 Alexey Shabalin <shaba@altlinux.ru> 1.20.1-alt14
- NMU: add systemd support

* Thu Jul 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt13
- libgpm-devel-static: added requirement on libtinfo-devel-static,
  reported by Andrew Borodin.

* Thu Feb 10 2011 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt12
- Rebuilt for debuginfo.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt11
- Rebuilt for soname set-versions.

* Mon Nov 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt10
- Removed obsolete %%install_info/%%uninstall_info calls.
- Removed obsolete explicit package requirements.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt9
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- gpm.init: Introduced $GPM_OPTIONS (closes: #1147).

* Sat Mar 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt8
- Dropped obsolete version of /usr/share/emacs/site-lisp/t-mouse.el*
  (#11042).
- Updated build dependencies.

* Fri Feb 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt7
- Fixed build on x86_64 platform.

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt6
- Fixed build on x86_64 platform (closes #4883).

* Wed Mar 24 2004 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt5
- Shutup Gpm_Open() when no gpm server available (#3867).

* Thu Feb 26 2004 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt4
- Fixed build with fresh autotools.

* Fri Jan 30 2004 Stanislav Ievlev <inger@altlinux.org> 1.20.1-alt3.1
- fix segfault with ncurses 5.4 (old_term == cur_term)
- added Debian patch to fix segfault while freeing gpm_stack

* Tue Aug 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt3
- libgpm: enhanced patch which makes wgetch and stdscr
  weak undefined symbols (from Jakub Jelinek).
- gpm: updated package and interpackage dependencies.

* Wed May 21 2003 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt2
- %_initdir/gpm: changed chkconfig levels to "2345 37 63".

* Sat Apr 26 2003 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt1
- Updated 1.20.1, rediffed patches.
- Daemonize properly (#0002549).
- Rewritten start/stop script to new rc scheme.

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt0.6rc1
- Fixed libgpm in linux console (#0001116).

* Sat Oct 26 2002 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt0.5rc1
- Regenerate configure & co., to fix xterm problem (#0001086).

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.20.1-alt0.4rc1
- Rebuilt in new environment.

* Thu Jul 18 2002 Dmitry V. Levin <ldv@altlinux.org> 1.20.1-alt0.3rc1
- Added /dev/gpmctl to files list.
- Added call to /sbin/pam_console_apply at the gpm startup (#0001116).
- Better detection of if this is an xterm-like terminal with mouse
  support, based on patch by Oskar Liljeblad (#0001086).
  Unfortunately, libgpm still looks like dirty hack.
- Disabled debugging in libgpm for a while.

* Wed Jul 17 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.20.1-alt0.2rc1
- Restored fields order in struct Gpm_Event to avoid ABI change.

* Tue Jul 09 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.20.1-alt0.1rc1
- 1.20.1rc1
- Fixed some patches and removed applied in source
- Fixed init script
- Rewrited syslog patch
- Fixed Genius Netmouse buttons detect code

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 1.19.6-alt3
- Relocated shared libraries back to %_libdir/:
  reverted first relocation made in 1.19.2-ipl2mdk (no need).
- Patched to avoid linking with termcap and curses libraries.

* Fri Jan 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.19.6-alt2
- Explicitly disabled SMP build.

* Mon Dec 10 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.19.6-alt1
- 1.19.6
- Imported some patches from Owl
- Added more documentation
- Added syslog patch
- Added gpm-root package

* Thu Oct 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.19.4-alt2
- Add -lpp patch

* Mon Sep 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.19.4-alt1
- 1.19.4
- Fixed descriptions.
- Fixed interpackage requires.
- Updated buildrequires.

* Fri May 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.19.3-ipl5mdk
- Rebuild to use new macros post_service and preun_service

* Mon May 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.19.3-ipl4mdk
- Closing sockets cleanup (closeall patch in Owl style).
- Moved static library to devel-static subpackage.

* Sat Jan 13 2001 Dmitry V. Levin <ldv@fandra.org> 1.19.3-ipl3mdk
- Renamed subpackages.
- Create tmpfiles in more secure way.
- Fix some compilation warnings.

* Wed Nov 22 2000 Dmitry V. Levin <ldv@fandra.org> 1.19.3-ipl2mdk
- Fixed makefile (ldconfig patch).
- Fixed texinfo documentation.

* Tue Oct 17 2000 Dmitry V. Levin <ldv@fandra.org> 1.19.3-ipl1mdk
- 1.19.3

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 1.19.2-ipl3mdk
- Merged RH & MDK security patches.
- Use FHS-compatible macros.

* Tue Jun 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.19.2-ipl2mdk
- Moved shared libraries into /lib, and split out lib subpackage.

* Tue Apr 25 2000 Dmitry V. Levin <ldv@fandra.org> 1.19.2-ipl1mdk
- 1.19.2

* Thu Apr 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.19.1-2mdk
- Correct groups.

* Thu Apr 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.19.1-1mdk
- Add security patch for gpm-root by redhat.
- gpm.init cleanup.
- 1.19.1
- Update groups.

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- And a relifting for spec.

* Wed Sep 15 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.18.0 final : WizardPad procotol and older Synaptics PS/2 touchpads
                 are now supported, gpm allows the touchpad
                 to be ignored if unplugged, and some other changes.

* Thu Aug 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix typo in gpm.init (#59).
- Fix building as user.

* Sun Aug  9 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 1.17.9

* Wed Jul 07 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- fix really stupid type-o (whats sleep?)

* Wed Jul 07 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- inc %release just to be safe

* Tue Jul  6 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- test for /sbin/install-info just incase it's not there

* Sat Jul  3 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- moved gpm-root.conf from /etc to /usr/etc so it actualy works

* Mon Apr 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add patch for the texinfo (new syntax ?).

* Sun Apr 11 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 1.17.7
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Thu Mar  4 1999 Matt Wilson <msw@redhat.com>
- updated to 1.17.5

* Tue Feb 16 1999 Cristian Gafton <gafton@redhat.com>
- avoid using makedev for internal functions (it is a #define in the system
  headers)

* Wed Jan 13 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 1.17.2.

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- enforce the use of -D_GNU_SOURCE so that it will compile on the ARM
- build against glibc 2.1

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscript

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- recompiled for manhattan

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 1.13

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added patch from Richard to get things to build on the SPARC

* Tue Oct 28 1997 Donnie Barnes <djb@redhat.com>
- fixed the emacs patch to install the emacs files in the right
  place (hopefully).

* Mon Oct 13 1997 Erik Troan <ewt@redhat.com>
- added chkconfig support
- added install-info

* Thu Sep 11 1997 Donald Barnes <djb@redhat.com>
- upgraded from 1.10 to 1.12
- added status/restart functionality to init script
- added define LIBVER 1.11

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
