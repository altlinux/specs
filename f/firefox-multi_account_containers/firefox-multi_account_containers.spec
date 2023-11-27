# SPEC file for the Firefox Multi-Account Containers extension

%define rname	multi_account_containers
%define cid	@testpilot-containers

Name:		%firefox_name-%rname
Version:	8.1.3
Release:	alt1

Summary:	Firefox Multi-Account Containers extension
Summary(ru_RU.UTF-8):	расширение Multi-Account Containers для Firefox

License:	%mpl
Group:		Networking/WWW
URL:		https://github.com/mozilla/multi-account-containers/
#URL:		https://addons.mozilla.org/ru/firefox/addon/multi-account-containers/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Firefox Multi-Account Containers extension lets keep parts of
the online activities separated into color-coded tabs that
preserve privacy. Cookies are separated by container, allowing
to use the web with multiple identities or accounts
simultaneously.

%description -l ru_RU.UTF-8
Расширение «Multi-Account Containers» для Firefox позволяет
хранить все аспекты работы в Интернете в отдельных независимых
вкладках. Пользовательские метки и цветная маркировка помогают
разделять различные виды деятельности в Интернете. Разделение
по контейнерам ресурсов сайтов даёт возможность работать с ними
одновременно с разными сетевыми идентичностями или учётными
записями.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Mon Nov 27 2023 Nikolay A. Fetisov <naf@altlinux.org> 8.1.3-alt1
- Initial build for ALT Linux Sisyphus
