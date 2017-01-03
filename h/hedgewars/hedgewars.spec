Name: hedgewars
Version: 0.9.22
Release: alt1

Summary: Game with heavily armed fighting hedgehogs
License: GPLv2
Group: Games/Strategy
URL: http://www.hedgewars.org/

Packager: Denis G. Samsonenko <ogion@altlinux.org>

Source0: %name-src-%version.tar.bz2
Patch0: %name-no-bytestring.patch

Requires: %name-data = %version

# Automatically added by buildreq on Fri Jul 19 2013
# optimized out: cmake-modules fontconfig fpc-compiler fpc-units-base fpc-units-db fpc-units-fcl fpc-units-gfx fpc-units-misc fpc-units-net fpc-units-rtl ghc7.6.1 ghc7.6.1-common ghc7.6.1-mtl ghc7.6.1-network ghc7.6.1-parsec ghc7.6.1-primitive ghc7.6.1-text ghc7.6.1-transformers libSDL-devel libXi-devel libavcodec-devel libavutil-devel libffi-devel libgmp-devel libopencore-amrnb0 libopencore-amrwb0 libpng-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libstdc++-devel pkg-config zlib-devel
BuildRequires: cmake fpc-units-fv fpc-units-gtk2 fpc-units-math fpc-units-multimedia gcc-c++ ghc7.6.1-dataenc ghc7.6.1-hslogger ghc7.6.1-random ghc7.6.1-utf8-string ghc7.6.1-vector libGLUT-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel libavformat-devel liblua5.1-devel phonon-devel chrpath
BuildRequires: chrpath ghc7.6.1-sha ghc7.6.1-entropy ghc7.6.1-zlib

%description
Each player controls a team of several hedgehogs. During the course of the 
game, players take turns with one of their hedgehogs. They then use whatever 
tools and weapons are available to attack and kill the opponents' hedgehogs, 
thereby winning the game. Hedgehogs may move around the terrain in a variety 
of ways, normally by walking and jumping but also by using particular tools 
such as the "Rope" or "Parachute", to move to otherwise inaccessible areas. 

Each turn is time-limited to ensure that players do not hold up the game 
with excessive thinking or moving.
A large variety of tools and weapons are available for players during the 
game: Grenade, Cluster Bomb, Bazooka, UFO, Shotgun, Desert Eagle, Fire Punch, 
Baseball Bat, Dynamite, Mine, Rope, Pneumatic pick, Parachute. Most weapons, 
when used, cause explosions that deform the terrain, removing circular chunks. 

The landscape is an island floating on a body of water, or a restricted cave 
with water at the bottom. A hedgehog dies when it enters the water (either 
by falling off the island, or through a hole in the bottom of it), it is 
thrown off either side of the arena or when its health is reduced, 
typically from contact with explosions, to zero (the damage dealt to the 
attacked hedgehog or hedgehogs after a player's or CPU turn is shown only 
when all movement on the battlefield has ceased).


%package data
Summary: Resources for %name game
Group: Games/Strategy
BuildArch: noarch

%description data
This package contains all the data files for %name.


%prep
%setup -q -n %name-src-%version
%patch0 -p1

%build
%cmake_insource -DWITH_SERVER=1 -DPHYSFS_SYSTEM=0 -DDATA_INSTALL_DIR=%_datadir/%name -Dtarget_library_install_dir="%_libdir"
%make_build VERBOSE=true

%install
%make_install DESTDIR=%buildroot install

# fix verify-elf's RPATH error
chrpath --delete %buildroot%_bindir/hwengine

# replace font copies with symlinks to system versions
rm -f %buildroot%_datadir/%name/Data/Fonts/DejaVuSans-Bold.ttf
rm -f %buildroot%_datadir/%name/Data/Fonts/wqy-zenhei.ttc
ln -s ../../../fonts/ttf/dejavu/DejaVuSans-Bold.ttf %buildroot%_datadir/%name/Data/Fonts/DejaVuSans-Bold.ttf
ln -s ../../../fonts/ttf/wqy-zenhei/wqy-zenhei.ttc  %buildroot%_datadir/%name/Data/Fonts/wqy-zenhei.ttc

# install desktop file and icons
mkdir -p %buildroot%_datadir/applications/

cat <<EOF >%buildroot%_datadir/applications/%name.desktop
[Desktop Entry]
Name=%name
Comment=Strategy action game
Exec=%name
Terminal=false
Type=Application
Icon=%name
StartupNotify=true
Categories=Game;ActionGame;StrategyGame;
EOF

install -p -D -m 644 misc/%{name}_ico.png %buildroot%_datadir/icons/hicolor/32x32/apps/%name.png
install -p -D -m 644 misc/%name.png %buildroot%_datadir/icons/hicolor/512x512/apps/%name.png

# install man file
install -p -D -m 644 man/%name.6 %buildroot%_mandir/man6/%name.6

%files
%doc README ChangeLog.txt CREDITS
%_bindir/*
%_libdir/*.so*
%_mandir/man6/*
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/512x512/apps/%name.png
%_datadir/pixmaps/%name.xpm
%_datadir/appdata/%name.appdata.xml

%files data
%_datadir/%name


%changelog
* Tue Jan 03 2017 Denis G. Samsonenko <ogion@altlinux.org> 0.9.22-alt1
- new version

* Sun May 24 2015 Denis G. Samsonenko <ogion@altlinux.org> 0.9.21.1-alt1
- new version
- %name-no-bytestring.patch updated

* Wed Apr 23 2014 Denis G. Samsonenko <ogion@altlinux.org> 0.9.20.5-alt1
- new version
- %name-compiler-opts.patch removed

* Sat Jul 20 2013 Denis G. Samsonenko <ogion@altlinux.org> 0.9.19.3-alt2
- %name-data subpackage
- font copies replaced with symlinks to system versions (#25350)
- icon added to desktop file (#22690)
- man file packaged

* Sat Jul 20 2013 Denis G. Samsonenko <ogion@altlinux.org> 0.9.19.3-alt1
- new version
- %name-no-bytestring.patch adapted from Fedora package
- %name-compiler-opts.patch

* Sun Nov 20 2011 Anton Farygin <rider@altlinux.ru> 0.9.17-alt1
- new version

* Sun Sep 18 2011 Anton Farygin <rider@altlinux.ru> 0.9.16-alt1
- new version

* Sat Feb 12 2011 Anton Farygin <rider@altlinux.ru> 0.9.15-alt1
- new version

* Wed Sep 29 2010 Anton Farygin <rider@altlinux.ru> 0.9.13-alt2
- rebuild in new environment

* Sun Apr 04 2010 Anton Farygin <rider@altlinux.ru> 0.9.13-alt1
- new version

* Wed Mar 10 2010 Anton Farygin <rider@altlinux.ru> 0.9.12-alt2
- fixed build with new fpc-2.4.0

* Sun Nov 15 2009 Anton Farygin <rider@altlinux.ru> 0.9.12-alt1
- new version

* Mon May 25 2009 Anton Farygin <rider@altlinux.ru> 0.9.11-alt1
- new version

* Tue Apr 14 2009 Anton Farygin <rider@altlinux.ru> 0.9.10-alt1
- new version

* Sun Mar 15 2009 Anton Farygin <rider@altlinux.ru> 0.9.9-alt2
- build hedgewars-server too

* Mon Jan 26 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1.1
- Fix summary

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Mon Nov 03 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Tue Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Sun Jun 22 2008 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt1
- build for Sisyphus
