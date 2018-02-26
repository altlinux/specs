# SPEC file for FoxyProxy Firefox extension

%define rname	foxyproxy_standard
%define version	3.4
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
* Fri Jan 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 3.4-alt1
- Initial build for ALT Linux Sisyphus
