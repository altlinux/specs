# SPEC file for the Tab2QR Firefox extension

%define rname	tab2qr
%define cid	\{dc3dce74-bf98-4eb4-adc4-75597edb6c5c\}

Name:		%firefox_name-%rname
Version:	4.0.0
Release:	alt1

Summary:	Tab2QR Firefox extension
Summary(ru_RU.UTF-8):	расширение Tab2QR для Firefox

License:	%mit
Group:		Networking/WWW
URL:		https://github.com/IFS49F/Tab2QR
#URL:		https://addons.mozilla.org/firefox/addon/tab2qr/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Tab2QR is a minimalistic Firefox extenstion to display URL of
the current page as QR code so it can be scaned with your phone
or tablet. QR codes are generated instantly in browser,
no third-party application used.

%description -l ru_RU.UTF-8
Расширение Tab2QR для Firefox выводит URL текущей страницы в
виде QR-кода - и передать его на мобильный телефон или планшет,
отсканировав его. QR-коды генерируются внутри браузера, без
искользования каких-либо сторонних приложений.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Sat Oct 21 2023 Nikolay A. Fetisov <naf@altlinux.org> 4.0.0-alt1
- New version

* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.0.0-alt1
- Initial build for ALT Linux Sisyphus
