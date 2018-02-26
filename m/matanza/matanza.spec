Name: matanza
Version: 0.13
Release: alt2.1

Summary:	Multiplayer console space game
Summary(ru_RU.KOI8-R): Многопользовательская консольная космическая игра
Copyright:	GPL
Group:		Games/Arcade
URL:		http://bachue.com/matanza
Source:		%name-%version.tar.gz
Source1: 	%{name}_menu
Source2: 	%{name}server_menu
Requires:       telnet

%description
Matanza is a multiplayer game. In it, every player controls a ship cruising
in space, aiming to destroy the other players (and, eventually, ships
controled by the computer).
By the way, it is pronounced MATANGA, not Matanza.
Currently, the only way to play is through telnet.

%description -l ru_RU.KOI8-R
Matanza --- многопользовательская игра, в которой каждый игрок управляет
космическим кораблём, стараясь уничтожить корабли других игроков (и при
случае корабли, управляемые компьютером). Между прочим, название игры
произносится как МАТАНГА, не Матанза. В настоящее время единственный способ
игры --- через подключение с помощью telnet.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

# not used
install -pD -m644 %SOURCE1 %buildroot%_menudir/%name
install -pD -m644 %SOURCE2 %buildroot%_menudir/%{name}server

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/matanza
%_bindir/matanza-ai

%changelog
* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2.1
- NMU: spec cleanup, get rid of deprecated macros

* Thu May 20 2004 Denis Ovsienko <pilot@altlinux.ru> 0.13-alt2
- Russian tags
- disabled menu files for better security
- less garbage in docs

* Sun Aug 03 2003 Denis Ovsienko <pilot@altlinux.ru> 0.13-alt1.1
- Fixed menu files and telnet dependency.

* Sun Aug 03 2003 Denis Ovsienko <pilot@altlinux.ru> 0.13-alt1.0
- Initial Sisyphus build
