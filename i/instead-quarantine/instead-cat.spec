Name:		instead-quarantine
Version:	0.3.1
Release:	alt1
Group:		Games/Adventure
Summary:	Quarantine -- INSTEAD game (russian)
Summary(ru_RU.UTF-8): Карантин -- игра для INSTEAD
License:	Distributable
Source:		http://instead-games.googlecode.com/files/%name-%version.zip
Packager:	Fr. Br. George <george@altlinux.ru>

BuildArch:	noarch
Requires:	instead

%define		instead %_datadir/instead/games
# Automatically added by buildreq on Mon Jan 04 2010
BuildRequires: unzip

%description
Quarantine -- INSTEAD game

This game is in Russian

%description -l ru_RU.UTF-8 
КАРАНТИН (нелинейный квест)

14 октября 1961 года. 87°52.09 N 147°14.81 E. Секретная дрейфующая полярная станция СП-2. 150 километров от Северного полюса. До начала полярной ночи — 7 дней.

— Эй, Морозов!!! Пойдем на торосы посмотрим.
— Хорошо, сейчас позову Белку и Паровоза...
— Карабин я взял!

Под ногами скрипел снег, мы шли друг за другом осматривать нашу льдину... Вот уже 5 месяцев она носила станцию на себе, и в последнее время начала капризничать. Хорошо, если до конца экспедиции она останется цела...

%prep
%setup -n quarantine

%build

%install
mkdir -p %buildroot%instead
cp -a . %buildroot%instead/quarantine

%files
%instead/quarantine

%changelog
* Tue Jan 19 2010 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Version up

* Mon Jan 11 2010 Fr. Br. George <george@altlinux.ru> 0.2.1-alt1
- Initial build from scratch

