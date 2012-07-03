Name: instead-cat
Version: 1.6
Release: alt1
Group: Games/Adventure
Summary: The return of the quantum cat -- INSTEAD game (russian)
Summary(ru_RU.UTF-8): Возвращение квантового кота -- игра для INSTEAD
License: Distributable
Source: %name-%version.zip
Packager: Fr. Br. George <george@altlinux.ru>
Url: http://instead-games.googlecode.com

BuildArch: noarch
Requires: instead

%define instead %_datadir/instead/games
# Automatically added by buildreq on Mon Jan 04 2010
BuildRequires: unzip

%description
The return of the quantum cat -- INSTEAD game

%description -l ru_RU.UTF-8
ВОЗВРАЩЕНИЕ КВАНТОВОГО КОТА

За окном моей хижины снова белеет снег, а в камине также как и тогда потрескивают дрова... Третья зима. Прошло уже две зимы, но те события, о которых я хочу рассказать, встают перед моими глазами так, словно это было вчера...

Я работал лесником уже больше десяти лет. Больше десяти лет я жил в своей хижине, окруженной лесом, собирая капканы браконьеров и выезжая раз в одну или две недели в близлежащий поселок... После воскресной службы в местной церкви я заходил в магазинчик и покупал необходимые мне вещи: патроны к дробовику, крупу, хлеб, лекарства...

Когда-то я был неплохим компьютерным специалистом... Впрочем, это уже не важно... Десять лет я не видел экрана монитора, и не жалею об этом.

Теперь я понимаю, что корни того, что тогда произошло лежат давно -- во второй половине 30-х... Хотя лучше начать все по-порядку...

%prep
%setup -n cat

%build
%install
mkdir -p %buildroot%instead
cp -a . %buildroot%instead/cat

%files
%instead/cat

%changelog
* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Autobuild version bump to 1.6

* Fri Sep 09 2011 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Autobuild version bump to 1.5

* Wed Sep 01 2010 Fr. Br. George <george@altlinux.ru> 1.3-alt2
- Homepage URL added

* Wed Aug 18 2010 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Version up

* Tue Jan 19 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Version up

* Mon Jan 11 2010 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Version up

* Mon Jan 04 2010 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build from scratch
