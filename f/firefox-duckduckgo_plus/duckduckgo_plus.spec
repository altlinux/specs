# SPEC file for the DuckDuckGo Plus Firefox extension

%define rname	duckduckgo_plus
%define cid	jid1-ZAdIEUB7XOzOJw@jetpack

Name:		%firefox_name-%rname
Version:	2022.12.27
Release:	alt1

Summary:	DuckDuckGo Plus Firefox extension
Summary(ru_RU.UTF-8):	расширение DuckDuckGo Plus для Firefox

License:	%asl 2.0
Group:		Networking/WWW
URL:		https://addons.mozilla.org/ru/firefox/addon/duckduckgo-for-firefox/
#URL:		https://github.com/duckduckgo/firefox-zeroclickinfo
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
DuckDuckGo is a search engine that does not track you.
This Firefox extension adds DuckDuckGo as the default address
bar, search bar and right-click search engine. Adds a handy
toolbar button for easy access to !bang tags. Adds DuckDuckGo
instant answers to Google/Bing.

%description -l ru_RU.UTF-8
DuckDuckGo - поисковая система с открытым исходным кодом,
которая не собирает какой-либо информации о пользователях
и не отслеживает их действия.
Расширение DuckDuckGo Plus для Firefox добавляет DuckDuckGo в
адресную строку, в поле поиска и в контекстное меню браузера.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 2022.12.27-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 2022.1.24-alt1
- New version

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 2021.9.30-alt1
- New version

* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 2021.7.9-alt1
- New version

* Sat Dec 16 2017 Nikolay A. Fetisov <naf@altlinux.org> 2017.12.7-alt1
- New version

* Sun Sep 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.22-alt1
- New version

* Sun Aug 13 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.17-alt1
- New version

* Sun Jul 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.10-alt1
- New version

* Thu Jun 29 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.5-alt1
- New version

* Mon May 01 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.4-alt1
- New version

* Sun Apr 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.2-alt1
- New version

* Sun Feb 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.1-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.8-alt1
- New version

* Sat Jul 30 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.6-alt1
- New version

* Sun Jun 12 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.2-alt1
- New version

* Thu Jan 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.6.1-alt1
- New version
- Signed version to work with Firefox >= 43.x

* Sat Sep 20 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.2-alt1
- New version

* Tue Nov 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.3.8-alt1.1
- Adapt for Firefox 24.x

* Sat Nov 02 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.8-alt1
- New version (Closes: #29548)

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.53-alt1
- New version

* Tue Jun 11 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.37-alt1
- Initial build for ALT Linux Sisyphus
