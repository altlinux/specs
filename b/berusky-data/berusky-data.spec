%define game_name berusky

Summary:   A datafile for Berusky
Name:      berusky-data
Version:   1.0
Release:   alt1
License:   GPL
Group:     Games/Other
Source:    http://www.anakreon.cz/download/berusky/tar.gz/%{name}-%{version}.tar.gz
URL:       http://www.anakreon.cz/
BuildArch: noarch
Packager:  Dmitriy Kulik <lnkvisitor@altlinux.org>

%description
A datafile for Berusky. Berusky is a 2D logic game based on an ancient 
puzzle named Sokoban.

An old idea of moving boxes in a maze has been expanded with new logic 
items such as explosives, stones, special gates and so on. 
In addition, up to five bugs can cooperate and be controlled by the player.

This package contains a data for the game, i.e. files with graphics, levels,
game rules and configuration.

%prep
%setup -q -n %name-%version

%install
mkdir -p %buildroot%_datadir/%game_name

mv GameData %buildroot%_datadir/%game_name
mv Graphics %buildroot%_datadir/%game_name
mv Levels   %buildroot%_datadir/%game_name
mv README   %buildroot%_datadir/%game_name
mv COPYING  %buildroot%_datadir/%game_name

mkdir -p %buildroot/var/games/%game_name
install -m 644 berusky.ini %buildroot/var/games/%game_name

%files
%defattr(-, root, root)
%_datadir/%game_name/*
/var/games/%game_name/*

%changelog
* Mon Mar 02 2009 Dmitriy Kulik  <lnkvisitor@altlinux.org> 1.0-alt1
- Build for ALT Linux Sisyphus

* Fri Apr 20 2007 Martin Stransky <stransky@redhat.com> 1.0-1
- initial build
