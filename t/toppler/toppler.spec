Name: toppler
Version: 1.3
Release: alt1

Group: Games/Arcade
Summary: Dangerously ascent of the tower.
Summary(ru_RU.UTF8): Опасное восхождение на башню.
Url: https://gitlab.com/roever/toppler/
License: GPLv3

Source0: %name-%version.tar.gz
Source1: toppler.desktop

Requires: libSDL2 libSDL2_mixer libSDL2_image
BuildRequires: gcc-c++ libSDL2-devel libSDL2_mixer-devel libSDL2_image-devel povray gimp libpng17-devel zlib-devel

ExclusiveArch: x86_64 i586 aarch6

%description
In this game you have to help a cute little green animal switch off some kind of "evil" mechanism.
The "power off switch" is hidden somewhere in high towers. On your way to the target you need to avoid a lot of 
strange robots that guard the tower.

%description -l ru_RU.UTF-8
В этой игре вы должны помочь зеленому животному выключить "злой" механизм. "Выключатель" находится на высокой башне. 
По пути к цели нужно избегать много странных охранников башни.

%prep
%setup -q

%build
%make_build BINDIR=%_gamesbindir DATADIR=%_gamesdatadir/ LOCALEDIR=%_datadir/locale/ \
            MANDIR=%_mandir LOCALSTATEDIR=%_localstatedir/games

%install
%makeinstall \
    BINDIR=%buildroot%_gamesbindir \
    DATADIR=%buildroot%_gamesdatadir \
    LOCALEDIR=%buildroot%_datadir/locale \
    MANDIR=%buildroot%_mandir \
    LOCALSTATEDIR=%buildroot%_localstatedir/games


install -m 755 -d %buildroot%_desktopdir/
install -m 644 %SOURCE1 %buildroot%_desktopdir/%{name}.desktop

install -m 755 -d %buildroot%_datadir/pixmaps/
install -m 644 dist/toppler.xpm %buildroot%_datadir/pixmaps/%{name}.xpm
install -m 644 dist/toppler40.xpm %buildroot%_datadir/pixmaps/%{name}40.xpm

%find_lang %name

%files -f %name.lang
%_gamesbindir/*
%_gamesdatadir/%name/*
%_desktopdir/%{name}.desktop
%_datadir/pixmaps/%{name}.xpm
%_datadir/pixmaps/%{name}40.xpm
%doc %_man6dir/*
%doc AUTHORS COPYING

%changelog
* Mon Jun  6 2022 Alexander Danilov <admsasha@altlinux.org> 1.3-alt1
- new version 1.3

* Sat Jan 04 2014 Evgeny V Shishkov <shev@altlinux.org> 1.1.6-alt1
- new version 1.1.6

