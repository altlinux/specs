# SPEC file for the Save As eBook Firefox extension

%define rname	save_as_ebook
%define cid	\{087005dc-849e-419b-acf6-32da1f83691d\}

Name:		%firefox_name-%rname
Version:	1.4.2
Release:	alt1

Summary:	Save As eBook Firefox extension
Summary(ru_RU.UTF-8):	расширение Save As eBook для Firefox

License:	%mit
Group:		Networking/WWW
URL:		https://github.com/alexadam/save-as-ebook
#URL:		https://addons.mozilla.org/firefox/addon/saveasebook/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Save As eBook is a Firefox extension to save a web page/selection
as an eBook (.epub format).

%description -l ru_RU.UTF-8
Расширение Save As eBook для Firefox позволяет сохранить страницу
или её выделенную часть как eBook (в формате .epub).

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.4.2-alt1
- Initial build for ALT Linux Sisyphus
