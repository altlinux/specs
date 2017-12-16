# SPEC file for uBlock Origin extension

%define rname	ublock_origin
%define version 1.14.22
%define release alt1
%define cid 	uBlock0@raymondhill.net
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	uBlock Origin extension for Firefox
Summary(ru_RU.UTF-8):	расширение uBlock Origin для Firefox

License:	%gpl3only
Group:		Networking/WWW
# URL:		https://github.com/gorhill/uBlock
URL:		https://addons.mozilla.org/ru/firefox/addon/ublock-origin/
BuildArch:	noarch

Source0:	%rname-%version.xpi

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description
uBlock Origin Firefox plugin is a efficient general-purpose
blocker, easy on CPU and memory.
uBlock Origin is not only an ad blocker; it extends the syntax
of the Adblock Plus filter syntax and is designed to work with
custom rules and filters.
Furthermore, advanced mode allows uBlock Origin to work in
default-deny mode, which mode will cause all 3rd-party network
requests to be blocked by default, unless allowed by the user.


%description -l ru_RU.UTF-8
Расширение uBlock Origin для Firefox - эффективный блокировщик
(фильтр) запросов. Он не только блокирует рекламу на страницах,
но также, использую синтаксис фильтров Adblock Plus, позволяет
добавлять свои правила и фильтры.
Кроме того, в продвинутом режиме uBlock Origin может работать
в режиме запрета запросов всех сторонних по отношению к сайту
ресурсов, если они специально не разрешены пользователем.

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
* Sat Dec 16 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.14.22-alt1
- New version

* Sun Sep 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.14.4-alt1
- New version

* Sun Jul 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.13.18-alt1
- New version

* Sat Jul 15 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.13.4-alt1
- New version

* Thu Jun 29 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.13.0-alt1
- New version

* Sat Jun 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.12.4-alt1
- New version

* Sun Apr 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.12.1-alt1
- New version

* Sat Mar 25 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.11.4-alt1
- New version

* Sun Feb 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.10.6-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.9.6-alt1
- New version

* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.7.6-alt1
- New version

* Sun Jun 12 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.7.0-alt1
- New version

* Sun Mar 20 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.6.4-alt1
- New version

* Sun Feb 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.5-alt1
- New version

* Thu Jan 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.3-alt1
- Initial build for ALTLinux Sisyphus
