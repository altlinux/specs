%define _fontsdir %_datadir/fonts/type1

Name: fonts-type1-urw
Version: 1.0.7pre44
Release: alt1
Serial: 2

Summary: Free versions of the 35 standard PostScript fonts
License: GPLv2
Group: System/Fonts/Type1
Url: ftp://ftp.gnome.ru/fonts/urw/release/

Source0: ftp://ftp.gnome.ru/fonts/urw/release/urw-fonts-%version.tar.bz2

Provides: urw-fonts = %serial:2.0
Obsoletes: urw-fonts < %serial:2.0

PreReq: fontconfig >= 2.4.2

BuildArch: noarch
BuildRequires: mkfontscale

%description
Free, good quality versions of the 35 standard PostScript(TM) fonts,
donated under the GPL by URW++ Design and Development GmbH.  The
fonts.dir file font names match the original Adobe names of the fonts
(e.g., Times, Helvetica, etc.).

This package also have cyrillic glyphs in basic fonts, added by
Valentin Filippov.

Install the %name package if you need free versions of standard
PostScript fonts.

%prep
%setup -q -c -n fonts

%install
mkdir -p %buildroot%_fontsdir/urw
find -name \*.\?f\? -print -exec cp -t %buildroot%_fontsdir/urw/ {} \;
mkfontscale %buildroot%_fontsdir/urw
ln -s fonts.scale %buildroot%_fontsdir/urw/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir/urw %buildroot%_sysconfdir/X11/fontpath.d/type1-urw:pri=40

%triggerun -- %name <= 2:1.0.7pre42-alt1
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r %_fontsdir/urw ||:
fi

%post
%_bindir/fc-cache %_fontsdir/urw ||:

%files
%doc ChangeLog README*
%_sysconfdir/X11/fontpath.d/*
%_fontsdir/urw

%changelog
* Thu Jan 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.7pre44-alt1
- 1.0.7pre44

* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.7pre43-alt1
- 1.0.7pre43

* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.7pre42-alt3
- fixed trigger logic

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.7pre42-alt2
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jun 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.7pre42-alt1
- 1.0.7pre42

* Mon Mar 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.7pre41-alt3
- added PreReq fontconfig (#9276)

* Tue Mar 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.7pre41-alt2
- fixed provides

* Mon Feb 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.7pre41-alt1
- determination version to 1.0.7pre41
- rebuild under the action of fonts policy

* Mon Feb 27 2006 Alexey Gladkov <legion@altlinux.ru> 1:2.1-alt1
- new version 1.0.7pre41
- package was renamed: urw-fonts -> urw-fonts-type1
- BuildRequires updated.
- spec cleanup

* Thu Sep 02 2004 AEN <aen@altlinux.ru> 1:2.0-alt26
- new fonts from frob (pre37)

* Wed Mar 10 2004 Stanislav Ievlev <inger@altlinux.org> 1:2.0-alt25
- fix building in hasher

* Fri Jul 11 2003 AEN <aen@altlinux.ru> 1:2.0-alt24
- pre22 with RH fixes

* Fri Nov 29 2002 AEN <aen@altlinux.ru> 1:2.0-alt23
- pre16.5

* Tue Oct 15 2002 AEN <aen@altlinux.ru> 1:2.0-alt22
- pre16

* Mon Oct 14 2002 AEN <aen@altlinux.ru> 1:2.0-alt21
- pre15

* Fri Oct 11 2002 AEN <aen@altlinux.ru> 1:2.0-alt20
- added some modified Valek's fonts from RH8

* Fri Oct 04 2002 AEN <aen@altlinux.ru> 1:2.0-alt19
- pre14
- PreReq fontconfig, fc-cache added to %post
- gnome-print scripts added to %post

* Mon May 20 2002 AEN <aen@logic.ru> 1:2.0-alt18
- pre11

* Wed May 15 2002 AEN <aen@logic.ru> 1:2.0-alt17
- back to pre4

* Tue May 14 2002 AEN <aen@logic.ru> 1:2.0-alt16
- pre10

* Wed Apr 10 2002 AEN <aen@logic.ru> 1:2.0-alt15
- #818 fixed

* Mon Mar 04 2002 AEN <aen@logic.ru> 1:2.0-alt14
- pre7 from Val
- *.pfm removed

* Wed Feb 06 2002 AEN <aen@logic.ru> 1:2.0-alt13
- pre7 from Val

* Fri Jan 18 2002 AEN <aen@logic.ru> 1:2.0-alt12
- pre4 from Val

* Tue Jan 15 2002 AEN <aen@logic.ru> 1:2.0-alt11
- fixes from val

* Fri Jan 04 2002 AEN <aen@logic.ru> 1: 2.0-alt10
- 1.0.7pre2 from Valek

* Tue Sep 11 2001 AEN <aen@logic.ru> 1:2.0-alt9
- fonts.scale fixed
* Fri Sep 7 2001 AEN <aen@logic.ru> 1:2.0-alt8
- new README from Valek

* Thu Sep 6 2001 AEN <aen@logic.ru> 1:2.0-alt7
- New snapshot.

* Tue Sep 4 2001 AEN <aen@logic.ru> 1:2.0-alt6
- New snapshot.

* Fri Aug 31 2001 AEN <aen@logic.ru> 1:2.0-alt5
- fixed Nimbus fonts from Val

* Thu Aug 30 2001 AEN <aen@logic.ru> 1:2.0-alt4
- Times-hebrew temporary removed
* Wed Jul 25 2001 AEN <aen@logic.ru> 1:2.0-alt3
- Version 1.0 of Val fonts
- hebrew glyphs added

* Fri Jul 20 2001 AEN <aen@logic.ru> 1:2.0-alt2
- beta2
* Tue Jul 17 2001 AEN <aen@logic.ru> 1:2.0-alt1
- new fonts with cyrillic glyphs from Valentin Filippov!
- Serial 1

* Sun Jan  28 2001 AEN <aen@logic.ru>
- font.map for enscript added
* Tue Jan 16 2001 AEN <aen@logic.ru>
- new fonts from Leon Kanter
- SO compatible font name added in fonts.scale

* Tue Nov 28 2000 AEN <aen@logic.ru>
- adopted to RE
- MICROSOFT changed to bcl :-)
- replaced fonts.scale, new encodings added

* Fri Apr 21 2000 Leon Kanter <leon@blackcatlinux.com>
- Added cyrillic glyphs to basic fonts

* Wed Mar 08 2000 Preston Brown <pbrown@redhat.com>
- argh! fonts.scale shouldn't have been symlinked to fonts.dir.  fixed.

* Mon Feb 28 2000 Preston Brown <pbrown@redhat.com>
- noreplace the fonts.dir config file

* Wed Feb 16 2000 Bill Nottingham <notting@redhat.com>
- need .pfb files too

* Mon Feb 14 2000 Preston Brown <pbrown@redhat.com>
- new URW++ fonts that include extra glyphs.

* Thu Jan 13 2000 Preston Brown <pbrown@redhat.com>
- remove vendor tag.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 8)

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- fixed up chkfontpath stuff

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb 15 1999 Preston Brown <pbrown@redhat.com>
- added missing fonts.dir, fonts.scale, %post, %postun using chkfontpath
- changed foundary from Adobe (which was a lie) to URW.

* Sat Feb 06 1999 Preston Brown <pbrown@redhat.com>
- fonts now live in %_datadir/fonts/default/Type1

* Fri Nov 13 1998 Preston Brown <pbrown@redhat.com>
- eliminated section that adds to XF86Config
- changed fonts to reside in /usr/share/fonts/default/URW, so they can be
  shared between X and Ghostscript (and other, future programs/applications)

* Fri Sep 11 1998 Preston Brown <pbrown@redhat.com>
- integrate adding fontdir to XF86Config

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- eliminate %post output

* Wed Jul  8 1998 Jeff Johnson <jbj@redhat.com>
- create from Stefan Waldherr <swa@cs.cmu.edu> contrib package.
