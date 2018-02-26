Name: joe
Version: 3.7
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: An easy to use modeless text editor
License: GPL
Group: Editors

URL: http://joe-editor.sourceforge.net/
Source: http://downloads.sf.net/joe-editor/joe-%version.tar.gz
Source1: joe_icons.tar.bz2
Source2: joe.desktop
Source3: joe.png

Patch1: joe-3.0-yuk-c-color.patch
Patch2: joe-3.5-cp1251.patch
Patch10: joe-3.7-joerc.patch
Patch11: joe-3.5-time.patch

# Automatically added by buildreq on Tue Nov 11 2008
BuildRequires: aspell libncurses-devel

%description
Joe is an easy to use, modeless text editor which would be very appropriate for
novices. Joe uses by default the same WordStar keybindings used in Borland's
development environment.

You should install joe if you've used it before and you liked it, or if you're
still deciding what text editor you'd like to use, or if you have a fondness for
WordStar. If you're just starting out, you should probably install joe because
it is very easy to use.

%prep
%setup -a1

%patch1 -p1
%patch2 -p1
%patch10 -p1
%patch11 -p1

%__subst 's/ -asis/-asis/' rc/j*rc.in
%__subst 's/ -guess_utf8/-guess_utf8/' rc/j*rc.in

%build
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

# This is automatically compressed afterwards...
pushd %buildroot%_man1dir
	ln -s joe.1 jmacs.1
	ln -s joe.1 jpico.1
	ln -s joe.1 jstar.1
	ln -s joe.1 rjoe.1
popd

install -pD -m644 joe_16.xpm %buildroot%_miconsdir/joe.xpm
install -pD -m644 joe_32.xpm %buildroot%_niconsdir/joe.xpm
install -pD -m644 joe_48.xpm %buildroot%_liconsdir/joe.xpm

install -pD -m644 %{SOURCE2} %buildroot%_desktopdir/joe.desktop
install -pD -m644 %{SOURCE3} %buildroot%_pixmapsdir/joe.png

# Thanks, but we will choose docs in files section
rm -rf %buildroot%_defaultdocdir

%files
%_bindir/*
%dir %_sysconfdir/joe
%config(noreplace) %_sysconfdir/joe/*
%_datadir/joe
%_man1dir/*
%lang(ru) %_mandir/ru/man?/*
%_desktopdir/*
%_pixmapsdir/*
%_niconsdir/joe.xpm
%_miconsdir/joe.xpm
%_liconsdir/joe.xpm
%doc HINTS LIST NEWS README

%changelog
* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 3.7-alt2
- Remove obsolete install time scripts.

* Tue Nov 11 2008 Victor Forsyuk <force@altlinux.org> 3.7-alt1
- 3.7
- Fix unnecessary wakeups (patch from Arjan van de Ven, RH#227487).

* Thu Feb 14 2008 Victor Forsyuk <force@altlinux.org> 3.5-alt2
- Aplied patch for correct localization in CP1251 codeset environment
  (thnx to led@ for idea).

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 3.5-alt1.0
- Automated rebuild.

* Thu Aug 03 2006 Victor Forsyuk <force@altlinux.ru> 3.5-alt1
- 3.5
- Patched temp files creation for spell check.

* Wed May 31 2006 Victor Forsyuk <force@altlinux.ru> 3.4-alt1
- 3.4

* Mon Jun 06 2005 Victor Forsyuk <force@altlinux.ru> 3.3-alt1
- 3.3.
- Config files made replacable with package updates.

* Tue Mar 22 2005 Victor Forsyuk <force@altlinux.ru> 3.2-alt1
- 3.2.

* Wed May 12 2004 Victor Forsyuk <force@altlinux.ru> 3.0-alt2
- Added patches from "Yura Kalinichenko <yuk at iceb.vinnitsa.com>".
- Gnome term patch from RH (via mdk spec :).

* Tue Apr 27 2004 Victor Forsyuk <force@altlinux.ru> 3.0-alt1
- New version.

* Fri Jan 24 2003 Dmitry V. Levin <ldv@altlinux.org> 2.9.8-alt0.2pre1
- Rebuilt in new environment.

* Fri May 31 2002 Victor Forsyuk <force@altlinux.ru> 2.9.8-alt0.1pre1
- 2.9.8pre1
- Added license file to docs.
- Added patch enabling -asis by default.

* Mon Oct 15 2001 Stanislav Ievlev <inger@altlinux.ru> 2.9.6-alt1
- 2.9.6

* Sat Mar 10 2001 Dmitry V. Levin <ldv@fandra.org> 2.8-ipl23mdk
- Security fix: don't use .joerc, only ~/.joerc and /etc/joe/joerc.

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 2.8-ipl22mdk
- RE adaptions.

* Wed Nov 22 2000 Vincent Danen <vdanen@mandrakesoft.com> 2.8-22mdk
- security fix: don't blindly write to DEADJOE, unlink and create it safely first.

* Mon Sep 25 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 2.8-21mdk
- sync with latest RedHat patches (procrc)
- removed patch7 (included into joe-resize2.patch) and patch10
  (same things into joe-vfile.patch).

* Mon Sep 25 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 2.8-20mdk
- fixed a typo in menu.
- included macro and BM fixes to SPEC file from Stefan van der
  Eijk <s.vandereijk@chello.nl>.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.8-19mdk
- automatically added BuildRequires

* Fri Apr 28 2000 Vincent Saugey <vince@mandrakesoft.com> 2.8-18mdk
- add three size of icons

* Thu Apr 13 2000 Vincent Saugey <vince@mandrakesoft.com> 2.8-17mdk
- Add menu entry
- Corrected group
- Remove strip and bzip2 in spec file

* Fri Feb 04 2000 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- merged with Bero's patch from Has de Goede <hans@highrise.nl> to fix the
  End Key.

* Fri Jan 28 2000 Francis Galiegue <francis@mandrakesoft.com> 2.8-15mdk
- Added missing %%defattr() in %%files section.

* Sat Dec 18 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- merged with latest Chris Gafton <gafton@redhat.com> patches
  (joe-2.8-security and joe-2.8-deadjoe).
- finally fixed a bug causing segfault on big files with short
  name (joe-2.8-vsmk).

* Thu Dec 02 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- Build release for Oxygen
- fix sucks on locale patch where -p1 delete the _filename_ ...

* Wed Aug 26 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- fixed a bug causing segfault on long filenames.

* Fri Jun 04 1999 Giuseppe Ghibò <ghibo@caesar.polito.it>
- added patch to get joe working on terminals supporting
  ti/te entries.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- added locale patch from  Petr Kolar <PETR.KOLAR@vslib.cz>
  (yeah, finally!)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 17)

* Wed Jan 20 1999 Alex deVries <puffin@redhat.com>
- added mipseb support

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Sep 15 1998 Cristian Gafton <gafton@redhat.com>
- built with Alan's -port patch

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- enable -asis in the config files so international keyboards will be better
  supported

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- /usr/lib/joe/* are config files

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- manhattan build

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- fixed termcap problems for terms other than 80x25
- added support for buildroot and BuildRoot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
