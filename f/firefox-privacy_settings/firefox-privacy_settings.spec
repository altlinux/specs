# SPEC file for Privacy Settings extension

%define rname	privacy_settings
%define version 0.2.4
%define release alt1
%define cid 	jid1-CKHySAadH4nL6Q@jetpack
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	Privacy Settings extension for Firefox
Summary(ru_RU.UTF-8):	расширение Privacy Settings для Firefox

License:	%mpl 2.0
Group:		Networking/WWW
# URL:		http://firefox.add0n.com/privacy-settings.html
# URL:		https://github.com/schomery/privacy-settings
URL:		https://addons.mozilla.org/ru/firefox/addon/privacy-settings/
BuildArch:	noarch

Source0:	%rname-%version.xpi

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description
Privacy Settings extension provides a toolbar panel for easily
altering Firefox's built-in privacy settings.

%description -l ru_RU.UTF-8
Расширение Privacy Settings предоставляет панель инструментов для
быстрого доступа к встроенным в Firefox настройкам приватности.

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
