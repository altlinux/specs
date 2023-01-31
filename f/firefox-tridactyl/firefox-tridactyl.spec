# SPEC file for the Tridactyl Firefox extension

%define rname	tridactyl
%define cid	tridactyl.vim@cmcaine.co.uk

Name:		%firefox_name-%rname
Version:	1.23.0
Release:	alt1

Summary:	Tridactyl Firefox extension

License:	%asl
Group:		Networking/WWW
URL:		https://github.com/tridactyl/tridactyl
#URL:		https://addons.mozilla.org/ru/firefox/addon/tridactyl-vim/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Tridactyl Firefox extension replaces Firefox's default control
mechanism with one modelled on the one true editor, Vim.
This is a "Firefox Quantum" replacement for VimFX, Vimperator
and Pentadactyl. Most common tasks you want your browser
to perform are bound to a single key press.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.23.0-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.22.0-alt1
- New version

* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.21.1-alt1
- Initial build for ALT Linux Sisyphus
