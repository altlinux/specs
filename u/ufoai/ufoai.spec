%set_verify_elf_method unresolved=strict

Name: ufoai
Version: 2.5
Release: alt4
Summary: UFO: Alien Invasion - build your team and stop the aliens
License: GPL
Group: Games/Strategy
Url: http://ufoai.sf.net

Source: %name-%version.tar
Patch1: ufoai-DSO.patch

BuildRequires: gcc-c++ zlib-devel libcurl-devel libjpeg-devel libpng-devel libSDL2_image-devel libSDL2_mixer-devel libSDL2_ttf-devel libogg-devel libvorbis-devel
BuildRequires: libtheora-devel libgtk+2-devel libgtkglext-devel libxml2-devel libgtksourceview-devel libopenal-devel texlive-latex-extra

Requires: %name-data = %EVR

# don't depend on blender just for helper scripts
%add_findreq_skiplist %_datadir/blender/scripts/blender/md2tag_export.py*
%add_findprov_skiplist %_datadir/blender/scripts/blender/md2tag_export.py*

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
Requires: %name = %EVR

%description server
"UFO: Alien Invasion" is a game inspired by the XCOM "UFO" series.
.
This package includes the standalone game server.
It is only needed if you want to setup a permanent game server.

%package data
Group: Games/Strategy
Summary: Data for UFO: Alien Invasion
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

%prep
%setup
%patch1 -p1

%build
%add_optflags -Wno-narrowing
export CFLAGS="${CFLAGS:-%optflags}"
export CXXFLAGS="${CXXFLAGS:-%optflags}"
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--bindir=%{_bindir} \
	--datadir=%{_datadir} \
	--enable-uforadiant

%make
%make uforadiant
%make lang
%make manual

%install
# For core
install -m 644 -pD base/game.so %buildroot%_libexecdir/%_gamesdir/%name/base/game.so
install -m 755 -pD ufo %buildroot%_libexecdir/%_gamesdir/%name/ufo
install -m 755 -pD debian/ufo %buildroot%_prefix/%_gamesdir/ufo
install -m 644 -pD debian/ufoai.xpm %buildroot%_pixmapsdir/ufoai.xpm
install -m 644 -pD debian/ufoai.desktop %buildroot%_desktopdir/ufoai.desktop
install -m 644 -pD debian/ufoai-safe.desktop %buildroot%_desktopdir/ufoai-safe.desktop
install -m 644 -pD debian/ufo.6 %buildroot%_man6dir/ufo.6
install -m 644 -pD debian/ufoded.6 %buildroot%_man6dir/ufoded.6

# For server
install -m 755 -pD ufoded %buildroot%_libexecdir/%_gamesdir/%name/
install -m 755 -pD debian/ufoded %buildroot%_prefix/%_gamesdir/
install -m 644 -pD debian/ufoded.xpm %buildroot%_pixmapsdir/
install -m 644 -pD debian/ufoded.desktop %buildroot%_desktopdir/
install -m 644 -pD debian/ufoded.6 %buildroot%_man6dir/

# For data
install -m 755 -d %buildroot%_gamesdatadir/%name/base
ln -s %_libexecdir/%_gamesdir/%name/base/game.so %buildroot%_gamesdatadir/%name/base/game.so
install -m 644 -pD base/*.pk3 %buildroot%_gamesdatadir/%name/base/
install -m 755 -d %buildroot%_gamesdatadir/%name/base/i18n
cp -r base/i18n/* %buildroot%_gamesdatadir/%name/base/i18n
install -m 644 -pD src/docs/tex/ufo-manual_EN.pdf %buildroot%_docdir/ufoai-data/ufo-manual_EN.pdf

# tools
install -m 755 -pD ufo2map %buildroot%_gamesbindir/
install -m 755 -pD ufomodel %buildroot%_gamesbindir/
install -m 644 -pD src/tools/blender/md2tag_export.py %buildroot%_datadir/blender/scripts/blender/md2tag_export.py
install -m 644 -pD debian/ufo2map.6 %buildroot%_man6dir/
install -m 755 -d %buildroot%_gamesdatadir/uforadiant/bitmaps/
install -m 644 -pD radiant/bitmaps/* %buildroot%_gamesdatadir/uforadiant/bitmaps/
install -m 755 -d %buildroot%_gamesdatadir/uforadiant/i18n/
cp -r radiant/i18n/* %buildroot%_gamesdatadir/uforadiant/i18n/
install -m 755 -d %buildroot%_gamesdatadir/uforadiant/sourceviewer/
install -m 644 -pD radiant/sourceviewer/* %buildroot%_gamesdatadir/uforadiant/sourceviewer/
install -m 755 -d %buildroot%_gamesdatadir/uforadiant/prefabs/
cp -r radiant/prefabs/* %buildroot%_gamesdatadir/uforadiant/prefabs/
install -m 755 -pD radiant/uforadiant %buildroot%_libexecdir/%_gamesdir/uforadiant/uforadiant
install -m 755 -pD debian/uforadiant %buildroot%_gamesbindir/uforadiant
install -m 644 -pD debian/uforadiant.xpm %buildroot%_pixmapsdir/uforadiant.xpm
install -m 644 -pD debian/uforadiant.desktop %buildroot%_desktopdir/uforadiant.desktop
install -m 644 -pD debian/uforadiant.6 %buildroot%_man6dir

%files
%doc README COPYING debian/changelog debian/copyright
%_libexecdir/%_gamesdir/%name/base/game.so
%_libexecdir/%_gamesdir/%name/ufo
%_gamesbindir/ufo
%_pixmapsdir/ufoai.xpm
%_desktopdir/ufoai.desktop
%_desktopdir/ufoai-safe.desktop
%_man6dir/ufo.6*

%files tools
%_gamesbindir/ufo2map
%_gamesbindir/ufomodel
%_datadir/blender/scripts/blender/md2tag_export.py
%_man6dir/ufo2map.6*
%_gamesdatadir/uforadiant
%_libexecdir/%_gamesdir/uforadiant/uforadiant
%_gamesbindir/uforadiant
%_pixmapsdir/uforadiant.xpm
%_desktopdir/uforadiant.desktop
%_man6dir/uforadiant.6*

%files server
%_libexecdir/%_gamesdir/%name/ufoded
%_gamesbindir/ufoded
%_pixmapsdir/ufoded.xpm
%_desktopdir/ufoded.desktop
%_man6dir/ufoded.6*

%files data
%_gamesdatadir/%name/base/game.so
%_gamesdatadir/%name/base/*.pk3
%_gamesdatadir/%name/base/i18n/*
%_docdir/ufoai-data/ufo-manual_EN.pdf

%changelog
* Thu Dec 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5-alt4
- Cleaned up spec and dependencies.

* Mon Sep 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5-alt3
- Fixed build with new toolchain.

* Sat Dec 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5-alt2
- (non-user-visible) verify-elf enabled.

* Tue Dec 13 2016 Mikhail Efremov <sem@altlinux.org> 2.5-alt1
- Build with SDL2.
- Use latest compiler.
- Updated to 2.5.

* Tue Apr 22 2014 Roman Savochenko <rom_as@altlinux.ru> 2.4-alt1.3
- DSO fix.

* Mon Mar 03 2014 Roman Savochenko <rom_as@altlinux.ru> 2.4-alt1.2
- Rebuild.

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.1
- Rebuilt with libpng15

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
