Name: pushover
Url: http://pushover.sourceforge.net/
License: GPL
Group: Games/Puzzles
Version: 0.0.3
Release: alt1
Summary: Puzzle with ant pushing dominoes to fall
Source: %name-%version.tar.gz
Source1: %name.png
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Nov 16 2008
BuildRequires: gcc-c++ libSDL-devel libSDL_mixer-devel libSDL_ttf-devel liblua5-devel libpng-devel

Requires: %name-themes = %version

%description
Pushover is a fun puzzle game originally published by Ocean in 1992. In this game you control an ant that can walk along platformt that are connected with ladders. On those platforms are dominos that need to fall according to some rules.

    * All dominos must fall and none must crash into another
    * One special domino must fall as last domino and that domino triggers the exit door to open when you enter the exit door the level has been completed
    * You may rearrange as many dominos as you want, except for the trigger. You may not place dominos in front of the doors, except for the vanishing domino.
    * You may push push once to start a chain reaction with the dominos leading to the fall of all of them
    * All this has to be done within a time limit (which is normally generous)
    * There are 10 different dominos that behave differently when pushed, some fall, some not, some wait a bit before they fall, some raise, some toppler until they meet an obstacle
    * There is a help in the game and introductory levels that show how all the dominos work
%package themes
License: GPL
Group: Games/Puzzles
Summary: Theme files for %name package
buildArch: noarch

%description themes
Pushover is a fun puzzle game originally published by Ocean in 1992. In this game you control an ant that can walk along platformt that are connected with ladders. On those platforms are dominos that need to fall according to some rules.

This package provides theme files for %name

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall
mkdir -p %buildroot%_desktopdir %buildroot%_datadir/pixmaps
cat > %name.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Pushover
Comment=Ant pushing dominoes puzzle game
Exec=%name
Icon=%name
Categories=Game;LogicGame;
EOF
install -m 644 %name.desktop %buildroot%_desktopdir
install -m 644 %SOURCE1 %buildroot%_datadir/pixmaps
%find_lang %name

%files -f %name.lang
%doc readme.txt AUTHORS
%_bindir/%name
%_datadir/%name/
%exclude %_datadir/%name/themes/*
%_desktopdir/%name.desktop
%_datadir/pixmaps/%name.png

%files themes
%_datadir/%name/themes/*

%changelog
* Sat May 14 2011 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Autobuild version bump to 0.0.3

* Sun Dec 20 2009 Fr. Br. George <george@altlinux.ru> 0.0.2-alt1
- Version up
- Themes noarch package split

* Mon Nov 17 2008 Fr. Br. George <george@altlinux.ru> 0.0.1-alt1
- Initial build from scratch

