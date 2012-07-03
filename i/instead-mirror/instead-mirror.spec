Name:		instead-mirror
Version:	0.4.1
Release:	alt1
Group:		Games/Adventure
Summary:	Mirror -- INSTEAD game (russian)
Summary(ru_RU.UTF-8): Зеркало -- игра для INSTEAD
License:	Distributable
Source:		http://instead-games.googlecode.com/files/%name-%version.zip
Packager:	Fr. Br. George <george@altlinux.ru>

BuildArch:	noarch
Requires:	instead

%define		instead %_datadir/instead/games
# Automatically added by buildreq on Mon Jan 04 2010
BuildRequires: unzip

%description
Mirror -- INSTEAD game

This game is in Russian

%description -l ru_RU.UTF-8 
Авторы оригинальной игры «ЗЕРКАЛО» для ZX Spectrum — творческая группа Art Work:
Коды и музыка — Пасечник И. А.
Сценарий и графика — Степанов В. Ю.
Адаптация для INSTEAD — Вадим В. Балашов.
vvb.backup@rambler.ru
Автор выражает огромную признательность Петру Косых за INSTEAD и неоценимую помощь, оказанную при разработке кода.

%prep
%setup -n mirror

%build

%install
mkdir -p %buildroot%instead
cp -a . %buildroot%instead/mirror

%files
%instead/mirror

%changelog
* Mon Jan 11 2010 Fr. Br. George <george@altlinux.ru> 0.4.1-alt1
- Version up

* Tue Jan 05 2010 Fr. Br. George <george@altlinux.ru> 0,4-alt1
- Initial build from scratch

