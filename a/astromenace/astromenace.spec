Name: astromenace
Version: 1.4.1
Release: alt2
Summary: Hardcore 3D space shooter with spaceship upgrade possibilities
Summary(ru_RU.UTF-8): Хардкорный космический 3D шутер с возможностью апгрейда корабля
%define cname AstroMenace

Group: Games/Arcade
License: GPLv3
Url: http://www.viewizard.com/
Source: %name-%version.tar.gz
Source1: icon.tar
Patch: %name-1.4.1-alt-gl-include-fix.patch
Provides: openastromenace
Obsoletes: openastromenace

Requires: %name-data

# Automatically added by buildreq on Thu Oct 14 2021
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libfreetype-devel libglvnd-devel libgpg-error libogg-devel libopenal-devel libsasl2-3 libstdc++-devel python3 python3-base sh4
BuildRequires: cmake gcc-c++ libGLU-devel libSDL2-devel libalut-devel libvorbis-devel

BuildRequires: libfreetype-devel

%description
AstroMenace stands out for a hardcore gameplay that absorbs you
completely as you repel the relentless attacks of diverse adversaries
and dodge hails of projectiles. During the game, you will face many
cunning opponents, having unique tactics and strategies and trying to
give you a rough time in their own peculiar way, so youll need all your
quick-wits to evade their attacks.

To demonstrate the pre-eminence against growing forces of evil you will
have to constantly improve your ship and armaments. The game offers you
to collect money during the battle, so you can purchase new weaponry and
equipment, choosing from a diverse list. You can carry out the
destruction with your favorite guns, switching between them whenever you
want.

AstroMenace is graphically unique. The quality of animation along with
special effects is stunning, and with all its picturesque backgrounds
adding brilliance to the visuals, the game is a true eye-candy. The
process of causing total annihilation has never looked so fascinating!

%description -l ru_RU.UTF-8
Космический вертикальный шутер очень высокого качества. Все модели
отрисованы в 3D и отображаются в перспективе. Отличные обои, хорошая
музыка, продуманный геймплей. Сложность игры гибко настраивается.

Поначалу разработка игры велась закрыто.
С версии 1.2.0 распространяется под GPL v3.

%package data
License: CC-BY-NC-SA-4.0
Group: Games/Arcade
Summary: Data files for %name
Summary(ru_RU.UTF-8): Файлы с данными для %name
BuildArch: noarch
Provides: openastromenace-data
Obsoletes: openastromenace-data
%description data
Data files for %name
%description -l ru_RU.UTF-8 data
Файлы с данными для %name

%prep
%setup -a1
%patch -p1

cat > %name.sh << EOF
#!/bin/sh
%_gamesbindir/%name.bin --dir=%_gamesdatadir/%name
EOF

cat > %name.desktop << EOF
[Desktop Entry]
Type=Application
Comment=3D space shooter
Comment=Космический 3D шутер
Terminal=false
Exec=%_gamesbindir/%name
Icon=%name
Name=%name
Encoding=UTF-8
Categories=Game;ArcadeGame;
EOF

%build
%cmake
%cmake_build

%install
install -D -m755 %_cmake__builddir/%name %buildroot%_gamesbindir/%name.bin
install -D -m755 %name.sh %buildroot%_gamesbindir/%name

install -D %name.desktop %buildroot%_desktopdir/%name.desktop
for n in 32 48 64 128; do \
  install -D icon/astromenace_$n.png \
    %buildroot%_iconsdir/hicolor/$n''x$n/apps/%name.png; \
done

install -D %_cmake__builddir/gamedata.vfs %buildroot%_gamesdatadir/%name/gamedata.vfs

%files
%doc *.md docs
%dir %_gamesdatadir/%name
%_gamesbindir/%{name}*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%files data
%_gamesdatadir/%name/*

%changelog
* Mon Jul  3 2023 Artyom Bystrov <arbars@altlinux.org> 1.4.1-alt2
- Fix build on GCC13

* Fri Oct 15 2021 Fr. Br. George <george@altlinux.ru> 1.4.1-alt1
- Autobuild version bump to 1.4.1

* Tue Jul 16 2013 Fr. Br. George <george@altlinux.ru> 1.3.2-alt1
- Autobuild version bump to 1.3.2

* Sat Mar 23 2013 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Autobuild version bump to 1.3.1
- Drop "open" prefix, so free version is maintained by developer now
- Fix patch

* Wed Oct 24 2012 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0
- Upstream switch back to SF
- Join separated data package

* Tue Mar 09 2010 Fr. Br. George <george@altlinux.ru> 1.2.080519-alt7
- Fix openal to libalut dependency change

* Sat Dec 12 2009 Fr. Br. George <george@altlinux.ru> 1.2.080519-alt6
- Fix new GCC buld (by iv@)

* Fri Dec 11 2009 Fr. Br. George <george@altlinux.ru> 1.2.080519-alt5
- Minor desktop file fix (closes #22227)

* Sat Mar 21 2009 Fr. Br. George <george@altlinux.ru> 1.2.080519-alt4
- Stub for get higher than 5.0

* Sat Mar 21 2009 Fr. Br. George <george@altlinux.ru> 1.2.080519-alt3
- Add desktop file

* Fri May 30 2008 Fr. Br. George <george@altlinux.ru> 1.2.080519-alt2
- Do stupid locale-depended build

* Tue May 27 2008 Fr. Br. George <george@altlinux.ru> 1.2.080519-alt1
- Version up

* Fri Apr 11 2008 Fr. Br. George <george@altlinux.ru> 1.2.080115-alt1
- Update to 080115
- Change upstream back to viewizard (from SF)

* Sat Oct 20 2007 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Initial build for ALT

