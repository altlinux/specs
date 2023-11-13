%define _name BlockOutII

Name: blockout2
Version: 2.5
Release: alt2.1

Summary: 3D Tetris game
Summary(ru_RU.UTF-8): Трехмерный вариант игры Тетрис
License: GPL-2.0-or-later
Group: Games/Arcade
Url: http://www.blockout.net/blockout2/

Source: http://downloads.sourceforge.net/blockout/bl25-src.tar.gz
Source1: http://downloads.sourceforge.net/blockout/bl25-linux-x86.tar.gz
Source2: %name.desktop
Source3: %name-512x512-2.svg

# fc patches
Patch0: %_name-2.3-syslibs.patch
Patch1: %_name-2.3-bl2Home.patch
Patch2: %_name-2.3-restore-resolution.patch
Patch3: %_name-2.3-libpng15.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1037001
Patch4: %_name-2.3-format-security.patch

Requires: %name-data = %version-%release

BuildRequires: gcc-c++ libSDL-devel libSDL_mixer-devel
BuildRequires: libpng-devel zlib-devel libalsa-devel
BuildRequires: %_bindir/convert desktop-file-utils dos2unix

%description
BlockOut II is a free adaptation of the original BlockOut DOS game
edited by California Dreams in 1989. BlockOut II has the same
features than the original game with few graphic improvements.
The score calculation is also nearly similar to the original game.
BlockOut II has been designed by an addicted player for addicted
players. BlockOut II is an open source project available for
both Windows and Linux.

%description -l ru_RU.UTF-8
BlockOut II является свободным клоном игры BlockOut для DOS,
выпущенной California Dreams в 1989 году. BlockOut II содержит
все возможности классической игры и улучшенную графику.
Подсчет очков также похож на оригинальную игру.

%package data
Group: Games/Arcade
Summary: Data files for BlockOut II
Summary(ru_RU.UTF-8): Данные для BlockOut II
BuildArch: noarch

%description data
BlockOut II is a free adaptation of the original BlockOut DOS game
edited by California Dreams in 1989. BlockOut II has the same
features than the original game with few graphic improvements.
The score calculation is also nearly similar to the original game.
BlockOut II has been designed by an addicted player for addicted
players. BlockOut II is an open source project available for
both Windows and Linux.

This package provides arch-independent data for BlockOut II.

%description -l ru_RU.UTF-8 data
BlockOut II является свободным клоном игры BlockOut для DOS,
выпущенной California Dreams в 1989 году. BlockOut II содержит
все возможности классической игры и улучшенную графику.
Подсчет очков также похож на оригинальную игру.


%prep
%setup -n BL_SRC -a1
cp %SOURCE2 .
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

dos2unix BlockOut/README.txt

# Remove bundled libraries
rm -rf ImageLib/src/png/{png,zlib}

%build
pushd ImageLib/src
%make_build CFLAGS="$RPM_OPT_FLAGS -Dlinux -c" \
    CXXFLAGS="$RPM_OPT_FLAGS -Dlinux -c"
popd

pushd BlockOut
%make_build \
    CXXFLAGS="$RPM_OPT_FLAGS -Dlinux `sdl-config --cflags` -I../ImageLib/src -c" \
    ADD_LIBS="-L../ImageLib/src -limagelib -lpng -lz"
popd

for r in 16 32 48; do
convert -scale $r BlockOut/block_icon.ico %_name-"$r"x"$r".png
done

%install
mkdir -p %buildroot{%_bindir,%_desktopdir,%_datadir/%name/{images,sounds}}
install -m 755 BlockOut/blockout %buildroot%_bindir/%name
install -p -m 644 blockout/images/* %buildroot%_datadir/%name/images
install -p -m 644 blockout/sounds/* %buildroot%_datadir/%name/sounds

desktop-file-install --dir %buildroot%_desktopdir %SOURCE2
mkdir -p %buildroot%_datadir/icons/hicolor/{16x16,32x32,48x48,scalable}/apps
install -p -m644 %SOURCE3 \
  %buildroot%_iconsdir/hicolor/scalable/apps/%_name.svg

#install -p -m 644 %_name-16x16.png \
#  %buildroot%_datadir/icons/hicolor/16x16/apps/%_name.png
#install -p -m 644 %_name-32x32.png \
#  %buildroot%_datadir/icons/hicolor/32x32/apps/%_name.png
#install -p -m 644 %_name-48x48.png \
#  %buildroot%_datadir/icons/hicolor/48x48/apps/%_name.png

%files
%_bindir/*
%doc BlockOut/README.txt

%files data
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/icons/hicolor/scalable/apps/%_name.svg

%changelog
* Mon Nov 13 2023 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt2.1
- installed automatically converted from block_icon.ico svg icon
- fixed License tag

* Fri Mar 30 2018 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt2
- new noarch -data subpackage
- removed wrapper, fixed bl2Home in bl2Home.patch
- replaced ImageMagick builddep by /usr/bin/convert
- updated desktop-file
- TODO: symbolic icon (GraphicsMagick bug)
- TODO: appdata.xml

* Sat Nov 29 2014 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- 2.5
- applied fc patchset

* Tue Mar 29 2011 Denis Kirienko <dk@altlinux.ru> 2.4-alt4
- Removed dependency to libmesa-devel

* Sun Nov 23 2008 Denis Kirienko <dk@altlinux.ru> 2.4-alt3
- Spec cleanup

* Tue Jan 15 2008 Denis Kirienko <dk@altlinux.ru> 2.4-alt2
- Fixed description
- Fixed bug with wrong dates at x86_64

* Sat Jan 12 2008 Denis Kirienko <dk@altlinux.ru> 2.4-alt1
- First build for Sisyphus
