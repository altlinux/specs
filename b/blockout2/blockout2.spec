Name: blockout2
Version: 2.4
Release: alt4

Summary: 3D Tetris game
Summary(ru_RU.UTF-8): Трехмерный вариант игры Тетрис

License: GPL
Group: Games/Arcade
Url: http://www.blockout.net/blockout2/
Packager: Denis Kirienko <dk@altlinux.ru>

Source0: bl24-src-linux-i586.tar.gz
Source1: %name.sh
Source2: %name.desktop
Patch0: %name-%version-alt-build.patch
Patch1: %name-%version-alt-x86_64.patch

BuildPreReq: libSDL-devel libSDL_mixer-devel gcc-c++

%description
BlockOut II is a free adaptation of the original BlockOut DOS game
edited by California Dreams in 1989. BlockOut II has the same
features than the original game with few graphic improvements.
The score calculation is also nearly similar to the original game.
BlockOut II has been designed by an addicted player for addicted
players. BlockOut II is an open source project available for
both Windows and Linux.

%description -l ru_RU.UTF-8
BlockOut II является свободным клоном игры BlockOut для DOS,
выпущенной California Dreams в 1989 году. BlockOut II содержит
все возможности классической игры и улучшенную графику.
Подсчет очков также похож на оригинальную игру.

%prep
%setup -q -n bl24_lin_src
cp %SOURCE1 %SOURCE2 .
patch -p1 -l -i %PATCH0
%ifarch x86_64
patch -p1 -l -i %PATCH1
%endif

%build
cd ImageLib/src
make
cd ../../BlockOut
make

%install
install -d %buildroot%_datadir/%name/images/
install  BlockOut/images/* %buildroot%_datadir/%name/images/
install -d %buildroot%_datadir/%name/sounds/
install  BlockOut/sounds/* %buildroot%_datadir/%name/sounds/
install -m 755 -D %name.sh %buildroot%_bindir/%name
install -m 755 -D BlockOut/blockout %buildroot%_bindir/%name.bin
install -m 644 -D %name.desktop %buildroot%_datadir/applications/%name.desktop

%files
%_bindir/*
%_datadir/%name
%_datadir/applications/%name.desktop

%changelog
* Tue Mar 29 2011 Denis Kirienko <dk@altlinux.ru> 2.4-alt4
- Removed dependency to libmesa-devel

* Sun Nov 23 2008 Denis Kirienko <dk@altlinux.ru> 2.4-alt3
- Spec cleanup

* Tue Jan 15 2008 Denis Kirienko <dk@altlinux.ru> 2.4-alt2
- Fixed description
- Fixed bug with wrong dates at x86_64

* Sat Jan 12 2008 Denis Kirienko <dk@altlinux.ru> 2.4-alt1
- First build for Sisyphus
