Name: freedroidrpg
Version: 0.15
Release: alt1

Summary: Isometric action game with RPG elements
License: GPL
Group: Games/Arcade
Url: http://freedroid.sf.net
Packager: Roman Savochenko <rom_as at altlinux.ru>

BuildPreReq: libSDL-devel libGLU-devel libjpeg-devel zlib-devel libpng-devel libSDL_image-devel libSDL_net-devel libvorbis-devel libSDL_mixer-devel libSDL_gfx-devel

Requires: %name-data = %version

Source: %name-%version.tar.bz2
Source1: %name.desktop
Source3: %name-16x16.png
Source4: %name-32x32.png
Source5: %name-48x48.png

%description
Interesting Diablo-like game featuring The Tux as the main character.

%package tools
Group: Games/Arcade
Summary: Some edit tools for Freedroid RPG
Requires: %name = %version-%release
%description tools
This package contains some edit tools required to
develop new content to the Freedroid RPG game. 

%package data
Group: Games/Arcade
Summary: Media files Freedroid RPG
BuildArch: noarch

%description data
This package contains media files for Freedroid RPG game

%prep
%setup -q

%build
%configure --datadir=%_gamesdatadir --bindir=%_gamesbindir
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

#install desktop file
mkdir -p %buildroot%_desktopdir
cp %SOURCE1 %buildroot%_desktopdir/

#install icons

install -D %SOURCE3 %buildroot%_miconsdir/%name.png
install -D %SOURCE4 %buildroot%_niconsdir/%name.png
install -D %SOURCE5 %buildroot%_liconsdir/%name.png

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README INSTALL
%_gamesbindir/freedroidRPG
#_man6dir/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_miconsdir/%name.png
%_niconsdir/%name.png

%files data
%_gamesdatadir/%name

%files tools
%_gamesbindir/croppy
%_gamesbindir/pngtoico
%_gamesbindir/explode_atlas
%_gamesbindir/explodefont
%_gamesbindir/gluefont
%_gamesbindir/make_atlas

%changelog
* Sat Jan 07 2012 Roman Savochenko <rom_as@altlinux.ru> 0.15-alt1
- Version 0.15 build for Sisyphus.

* Wed Jan 26 2011 Roman Savochenko <rom_as@altlinux.ru> 0.14.1-alt1
- Version 0.14.1 build for Sisyphus.

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.1
- Rebuilt with python 2.6

* Sun Nov 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt1
- Updated to 0.11.1
- Moved media files to %name-data subpackage
- Removed editor subpackage

* Mon Sep 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.10.3-alt1
- New upstream version.

* Fri Jul 06 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.10.2-alt1
- New upstream version.

* Sun Feb 25 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.10.1-alt1
- New upstream version.

* Mon Jan 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.10.0-alt1
- New upstream version.
- Switched to freedesktop menu.

* Fri Nov 04 2005 Damir Shayhutdinov <damir@altlinux.ru> 0.9.13-alt1
- Initial build for Sisyphus.

