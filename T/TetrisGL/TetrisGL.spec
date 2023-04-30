Name: TetrisGL
Version: 1.0.2
Release: alt5

Summary: Just another tetris game with OpenGL graphics
License: GPLv3
Group: Games/Arcade

Url: http://github.com/BaZzz01010101/TetrisGL
Source0: %name-%version.tar
Source1: TetrisGL-32.png
Source2: TetrisGL-48.png
Source3: TetrisGL-64.png
Source4: TetrisGL-96.png
Source5: TetrisGL-128.png

Patch0: 0001-Add-time.h-in-Crosy.cpp.patch

BuildRequires: cmake rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: libGLEW-devel
BuildRequires: libglfw3-devel
BuildRequires: libglm-devel
BuildRequires: rapidjson
BuildRequires: libfreetype-devel
BuildRequires: libstb-devel
BuildRequires: libalsa-devel

%description
This project has developed for training purposes only.
It has been written in C++ and uses OpenGL to render all graphics.

Ported to Linux/e2k online: http://youtu.be/761Ab1SDZsQ
(see http://github.com/Imp5/TetrisGL)

NB: users must be in the `games' group to play,
care for them not to get stuck!

%prep
%setup

%patch0 -p1

%build
%cmake_insource
%make_build # VERBOSE=1

cat > %name << EOF
#!/bin/sh
exec %_libexecdir/%name/%name
EOF

cat > %name.desktop << EOF
[Desktop Entry]
Name=%name
Comment=Tetris with nifty graphics
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

cp -at . -- %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5

%install
rm -f bin/*.{exe,dll}

mkdir -p %buildroot%_libexecdir/%name
cp -a bin/* %buildroot%_libexecdir/%name

install -D /dev/null %buildroot%_localstatedir/games/%name.scores
ln -srf %buildroot{%_localstatedir/games/%name.scores,%_libexecdir/%name/leaderboard.dat}

install -D bin/settings.dat %buildroot%_localstatedir/games/%name.settings
ln -srf %buildroot{%_localstatedir/games/%name.settings,%_libexecdir/%name/settings.dat}

install -pDm755 ../bin/%name %buildroot%_libexecdir/%name/%name
install -pDm755 %name %buildroot%_bindir/%name

install -pDm644 %name.desktop %buildroot%_desktopdir/%name.desktop

for i in 32 48 64 96 128; do
	install -pDm644 %name-$i.png \
		%buildroot%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done

%files
%doc README.md
%_libexecdir/%name
%attr(0755,root,games) %_bindir/%name
%attr(2711,root,games) %_libexecdir/%name/%name
%attr(0664,root,games) %_localstatedir/games/%name.scores
%attr(0664,root,games) %_localstatedir/games/%name.settings
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop

%changelog
* Sun Apr 30 2023 Artyom Bystrov <arbars@altlinux.org> 1.0.2-alt5
- fix build proccess on modern Sisyphus stack
- fix rights of running script

* Tue Jul 05 2022 Michael Shigorin <mike@altlinux.org> 1.0.2-alt4
- updated to g24aec3e, dropped glfw version hack

* Sat Jan 16 2021 Michael Shigorin <mike@altlinux.org> 1.0.2-alt3
- Imp5: enabled sound (ported from FMOD to ALSA)
- restricted the binary to games group (so it's more obvious)
- added icons

* Wed Jan 13 2021 Michael Shigorin <mike@altlinux.org> 1.0.2-alt2
- added desktop file

* Tue Jan 12 2021 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1
- initial package

