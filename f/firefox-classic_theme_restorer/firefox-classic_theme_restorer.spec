%define rname	classic_theme_restorer
%define cid 	ClassicThemeRestorer@ArisT2Noia4dev
%define ciddir  %firefox_noarch_extensionsdir/%cid

Name: firefox-classic_theme_restorer
Version: 1.4.9
Release: alt1

Summary: Classic Theme Restorer (Customize Australis) extension for Firefox
License: Mozilla Public License, version 2.0
Group: Networking/WWW

Url: https://addons.mozilla.org/en-US/firefox/addon/classicthemerestorer/
Source: classic_theme_restorer_customize_australis-%version-fx.xpi
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-firefox
BuildRequires: unzip

# these are ELF binaries for Mozilla Weave
%define _verify_elf_method skip
%brp_strip_none %ciddir
AutoReq: yes, nolib, noshell

%description
'Classic Theme Restorer' brings back appmenu button, squared tabs,
add-ons bar, small nav-bar buttons, a few older buttons and more
to Firefox Australis UI.

Use 'Customize' menu to move buttons on toolbars.

%prep
%setup -c

%install
mkdir -p %buildroot/%ciddir
cp -pr * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then [ ! -d "%ciddir" ] || rm -rf "%ciddir"; fi

%files
%ciddir

%changelog
* Sun Mar 20 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.4.9-alt1
- Version 1.4.9-alt1

* Mon Sep 01 2014 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue May 20 2014 Michael Shigorin <mike@altlinux.org> 1.1.9-alt1
- built for ALT Linux

