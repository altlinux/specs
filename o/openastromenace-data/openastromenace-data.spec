Name: openastromenace-data
Version: 1.2.0
Release: alt1
Summary: Hardcore 3D space shooter with spaceship upgrade possibilities (artwork).
Summary(ru_RU.KOI8-R): Хардкорный космический 3D шутер с возможностью апгрейда корабля (уровни)
%define sname oamenace
%define cname AstroMenace

Group: Games/Arcade
License: GPL
Url: http://www.viewizard.com/
Source0: http://downloads.sourceforge.net/%name/%sname-data-%version.tar.bz2
Source1: http://downloads.sourceforge.net/%name/%sname-lang-en-%version.tar.bz2
Source2: http://downloads.sourceforge.net/%name/%sname-lang-ru-%version.tar.bz2
Packager: Fr. Br. George <george@altlinux.ru>

%description
Artwork for %cname game (package openastromenace)
 
%description -l ru_RU.KOI8-R
Уровни для игры %cname (пакет openastromenace)

%prep
%setup -cq
tar -xf %SOURCE1
tar -xf %SOURCE2

%build

%install
mkdir -p %buildroot%_gamesdatadir/%cname
cp -a * %buildroot%_gamesdatadir/%cname/

%files
%_gamesdatadir/%cname/*

%changelog
* Sat Oct 20 2007 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Initial build for ALT

