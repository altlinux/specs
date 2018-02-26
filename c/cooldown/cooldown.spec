Name:		cooldown
# svn info cooldown | sed -n 's/Revision: *//p'
Version:	24
Release:	alt1
Summary:	Advanced PipeMania clone
Group:		Games/Arcade
# svn checkout http://cooldown-game.googlecode.com/svn/trunk cooldown
Source:		%name-%version.tar
Source1:	%{name}4.png
Patch:		%name-linux.patch
License:	GPLv3
URL:		http://cooldown-game.googlecode.com

Requires:	%name-data == %version, %name-font

# Automatically added by buildreq on Fri Sep 03 2010
BuildRequires: ImageMagick-tools cmake gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel

%description
This game was inspired by the old game PipeMania, although it changed
a lot during development. Cooldown is created as an entry for Pandora
Angst Coding Competition 2010, but the development doesn't stop at the
deadline ;)

Your task is to cool down the ball coming from the start field. 100
levels, increasing difficulty, pipes in 4 colors, special tiles,
multiple balls.

%package data
Summary: CC-BY data for %name game
License: CC-BY
Group:	Games/Arcade

%description data
CC-BY data for %name game

%package font
Summary: Distributable non-free font for %name game
License: Distributable
Group:	Games/Arcade

%description font
Distributable non-free font for %name game

%prep
%setup
%patch -p1

find . -depth -name .svn -exec rm -rf {} \;
sed -i 's|@DATADIR@|%_gamesdatadir/%name|' src/main.cpp

cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Name=Cooldown
GenericName=Pipe connetcting game
Comment=%summary
Categories=Game;ArcadeGame;
Exec=%_gamesbindir/%name
Icon=%name
@@@

for N in 128x128 24x24 64x64 32x32 48x48; do
convert %SOURCE1 -resize $N $N.png; done

%build
mkdir build
cd build
cmake .. -DCMAKE_SKIP_RPATH:BOOL=yes \
            -DCMAKE_BUILD_TYPE=MinSizeRel \
            -DCMAKE_C_FLAGS:STRING='-pipe -Wall -O2' \
            -DCMAKE_CXX_FLAGS:STRING='-pipe -Wall -O2' \
            -DCMAKE_INSTALL_PREFIX=/usr \
            -DLIB_DESTINATION=lib64 \
            %if "lib64" == "lib64" 
            -DLIB_SUFFIX="64"
            %else 
            -DLIB_SUFFIX=""
            %endif 

%make_build

%install
for N in *x*.png; do
  install -D $N %buildroot%_iconsdir/hicolor/${N%%.*}/apps/%name.png
done
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

cd build
mkdir -p %buildroot%_gamesdatadir/%name
for N in ../data/*; do cp -a `basename $N` %buildroot%_gamesdatadir/%name/; done
install -D %name %buildroot%_gamesbindir/%name

%files
%doc [^C]*.txt* 
%_gamesbindir/%name
%dir %_gamesdatadir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop

%files data
%_gamesdatadir/%name/[^f]*

%files font
%_gamesdatadir/%name/fonts

%changelog
* Fri Sep 03 2010 Fr. Br. George <george@altlinux.ru> 24-alt1
- Initial build from scratch

