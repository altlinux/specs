Name: bjs
Version: 0.1.3
Release: alt3
Summary: 3D tank battle
License: GPLv2
Group: Games/Arcade
Url: http://bjs.sourceforge.net/
Source: %name-%version.tar.gz

# Automatically added by buildreq on Wed Jan 05 2011
BuildRequires: cegui06-devel gcc-c++ zlib-devel libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libfreetype-devel liblua5-devel libomniORB-devel libopenal-devel python-modules

%description
BJS is a funny arcade 3D multiplayer tank battle. It is fuly playable and very
fun in multiplayer. Of course the single player is also possible.
The goal of the game is just to create a good time for players ;-) There is no story.
You just get tank and go shooting other players. Currently we are having 5 different
tanks, 6 maps, 9 powerups and 4 weapons.

%prep
%setup -q
#rm -rf src/libs/{SDL_gfx,freealut,glew,ode-0.7,tinyxml}
#find . -type f -print0 | xargs -r0 subst "s|tinyxml/tinyxml.h|tinyxml.h|g"
subst "s|lua5.1|lua|g" Makefile
subst "s|CEGUI-OPENGL|CEGUI-OPENGL-0.6|g" Makefile
sed -i '/Icon/s/.png//g' misc/bjs.desktop

%build
make idl
%make_build

%install
%make install DESTDIR=%buildroot/usr

%files
%doc NEWS
%_bindir/*
%_man6dir/*
%_pixmapsdir/*
%_desktopdir/*
%_datadir/games/%name

%changelog
* Sat Sep 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.3-alt3
- Fix build

* Sun Jul 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.3-alt2
- Fix build

* Wed Jan 05 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.3-alt1
- Build for ALT
