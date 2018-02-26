Name: neverball
Version: 1.5.4
Release: alt4

Summary: OpenGL golf-based game
License: GPL
Group: Games/Other

Url: http://www.icculus.org/neverball/

Source0: http://www.icculus.org/neverball/%name-%version.tar.gz
Source1: %name-48.png
Source2: %name-32.png
Source3: %name-16.png
Source4: neverputt-48.png
Source5: neverputt-32.png
Source6: neverputt-16.png
Patch: neverball-1.5.4-dso.patch

Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: freetype2-devel libGLU-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel zlib-devel
BuildRequires: libjpeg-devel libpng-devel libalsa-devel libvorbis-devel libX11-devel libphysfs-devel fonts-ttf-dejavu

Obsoletes: neverputt <= %version-%release
Conflicts: neverputt <= %version-%release

%description
Tilt the floor to roll a ball through an obstacle course
before time runs out.

Neverball is part puzzle game, part action game,
and entirely a test of skill.

Also found here is Neverputt, a hot-seat multiplayer miniature
golf game using the physics and graphics of Neverball.

%description -l ru_RU.KOI8-R
Симпатичная OpenGL-игрушка, очень напоминающая гольф.

%prep
%setup
%patch -p0
sed -i 's|\(ALL_CFLAGS\ \:\=.*\)|\1 -g|' Makefile

%build
%make_build DATADIR=%_datadir/%name

%install
mkdir -p %buildroot%_datadir/%name/
mkdir -p %buildroot%_gamesbindir

cp -a data/* %buildroot%_datadir/%name/
find %buildroot%_datadir/%name/ -type f -name "*.map"|xargs rm -f

install -pm755 -s %name %buildroot%_gamesbindir
install -pm755 -s neverputt %buildroot%_gamesbindir

# Install the desktop files
cat > neverball.desktop << EOF
[Desktop Entry]
Name=Neverball
Comment=Test of skill, part puzzle game and part action game
Exec=%_gamesbindir/neverball
Icon=neverball
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF
cat > neverputt.desktop << EOF
[Desktop Entry]
Name=Neverputt
Comment=Multiplayer miniature golf game
Exec=%_gamesbindir/neverputt
Icon=neverputt
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -pDm644 %SOURCE1 %buildroot%_liconsdir/%name.png
install -pDm644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -pDm644 %SOURCE3 %buildroot%_miconsdir/%name.png
install -pDm644 %SOURCE4 %buildroot%_liconsdir/neverputt.png
install -pDm644 %SOURCE5 %buildroot%_niconsdir/neverputt.png
install -pDm644 %SOURCE6 %buildroot%_miconsdir/neverputt.png

mkdir -p %buildroot%_datadir/applications
cp -a never*.desktop %buildroot%_datadir/applications

# Use system fonts instead of bundling our own
#rm %buildroot%_datadir/%name/data/ttf/DejaVuSans-Bold.ttf
#mkdir %buildroot%_datadir/%name/ttf/
#ln -s %_datadir/fonts/ttf/dejavu/DejaVuSans-Bold.ttf \
#	%buildroot%_datadir/%name/data/ttf/DejaVuSans-Bold.ttf
ln -sf %_datadir/fonts/ttf/dejavu/DejaVuSans-Bold.ttf \
	%buildroot%_datadir/%name/ttf/DejaVuSans-Bold.ttf

%find_lang %name

%files -f %name.lang
%doc README
%_gamesbindir/*
%dir %_datadir/%name
%_datadir/%name/*
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/neverputt.png
%_niconsdir/neverputt.png
%_miconsdir/neverputt.png
%_datadir/applications/*

%changelog
* Sun May 06 2012 Michael Shigorin <mike@altlinux.org> 1.5.4-alt4
- *fixed* datadir issues (closes: #23162)
- applied fedora patch (a bit more complete than gentoo one)
- minor spec cleanup

* Thu Aug 25 2011 Ilya Mashkin <oddity@altlinux.ru> 1.5.4-alt3
- fix font again

* Wed Aug 24 2011 Ilya Mashkin <oddity@altlinux.ru> 1.5.4-alt2
- fix DATADIR (Closes: #26116)
- use system fonts (Closes: #25351)

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.4-alt1.1
- Rebuilt with libphysfs 2.0.2

* Sun Dec 06 2009 Ilya Mashkin <oddity@altlinux.ru> 1.5.4-alt1
- 1.5.4
- fix desktop files

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.4.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for neverball
  * update_menus for neverball
  * postclean-05-filetriggers for spec file

* Mon Jan 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.4.0-alt2
- Removed erroneus Requires.
- Removed erroneus BuildRequires.
- Removed old XFree kludges.
- Rewrote descriptions.
- Minor spec cleanup.
- Added freedesktop menu file.
- Added post/postun.

* Fri Oct 29 2004 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Jul 06 2004 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- added icons
- new version (merged with neverputt)

* Fri Oct 31 2003 Alexander Bokovoy <ab@altlinux.ru> 0.25.12-alt1
- Initial build for Sisyphus

