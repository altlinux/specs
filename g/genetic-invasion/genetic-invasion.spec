Name: genetic-invasion
Version: 0.4.1
Release: alt1.1
Summary: A tower defence game with enemy genetic adaptation
License: GPLv3
Group: Games/Arcade
# git://haxx.es/genetic-invasion.git
Source: %name-%version.tar
Requires: %name-data

BuildRequires:	libgomp-devel

# Automatically added by buildreq on Tue Sep 06 2011
# optimized out: cmake-modules libGL-devel libGLU-devel libgomp-devel libstdc++-devel
BuildRequires: cmake gcc-c++ libeo-devel libsfml-devel

%description
GeneticInvasion is a tower defence game under a free license.

What makes it different from all the tower defences you've played so far
is that is uses genetic algorithm to make the enemies evolve.
No more scripted increasing difficulty system.

The enemies adapt themselves.
You improve your defence, they are going stronger.
You have a minefield to protect you, they begin to fly.
You build a whole lot of anti-air turret, they stop flying.
You can guess how that ends : you lose.

%package data
Group: Games/Arcade
License: CC-BY-SA
BuildArch: noarch
Summary: Data files and music for %name
%description data
Data files and music for %name

%prep
%setup
cat > %name.sh <<@@@
#!/bin/sh
mkdir -p "\$HOME/.%name"
cd "\$HOME/.%name"
test -d data || { rm -f data; ln -s %_gamesdatadir/%name/data .; }
%_gamesbindir/%name.bin
@@@

%build
%cmake
(
cd BUILD
%make_build
)

%install
install -D BUILD/bin/GeneticInvasion %buildroot%_gamesbindir/%name.bin
install -m755 -D %name.sh %buildroot%_gamesbindir/%name

mkdir -p %buildroot%_gamesdatadir/%name
cp -a data %buildroot%_gamesdatadir/%name/

%files
%_gamesbindir/*

%files data
%_gamesdatadir/%name

%changelog
* Tue Jun 19 2012 Fr. Br. George <george@altlinux.ru> 0.4.1-alt1.1
- Fix funny libgomp misversion

* Wed Sep 07 2011 Fr. Br. George <george@altlinux.ru> 0.4.1-alt1
- Autobuild version bump to 0.4.1

* Wed Sep 07 2011 Fr. Br. George <george@altlinux.ru> 0.4-alt1
- Setting build scheme

