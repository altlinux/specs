Name: kde-theme-alt
Version: 0.1
Release: alt1

Summary: ALT KDE theme
Group: Graphics
URL: https://altlinux.org
License: GPL-3.0

Source: %name-%version.tar

BuildArch: noarch

Requires: icon-theme-altos
Requires: x-cursor-themes-breezex

%description
ALT theme for KDE.

%prep
#setup

#install

%files
#%_datadir/plasma/look-and-feel/org.basealt.kde.desktop

%changelog
* Mon Nov 18 2024 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial build
