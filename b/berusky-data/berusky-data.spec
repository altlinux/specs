%define game_name berusky

Name:      berusky-data
Version:   1.7
Release:   alt1
Summary:   A datafile for Berusky
License:   GPL
Group:     Games/Other
Source:    http://www.anakreon.cz/download/berusky/tar.gz/%{name}-%{version}.tar.gz
URL:       http://www.anakreon.cz/
BuildArch: noarch

%description
A datafile for Berusky. Berusky is a 2D logic game based on an ancient 
puzzle named Sokoban.

An old idea of moving boxes in a maze has been expanded with new logic 
items such as explosives, stones, special gates and so on. 
In addition, up to five bugs can cooperate and be controlled by the player.

This package contains a data for the game, i.e. files with graphics, levels,
game rules and configuration.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%game_name

mv GameData %buildroot%_datadir/%game_name
mv Graphics %buildroot%_datadir/%game_name
mv Levels   %buildroot%_datadir/%game_name
mv README   %buildroot%_datadir/%game_name
mv COPYING  %buildroot%_datadir/%game_name

%files
%_datadir/%game_name/*

%changelog
* Tue Jun 05 2018 Grigory Ustinov <grenka@altlinux.org> 1.7-alt1
- Build new version.

* Mon Mar 02 2009 Dmitriy Kulik  <lnkvisitor@altlinux.org> 1.0-alt1
- Build for ALT Linux Sisyphus

* Fri Apr 20 2007 Martin Stransky <stransky@redhat.com> 1.0-1
- initial build
