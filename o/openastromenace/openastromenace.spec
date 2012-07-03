Name: openastromenace
%define stamp 080519
Version: 1.2.%stamp
Release: alt7
Summary: Hardcore 3D space shooter with spaceship upgrade possibilities.
Summary(ru_RU.KOI8-R): Хардкорный космический 3D шутер с возможностью апгрейда корабля
%define sname oamenace
%define cname AstroMenace

Group: Games/Arcade
License: GPL
Url: http://www.viewizard.com/
#Source: http://www.viewizard.com/download/%{cname}SourceCode_%stamp.zip
Source: http://www.viewizard.com/download/%{cname}SourceCode_%stamp.tar
Source1: %cname.sh
Source2: icon.tar
#Source: http://downloads.sourceforge.net/%name/%sname-src-%version.tar.bz2
Packager: Fr. Br. George <george@altlinux.ru>
Patch: %name-1.2.080519-alt-glext-include-fix.patch

Requires: %name-data

# Automatically added by buildreq on Tue Mar 09 2010
BuildRequires: cmake gcc-c++ libGL-devel libSDL-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXext-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libalut-devel libjpeg-devel libvorbis-devel libxkbfile-devel xorg-xf86vidmodeproto-devel

%description
AstroMenace stands out for a hardcore gameplay that absorbs you completely as you repel the relentless attacks of diverse adversaries and dodge hails of projectiles. During the game, you will face many cunning opponents, having unique tactics and strategies and trying to give you a rough time in their own peculiar way, so youll need all your quick-wits to evade their attacks.
 
To demonstrate the pre-eminence against growing forces of evil you will have to constantly improve your ship and armaments. The game offers you to collect money during the battle, so you can purchase new weaponry and equipment, choosing from a diverse list. You can carry out the destruction with your favorite guns, switching between them whenever you want.
 
AstroMenace is graphically unique. The quality of animation along with special effects is stunning, and with all its picturesque backgrounds adding brilliance to the visuals, the game is a true eye-candy. The process of causing total annihilation has never looked so fascinating!
 
%description -l ru_RU.KOI8-R
Космический вертикальный шутер очень высокого качества. Все модели отрисованы в 3D и отображаются в перспективе. Отличные обои, хорошая музыка, продуманный геймплей. Сложность игры гибко настраивается.

Поначалу разработка игры велась закрыто. С версии 1.2.0 распространяется под GPL v3.

%prep
%setup -q -n %{cname}SourceCode
%patch

%build

cmake .
sed -i '/^[/#]*define [A-Z][A-Z][ ]*$/d;/#if !defined(EN) && !defined(DE) && !defined(RU)/a\
#define RU
' AstroMenaceSource/Defines.h
%make_build
mv %cname %name.ru
sed -i '/^[/#]*define [A-Z][A-Z][ ]*$/d;/#if !defined(EN) && !defined(DE) && !defined(RU)/a\
#define EN
' AstroMenaceSource/Defines.h
%make_build
mv %cname %name.en

cat > %name.desktop << EOF
[Desktop Entry]
Type=Application
Comment=3D space shooter
Terminal=false
Exec=%cname
Icon=%name
Name=%name
Encoding=UTF-8
Categories=Game;ArcadeGame;
EOF

tar xf %SOURCE2

%install
install -Ds -m755 %name.ru %buildroot%_gamesbindir/%cname.ru
install -Ds -m755 %name.en %buildroot%_gamesbindir/%cname.en
install -D -m755 %SOURCE1 %buildroot%_gamesbindir/%cname
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
for n in 32 48 64 128; do \
  install -D icon/astromenace_$n.png \
    %buildroot%_iconsdir/hicolor/$n''x$n/apps/%name.png; \
done

mkdir -p %buildroot%_gamesdatadir/%cname

%files
%doc ReadMe.txt
%dir %_gamesdatadir/%cname
%_gamesbindir/%{cname}*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
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

