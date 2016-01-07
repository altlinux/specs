# SPEC file for uMatrix extension

%define rname	umatrix
%define version 0.9.3.1
%define release alt1
%define cid 	uMatrix@raymondhill.net
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	uMatrix extension for Firefox
Summary(ru_RU.UTF-8):	расширение uMatrix для Firefox

License:	%gpl3only
Group:		Networking/WWW
# URL:		https://github.com/gorhill/uMatrix
URL:		https://addons.mozilla.org/ru/firefox/addon/umatrix/
BuildArch:	noarch

Source0:	%rname-%version.xpi

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description
uMatrix Firefox extension provides point & click interface to
forbid/allow any class of requests made by browser. Use it to
block scripts, iframes, ads, facebook, etc.

%description -l ru_RU.UTF-8
Расширение uMatrix для Firefox предоставляет простой интерфейс
для запрещения/разрешения любых видов запросов, которые выполняет
браузер при просмотре страниц. Оно может быть использования
для блокирования скриптов, iframe'ов, рекламы, facebook'а и т.п.

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
* Thu Jan 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.3.1-alt1
- Initial build for ALTLinux Sisyphus
