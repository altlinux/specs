%define rev	41700116
Name: populate
Version: 0.0.0
Release: alt1.%rev
Summary: The game logic is written in vala and cairo
Summary(ru_RU.UTF-8): Логическая игра, написанная на vala и cairo
Group: Games/Puzzles
License: GPLv3
Url: https://github.com/alsoijw/populate.git
Packager: Anton Midyukov <antohami@altlinux.org>

Source0: %name-%version.tar
Source1: %name.desktop
Source2: %name-16x16.png
Source3: %name-32x32.png
Source4: %name-48x48.png
Patch1: libgee0.8-fix.patch
BuildRequires: vala libgtk+3-devel libgee0.8-devel

%description
Description: the playing field is made up of hexagons. You can choose any of
your hexagons (they have a green color) by clicking the left mouse button.
Adjacent free cells will be highlighted. Then click the left mouse button over
one of them. Now this cell is yours, and all rival's adjacent hexagons will
become yours too. Similarly you can lose your cells during AI's turn. The main
goal is to take as many hexagons as you can. The game is over once all hexagons
are occupied.

%description -l ru_RU.UTF-8
Поле состоит из шестигранников. Вы можите выбрать любой свой шестигранник (ваши
шестигранники зелёного цвета), щелкнув по нему левой кнопкой. Свободные ячейки
рядом с ним будут подсвечены. Кликните по любой из них левой кнопкой. Вы заняли
эту ячейку. Все ячейки противника рядом с ней станут вашими. И наоборот, ваши
ячейки перейдут к врагу если он займёт шестигранник рядом с вашими ячейками.
Ваша задача занять как можно больше шестигранников. Как только все шестигранники
будут заняты игра прекратится.

%prep
%setup -q
%patch1 -p1

%build
#make_build 
./do make

%install
#makeinstall_std
install -Dp -m0755 %name %buildroot%_bindir/%name
install -Dp -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -Dp -m0644 %SOURCE2 %buildroot%_miconsdir/%name.png
install -Dp -m0644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -Dp -m0644 %SOURCE4 %buildroot%_liconsdir/%name.png

%files
%_bindir/%name
%_desktopdir/*
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*

%changelog
* Thu Dec 24 2015 Anton Midyukov <antohami@altlinux.org> 0.0.0-alt1.41700116
- Initial build for ALT Linux Sisyphus.
