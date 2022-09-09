Name: nbsdgames
Version: 5
Release: alt1

Summary: Popular set of 18 modern console games
Summary(ru_RU.UTF-8): Популярный набор из 18 современных консольных игр

License: CC0-1.0
Group: Games/Other
Url: https://github.com/abakh/nbsdgames

# Source-url: https://github.com/abakh/nbsdgames/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: libncurses-devel
BuildRequires: /usr/bin/convert

%description
A collection of 18 console games for sysadmins who are bored at work.
The collection includes: Jewels (Game with Tetris-like gameplay), Sudoku,
Mines (Sapper), Reversi, Checkers, Battleship, SOS, Rabbit Hole (A maze
exploration game in which you have to collect items from all over the maze
instead of reaching the end.), Pipes (like the famous Pipe Mania), Fifteen,
Memoblocks (A similar game was included in Windows 7), Fisher, Mancher,
Miketron, Redsquare (Conway's Game of Life is now playable!), Darrt (with
original gameplay!), Serpent duel, Tugow (number pad training game).

%description -l ru_RU.UTF-8
Сборник из 18 консольных игр для сисадминов, которым скучно на работе.
Коллекция включает в себя: Jewels (Игра с геймплеем, похожим на тетрис),
Sudoku, Mines (Сапер), Reversi, Checkers, Battleship, SOS, Rabbit Hole
(Игра про исследование лабиринта, в которой вам нужно собирать предметы со
всего лабиринта, а не доходить до конца.), Pipes (как и знаменитая Pipe Mania),
Fifteen, Memoblocks (Похожая игра была включена в Windows 7), Fisher, Mancher,
Miketron, Redsquare (Игра жизни Конвея стала играбельной!), Darrt (
с оригинальным геймплеем!), Serpent duel, Tugow (тренировочная игра с цифровой
клавиатурой).

%prep
%setup

# Key "Encoding" is outdated, remove it
sed -i "/Encoding=UTF-8/d" nbsdgames.desktop

%build
%make_build

%install
mkdir -p %buildroot{%_bindir,%_man6dir}
%makeinstall_std \
    manpages \
    GAMES_DIR=%buildroot%_bindir \
    MAN_DIR=%buildroot%_man6dir

install -D %name.desktop %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 %name.svg %buildroot%_miconsdir/%name.png
convert -resize 32x32 %name.svg %buildroot%_niconsdir/%name.png
convert -resize 48x48 %name.svg %buildroot%_liconsdir/%name.png

%files
%doc README.md
%_bindir/*
%_desktopdir/%name.desktop
%_man6dir/*.xz
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Thu Sep 08 2022 Evgeny Chuck <koi@altlinux.org> 5-alt1
- new version (5) with rpmgs script
- initial build for ALT Linux Sisyphus

