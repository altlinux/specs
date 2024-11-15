%define oname qjoypad
Name: qjoypad-qt5
Version: 4.3.1
Release: alt1

Summary: A joystick-keyboard mapper
Summary(ru_RU.UTF-8): Программа для превращения событий джойстика в события клавиатуры
License: %gpl2only
Group: Games/Other
Url: https://github.com/panzi/qjoypad

Source0: %name-%version.tar

Requires: libqt5-core
Requires(post,postun): desktop-file-utils

# Automatically added by buildreq on Wed Sep 15 2010
BuildRequires(pre): rpm-build-licenses, desktop-file-utils rpm-macros-cmake cmake
BuildRequires: gcc-c++ libX11-devel libXtst-devel qt5-base-devel qt5-tools-devel qt5-x11extras-devel

%description
QJoyPad is a simple Linux/QT program that lets you use your gaming devices
where you want them: in your games! QJoyPad takes input from a gamepad or
joystick and translates it into key strokes or mouse actions, letting you
control any XWindow program with your game controller. QJoyPad also gives
you the advantage of multiple saved layouts so you can have a separate setting
for every game, or for every class of game!

This is a fork of QJoyPad with some small additional features, Qt 5 port and some bug/memory leak fixes.

%description -l ru_RU.UTF-8
QJoyPad -- это простая программа для Linux на Qt, которая позволит наконец
применить ваш джойстик по назначению -- для управления играми! QJoyPad превращает
нажатия на геймпад или джойстик в коды клавиатуры или движения мыши, так что
вы теперь можете управлять с помощью игрового контроллера любой программой для
X Window System. QJoyPad поддерживает несколько вариантов привязок, так что вы
можете хранить разные настройки для каждой игры или типа игр.

Данная программа является форком оригинального QJoyPad, с добавлением некоторых улучшений, переносом на Qt5
и исправлением утечек памяти.

%prep
%setup

%build
%cmake DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc *.txt *.md
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/24x24/apps/%oname.png
%_iconsdir/hicolor/64x64/apps/%oname.png
%_datadir/%oname/translations/*.qm

%changelog
* Fri Oct 11 2024 Artyom Bystrov <arbars@altlinux.org> 4.3.1-alt1
- Initial build for Sisyphus
