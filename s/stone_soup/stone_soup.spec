Name: stone_soup
Version: 0.10.2
Release: alt1
Summary: Roguelike with tiled and ascii interfaces
License: GPLv2
Group: Games/Adventure
Source: %name-%version-nodeps.tar.xz
Url: http://crawl.develz.org/wordpress/
Patch: stone_soup-0.10.2-throw.patch

Requires: %name-data = %version, %name-tiles = %version

# Automatically added by buildreq on Fri Jul 29 2011
# optimized out: fontconfig libGL-devel libGLU-devel libSDL-devel libstdc++-devel pkg-config zlib-devel
BuildRequires: ImageMagick-tools flex gcc-c++ libSDL_image-devel libfreetype-devel liblua5-devel libpng-devel libsqlite3-devel libncursesw-devel perl-Unicode-Collate

%description
Dungeon Crawl Stone Soup is an open-source, single-player, role-playing
roguelike game of exploration and treasure-hunting in dungeons filled
with dangerous and unfriendly monsters in a quest to rescue the
mystifyingly fabulous Orb of Zot.

%package data
Summary: Data files for %name, %summary
Group: Games/Adventure
BuildArch: noarch
%description data
Data files for %name, %summary

%package tiles
Summary: Tiles for %name, %summary
Group: Games/Adventure
BuildArch: noarch
%description tiles
Tiles for %name, %summary

%package ncurses
Summary: Console version of %name, %summary
Group: Games/Adventure
Requires: %name-data = %version
%description ncurses
Console version of %name, %summary

%prep
%setup
%patch -p1

cat > %name.desktop <<@@@
[Desktop Entry]
Name=Dungeon Crawl Stone Soup
Comment=Single-player role-playing roguelike game
Icon=%name
Exec=crawl-tiled
Terminal=false
Categories=Game;RolePlaying;
Type=Application
@@@

for N in 16 24 32; do
  convert source/dat/tiles/stone_soup_icon-32x32.png -resize ${N}x${N} $N.png
done

for N in 64 128 192 256; do
  convert source/dat/tiles/stone_soup_icon-512x512.png -resize ${N}x${N} $N.png
done
rm -f source/.cflags

%build
cd source
%make_build DATADIR=%_datadir/%name/ SAVEDIR=~/.crawl/
mv crawl ..
make clean
rm -f .cflags
%make_build TILES=1 DATADIR=%_datadir/%name/ SAVEDIR=~/.crawl/

%install
for N in [1-9]*.png; do
  S=${N%%.*}
  install -D $N %buildroot/%_iconsdir/hicolor/${S}x${S}/apps/%name.png
done

install -D %name.desktop %buildroot%_desktopdir/%name.desktop

cd source
%makeinstall TILES=1 DATADIR=share/%name/ SAVEDIR=~/.crawl/
mv %buildroot/%_bindir/crawl %buildroot/%_bindir/crawl-tiled
install ../crawl %buildroot/%_bindir/crawl

%files
%_bindir/crawl-tiled
%_iconsdir/hicolor/*/*/*.png
%_desktopdir/*.desktop

%files data
%dir %_datadir/%name
%exclude %_datadir/%name/dat/tiles
%_datadir/%name/*

%files tiles
%_datadir/%name/dat/tiles

%files ncurses
%_bindir/crawl

%changelog
* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 0.10.2-alt1
- Autobuild version bump to 0.10.2
- Fix build

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 0.9.2-alt1
- Autobuild version bump to 0.9.2

* Wed Sep 07 2011 Fr. Br. George <george@altlinux.ru> 0.9.1-alt1
- Autobuild version bump to 0.9.1

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 0.9.0-alt1
- Autobuild version bump to 0.9.0
- Fix ncurses dependense typo

* Fri Jul 29 2011 Fr. Br. George <george@altlinux.ru> 0.8.1-alt2
- Separate tiled and ncurses versions

* Fri Jul 29 2011 Fr. Br. George <george@altlinux.ru> 0.8.1-alt1
- Autobuild version bump to 0.8.1
- Desktop file added
- Noarch part separated

* Fri Jul 29 2011 Fr. Br. George <george@altlinux.ru> 0.8.0-alt1
- Initial 'zero version' build from scratch

