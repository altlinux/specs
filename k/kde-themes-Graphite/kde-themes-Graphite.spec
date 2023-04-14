%define _kvantumdir %_datadir/Kvantum
%define _auroraedir %_datadir/aurorae/themes
%define _schemesdir %_datadir/color-schemes
%define _lookfeeldir %_datadir/plasma/look-and-feel
%define _plasmadir %_datadir/plasma/desktoptheme

Name:    kde-themes-Graphite
Version: 220208
Release: alt1

Summary: Graphite is a flat Design theme for KDE Plasma desktop
License: GPL-3.0
Group:   Graphical desktop/KDE
Url:     https://github.com/vinceliuice/Graphite-kde-theme

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

Requires: Kvantum

%description
Graphite theme for KDE Plasma

In this set of packages you'll find:
- Aurorae Themes
- Kvantum Themes
- Plasma Color Schemes
- Plasma Desktop Themes
- Plasma Global Themes


%prep
%setup

%install
mkdir -p %buildroot{%_kvantumdir,%_auroraedir,%_lookfeeldir,%_plasmadir}

cp -r Kvantum/* %buildroot%_kvantumdir
cp -r aurorae/* %buildroot%_auroraedir
cp -r color-schemes/ %buildroot%_schemesdir
cp -r plasma/desktoptheme/* %buildroot%_plasmadir
cp -r plasma/look-and-feel/* %buildroot%_lookfeeldir

%files
%_kvantumdir/*
%_auroraedir/*
%_schemesdir/*.colors
%_lookfeeldir/
%_plasmadir/

%changelog
* Wed Apr 12 2023 Artyom Bystrov <arbars@altlinux.org> 220208-alt1
- New version 220208.

* Tue Apr 11 2023 Artyom Bystrov <arbars@altlinux.org> 2022-02-08-alt1
- Initial build for Sisyphus
