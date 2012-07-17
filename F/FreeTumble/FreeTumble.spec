Name:		FreeTumble
Version:	1.0
Release:	alt1.1
Summary:	Remove same color stones zones to prevent the stones to reach the top
Group:		Games/Puzzles
License:	GPLv3
URL:		http://sourceforge.net/projects/freetumble/
Source:		%{name}V%{version}_src.tar.gz
Source1:	%{name}V%{version}_Linux32.tar.gz
Source2:	%name.png
Patch:    FreeTumble-1.0-alt-gcc4.6.patch
Requires:	%name-data

# Automatically added by buildreq on Sun Jun 05 2011
# optimized out: libGL-devel libGLU-devel libstdc++-devel python-base python-modules python-modules-compiler python-modules-email
BuildRequires: gcc-c++ libsfml-devel scons

%description
FreeTumble is a free multi-platform puzzle game, developed in c++ with
sfml.It features 3 different game modes, the player has to remove same
color stones zones, in order to prevent the stones to reach the top, or
to clear the entire grid.

%package data
Summary: Data files for %name
Group: Games/Puzzles
BuildArch: noarch
%description data
Data files for %name, %summary

%package music
Summary: Music files for %name
Group: Games/Puzzles
License: CC-BY-NC-SA
BuildArch: noarch
%description music
Music files for %name, %summary.
Note this files are for non-commercial use only.
Licensed under CC-BY-NC-SA 2.5 and 3.0

%prep
%setup -n %name
%patch -p2

cat > %name.sh <<@@@
#!/bin/sh
D="\$HOME/.local/share/%name"

test -d "" || {
mkdir -p "\$D/data"
ln -s /usr/share/games/%name/data/media "\$D/data"
cp /usr/share/games/%name/data/game.ini "\$D/data/game.ini"
ln -s /var/lib/games/%name/* "\$D/data"
ln -s /usr/games/%name.bin "\$D/%name"
}
cd "\$D"
./%name
@@@

cat > %name.desktop <<@@@
[Desktop Entry]
Version=1.0
Type=Application
Name=%name
Comment=%summary
Exec=%name
Categories=Game;BlocksGame;
Icon=%name
@@@

tar xf %SOURCE1
mv %name .%name

%build
scons

%install
install -Ds %name %buildroot%_gamesbindir/%name.bin
install -D %name.sh %buildroot%_gamesbindir/%name
mkdir -p %buildroot%_localstatedir/games/%name
mkdir -p %buildroot%_gamesdatadir/%name
cp -r .%name/data %buildroot%_gamesdatadir/%name/
install .%name/data/reset_scores.dat .%name/data/scores.dat %buildroot%_localstatedir/games/%name/
install -D %SOURCE2 %buildroot%_liconsdir/%name.png
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc README
%dir %_gamesdatadir/%name
%dir %_gamesdatadir/%name/data
%dir %_localstatedir/games/%name
%attr(2711,root,games) %_gamesbindir/%name.bin
%attr(755,root,games) %_gamesbindir/%name
%attr(664,root,games) %_localstatedir/games/%name/scores.dat
%attr(644,root,games) %_localstatedir/games/%name/reset_scores.dat
%_localstatedir/games/%name/reset_scores.dat
%_gamesdatadir/%name/data/[^m]*
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%files data
%_gamesdatadir/%name/data/media
%dir %_gamesdatadir/%name/data/media/music
%exclude %_gamesdatadir/%name/data/media/music/*

%files music
%_gamesdatadir/%name/data/media/music

%changelog
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Fixed build

* Mon Jun 06 2011 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build from scratch

