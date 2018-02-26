Name:		infector
Version:	0.4
Release:	alt2
Group:		Games/Puzzles
Summary:	Simple, clean implementation of the board games Ataxx and Hexxagon
License:	GPLv3
Source:		http://infector.mangobrain.co.uk/downloads/%name-%version.tar.gz
Patch:		%name-0.2-memory.patch
Packager: Fr. Br. George <george@altlinux.ru>
BuildRequires:	xdg-utils
# Automatically added by buildreq on Thu Mar 12 2009
BuildRequires: gcc-c++ intltool libglademm-devel

%description
Infector is a simple, clean implementation of the board games Ataxx and Hexxagon. It features support for two or four players (two only on hexagonal boards), a rudimentary AI  player, and network play. Currently it has only been built and tested on Linux and Windows.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
# FIX
cp -rp "$HOME/.local/"* %buildroot/usr/
sed -i 's/=.*buildroot/=/' %buildroot%_desktopdir/%name.desktop
%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.*
%_desktopdir/%name.desktop

%changelog
* Thu Jan 21 2010 Fr. Br. George <george@altlinux.ru> 0.4-alt2
- Fix desktop file Exec path

* Thu Oct 08 2009 Fr. Br. George <george@altlinux.ru> 0.4-alt1
- Version up

* Thu Mar 12 2009 Fr. Br. George <george@altlinux.ru> 0.2-alt1
- Initial build from scratch

