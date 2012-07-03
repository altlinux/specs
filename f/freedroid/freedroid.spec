Name:		freedroid
Version:	1.0.2
Release:	alt1.qa1
Summary:	A clone of the game "Paradroid"
Group:		Games/Arcade
License:	GPLv2
Source:		%name-%version.tar.gz
Source1:	paraicon.png
URL:		http://www.freedroid.org/
Requires: %name-data = %version

# Automatically added by buildreq on Sun Apr 03 2011
# optimized out: libSDL-devel libX11-devel xorg-xproto-devel zlib-devel
BuildRequires: libSDL_image-devel libSDL_mixer-devel libjpeg-devel libpng-devel libvorbis-devel

%description
FreedroidClassic is a clone of the game "Paradroid" which was released
on Commodore 64 in 1985. In this game, you control a robot located
within an interstellar spaceship consisting of several decks connected
by elevators.

The aim of the game is to destroy all enemy robots by either shooting
them or seizing control over them by creating connections in a short
subgame of electric circuits. The graphics are designed to be a fairly
faithful reproduction of the original game, but a modern set of tiles is
also available.


%package data
BuildArch: noarch
Group: Games/Arcade
Summary: Art and level data for %name game

%description data
%summary

%prep
%setup
sed -i 's/\[vorbis/[vorbisfile/g' configure.ac

cat > %name.desktop <<@@@
[Desktop Entry]
Name=FreeDroid Classics
Comment=%summary
Exec=freedroid
Icon=freedroid
Type=Application
Categories=Game;ArcadeGame;
@@@

%build
%autoreconf
%configure --disable-sdltest --with-x
%make_build

%install
%makeinstall
install -D %SOURCE1 %buildroot/%_niconsdir/%name.png
install -D %name.desktop %buildroot/%_desktopdir/%name.desktop

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%_bindir/*
%_man6dir/*
%_niconsdir/%name.png
%_desktopdir/%name.desktop
%dir %_datadir/%name

%files data
%_datadir/%name/*

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * macos-ds-store-file-in-package for freedroid-data

* Mon Apr 04 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Initial build from scratch

