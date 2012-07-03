Name: Transcend
Version: 0.3
Release: alt4
Summary: Transcend can best be described as retro-style, abstract, 2D shooter
License: GPL
Group: Games/Arcade
Url: http://transcend.sourceforge.net/
Packager: Fr. Br. George <george@altlinux.ru>
Source0: %{name}_%{version}_UnixSource.tar.gz
Source1: %name.png

# Automatically added by buildreq on Tue Apr 05 2011
# optimized out: libGL-devel libGLU-devel libX11-devel libXext-devel libstdc++-devel
BuildRequires: gcc-c++ libXi-devel libXmu-devel libfreeglut-devel

BuildRequires: desktop-file-utils

%description
Transcend can best be described as retro-style, abstract, 2D shooter. The graphics are geometrical, and the pace is sometimes frenzied.

Two features set Transcend apart from other games. First, its dynamic graphical engine, which can smoothly morph from one complex shape to another, produces striking displays. Combining these dynamic shapes with subtle randomizations makes each play through a Transcend level visually different from the last. The second novel feature is Transcend's musical power-up system. As you play through a level, you are simultaneously assembling an abstract visual collage and arranging a unique piece of music. Transcend merges video games with pure art - it can be viewed either as a game or as a multimedia sculpture.

%prep
%setup -q -n %{name}_%{version}_UnixSource

%build
echo 1 | ./runToBuild

%install
install -dm 755 %buildroot%_bindir
install -dm 755 %buildroot%_gamesbindir
install -m 755 %{name}App %buildroot%_gamesbindir/

install -dm 755 %buildroot%_datadir/%name
cp -r levels %buildroot%_datadir/%name

# startscript
cat > %name.sh <<EOF
#! /bin/bash
if [ ! -e \$HOME/.%name ]; then
	mkdir -p \$HOME/.%name
	cd \$HOME/.%name
	ln -s %_datadir/%name/levels .
fi

cd \$HOME/.%name
%_gamesbindir/%{name}App
EOF
install -m 755 %name.sh \
	%buildroot%_bindir/%name

# icon
install -dm 755 %buildroot%_datadir/pixmaps
install -m 644 %SOURCE1 \
	%buildroot%_datadir/pixmaps/%name.png

install -dm 755 %buildroot/%_datadir/applications
cat > %name.desktop << EOF
[Desktop Entry]
Type=Application
Comment=Cultivation is a game about the interactions within a gardening community
Terminal=false
Exec=%name
Icon=%name
Name=%name
Encoding=UTF-8
Categories=Game;ArcadeGame;
EOF
desktop-file-install --dir=%buildroot%_datadir/applications %name.desktop --vendor=""

%files
%doc %name/doc/*
%_gamesbindir/%{name}App
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/applications/*.desktop
%_datadir/pixmaps/*.png

%changelog
* Tue Apr 05 2011 Fr. Br. George <george@altlinux.ru> 0.3-alt4
- Forbidden requires eliminated

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3-alt3.1
- NMU:
  * updated build dependencies

* Sat Sep 27 2008 Fr. Br. George <george@altlinux.ru> 0.3-alt3
- Build fix

* Sun Sep 23 2007 Fr. Br. George <george@altlinux.ru> 0.3-alt2
- Desktop file fixed

* Sat Sep 22 2007 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build for ALT

* Sat Sep 22 2007 Fr. Br. George <george@altlinux.ru> 8-alt1
- Initial build for ALT
