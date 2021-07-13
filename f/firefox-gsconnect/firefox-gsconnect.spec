# SPEC file for the GSConnect Firefox extension

%define rname	gsconnect
%define cid	gsconnect@andyholmes.github.io

Name:		%firefox_name-%rname
Version:	8.0
Release:	alt1

Summary:	GSConnect Firefox extension

License:	%gpl2only
Group:		Networking/WWW
URL:		https://github.com/GSConnect/gnome-shell-extension-gsconnect
#URL:		https://addons.mozilla.org/firefox/addon/gsconnect/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
GSConnect is a Firefox extension for sharing links with phones,
tablets and other devices connected with the GSConnect GNOME
Shell extension.

KDE Connect allows devices to securely share content like
notifications or files and other features like SMS messaging
and remote control. GSConnect is a complete implementation
of KDE Connect especially for GNOME Shell.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 8.0-alt1
- Initial build for ALT Linux Sisyphus
