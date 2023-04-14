%define theme Graphite

Name:    x-cursor-themes-Graphite
Version: 211126
Release: alt1

Summary: Graphite cursors theme for linux desktops
License: GPL-3.0
Group:   Graphics
Url:     https://github.com/vinceliuice/Graphite-cursors

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

#BuildRequires:

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%_iconsdir/%theme
cp -r dist-light %buildroot%_iconsdir/%theme-cursors
cp -r dist-dark %buildroot%_iconsdir/%theme-dark-cursors
cp -r dist-light-nord %buildroot%_iconsdir/%theme-light-nord-cursors
cp -r dist-dark-nord %buildroot%_iconsdir/%theme-dark-nord-cursors

%files
%_iconsdir/%theme-*

%changelog
* Sat Apr 15 2023 Artyom Bystrov <arbars@altlinux.org> 211126-alt1
- New version 211126.

* Fri Apr 14 2023 Artyom Bystrov <arbars@altlinux.org> 2021-11-26-alt1
- Initial build for Sisyphus
