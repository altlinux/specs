Name: stone_soup
Version: 0.18.1
Release: alt1.1
%define Sum Roguelike with tiled and ascii interfaces
Summary: %Sum
License: GPLv2
Group: Games/Adventure
Source: %name-%version.tar.gz
Url: http://crawl.develz.org/wordpress/

Requires: %name-data = %version, %name-tiles = %version

# Automatically added by buildreq on Wed Apr 22 2015
# optimized out: fontconfig libGL-devel libSDL2-devel libcloog-isl4 libncurses-devel libstdc++-devel libtinfo-devel pkg-config zlib-devel
BuildRequires: ImageMagick-tools flex fonts-ttf-dejavu gcc-c++ git-core libGLU-devel libSDL2_image-devel libfreetype-devel lua5.1-devel libncursesw-devel libpng-devel libsqlite3-devel perl-Unicode-Collate

BuildRequires: fonts-ttf-dejavu

%description
Dungeon Crawl Stone Soup is an open-source, single-player, role-playing
roguelike game of exploration and treasure-hunting in dungeons filled
with dangerous and unfriendly monsters in a quest to rescue the
mystifyingly fabulous Orb of Zot.

%package data
Summary: Data files for %name, %Sum
Group: Games/Adventure
BuildArch: noarch
%description data
Data files for %name, %Sum

%package tiles
Summary: Tiles for %name, %Sum
Group: Games/Adventure
BuildArch: noarch
%description tiles
Tiles for %name, %Sum

%package ncurses
Summary: Console version of %name, %Sum
Group: Games/Adventure
Requires: %name-data = %version
%description ncurses
Console version of %name, %Sum

%prep
%setup

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

echo %version > crawl-ref/source/util/release_ver

for N in 16 24 32; do
  convert crawl-ref/source/dat/tiles/stone_soup_icon-32x32.png -resize ${N}x${N} $N.png
done

for N in 64 128 192 256; do
  convert crawl-ref/source/dat/tiles/stone_soup_icon-512x512.png -resize ${N}x${N} $N.png
done

sed -i 's/install: all/install:/' crawl-ref/source/Makefile

%build
cd crawl-ref/source
find . -name .cflags -exec rm {} \;
%make_build DATADIR=%_datadir/%name/ SAVEDIR=~/.crawl/
mv crawl ..

make clean
find . -name .cflags -exec rm {} \;
%make_build TILES=1 DATADIR=%_datadir/%name/ SAVEDIR=~/.crawl/

%install
for N in [1-9]*.png; do
  S=${N%%.*}
  install -D $N %buildroot/%_iconsdir/hicolor/${S}x${S}/apps/%name.png
done

install -D %name.desktop %buildroot%_desktopdir/%name.desktop

cd crawl-ref/source
%makeinstall TILES=1 DATADIR=share/%name/ SAVEDIR=~/.crawl/ STRIP=touch
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
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.18.1-alt1.1
- NMU: rebuild with new lua

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.18.1-alt1
- Autobuild version bump to 0.18.1

* Thu Dec 24 2015 Fr. Br. George <george@altlinux.ru> 0.17.1-alt1
- Autobuild version bump to 0.17.1

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 0.17.0-alt1
- Autobuild version bump to 0.17.0

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 0.16.1-alt1
- Autobuild version bump to 0.16.1
- Fix build and req (switch to SDL2)

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 0.15.2-alt1
- Autobuild version bump to 0.15.2

* Tue Sep 30 2014 Fr. Br. George <george@altlinux.ru> 0.15.1-alt1
- Autobuild version bump to 0.15.1
- Drop unused patch

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 0.14.1-alt1
- Autobuild version bump to 0.14.1

* Thu Apr 24 2014 Fr. Br. George <george@altlinux.ru> 0.14.0-alt1
- Autobuild version bump to 0.14.0

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 0.13.2-alt1
- Autobuild version bump to 0.13.2

* Thu Feb 20 2014 Fr. Br. George <george@altlinux.ru> 0.13.1-alt1
- Autobuild version bump to 0.13.1
- Fix patch

* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 0.12.3-alt1
- Autobuild version bump to 0.12.3

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 0.12.1-alt1
- Autobuild version bump to 0.12.1
- Fix build

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 0.11.2-alt1
- Autobuild version bump to 0.11.2

* Tue Oct 23 2012 Fr. Br. George <george@altlinux.ru> 0.11.0-alt1
- Autobuild version bump to 0.11.0

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 0.10.3-alt1
- Autobuild version bump to 0.10.3

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

