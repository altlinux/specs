# Conditional build:
# _with_cheaters

Name: Maelstrom
Version: 3.0.6
Release: alt3.1

Summary: Rockin' asteroids game
License: GPL for code, artwork and sounds can be redistributed only with Maelstrom
Group: Games/Arcade

Packager: Ilya Mashkin <oddity@altlinux.ru>

Url: http://www.devolution.com/~slouken/projects/Maelstrom/
# Source0-md5:	8aab0e75ca52808fd6777535ebb1f1c4
Source0: http://www.devolution.com/~slouken/projects/Maelstrom/src/%name-%version.tar.gz
Source1: %name.desktop
Source2: %name.menu
Patch0: %name-cheaters.patch
Patch1: %name-dirs.patch
Patch2: %name-amfix.patch
Patch3: %name-sec.patch
Patch10: %name-3.0.5-setgid.patch
Patch11: maelstrom-gcc34.patch
Patch12: Maelstrom-3.0.6-64bit.patch

# Automatically added by buildreq on Wed Oct 19 2005
BuildRequires: esound gcc-c++ libSDL-devel libSDL_net-devel libstdc++-devel

BuildRequires: libSDL_net-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libstdc++-devel

%define gamedir %_datadir/Maelstrom
%define scoredir %_localstatedir/%_gamesdir
%define _desktopdir %_datadir/applications

%define specflags_ia32	 -fomit-frame-pointer

Summary(pl):	Gra, w ktÛrej strzelasz do asteroidÛw
Summary(pt_BR):	Maelstrom - um jogo tipo Asteroids muito bem-feito
Summary(ru_RU.KOI8-R): Û‘¡“Ÿ≈ ƒœ¬“Ÿ≈ ·”‘≈“œ…ƒŸ ;-)
Summary(uk_UA.KOI8-U): Û‘¡“œ◊…ŒŒ¡ «“¡ ·”‘≈“œßƒ… ;-)

%description
Maelstrom is a rockin' asteroids game ported from the Macintosh
Originally written by Andrew Welch of Ambrosia Software, and ported
to UNIX and then SDL by Sam Lantinga <slouken@devolution.com>.

%description -l pl
Maelstrom jest kosmiczn± strzelank± sportowan± na UNIXy i SDL przez
Sama Lantinga <slouken@devolution.com>, oryginalnie napisan± na
Macintosha przez Andrew Welcha z Ambrosia Software.

%description -l pt_BR
O Maelstrom È um jogo de asterÛides vagantes portado do Macintosh,
originalmente escrito por Andrew Welch da Ambrosia Software, e portado
para o UNIX e SDL por Sam Lantinga.

Sua nave est· no temido cÌrculo de asterÛides "Maelstrom", e vocÍ tem
que sobreviver explodindo todos os asterÛides e evitando outros
inimigos como estrelas Nova, turbilhıes e naves e minas Shenobi.

Gr·ficos 3D muito legais e sons, com suporte a temas e jogos via rede.

%description -l ru_RU.KOI8-R
Maelstrom -- …«“¡ ◊”≈» ◊“≈Õ≈Œ … Œ¡“œƒœ◊ "·”‘≈“œ…ƒŸ", ”–œ“‘…“œ◊¡ŒŒ¡— ” Ì¡Àœ◊.

%description -l uk_UA.KOI8-U
Maelstrom -- «“¡ ’”¶» ﬁ¡”¶◊ ‘¡ Œ¡“œƒ¶◊ "·”‘≈“œßƒ…", —À’ –œ“‘œ◊¡Œœ ⁄ Ì¡À¶◊.

%prep
%setup	-q
# everlasting shield, more shots available, all-in-one equipment and
# reversed bonus in time function ;)
%{?_with_cheaters:%patch0 -p1}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch10 -p1 -b .setgid
%patch11 -p1 -b .gcc34
%patch12 -p1 -b .64bit

%build
rm -f missing
touch NEWS AUTHORS ChangeLog Makefile.in
%__aclocal
%__autoconf
%__automake -a -f
%configure
%__make

%install
%__make install DESTDIR=%buildroot

#mv %buildroot%prefix/bin %buildroot%prefix/X11R6
rm -f %buildroot%gamedir/Images/Makefile*
rm -f Docs/Makefile*

# /usr is read-only
%__install -d %buildroot%scoredir
%__mv -f %buildroot%gamedir/Maelstrom-Scores %buildroot%scoredir/
%__ln_s -f %scoredir/Maelstrom-Scores %buildroot%gamedir/

# not needed (examples for internal Mac library)
# and playwave conflicts with SDL_mixer
rm -f %buildroot%_bindir/{macres,playwave,snd2wav}

%__install -pD %SOURCE1 %buildroot%_desktopdir/%name.desktop
#__install -pD %SOURCE2 %buildroot%_menudir/%name


%files
%doc README* Changelog CREDITS Docs
#_bindir/Maelstrom
%_bindir/*
%gamedir
%config(noreplace) %verify(not md5 size mtime) %scoredir/Maelstrom-Scores
%_desktopdir/*
#_menudir/*

%changelog
* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 3.0.6-alt3.1
- fix desktop file

* Fri Apr 03 2009 Ilya Mashkin <oddity@altlinux.ru> 3.0.6-alt3
- remove menu file (#18845) .desktop file is present
- install files with default permissions
- remove deprecated macros

* Sat Nov 01 2008 Ilya Mashkin <oddity@altlinux.ru> 3.0.6-alt2
- fix 64-bit build

* Sat Oct 18 2008 Ilya Mashkin <oddity@altlinux.ru> 3.0.6-alt1.1
- resurrect from orphaned

* Wed Oct 19 2005 Michael Shigorin <mike@altlinux.org> 3.0.6-alt1
- 3.0.6
- re-merged with PLD 3.0.6-5 (spec revision 1.19);
  these folks @pld-linux.org improved it:
  juandon, qboosh, gotar, misi3k, malekith, radek, undefine,
  arekm, havner, tiwek
- added RH setgid patch
- make setgid games binary
- gcc34 patch from Gentoo
- spec cleanup
- define %%_desktopdir by hand...
- added menu file

* Mon Apr 28 2003 Michael Shigorin <mike@altlinux.ru> 3.0.5-alt1
- built for ALT Linux
- spec adapted from PLD <feedback@pld.org.pl>
  All persons listed below can be reached at <cvs_login>@pld.org.pl
  kloczek, qboosh, gotar
- scorefile perms changed from world-writable to games-group-writable
  (should I also make binary setgid games?)


$Log: Maelstrom.spec,v $
Revision 1.19  2005/04/25 18:57:34  tiwek
- update patch

Revision 1.18  2004/07/04 00:23:00  havner
- wrrr

Revision 1.17  2004/06/20 21:36:19  arekm
- fix specflags (quotation here is buggy)

Revision 1.16  2004/03/16 16:08:11  undefine
- pt_BR translations from conectiva

Revision 1.15  2003/12/03 13:38:40  gotar
- _applnkdir -> _desktopdir

Revision 1.14  2003/06/28 19:36:24  gotar
- -fomit-frame-pointer on ia32

Revision 1.13  2003/06/22 20:37:04  gotar
- added some useful comment

Revision 1.12  2003/06/19 19:54:00  radek
- release 3: fixed .desktop

Revision 1.11  2003/06/04 18:01:29  radek
- fixed URLs, added md5 checksum

Revision 1.10  2003/05/26 16:24:19  malekith
- massive attack: adding Source-md5

Revision 1.9  2003/05/25 05:45:21  misi3k
- massive attack s/pld.org.pl/pld-linux.org/

Revision 1.8  2003/05/21 16:29:48  misi3k
- rel 2
- added sec patch (Maelstrom Local Buffer Overflow)

Revision 1.7  2003/02/08 00:02:58  gotar
- upgraded to 3.0.6 (fixes)

Revision 1.6  2003/01/19 18:45:14  qboosh
- typo in Group

Revision 1.5  2003/01/18 22:53:34  juandon
- removed two lines with define

Revision 1.4  2002/10/20 07:56:03  gotar
- changed URLs to local

Revision 1.3  2002/09/10 20:02:46  kloczek
- cleanups.

Revision 1.2  2002/06/27 21:53:14  qboosh
- fixed FHS compl.: added dirs patch, moved data to %%{_datadir}/Maelstrom,
  scores to /var/games
- amfix patch to allow rebuild ac/am
- resolved conflict with SDL_mixer
- release 2

Revision 1.1  2002/06/19 23:07:40  gotar
- initial release, STBR.
