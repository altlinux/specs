Name: tecnoballz
Version: 0.92
Release: alt2
Summary: A Brick Busting game
Packager: Fr. Br. George <george@altlinux.ru>

Group: Games/Arcade
License: GPLv3+
Url: http://linux.tlk.fr/games/TecnoballZ/
Source0: http://linux.tlk.fr/games/TecnoballZ/download/%name-%version.tgz
Source1: %name.xpm
Source2: %name.desktop
# Vine Linux
Patch0: %name-0.91-datadir-ALT.patch
Patch1: %name-0.91-owner.patch
# Debian
#Patch2: %name-0.91-hiscorepath.patch
# BoredByPolitics
Patch3: %name-0.91-build.patch
# Martin Michlmayr
Patch4: %name-0.91-gcc41.patch
# Upstream CVS
Patch5: %name-0.91-configfile.patch
# Hans de Goede
Patch6: %name-0.91-64-bit.patch
Patch7: %name-0.91-no-smpeg.patch
Patch8: %name-0.91-dropsgid-ALT.patch
Patch9: %name-0.91-as-needed.patch
Patch10: tecnoballz-0.92-alt-coord_x.patch

BuildRequires: desktop-file-utils xorg-util-macros

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: gcc-c++ imake libSDL-devel libSDL_image-devel libSDL_mixer-devel libX11-devel libmikmod-devel libsmpeg-devel libvorbis-devel xorg-cf-files

%description
TecnoballZ is a "breaking blocks" game that was first written for the
Amiga platfrom.
You'll need to break all the blocks in each level. The game is divided
into Areas which are divided into Levels. Between some levels, you
have to defeat a guardian to pass to the next level. When passing an
Area, a new edge is open. You can buy weapons and bonus between levels
with the money earned during the game.

%prep
%setup -q
#patch0 -p1
#patch1 -p1
#patch2 -p1
#patch3 -p2
#patch4 -p1
#patch5 -p1
#patch6 -p1
#patch7 -p1
##patch8 -p1
##patch9 -p1
%patch10

#fix man encodig
#iconv -f ASCII -t UTF-8 man/tecnoballz.1 > man/tecnoballz.1.conv && mv -f man/tecnoballz.1.conv man/tecnoballz.1
iconv -f ISO8859-1 -t UTF-8 man/%name.fr.6 > man/%name.fr.6.conv && mv -f man/%name.fr.6.conv man/%name.fr.6

%build
rm -rf autom4te.cache config.log config.status Makefile configure config.h
%autoreconf
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir --localstatedir=%_localstatedir/games

%make_build gamesdir=%_gamesbindir datadir=%_gamesdatadir scoredir=%_localstatedir/games

%install
%makeinstall DESTDIR=%buildroot gamesdir=%_gamesbindir datadir=%_gamesdatadir scoredir=%_localstatedir/games

# install man6
mkdir -p %buildroot%_mandir/man6/
mkdir -p %buildroot%_mandir/fr/man6/
#sed s/TH\ TecnoballZ/TH\ TecnoballZ\ 6/ < man/%name.1 > man/%name.6
#sed s/TH\ TecnoballZ/TH\ TecnoballZ\ 6/ < man/%name.fr.1 > man/%name.fr.6
install -p -m0644 man/%name.6 %buildroot%_man6dir/%name.6
install -p -m0644 man/%name.fr.6 %buildroot%_mandir/fr/man6/%name.6
install -p -m0644 src/TecnoballZ/*.xml %buildroot%_gamesdatadir/%name
cp -r src/TecnoballZ/texts %buildroot%_gamesdatadir/%name/

# install desktop file
mkdir -p %buildroot%_desktopdir
desktop-file-install --vendor "" \
  --dir %buildroot%_desktopdir \
  %SOURCE2

# install icon
mkdir -p %buildroot%_niconsdir
install -p -m 0644 %SOURCE1 %buildroot%_niconsdir/%name.xpm

%files
%attr(2711,root,games) %_gamesbindir/%name
%_gamesdatadir/%name
%_man6dir/%name.6*
%_mandir/fr/man6/%name.6*
%_niconsdir/%name.xpm
%_desktopdir/%name.desktop
%doc AUTHORS CHANGES COPYING README
%attr(664,root,games) %config(noreplace) %_localstatedir/games/%name.hi

%changelog
* Thu Dec 10 2009 Fr. Br. George <george@altlinux.ru> 0.92-alt2
- Fix missing highscore bug

* Tue Dec 02 2008 Fr. Br. George <george@altlinux.ru> 0.92-alt1
- Version up
- Invalidate all the patches
- GCC4.3 incompatible typo fix

* Fri Nov 30 2007 Fr. Br. George <george@altlinux.ru> 0.91-alt1
- Initial build for ALT from FC

* Sat Aug 25 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-6
- changed license due to new guidelines
- removed %%{?dist} tag from changelog
- updated icon cache scriptlets to be compliant to new guidelines
- changed desktop categories from Game;ArcadeGame; to
  Game;ArcadeGame;BlocksGame; (resolves bugzilla #250940)

* Tue Apr 03 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-5
- changed summary to avoid naming trademarks.

* Sun Apr 01 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-4
- corrected silly error in the %%postun script

* Sat Mar 31 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-3
- added a patch by Hans de Goede to drop setgid privileges when not needed
- changed icon cache scriptles to be compliant with updated guidelines
- changed vendor to fedora in desktop-file-install

* Wed Mar 25 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-2
- moved from Livna to Fedora
- added a patch by Hans de Goede to fix compiling on 64 bits (Livna #1367)
- added a patch by Hans de Goede not to require smpeg (Livna #1367)
- changed desktop category to Game;ArcadeGame
- binary setgid 'games' in order to allow a shared scoreboard file
- cosmetic changes

* Sun Dec 17 2006 Andrea Musuruane <musuruan@gmail.com> 0.91-1
- initial build for Livna based on Vine Linux package
- used icon file from Debian package
- used patches from Debian and Vine Linux packages
- used a patch by BoredByPolitics via happypenguin.org to fix building
- used a patch by Martin Michlmayr to fix compiling with gcc 4.1 (Debian
  #355841)
- used a patch from upstream to fix segfault into configfile.cc file

