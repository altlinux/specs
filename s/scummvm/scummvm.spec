Name: scummvm
Version: 1.4.1
Release: alt1

Summary: Graphic adventure game interpreter
Group: Games/Adventure
License: GPL
Url: http://www.scummvm.org

Source: %name-%version.tar.bz2
Patch: scummvm-1.3.0-mp2player.patch

Provides: %_gamesdatadir/%name

# Automatically added by buildreq on Thu Nov 10 2011 (-bi)
# optimized out: elfutils libGL-devel libGLU-devel libalsa-devel libogg-devel libstdc++-devel pkg-config zlib-devel
BuildRequires: gcc-c++ libSDL-devel libfaad-devel libflac-devel libfluidsynth-devel libmad-devel libpng-devel libreadline-devel libtheora-devel libvorbis-devel

%description
ScummVM is a collection of interpreters, capable of emulating several
adventure game engines. ScummVM mainly supports games created using
SCUMM (Script Creation Utility for Maniac Mansion), used in various
LucasArts games such as Monkey Island, Day of the Tentacle, and others.

ScummVM also contains interpreters for several non-SCUMM games. Currently
these are Beneath a Steel Sky, Broken Sword 1 & 2, Flight of the Amazon
Queen, Simon the Sorcerer 1 & 2, The Legend of Kyrandia and The Feeble
Files.

%prep
%setup
%patch -p1

%build
#remove_optflags %optflags_optimization
#CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
#CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
#FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ;
./configure \
	--prefix=%prefix \
	--bindir=%_bindir \
	--mandir=%_mandir \
	--enable-release \
	--disable-nasm --disable-tremor \
	--enable-text-console --enable-opengl
%make_build

%install
%makeinstall_std

# Menu, themes and extra files
install -pD -m644 dists/%name.desktop %buildroot%_datadir/applications/%name.desktop
mkdir -p %buildroot%_datadir/%name
install -p -m644 dists/engine-data/*.dat %buildroot%_datadir/%name/
install -p -m644 dists/engine-data/*.cpt %buildroot%_datadir/%name/
install -p -m644 dists/engine-data/*.tbl %buildroot%_datadir/%name/

install -D dists/maemo/scummvm64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -D dists/maemo/scummvm48.png %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
install -D icons/scummvm.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%doc AUTHORS README NEWS TODO COPYING
%exclude %_defaultdocdir/%name
%_bindir/scummvm
%_man6dir/scummvm.6*
%_datadir/pixmaps/scummvm.xpm
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/*/apps/*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 1.4.1-alt1
- Autobuild version bump to 1.4.1

* Thu Nov 10 2011 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Autobuild version bump to 1.4.0
- Fix build and dependencies

* Sat Jul 23 2011 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Autobuild version bump to 1.3.1

* Wed Jun 01 2011 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0
- Some extensions enabled
- Some icons added

* Thu Nov 18 2010 Alexey I. Froloff <raorn@altlinux.org> 1.2.0-alt1
- [1.2.0]
 + Fascination
 + Sierra SCI0 - SCI1.1 (see NEWS for full list)
 + Added support for GUI localization

* Tue Sep 28 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.1-alt1
- [1.1.1]
 + Blue's Art Time Activities
 + Blue's Reading Time Activities
 + Freddi Fish 5: The Case of the Creature of Coral Cove
 + Pajama Sam: Games to Play on Any Day
 + SPY Fox 3: Operation Ozone
 + Dragon History
 + TeenAgent

* Mon Feb 15 2010 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt1
- [1.0.0]
 + Discworld
 + Discworld 2 - Missing Presumed ...!?
 + Return to Zork
 + Leather Goddesses of Phobos 2
 + The Manhole
 + Rodney's Funscreen
 + Cruise for a Corpse

* Mon Jun 15 2009 Alexey I. Froloff <raorn@altlinux.org> 0.13.1-alt1
- [0.13.1]

* Wed Mar 11 2009 Sir Raorn <raorn@altlinux.ru> 0.13.0-alt1
- [0.13.0]
 + Blue's 123 Time Activities
 + Blue's ABC Time Activities
 + Bud Tucker in Double Trouble
 + The 7th Guest
- Fixed desktop-file-validate warnings

* Sun Jan 11 2009 Sir Raorn <raorn@altlinux.ru> 0.12.0-alt2
- Disabled ix86 assembly optimizations
- Removed obsolete %%update_menus/%%clean_menus calls

* Tue Sep 02 2008 Sir Raorn <raorn@altlinux.ru> 0.12.0-alt1
- [0.12.0]
 + The Legend of Kyrandia: Book Two: Hand of Fate
 + The Legend of Kyrandia: Book Three: Malcolm's Revenge
 + Lost in Time
 + The Bizarre Adventures of Woodruff and the Schnibble
 + Waxworks (PC version)
 + I Have no Mouth, and I must Scream (Macintosh version)
 + Drascula: The Vampire Strikes Back

* Thu Jan 24 2008 Sir Raorn <raorn@altlinux.ru> 0.11.0-alt1
- [0.11.0]
 + I Have no Mouth, and I Must Scream (demo and full game)
 + Elvira: Mistress of the Dark and Elvira 2: The Jaws of Cerberus
 + Better support for early Sierra AGI titles

* Fri Dec 14 2007 Sir Raorn <raorn@altlinux.ru> 0.10.0-alt2
- Engine data updated from tag release-0-10-0

* Thu Aug 23 2007 Sir Raorn <raorn@altlinux.ru> 0.10.0-alt1
- [0.10.0]
 + Sierra AGI engine: Space Quest I & II, King's Quest I-III and many
   more, including a vast number of fan-made games
 + Cinematique evo 1 engine: Future Wars
 + GOB engine: Bargon Attack, Gobliins 2, Goblins 3, Ween: The Prophecy
 + AGOS engine: Simon the Sorcerer's Puzzle Pack
 + Parallaction engine: Nippon Safes Inc.
 + Touche: The Adventures of the Fifth Musketeer engine

* Tue Dec 12 2006 Sir Raorn <raorn@altlinux.ru> 0.9.1-alt1
- [0.9.1]

* Fri Jun 30 2006 Sir Raorn <raorn@altlinux.ru> 0.9.0-alt1
- [0.9.0]
 + Support for The Legend of Kyrandia and The Feeble Files
 + New improved GUI
 + Reworked detection code for SCUMM games
 + Added subtitle configuration controls to the options dialog
 + Numerous bugfixes in the SCUMM, SAGA, Simon, Broken Sword 2 and BASS engines
- Default theme placed in %_datadir/%name/themes
- Added sky.cpt and kyra.dat from https://svn.sourceforge.net/svnroot/scummvm/engine-data/trunk/
- Default "extrapath" set to %_datadir/%name/engine-data
- Default "themepath" set to %_datadir/%name/themes

* Sun Feb 12 2006 Sir Raorn <raorn@altlinux.ru> 0.8.2-alt1
- [0.8.2]

* Tue Jan 31 2006 Sir Raorn <raorn@altlinux.ru> 0.8.1-alt1
- [0.8.1]
- Removed debian-style menu

* Mon Oct 31 2005 Sir Raorn <raorn@altlinux.ru> 0.8.0-alt1
- [0.8.0]
- Updated Summary/description
- Fixed menu entry (closes: #5352)
- Added .desktop file
- Added %%_gamesdatadir/%name

* Tue Mar 29 2005 Sir Raorn <raorn@altlinux.ru> 0.7.1-alt1
- [0.7.1]
- Summary/Description translations dropped (specspo migration)

* Fri Dec 24 2004 Sir Raorn <raorn@altlinux.ru> 0.7.0-alt1
- [0.7.1]
- Wrapper is no longer needed (upstram sets default save path to ~/.scummvm)

* Wed Aug 04 2004 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt1.1
- Oops! Fix %_bindir/scummvm attrs

* Tue Aug 03 2004 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt1
- [0.6.1]
- Keep save files in ~/.scummvm (Closes #3921)

* Sat Mar 27 2004 Sir Raorn <raorn@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Feb 23 2004 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt2
- CVS snapshot 20040223 (0.5.7-cvs)

* Wed Aug 13 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Wed Jun 25 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Mon Dec 23 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.3.0b-alt1
- ALTLnux build
