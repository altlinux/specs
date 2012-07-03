Name:		jag
Version:	0.3.2
Release:	alt2
License:	GPLv3
Group:		Games/Puzzles
Summary:	An arcade-puzzle 2D game to break all of the target blocks
URL:		http://jag.xlabsoft.com
Source:		http://jag.xlabsoft.com/files/%name-%version-src.zip
Source1:	http://jag.xlabsoft.com/files/%name-%version-data.zip
# wget -k -p http://jag.xlabsoft.com/about.php
Source2:	jag.xlabsoft.com-%version.tar

# Automatically added by buildreq on Sun Jul 12 2009
BuildRequires: gcc-c++ libGL-devel libSDL-devel libSDL_mixer-devel libXrandr-devel libXrender-devel libqt4-devel unzip

Requires:	%name-data = %version

%description
JAG is an arcade-puzzle 2D game which runs on Linux and Windows. It is
free and opensource.

The aim of JAG is to break all of the target pieces on each level, and
to do this before the time runs out. Keep doing this until you have
beaten the last level and won the game.

Move game pieces using mouse into matches of 3 or more in a straight
line horizontally or vertically. Doing this on top of the target cells
will break them. The faster targets are removed, the bigger is score.

There are single and double targets. Unlike the single ones, double
targets are removed in two turns.

Some pieces are blocked. Before removing such ones, blocks should be
destroyed. Blocks also can be single or double.

By breaking pieces and targets, you're earning score which can be spent
for applying a special tool. Tools make the life easier as they're
mostly intended for breaking several pieces at a time, including blocks
and targets.

By breaking pieces of the same type, you're also increasing bonus
counters. If you will collect 500 and more items, you can remove all the
same items from the field.

%package data
Group:		Games/Puzzles
Summary:	Data failes for %name, %summary
Buildarch:	noarch
%description data
Data failes for %name, %summary

%prep
%setup -n %name-%version-src
sed -i.orig '
s@/usr/local/bin@%_gamesbindir@g
s@/usr/local/games@%_gamesdatadir@g
s@-lSDLmain@-lSDL -lX11@g
' Game.pro
sed -i.orig 's@/usr/local/games@%_gamesdatadir@' main.cpp
unzip %SOURCE1
mv %name-%version-data/data .
tar xf %SOURCE2

mv jag.xlabsoft.com-%version/about.php jag.xlabsoft.com-%version/index.html

%build
qmake-qt4
%make_build

cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Categories=Game;BlocksGame;
Exec=%name
Icon=%name
Terminal=false
Name=JAG
GenericName=Arcade-puzzle 2D game
Comment=%summary
@@@

%install
%makeinstall INSTALL_ROOT=%buildroot
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -D images/item6.png %buildroot%_liconsdir/%name.png
cp -a data/* %buildroot%_gamesdatadir/%name/

%files
%doc data/help/* jag.xlabsoft.com-%version/*
%_gamesbindir/*
%dir %_gamesdatadir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%files data
%_gamesdatadir/%name/*


%changelog
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 0.3.2-alt2
- DSO list completion

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 0.3.2-alt1
- Version up
- Data package splitted

* Thu Feb 04 2010 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Version up

* Sun Jan 03 2010 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Version up

* Wed Sep 02 2009 Fr. Br. George <george@altlinux.ru> 0.2.5-alt1
- Version up

* Mon Jul 13 2009 Fr. Br. George <george@altlinux.ru> 0.2.3-alt2
 - /usr/local/games hardcoded out

* Sun Jul 12 2009 Fr. Br. George <george@altlinux.ru> 0.2.3-alt1
- Initial build from scratch

