# SPEC file for the URLs List Firefox extension

%define rname	urls_list
%define cid	\{88664789-f91e-40e1-adb9-e4e9a8c48867\}

Name:		%firefox_name-%rname
Version:	0.5.0
Release:	alt1

Summary:	URLs List Firefox extension
Summary(ru_RU.UTF-8):	расширение URLs List Firefox

License:	%mit
Group:		Networking/WWW
URL:		https://github.com/moritz-h/urls-list
#URL:		https://addons.mozilla.org/firefox/addon/urls-list/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
URLs List is a Firefox extenstion that lists the URLs of all tabs
from the current window as copyable plaintext. Also this extension
can load a plaintext list of urls to individual tabs.

%description -l ru_RU.UTF-8
Расширение URLs List для Firefox выводит список URL всех открытых
в текущем окне вкладок в виде, пригодном для копирования в буфер
обмена. Также это расширение позволяет загрузить список URL в
набор новых вкладок окна браузера.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.5.0-alt1
- Initial build for ALT Linux Sisyphus
