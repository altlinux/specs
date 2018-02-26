Name: xjewel
Version: 1.6
Release: alt6
Epoch: 1

Summary: An X Window System game of falling jewel blocks
License: MIT
Group: Games/Arcade

Url: http://www.opennet.ru/openforum/vsluhforumID3/40415.html
Source0: ftp://ftp.x.org/R5contrib/xjewel-1.6.tar.z
Source1: xjewel.desktop
Source2: %{name}16.xpm
Source3: %{name}32.xpm
Source4: %{name}48.xpm
Patch0: xjewel-1.6-imake.patch.bz2
Patch1: xjewel-1.6-enhance.patch.bz2
Patch2: xjewel-1.6-nobr.patch.bz2
Patch3: xjewel-1.6-arch-help.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Dec 13 2009
BuildRequires: imake libX11-devel libXext-devel xorg-cf-files

%description
Xjewel is an X Window System game much like Domain/Jewelbox
or Sega's Columns.

The point of the game is to move or rotate the blocks as they fall,
to get jewels in patterns of three when they come to rest.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
xmkmf
make "RPM_OPT_FLAGS=%optflags"

%install
mkdir -p %buildroot%_localstatedir/games
%makeinstall_std install.man
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pDm644 %SOURCE2 %buildroot%_miconsdir/%name.xpm
install -pDm644 %SOURCE3 %buildroot%_niconsdir/%name.xpm
install -pDm644 %SOURCE4 %buildroot%_liconsdir/%name.xpm

%files
%_bindir/*
%config %_localstatedir/games/xjewel.scores
%_man1dir/*
%_desktopdir/*
%_niconsdir/*
%_miconsdir/*
%_liconsdir/*

%changelog
* Wed Feb 22 2012 Michael Shigorin <mike@altlinux.org> 1:1.6-alt6
- added Arch patch by Anton Bazhenov to fix font/kbd issues
  (closes: #26920)

* Tue Dec 15 2009 Michael Shigorin <mike@altlinux.org> 1:1.6-alt5
- argh, dropped overlooked obsolete manual BR

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1:1.6-alt4
- buildreq (thx repocop)

* Mon Jul 27 2009 Michael Shigorin <mike@altlinux.org> 1:1.6-alt3
- applied repocop patch
- replaced debian menufile with freedesktop one
- spec cleanup

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1:1.6-alt2
- applied repocop patch

* Tue Apr 01 2008 Michael Shigorin <mike@altlinux.org> 1:1.6-alt1
- picked up an orphan
- use original source tarball
- removed reference to tetris from description so as to say
  that Alexey Pazhitnov's got white back!
- added an Url:
- buildreq

* Tue Oct 15 2002 Stanislav Ievlev <inger@altlinux.ru> 1.6-ipl12mdk
- fixed paths

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1.6-ipl11mdk
- rebuild

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Fri Sep 15 2000 David BAUDENS <baudens@mandrakesoft.com> 1.6-9mdk
- Macros
- %%{_update_menus} & %%{_clean_menus}
- Fix Title in Menu entry

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.6-8mdk
- automatically added BuildRequires

* Wed May 03 2000 dam's <damien@mandrakesoft.com> 1.6-7mdk
- Corrected icons

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 1.6-6mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 1.6-5mdk
- Added menu entry

* Mon Mar 27 2000 dam's <damien@mandrakesoft.com> 1.6-4mdk
- Release.

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- rebuild for new environment

* Thu May  6 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 11)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
