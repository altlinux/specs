Name: chroma
Version: 1.14
Release: alt1
Group: Games/Puzzles
License: GPLv2
Source: %name-%version.tar.bz2
Summary: An abstract colourful puzzle game
Url: http://www.level7.org.uk/chroma/
Packager: Fr. Br. George <george@altlinux.ru>

Requires: %name-data
# Automatically added by buildreq on Tue Sep 06 2011
# optimized out: fontconfig libSDL-devel libtinfo-devel
BuildRequires: ImageMagick-tools libSDL_image-devel libfreetype-devel libncurses-devel zlib-devel

%description
Chroma is an abstract puzzle game. A variety of colourful shapes are arranged in a series of increasingly complex patterns, forming fiendish traps that must be disarmed and mysterious puzzles that must be manipulated in order to give up their subtle secrets. Initially so straightforward that anyone can pick it up and begin to play, yet gradually becoming difficult enough to tax even the brightest of minds.

It features:

    * twenty one levels, ranging from beginner to expert
    * infinite undo and redo capability, as well as replay of solutions
    * a choice of smooth graphics or a minimal, text based version
    * a level editor to allow you to design your own puzzles
    * released under an open source licence, free to play

%package data
Group: Games/Puzzles
License: GPLv2
Summary: Data files for %name abstract colourful puzzle game
%description data
%summary

%prep
%setup

%build
%autoreconf
%configure
%make_build
#convert iconcurses.ico %name-curses.png
convert iconsdl.ico %name-sdl.png
cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Name=Chroma
Comment=An abstract colourful puzzle
Exec=chroma
Categories=Game;LogicGame;
Icon=chroma
@@@

%install
%makeinstall
#install -D %name-curses-1.png %buildroot/%_miconsdir/%name-curses.png
#install -D %name-curses-3.png %buildroot/%_niconsdir/%name-curses.png
#install -D %name-curses-5.png %buildroot/%_liconsdir/%name-curses.png
install -D %name-sdl-1.png %buildroot/%_miconsdir/%name.png
install -D %name-sdl-3.png %buildroot/%_niconsdir/%name.png
install -D %name-sdl-5.png %buildroot/%_liconsdir/%name.png
install -D %name.desktop %buildroot/%_desktopdir/%name.desktop

%files
%doc README
%_bindir/*
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop

%files data
%_datadir/%name

%changelog
* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 1.14-alt1
- Autobuild version bump to 1.14
- As-needed patch implemented by upstream (removed)

* Tue Sep 06 2011 Fr. Br. George <george@altlinux.ru> 1.13-alt2
- Autobuild watchfile added
- Fix build

* Mon Aug 23 2010 Fr. Br. George <george@altlinux.ru> 1.13-alt1
- Version up

* Mon Jul 05 2010 Fr. Br. George <george@altlinux.ru> 1.12-alt1
- Version up

* Wed Mar 24 2010 Fr. Br. George <george@altlinux.ru> 1.10-alt2
- Fix repocop warning

* Fri Mar 12 2010 Fr. Br. George <george@altlinux.ru> 1.10-alt1
- Initial build from scratch

