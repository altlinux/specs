# SPEC file for uMatrix extension

%define rname	umatrix
%define cid	uMatrix@raymondhill.net

Name:		%firefox_name-%rname
Version:	1.4.4
Release:	alt1

Summary:	uMatrix extension for Firefox
Summary(ru_RU.UTF-8):	расширение uMatrix для Firefox

License:	%gpl3only
Group:		Networking/WWW
# URL:		https://github.com/gorhill/uMatrix
URL:		https://addons.mozilla.org/ru/firefox/addon/umatrix/
BuildArch:	noarch

Source0:	%rname.xpi

Packager:       Nikolay A. Fetisov <naf@altlinux.org>

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

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 20 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.4.4-alt1
- New version
  - Fix infinite recursion with maliciously crafted URL
  - Remove obsolete assets
  - Remove no longer existing hpHosts
  - mvps host list secure protocol http => https

* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.4.0-alt1
- New version

* Sat Dec 16 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.20-alt1
- New version

* Sat Jun 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.0.0-alt1
- New version

* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.3.6-alt1
- New version

* Sun Mar 20 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.3.3-alt1
- New version

* Sun Feb 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.3.2-alt1
- New version

* Thu Jan 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.3.1-alt1
- Initial build for ALTLinux Sisyphus
