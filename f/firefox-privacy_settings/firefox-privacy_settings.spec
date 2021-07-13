# SPEC file for Privacy Settings extension

%define rname	privacy_settings
%define cid	jid1-CKHySAadH4nL6Q@jetpack

Name:		%firefox_name-%rname
Version:	0.3.7
Release:	alt1

Summary:	Privacy Settings extension for Firefox
Summary(ru_RU.UTF-8):	расширение Privacy Settings для Firefox

License:	%mpl 2.0
Group:		Networking/WWW
# URL:		http://firefox.add0n.com/privacy-settings.html
# URL:		https://github.com/schomery/privacy-settings
URL:		https://addons.mozilla.org/ru/firefox/addon/privacy-settings/
BuildArch:	noarch

Source0:	%rname.xpi

Packager:       Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description
Privacy Settings extension provides a toolbar panel for easily
altering Firefox's built-in privacy settings.

%description -l ru_RU.UTF-8
Расширение Privacy Settings предоставляет панель инструментов для
быстрого доступа к встроенным в Firefox настройкам приватности.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.3.7-alt1
- New version

* Sat Jun 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.2.6-alt1
- New version

* Sun Apr 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.2.5-alt1
- New version

* Sun Feb 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.2.4-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.3-alt1
- New version

* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.2-alt1
- New version

* Sun Jun 12 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.1-alt1
- New version

* Sun Mar 20 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.1.9.1-alt1
- New version

* Thu Jan 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.1.8-alt1
- Initial build for ALTLinux Sisyphus
