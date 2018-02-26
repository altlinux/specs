Name: ufoai
Version: 2.4
Release: alt1
Source: %name-%version.tar
Summary: UFO: Alien Invasion - build your team and stop the aliens
License: GPL
Group: Games/Strategy
Url: http://ufoai.sf.net
Packager: Roman Savochenko <rom_as@altlinux.ru>
Requires: %name-data = %version

BuildPreReq: gcc4.5-c++ zlib-devel libcurl-devel libjpeg-devel libpng-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libogg-devel libvorbis-devel
BuildPreReq: libtheora-devel libgtk+2-devel libgtkglext-devel libxml2-devel libgtksourceview-devel libopenal-devel texlive-latex-extra
#BuildPreReq: libSDL-devel libmesa-devel libxvid-devel

%define srcname %name-%version

%set_verify_elf_method no

%description
"UFO: Alien Invasion" is a game inspired by the XCOM "UFO" series.
.
As manager of an international military force dedicated to stop the
Alien Invasion, you prepare your soldiers and attack the aliens on
various sites on the Earth.
.
The tactical part of the game uses OpenGL, and is based on the Quake2
engine. A multiplayer mode is also available

%package server
Group: Games/Strategy
Summary: UFO: Alien Invasion - standalone game server
Requires: %name = %version
%description server
"UFO: Alien Invasion" is a game inspired by the XCOM "UFO" series.
.
This package includes the standalone game server.
It is only needed if you want to setup a permanent game server.

%package data
Group: Games/Strategy
Summary: Data for UFO: Alien Invasion
#Requires: fonts-ttf-freefont, fonts-ttf-dejavu, fonts-ttf-thai
BuildArch: noarch
%description data
"UFO: Alien Invasion" is a game inspired by the XCOM "UFO" series.
.
This package contains rest of the non-optional game data for UFO:AI:
models, units, sound effects, etc.

%package tools
Group: Games/Strategy
Summary: UFO: Alien Invasion - data-building tool
%description tools
"UFO: Alien Invasion" is a game inspired by the XCOM "UFO" series.
.
This package includes the map-compiling tool and some blender
scripts for modelling.

#package map-sources
#Group: Games/Strategy
#Summary: UFO: Alien Invasion - map-sources
#Requires: %name-tools = %version
#description map-sources
#"UFO: Alien Invasion" is a game inspired by the XCOM "UFO" series.
#.
# This package includes the map-sources. Edit them with UFORadiant

%prep
%setup -q -n %srcname

%build
#autoreconf
./configure --prefix=%{_prefix} --enable-uforadiant
#CFLAGS="-O2" CXXFLAGS="-O2"
%make
%make uforadiant
%make lang
%make manual
#make maps

%install
#make DESTDIR=%buildroot install
# For core
install -m 644 -pD base/game.so %buildroot/usr/lib/games/ufoai/base/game.so
install -m 755 -pD ufo %buildroot/usr/lib/games/ufoai/ufo
install -m 755 -pD debian/ufo %buildroot/usr/games/ufo
install -m 644 -pD debian/ufoai.xpm %buildroot/usr/share/pixmaps/ufoai.xpm
install -m 644 -pD debian/ufoai.desktop %buildroot/usr/share/applications/ufoai.desktop
install -m 644 -pD debian/ufoai-safe.desktop %buildroot/usr/share/applications/ufoai-safe.desktop
install -m 644 -pD debian/ufo.6 %buildroot/%_man6dir/ufo.6
install -m 644 -pD debian/ufoded.6 %buildroot/%_man6dir/ufoded.6

# For server
install -m 755 -pD ufoded %buildroot/usr/lib/games/ufoai/
install -m 755 -pD debian/ufoded %buildroot/usr/games/
install -m 644 -pD debian/ufoded.xpm %buildroot/usr/share/pixmaps/
install -m 644 -pD debian/ufoded.desktop %buildroot/usr/share/applications
install -m 644 -pD debian/ufoded.6 %buildroot/%_man6dir

# For data
install -m 755 -d %buildroot/usr/share/games/ufoai/base
ln -s /usr/lib/games/ufoai/base/game.so %buildroot/usr/share/games/ufoai/base/game.so
install -m 644 -pD base/*.pk3 %buildroot/usr/share/games/ufoai/base/
install -m 755 -d %buildroot/usr/share/games/ufoai/base/i18n
cp -r base/i18n/* %buildroot/usr/share/games/ufoai/base/i18n
install -m 644 -pD src/docs/tex/ufo-manual_EN.pdf %buildroot/usr/share/doc/ufoai-data/ufo-manual_EN.pdf
#install -m 644 -pD base/media/UnDinaruBold.ttf %buildroot/usr/share/games/ufoai/media/UnDinaruBold.ttf
#install -m 644 -pD base/media/ume-pgo4.ttf %buildroot/usr/share/games/ufoai/media/ume-pgo4.ttf
## add links to fonts
#ln -s /usr/share/fonts/truetype/freefont/FreeSans.ttf %buildroot/usr/share/games/ufoai/media/FreeSans.ttf
#ln -s /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf %buildroot/usr/share/games/ufoai/media/DejaVuSans.ttf
#ln -s /usr/share/fonts/truetype/thai/Loma.ttf %buildroot/usr/share/games/ufoai/media/Loma.ttf
#ln -s /usr/share/fonts/truetype/thai/Norasi.ttf %buildroot/usr/share/games/ufoai/media/Norasi.ttf
#ln -s /usr/share/fonts/truetype/wqy/wqy-zenhei.ttf %buildroot/usr/share/games/ufoai/media/wqy-zenhei.ttf
#ln -s /usr/share/fonts/truetype/unfonts/UnGraphicBold.ttf %buildroot/usr/share/games/ufoai/media/UnGraphicBold.ttf

# tools
install -m 755 -pD ufo2map %buildroot/usr/games/
install -m 755 -pD ufomodel %buildroot/usr/games/
install -m 644 -pD src/tools/blender/md2tag_export.py %buildroot/usr/share/blender/scripts/blender/md2tag_export.py
#install -m 644 -pD contrib/scripts/bashcompletion/ufo2map %buildroot/etc/bash_completion.d/ufo2map
#install -m 644 -pD contrib/scripts/bashcompletion/ufomodel %buildroot/etc/bash_completion.d/ufomodel
install -m 644 -pD debian/ufo2map.6 %buildroot/%_man6dir
install -m 755 -d %buildroot/usr/share/games/uforadiant/bitmaps/
install -m 644 -pD radiant/bitmaps/* %buildroot/usr/share/games/uforadiant/bitmaps/
#install -m 755 -d %buildroot/usr/share/games/uforadiant/games/
#install -m 644 -pD radiant/games/* %buildroot/usr/share/games/uforadiant/games/
install -m 755 -d %buildroot/usr/share/games/uforadiant/i18n/
cp -r radiant/i18n/* %buildroot/usr/share/games/uforadiant/i18n/
#install -m 755 -d %buildroot/usr/share/games/uforadiant/plugins/
#install -m 644 -pD radiant/plugins/*.so %buildroot/usr/share/games/uforadiant/plugins/
#install -m 755 -d %buildroot/usr/share/games/uforadiant/shaders/
#install -m 644 -pD radiant/shaders/*.shader %buildroot/usr/share/games/uforadiant/shaders/
install -m 755 -d %buildroot/usr/share/games/uforadiant/sourceviewer/
install -m 644 -pD radiant/sourceviewer/* %buildroot/usr/share/games/uforadiant/sourceviewer/
install -m 755 -d %buildroot/usr/share/games/uforadiant/prefabs/
cp -r radiant/prefabs/* %buildroot/usr/share/games/uforadiant/prefabs/
install -m 755 -pD radiant/uforadiant %buildroot/usr/lib/games/uforadiant/uforadiant
install -m 755 -pD debian/uforadiant %buildroot/usr/games/uforadiant
install -m 644 -pD debian/uforadiant.xpm %buildroot/usr/share/pixmaps/uforadiant.xpm
install -m 644 -pD debian/uforadiant.desktop %buildroot/usr/share/applications/uforadiant.desktop
install -m 644 -pD debian/uforadiant.6 %buildroot/%_man6dir

# map-sources
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/
#install -m 644 -pD base/maps/*.map %buildroot/usr/share/games/ufoai/base/maps/
#install -m 644 -pD base/maps/*.ump %buildroot/usr/share/games/ufoai/base/maps/
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/africa
#install -m 644 -pD base/maps/africa/*.map %buildroot/usr/share/games/ufoai/base/maps/africa
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/alienb
#install -m 644 -pD base/maps/alienb/*.map %buildroot/usr/share/games/ufoai/base/maps/alienb
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/b
#install -m 644 -pD base/maps/b/*.map %buildroot/usr/share/games/ufoai/base/maps/b
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/bomber_city
#install -m 644 -pD base/maps/bomber_city/*.map %buildroot/usr/share/games/ufoai/base/maps/bomber_city
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/bridge
#install -m 644 -pD base/maps/bridge/*.map %buildroot/usr/share/games/ufoai/base/maps/bridge
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/cemetery
#install -m 644 -pD base/maps/cemetery/*.map %buildroot/usr/share/games/ufoai/base/maps/cemetery
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/city_disco
#install -m 644 -pD base/maps/city_disco/*.map %buildroot/usr/share/games/ufoai/base/maps/city_disco
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/construction
#install -m 644 -pD base/maps/construction/*.map %buildroot/usr/share/games/ufoai/base/maps/construction
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/community_centre
#install -m 644 -pD base/maps/community_centre/*.map %buildroot/usr/share/games/ufoai/base/maps/community_centre
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/country
#install -m 644 -pD base/maps/country/*.map %buildroot/usr/share/games/ufoai/base/maps/country
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/druglord
#install -m 644 -pD base/maps/druglord/*.map %buildroot/usr/share/games/ufoai/base/maps/druglord
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/eaglenest
#install -m 644 -pD base/maps/eaglenest/*.map %buildroot/usr/share/games/ufoai/base/maps/eaglenest
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/farm
#install -m 644 -pD base/maps/farm/*.map %buildroot/usr/share/games/ufoai/base/maps/farm
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/forest
#install -m 644 -pD base/maps/forest/*.map %buildroot/usr/share/games/ufoai/base/maps/forest
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/frozen
#install -m 644 -pD base/maps/frozen/*.map %buildroot/usr/share/games/ufoai/base/maps/frozen
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/gasstation
#install -m 644 -pD base/maps/gasstation/*.map %buildroot/usr/share/games/ufoai/base/maps/gasstation
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/ice
#install -m 644 -pD base/maps/ice/*.map %buildroot/usr/share/games/ufoai/base/maps/ice
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/industrial
#install -m 644 -pD base/maps/industrial/*.map %buildroot/usr/share/games/ufoai/base/maps/industrial
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/italy
#install -m 644 -pD base/maps/italy/*.map %buildroot/usr/share/games/ufoai/base/maps/italy
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/japan
#install -m 644 -pD base/maps/japan/*.map %buildroot/usr/share/games/ufoai/base/maps/japan
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/laboratory
#install -m 644 -pD base/maps/laboratory/*.map %buildroot/usr/share/games/ufoai/base/maps/laboratory
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/mart
#install -m 644 -pD base/maps/mart/*.map %buildroot/usr/share/games/ufoai/base/maps/mart
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/military_convoy
#install -m 644 -pD base/maps/military_convoy/*.map %buildroot/usr/share/games/ufoai/base/maps/military_convoy
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/oriental
#install -m 644 -pD base/maps/oriental/*.map %buildroot/usr/share/games/ufoai/base/maps/oriental
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/shelter
#install -m 644 -pD base/maps/shelter/*.map %buildroot/usr/share/games/ufoai/base/maps/shelter
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/spedition
#install -m 644 -pD base/maps/spedition/*.map %buildroot/usr/share/games/ufoai/base/maps/spedition
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/stadium
#install -m 644 -pD base/maps/stadium/*.map %buildroot/usr/share/games/ufoai/base/maps/stadium
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/transport
#install -m 644 -pD base/maps/transport/*.map %buildroot/usr/share/games/ufoai/base/maps/transport
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/tropic
#install -m 644 -pD base/maps/tropic/*.map %buildroot/usr/share/games/ufoai/base/maps/tropic
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/ufocrash
#install -m 644 -pD base/maps/ufocrash/*.map %buildroot/usr/share/games/ufoai/base/maps/ufocrash
#install -m 755 -d %buildroot/usr/share/games/ufoai/base/maps/village
#install -m 644 -pD base/maps/village/*.map %buildroot/usr/share/games/ufoai/base/maps/village

%files
%doc README COPYING debian/changelog debian/copyright
/usr/lib/games/ufoai/base/game.so
/usr/lib/games/ufoai/ufo
/usr/games/ufo
/usr/share/pixmaps/ufoai.xpm
/usr/share/applications/ufoai.desktop
/usr/share/applications/ufoai-safe.desktop
%_man6dir/ufo.6*
#_man6dir/ufoded.6*

%files tools
/usr/games/ufo2map
/usr/games/ufomodel
/usr/share/blender/scripts/blender/md2tag_export.py
#/etc/bash_completion.d/ufo2map
#/etc/bash_completion.d/ufomodel
%_man6dir/ufo2map.6*
/usr/share/games/uforadiant
/usr/lib/games/uforadiant/uforadiant
/usr/games/uforadiant
/usr/share/pixmaps/uforadiant.xpm
/usr/share/applications/uforadiant.desktop
%_man6dir/uforadiant.6*

%files server
/usr/lib/games/ufoai/ufoded
/usr/games/ufoded
/usr/share/pixmaps/ufoded.xpm
/usr/share/applications/ufoded.desktop
%_man6dir/ufoded.6*

%files data
#doc howtoplay/*
/usr/share/games/ufoai/base/game.so
/usr/share/games/ufoai/base/*.pk3
/usr/share/games/ufoai/base/i18n/*
/usr/share/doc/ufoai-data/ufo-manual_EN.pdf
#/usr/share/games/ufoai/media/UnDinaruBold.ttf
#/usr/share/games/ufoai/media/ume-pgo4.ttf
#/usr/share/games/ufoai/media

#files map-sources
#/usr/share/games/ufoai/base/maps

%changelog
* Fri Apr 27 2012 Roman Savochenko <rom_as@altlinux.ru> 2.4-alt1
- Build version 2.4.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.1-alt1.1
- Rebuild with Python-2.7

* Fri Apr 1 2011 Roman Savochenko <rom_as@altlinux.ru> 2.3.1-alt1
- Build version 2.3.1 for ALTLinux.

* Sun Jul 18 2010 Roman Savochenko <rom_as@altlinux.ru> 2.3-alt0.M51.1
- Version 2.3 build for Branch 5.1.

* Fri Jul 2 2010 Roman Savochenko <rom_as@altlinux.ru> 2.3-alt1
- Initial build version 2.3 for ALTLinux.

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for ufoai
  * postclean-05-filetriggers for spec file

* Fri Oct 10 2008 Roman Savochenko <rom_as@altlinux.ru> 2.2.1-alt1
- First build for ALTLinux.
