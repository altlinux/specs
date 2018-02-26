Name: pdksh
Version: 5.2.14
Release: alt2
Epoch: 1

Summary: A public domain clone of the Korn shell (ksh)
License: Public Domain
Group: Shells

Url: http://www.cs.mun.ca/~michael/pdksh/
Source: http://www.cs.mun.ca/~michael/pdksh/files/%name-%version.tar.bz2
Patch0: pdksh-5.2.14-patches1.patch
Patch1: pdksh-5.2.14-alignia64.patch
Patch2: pdksh-5.2.14-patches2.patch
Patch3: pdksh-5.2.14-coreutils-posix-fix.patch
Packager: Michael Shigorin <mike@altlinux.org>

Provides: /bin/ksh

%description
The %name package contains PD-ksh, a clone of the Korn shell (ksh).
The ksh shell is a command interpreter intended for both interactive
and shell script use.  Ksh's command language is a superset of the
sh shell language.

Install the %name package if you want to use a version of the ksh
shell.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%make_build

%install
mkdir -p %buildroot%_bindir
install -pD -m755 ksh %buildroot/bin/ksh
install -pD -m644 ksh.1 %buildroot%_man1dir/ksh.1
ln -s ksh.1 %buildroot%_man1dir/%name.1
ln -s ../../bin/ksh %buildroot%_bindir/
ln -s ksh %buildroot%_bindir/%name

%files
/bin/*
%_bindir/*
%_man1dir/*
%doc BUG-REPORTS ChangeLog* CONTRIBUTORS LEGAL NEWS NOTES PROJECTS README

%changelog
* Fri Mar 21 2008 Michael Shigorin <mike@altlinux.org> 1:5.2.14-alt2
- fixed build with current coreutils
  + patch from Gentoo, see http://bugs.gentoo.org/31835

* Wed Feb 20 2008 Michael Shigorin <mike@altlinux.org> 1:5.2.14-alt1
- alt1 (5.2.14 is the current upstream version)
- added Url:, Packager:
- spec macro abuse cleanup

* Mon Sep 09 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.14-ipl12mdk
- Turned all absolute symlinks unto relative.
- Removed %%post/%%postun scripts.

* Fri Sep 06 2002 Michael Shigorin <mike@altlinux.ru> 5.2.14-ipl11mdk
- added Provides: /bin/ksh to improve compatibility
- spec cleanup (removed perl req)

* Tue Apr 02 2002 Stanislav Ievlev <inger@altlinux.ru> 5.2.14-ipl10mdk
- Rebuilt
- Added patches from RH (from author)

* Mon Dec 11 2000 Dmitry V. Levin <ldv@fandra.org> 5.2.14-ipl9mdk
- RE adaptions.

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 5.2.14-9mdk
- fix the %%post scripts

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 5.2.14-8mdk
- macroization
- BM

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 5.2.14-7mdk
- new group + lceanup

* Tue Nov 02 1999 John Buswell <johnb@mandrakesoft.com>
- Rebuild and Repackage for oxygen (release 6)

* Tue Sep 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix wrong manpages (#216) (#135).

* Fri Jul 16 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 5.2.14.
- Removing unused patch.

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Wed Mar 17 1999 Jeff Johnson <jbj@redhat.com>
- glibc 2.1 doesn't init sys_siglist for 32 <= i < NSIG (#1473)

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- upgrade to 5.2.13.

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the spec file

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
