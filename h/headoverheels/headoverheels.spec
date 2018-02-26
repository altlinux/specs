Name:		headoverheels
Summary:	Remake of the classical game of the 80's
Version:	1.0.1
Release:	alt1
Source:		http://www.headoverheels2.com/descargas/%name-%version.tar.bz2
Source1:	%name-icons.tar.bz2
Url:		http://www.headoverheels2.com/
Requires:	%name-data = %version

Group: Games/Arcade
License: GPL

# Automatically added by buildreq on Thu Jun 14 2012
# optimized out: libogg-devel libstdc++-devel libvorbis-devel libxerces-c28
BuildRequires: gcc-c++ liballegro-devel libxerces-c28-devel

%description
Remake of the classical "Head Over Heels" game of the 80's.

%package data
Group:		Games/Arcade
Summary:	Level files and music for %name
BuildArch:	noarch

%description data
Level files and music for %name

%prep
%setup -a 1
sed -i  's/^AM_LDFLAGS =/LIBS =/' src/Makefile.am

cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Name=Head Over Heels
Comment=%summary
Icon=%name
Exec=%name
Categories=Game;ArcadeGame;
Terminal=false
@@@

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

# icon
install -D -m 644 %{name}48.png %buildroot%_liconsdir/%name.png
install -D -m 644 %{name}32.png %buildroot%_niconsdir/%name.png
install -D -m 644 %{name}16.png %buildroot%_miconsdir/%name.png

install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/headoverheels
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_desktopdir/%name.desktop

%files data
%dir %_datadir/headoverheels
%_datadir/headoverheels/*

%changelog
* Fri Jun 15 2012 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from upstream spec

