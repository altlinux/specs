Name: gnome-quod
Version: 0.2.3
Release: alt1
Summary: Place pieces on a grid so that they make a square
Group: Games/Puzzles
License: GPL3
Source: %name-%version.tar.bz2

Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Sep 26 2010
BuildRequires: ImageMagick-tools gcc-c++ intltool libgtkmm2-devel librsvg-devel libxml++2-devel

%description
Quod, a game invented by G. Keith Still, has simple rules, but playing well
requires sophisticated strategy. The goal of the game is to place pieces on a
grid so that they make a square. The player who makes a square first wins.
Squares can be any size and orientation, and players have a limited supply of
blocking pieces, which adds to the complexity and interest.

%prep
%setup
sed -i 's/^LF_/# LF_/' configure.ac
for s in 16 32 48 64 128; do convert pixmaps/quod.png -resize ${s}x${s} $s.png; done
%build
%autoreconf
%configure
%make_build

%install
%makeinstall
for s in 16 32 48 64 128; do 
  install -D $s.png %buildroot%_iconsdir/hicolor/${s}x${s}/apps/quod.png
done
%find_lang %name

%files -f %name.lang
%doc README NEWS THANKS
%_bindir/*
%_desktopdir/%name.desktop
%_pixmapsdir/quod.png
%_pixmapsdir/%name
%_iconsdir/hicolor/*/apps/*
%dir %_datadir/%name
%_datadir/%name/*
%_man6dir/*
%changelog
* Sun Sep 26 2010 Fr. Br. George <george@altlinux.ru> 0.2.3-alt1
- Autobuild version bump to 0.2.3

* Sat Nov 29 2008 Fr. Br. George <george@altlinux.ru> 0.1.0-alt1
- Initial build from scratch

