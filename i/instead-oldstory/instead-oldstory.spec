Name:		instead-oldstory
Version:	0.4.2
Release:	alt1
Group:		Games/Adventure
Summary:	An old story -- INSTEAD game (russian)
Summary(ru_RU.UTF-8): Одна старая история -- игра для INSTEAD
License:	Distributable
Source:		http://instead-games.googlecode.com/files/%name-%version.zip
Packager:	Fr. Br. George <george@altlinux.ru>

BuildArch:	noarch
Requires:	instead

%define		instead %_datadir/instead/games
# Automatically added by buildreq on Mon Jan 04 2010
BuildRequires: unzip

%description
An old story -- INSTEAD game

This game is in Russian

%description -l ru_RU.UTF-8 
Эта история началась в последний день лета. С утра лил проливной дождь, и я просидел у окна до самого вечера, разглядывая капли на стекле. Накануне я получил приглашение из института со странным названием ВНИЗ. В приглашении сообщалось, что мои достижения в области реверсирования сознания очень заинтересовали руководство института, и мне предлагаются все условия для работы в стенах ВНИЗ, включая заманчивую зарплату.

Не скрою, предложение было своевременным, дела мои шли не важно, тематика моих работ мало кого интересовала. Но что-то мешало мне сразу ответить на письмо. Я медлил. Сейчас, когда все пережитое осталось в прошлом, я понимаю, что это странное ноющее ощущение в душе называется предчувствием.

%prep
%setup -n oldstory

%build

%install
mkdir -p %buildroot%instead
cp -a . %buildroot%instead/oldstory

%files
%instead/oldstory

%changelog
* Tue Jan 05 2010 Fr. Br. George <george@altlinux.ru> 0.4.2-alt1
- Initial build from scratch

