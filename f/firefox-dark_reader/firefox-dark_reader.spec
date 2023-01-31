# SPEC file for the Dark Reader Firefox extension

%define rname	dark_reader
%define cid	addon@darkreader.org

Name:		%firefox_name-%rname
Version:	4.9.62
Release:	alt1

Summary:	Dark Reader Firefox extension
Summary(ru_RU.UTF-8):	расширение DuckDuckGo Plus для Firefox

License:	%mit
Group:		Networking/WWW
URL:		https://darkreader.org/
#URL:		https://addons.mozilla.org/ru/firefox/addon/darkreader/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Dark Reader is a eye-care Firefox extension that enables night
mode creating dark themes for websites on the fly. Dark Reader
inverts bright colors making them high contrast and easy to
read at night.

You can adjust brightness, contrast, sepia filter, dark mode,
font settings and ignore-list.

%description -l ru_RU.UTF-8
Dark Reader - расширение для Firefox, которое переводит браузер
в ночной режим. Дарк Ридер заменяет светлый фон тёмным, что
снижает усталость глаз при долгой работе за компьютером либо
при просмотре веб-страниц ночью.

Имеется возможность настраивать яркость, контрастность, шрифт,
режим инверсии, режим наложения жёлтого фильтра (сепия).

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 4.9.62-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 4.9.45-alt1
- New version

* Fri Nov 19 2021 Nikolay A. Fetisov <naf@altlinux.org> 4.9.42-alt1
- New version

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 4.9.41-alt1
- New version

* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 4.9.34-alt1
- Initial build for ALT Linux Sisyphus
