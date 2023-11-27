# SPEC file for the Sidebery Firefox extension

%define rname	sidebery
%define cid	3c078156-979c-498b-8990-85f7987dd929

Name:		%firefox_name-%rname
Version:	5.0.0
Release:	alt1

Summary:	Firefox extension for managing tabs and bookmarks in sidebar
Summary(ru_RU.UTF-8):	расширение Firefox для управление вкладками и закладками в боковой панели

License:	%mit
Group:		Networking/WWW
URL:		https://addons.mozilla.org/ru/firefox/addon/sidebery/
#URL:		https://github.com/mbnuqw/sidebery
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Sidebery extension for Firefox provides the list of tabs structured
in a tree, bookmarks and history within the customizable panels.
It aims to be fast and configurable.


%description -l ru_RU.UTF-8
Расширение Sidebery для Firefox позволяет выводить в настраиваемой
боковой панели структурированный в виде дерева список вкладок,
закладок и истории посещений браузера.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Mon Nov 27 2023 Nikolay A. Fetisov <naf@altlinux.org> 5.0.0-alt1
- Initial build for ALT Linux Sisyphus
