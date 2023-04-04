Name: lbreakouthd
Version: 1.1.2
Release: alt1
Summary: Classic Breakout-Style Game
License: GPLv2+
Group: Games/Arcade
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://lgames.sourceforge.net/LBreakoutHD/
Source: https://downloads.sourceforge.net/project/lgames/%name/%name-%version.tar.gz
Source1: https://sourceforge.net/projects/lgames/files/add-ons/lbreakout2/lbreakout2-levelsets-20160512.tar.gz
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(SDL2_ttf)
BuildRequires: pkgconfig(sdl2)

%description
LBreakoutHD is a scaleable 16:9 remake of LBreakout2, a Breakout-style
arcade game for Linux featuring a number of added graphical enhancements
and effects. You control a paddle at the bottom of the playing field
and must destroy bricks at the top by bouncing balls against them.

%prep
%setup

%build
%configure \
    --bindir=%_gamesbindir \
    --datadir=%_gamesdatadir \
    --localstatedir=%_localstatedir/games
%make_build

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/%name/levels
tar -xf %SOURCE1 -C %buildroot%_datadir/%name/levels

%find_lang %name

%files -f %name.lang
%doc Changelog README TODO
#_datadir/games/icons/lbreakouthd256.gif
%_datadir/games/icons/hicolor/*/apps/lbreakouthd.png
%dir %_datadir/games/%name/themes/
%_datadir/games/%name/themes/*
%dir %_datadir/games/%name/levels/
%dir %_datadir/games/%name/levels/*
%attr(2711,root,games) %_gamesbindir/%name
%_gamesbindir/%name
%_datadir/%name
%_datadir/games/applications/%name.desktop
%attr(664,games,games) %_localstatedir/games/%name.hscr

%changelog
* Tue Apr 04 2023 Ilya Mashkin <oddity@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Dec 29 2022 Ilya Mashkin <oddity@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed Nov 23 2022 Ilya Mashkin <oddity@altlinux.ru> 1.1-alt1
- 1.1

* Sun May 01 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Tue Mar 08 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Sun Feb 13 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.8-alt1
- Initial build
