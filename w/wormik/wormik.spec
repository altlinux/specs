Name: wormik
Version: 1.0
Release: alt1.qa4
Summary: Wormik is simple snake-type game
Copyright: GPL
Group: Games/Arcade
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://atrey.karlin.mff.cuni.cz/~rat/wormik/
Source: wormik-1.0.tar.gz
Source2: %name.png

Requires: freefont-fonts-ttf

# Automatically added by buildreq on Mon Jul 12 2004 (-bi)
BuildRequires: esound freetype2 gcc-c++ libSDL-devel libSDL_image-devel libSDL_ttf-devel libpng-devel libstdc++-devel zlib-devel

%description
Wormik is an implementation of the classic worm game.
The player must collect food, which makes the worm grow.
The only interesting anomaly is that it can eat itself.

%prep
%setup -qn %name
%__subst "s/courbd.ttf/FreeMonoBold.ttf/" gui_sdl.cxx

%build
%__make

%install
mkdir -p %buildroot%_gamesbindir %buildroot%_gamesdatadir/%name
install -m 755 %name %buildroot%_gamesbindir/
install -m 644 %{name}_*.png %buildroot%_gamesdatadir/%name/
mkdir -p %buildroot%_niconsdir
install -m 644 %SOURCE2 %buildroot%_niconsdir/

#menu support
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Wormik
Comment=Wormik - simple snake-type game
Icon=%{name}
Exec=%_gamesbindir/%name
#Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF


%files
%_gamesbindir/%name
%_gamesdatadir/%name/*
%_desktopdir/%{name}.desktop
%_niconsdir/%name.png

%changelog
* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1.qa4
- NMU: converted debian menu to freedesktop

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0-alt1.2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for wormik
  * update_menus for wormik
  * postclean-05-filetriggers for spec file

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 1.0-alt1.2
- rebuild
- update requires

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Jul 12 2004 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Initial release for Sisyphus

