%define rname	yandexbar
%define version 6.5
%define release alt1
%define cid 	yasearch@yandex.ru
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release: 	%release

Summary:	YandexBar plugin for Firefox
Summary(ru_RU.UTF-8):Расширение Яндекс.Бар для Firefox

License:	Yandex (proprioritary)
Group:		Networking/WWW
URL:		http://bar.yandex.ru/firefox/
BuildArch:	noarch

Source0:	http://download.yandex.ru/bar/firefox/%rname-%version.xpi

Packager:	Ilya Mashkin <oddity@altlinux.ru>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:	unzip

%description
YandexBar is an extension for Mozilla-Firefox thats allow
to easily use Yandex services. 

%description -l ru_RU.UTF-8
Яндекс.Бар — это расширение для браузера Mozilla Firefox, 
которое встраивается в ваш браузер в виде дополнительной 
панели инструментов.

Что умеет Яндекс.Бар:
* Производить удобный и быстрый поиск прямо из Firefox
* Отображать информацию о погоде и пробках
* Отображать информацию о новых событиях на сервисах Ядекса,
  таких как почта, Мой Круг или Яндекс Фотки.
* ... и многое многое другое.

Помимо этого, в Яндекс Бар входит набор полезных инструментов, 
таких как:
    * Визуальные закладки — в один клик откроют любимые сайты; 
    * Подсветка найденного — выделит искомые слова; 
    * Проверка орфографии — не даст ошибиться; 
    * Отзывы — покажут мнения пользователей о сайтах.

%prep
%setup -c

%install
%__mkdir_p %buildroot/%ciddir
unzip -qq -d %buildroot/%ciddir %SOURCE0

%postun
if [ "$1" = 0 ]; then
    [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Wed Feb 08 2012 Ilya Mashkin <oddity@altlinux.ru> 6.5-alt1
- 6.5

* Thu Oct 27 2011 Ilya Mashkin <oddity@altlinux.ru> 6.0-alt1
- 6.0

* Mon Aug 22 2011 Radik Usupov <radik@altlinux.org> 5.3.0-alt2
- Special version for ALTLinux

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 5.3.0-alt1
- New release (5.3.0).

* Fri Apr 08 2011 Radik Usupov <radik@altlinux.org> 5.2.3-alt1
- New release for ALTLinux (5.2.3)
- New packager

* Tue Jan 26 2010 Alexey Gladkov <legion@altlinux.ru> 4.3-alt1
- New release (4.3).

* Tue Sep 22 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.2-alt1
- First build for Sisyphus.


