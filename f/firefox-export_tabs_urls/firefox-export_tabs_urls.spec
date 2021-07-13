# SPEC file for the Export Tabs URLs Firefox extension

%define rname	export_tabs_urls
%define cid	\{17165bd9-9b71-4323-99a5-3d4ce49f3d75\}

Name:		%firefox_name-%rname
Version:	0.2.12
Release:	alt1

Summary:	Export Tabs URLs Firefox extension
Summary(ru_RU.UTF-8):	расширение Export Tabs URLs для Firefox

License:	%gpl3only
Group:		Networking/WWW
URL:		https://github.com/alct/export-tabs-urls
#URL:		https://addons.mozilla.org/firefox/addon/export-tabs-urls-and-titles/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Export Tabs URLs Firefox extension lists the URLs of all the open
tabs and copy that list to clipboard or export it to a file.

%description -l ru_RU.UTF-8
Расширение Export Tabs URLs для Firefox выводит список URL всех
открытых вкладок и позволяет скопировать его в буфер обмена или
экспортировать в файл.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.2.12-alt1
- Initial build for ALT Linux Sisyphus
