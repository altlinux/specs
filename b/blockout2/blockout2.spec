%define _name BlockOutII

Name: blockout2
Version: 2.5
Release: alt1

Summary: 3D Tetris game
Summary(ru_RU.UTF-8): Трехмерный вариант игры Тетрис

License: GPL
Group: Games/Arcade
Url: http://www.blockout.net/blockout2/
Packager: Denis Kirienko <dk@altlinux.ru>

Source: http://downloads.sourceforge.net/blockout/bl25-src.tar.gz
Source1: http://downloads.sourceforge.net/blockout/bl25-linux-x86.tar.gz
Source2: %name.sh
Source3: %name.desktop

# fc patches
Patch0: %_name-2.3-syslibs.patch
Patch1: %_name-2.3-bl2Home.patch
Patch2: %_name-2.3-restore-resolution.patch
Patch3: %_name-2.3-libpng15.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1037001
Patch4: %_name-2.3-format-security.patch

BuildRequires: gcc-c++ libSDL-devel libSDL_mixer-devel
BuildRequires: libpng-devel zlib-devel libalsa-devel
BuildRequires: ImageMagick desktop-file-utils dos2unix

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

%prep
%setup -n BL_SRC -a1
cp %SOURCE2 %SOURCE3 .
%patch0 -p1
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

dos2unix BlockOut/README.txt

# Remove bundled png library
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

convert BlockOut/block_icon.ico %_name.png

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name/images
mkdir -p %buildroot%_datadir/%name/sounds

install -m 755 BlockOut/blockout %buildroot%_bindir/%name.bin
install -m 755 -D %name.sh %buildroot%_bindir/%name
install -p -m 644 blockout/images/* %buildroot%_datadir/%name/images
install -p -m 644 blockout/sounds/* %buildroot%_datadir/%name/sounds

mkdir -p %buildroot%_datadir/applications
desktop-file-install --dir %buildroot%_datadir/applications %SOURCE3
mkdir -p %buildroot%_datadir/icons/hicolor/16x16/apps
mkdir -p %buildroot%_datadir/icons/hicolor/32x32/apps
mkdir -p %buildroot%_datadir/icons/hicolor/48x48/apps
install -p -m 644 %_name-1.png \
  %buildroot%_datadir/icons/hicolor/16x16/apps/%_name.png
install -p -m 644 %_name-0.png \
  %buildroot%_datadir/icons/hicolor/32x32/apps/%_name.png
install -p -m 644 %_name-2.png \
  %buildroot%_datadir/icons/hicolor/48x48/apps/%_name.png

%files
%_bindir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%_name.png
%doc BlockOut/README.txt

%changelog
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
