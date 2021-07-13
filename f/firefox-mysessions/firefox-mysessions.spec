# SPEC file for the MySessions Firefox extension

%define rname	mysessions
%define cid	balyaev@gmail.com

Name:		%firefox_name-%rname
Version:	2021.6.0
Release:	alt1

Summary:	MySessions Firefox extension
Summary(ru_RU.UTF-8):	расширение MySessions для Firefox

License:	%mpl
Group:		Networking/WWW
URL:		https://addons.mozilla.org/firefox/addon/my-sessions/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
MySessions is a Firefox simple session manager. You can quickly
save your current browser state and reload it whenever necessary.

The main task of this extension is to save sessions at any cost.
As a repository, browser bookmarks are selected as the most
reliable and secure storage.

%description -l ru_RU.UTF-8
Расширение MySessions для Firerfox - это простой менеджер сессий.
Оно позволяет быстро сохранить текущее состояние браузера и при
необходимости восстановить его.

Основная задача этого расширения - сохранение сессий любой ценой.
В качестве хранилища выбрано закладки браузера, как наиболее
надежное и безопасное хранилище.


# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 2021.6.0-alt1
- Initial build for ALT Linux Sisyphus
