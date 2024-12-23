Name: kde-theme-alt
Version: 0.3
Release: alt1

Summary: ALT KDE theme
Group: Graphics
URL: https://altlinux.org
License: GPL-3.0

Source: %name-%version.tar

BuildArch: noarch

Requires: icon-theme-altos
Requires: x-cursor-themes-breezex
Requires: gtk-theme-breeze

%description
ALT theme for KDE.

%prep
%setup

%install
mkdir -p %buildroot/%_datadir/plasma/look-and-feel/
cp -ar look-and-feel/org.basealt.altos*.desktop %buildroot/%_datadir/plasma/look-and-feel/
mkdir -p %buildroot/%_datadir/plasma/desktoptheme/
cp -ar desktoptheme/altos-* %buildroot/%_datadir/plasma/desktoptheme/

%files
%_datadir/plasma/look-and-feel/org.basealt.altos*.desktop/
%_datadir/plasma/desktoptheme/altos-*/

%changelog
* Mon Dec 23 2024 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt1
- update icons

* Fri Dec 13 2024 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt1
- add basic data

* Mon Nov 18 2024 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial build
