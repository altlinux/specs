# SPEC file for the Save PDF Firefox extension

%define rname	save_pdf
%define cid	\{077f4ca9-a296-4624-9524-4e9b3835f512\}

Name:		%firefox_name-%rname
Version:	0.1
Release:	alt1

Summary:	Save PDF Firefox extension
Summary(ru_RU.UTF-8):	расширение Save PDF для Firefox

License:	%mpl
Group:		Networking/WWW
URL:		https://addons.mozilla.org/firefox/addon/save-pdf/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Save PDF Firefox extensions saves current page as PDF.
It uses only built-in Firefox converter and does not
requires any permissions or no third-party servers.

%description -l ru_RU.UTF-8
Расширение Save PDF для Firefox сохраняет текущую страницу
как документ PDF. Оно использует только встроенные механизмы
Firefox, не требует каких-либо разрешений и не использует
сторонних серверов.


# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
