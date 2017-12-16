# SPEC file for FoxyProxy Firefox extension

%define rname	foxyproxy_standard
%define version	6.1.9
%define release alt1
%define cid 	foxyproxy@eric.h.jung
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	advanced proxy management tool
Summary(ru_RU.UTF-8):	расширенная утилита управления настройками прокси-серверов

License:	%gpl2plus
Group:		Networking/WWW
#URL:		http://getfoxyproxy.org/
URL:		https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/
BuildArch:	noarch

Source0:	%rname-%version.xpi

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description
Firefox extension FoxyProxy Standard is an advanced proxy
management tool that completely replaces Firefox's proxy
configuration. FoxyProxy Standard offers multiple proxies
support, allows to define which proxy to use (or none!)
for arbitrary URLs using wildcards, regular expression
and other conveniences, includes out-of-box support for
Tor network and a lot more.

%description -l ru_RU.UTF-8
Расширение FoxyProxy Standard для Firefox  - расширенная
утилита управления настройками прокси-серверов, которая
полностью заменяет стандартные настройки прокси в Firefox.
FoxyProxy предоставляет поддержку одновременно нескольких
серверов прокси, позволяя указать какой прокси задействовать
(или вообще не задействовать) для конкретных  URL используя
шаблоны, регулярные выражения и прочие возможности, имеет
встроенную поддержку работы с сетью Tor, и многое другое.

%prep
%setup -c

%install
mkdir -p --  %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir


%changelog
* Sat Dec 16 2017 Nikolay A. Fetisov <naf@altlinux.org> 6.1.9-alt1
- New version

* Sun Feb 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 4.6.5-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 4.5.7-alt1
- New version

* Sun Mar 20 2016 Nikolay A. Fetisov <naf@altlinux.ru> 4.5.6-alt1
- New version

* Thu Jan 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 4.5.5-alt1
- New version
- Signed version to work with Firefox >= 43.x

* Sat Sep 20 2014 Nikolay A. Fetisov <naf@altlinux.ru> 4.2.4-alt1
- New version 4.2.4

* Sat Nov 02 2013 Nikolay A. Fetisov <naf@altlinux.ru> 4.2.3-alt1
- New version 4.2.3

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 4.2.2-alt1
- New version 4.2.2

* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 4.1.4-alt1
- New version 4.1.4

* Wed Dec 19 2012 Andrey Cherepanov <cas@altlinux.org> 4.1-alt1
- New version 4.1

* Fri Jan 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 3.4-alt1
- Initial build for ALT Linux Sisyphus
