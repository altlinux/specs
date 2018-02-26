Name: netherearth
Version: 0.52
Release: alt2.qa1
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: NetherEarth is a first RTS initially wrote for ZX-Spectrum
Summary(ru_RU.UTF-8): NetherEarth - это первая стратегия для ZX-Spectrum

# Permission to distribute the game is granted by author.
# See forum http://www.braingames.getput.com/forum/forum_posts.asp?TID=192&PN=1
License: distributable
Group: Games/Strategy
Url: http://www.braingames.getput.com/nether/

# http://www.braingames.getput.com/nether/sources.zip
Source0: %name-%version.tar
Source1: %name-%version-data.tar
Source2: %name.run
Source3: %name-%version-doc.tar
Source4: %{name}32.png
Source5: %{name}48.png

Patch: %name-%version-alt.patch

# Automatically added by buildreq on Sun Feb 01 2009
BuildRequires: gcc-c++ libglut-devel libSDL-devel libSDL_mixer-devel
BuildRequires: desktop-file-utils

%description
As in almost all strategy games, the goal is to eliminate the enemy.
To achieve it, you have WARBASES, that have the ability to produce
ROBOTS (your combat units). You can design your own robots by combining
several pieces (TRACKS, ANTIGRAVITATIONAL DEVICE, CANNONS, MISSILE
BAYS, etc). To build robots you need RESOURCE points.

%description -l ru_RU.UTF-8
Как и в других стратегиях, смысл заключается в уничтожении врагов.
Для этого вас есть БАЗЫ, выпускающие РОБОТОВ (ваши боевые единицы).
Можно конструировать различные виды роботов, комбинируя имеющиеся
запчасти (ГУСЕНИЦЫ, ПЛАТФОРМЫ, ПУШКИ, РАКЕТЫ и т.д.). Чтобы собирать
роботов, также нужны РЕСУРСЫ.

%prep
%setup -q -a3
%patch -p1
sed -e 's,@DATADIR@,%_datadir,g; s,@BINDIR@,%_x11bindir,g' %SOURCE2 > %name.run

%build
%make_build

%install
install -D -m755 nether_earth %buildroot%_x11bindir/%name
install -D -m755 %name.run %buildroot%_x11bindir/%name.run
install -D -m644 %SOURCE4 %buildroot%_niconsdir/%name.png
install -D -m644 %SOURCE5 %buildroot%_liconsdir/%name.png

# Menu entry
mkdir -p %buildroot%_desktopdir
cat >%buildroot%_desktopdir/%name.desktop<<EOF
[Desktop Entry]
Name=NetherEarth
Comment=ZX Spectrum game remake
GenericName=A real-time strategy
Exec=%name.run
Terminal=false
Type=Application
Icon=%name
Categories=Game
EOF

mkdir -p %buildroot%_datadir/%name
tar xf %SOURCE1 -C %buildroot%_datadir/%name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=StrategyGame \
	%buildroot%_desktopdir/netherearth.desktop

%files
%doc html/*
%doc %_datadir/%name/readme.txt
%_x11bindir/%name
%_x11bindir/%name.run
%_datadir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_niconsdir/%name.png


%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.52-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for netherearth

* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.52-alt2
- fix build

* Sun Feb 01 2009 Grigory Batalov <bga@altlinux.ru> 0.52-alt1
- New upstream release.
- Specfile recreated.
- Manual was added.

* Wed Apr 30 2003 Kuznecov Ilya <kuznecov@blok-caf.ru> 0.41-kuznecov1
- build for ALTLinux
