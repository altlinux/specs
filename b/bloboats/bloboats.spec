Name:		bloboats
Version:	1.0.2
Release:	alt2
License:	GPLv2
Summary:	Arcade-like boat racing game
Group:		Games/Arcade
Source:		http://bloboats.dy.fi/mirror/bloboats-%version.tar.gz
URL:		http://bloboats.dy.fi/about.php
Requires:	%name-data

# Automatically added by buildreq on Sun Mar 13 2011
BuildRequires: gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libmpc

%description
Bloboats is an arcade-like boat racing game contributing to the Assembly
'06 game development competition in the hybrid spirit of SMB-like
platform jumpers and elasto mania / xmoto like
motocross-I'm-faster-than-you games.

The objective of Bloboats is to reach MS Enterprise as fast as possible
to save it from the hands of the terrible Tentacle Monsters of an
Unknown Master and the same time beat your friend and laugh at his or
her puny time.

%package data
License:	CCSampling+
BuildArch:	noarch
Summary:	Data files for %name (under CC Sampling+ license).
Group:		Games/Arcade

%description data
Data files for %name (under CC Sampling+ license).

%prep
%setup
# GCC6 fix
sed -i 's/ghostfile=false/ghostfile=NULL/' src/menu.cpp

cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Name=BloBoats
Comment=%summary
Exec=%name
Icon=%name
Terminal=false
Categories=Game;ArcadeGame;
@@@

%build
%make_build PREFIX="" DATADIR="%_datadir/%name"

%install
%makeinstall PREFIX=%buildroot DATADIR="%buildroot%_datadir/%name"
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -D data/images/icon.png %buildroot%_niconsdir/%name.png

%files
%_bindir/*
%_sysconfdir/%{name}*
%_desktopdir/%name.desktop
%_niconsdir/%name.png

%files data
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Wed Jan 18 2017 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2
- GCC6 fix

* Sun Mar 13 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Initial build from scratch

