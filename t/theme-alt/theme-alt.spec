%define _unpackaged_files_terminate_build 1

Name: theme-alt
Version: 1.0
Release: alt0.beta4
Summary: ALT theme

License: GPL-3.0
Group: Graphics
URL: https://altlinux.org

Source: %name-%version.tar

BuildArch: noarch

Requires: gtk-theme-qogir
Requires: kde5-plasma-theme-qogir
Requires: icon-theme-alt

%description
ALT theme based on Qogir theme.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/kf5/plasma/look-and-feel
cp -a org.basealt.alt.desktop %buildroot%_datadir/kf5/plasma/look-and-feel
mkdir -p %buildroot%_datadir/kf5/plasma/desktoptheme
cp -a desktoptheme/ALT %buildroot%_datadir/kf5/plasma/desktoptheme
mkdir -p %buildroot%_datadir/wallpapers/ALT
cp -a wallpapers/ALT %buildroot%_datadir/wallpapers
mkdir -p %buildroot%_datadir/kf5
cp -a color-schemes %buildroot%_datadir/kf5

%files
%_datadir/kf5/plasma/look-and-feel/org.basealt.alt.desktop
%_datadir/wallpapers/ALT
%_datadir/kf5/color-schemes/*.colors
%_datadir/kf5/plasma/desktoptheme/ALT

%changelog
* Fri Aug 30 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.beta4
- Added splash theme.

* Tue Aug 20 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.beta3
- Initial build in Sisyphus.
