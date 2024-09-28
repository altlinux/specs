%define plugin_id a2n.blur

Name: kde-plasma-addon-active-blur
Version: 3.1.1
Release: alt1
Summary: kde plasma wallpaper plugin that blur the wallpaper when a window is active
License: GPL-3.0
Group: Graphical desktop/KDE
Url: https://github.com/bouteillerAlan/blurredwallpaper

Source: %name-%version.tar

BuildArch: noarch

Provides: kde5-plasma-active-blur = %EVR
Obsoletes: kde5-plasma-active-blur < %EVR

%description
Blur the wallpaper if a windows is active.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/plasma/wallpapers
cp -pr %plugin_id %buildroot%_datadir/plasma/wallpapers

%files
%_datadir/plasma/wallpapers/%plugin_id

%changelog
* Sat Sep 28 2024 Alexander Makeenkov <amakeenk@altlinux.org> 3.1.1-alt1
- Updated to version 3.1.1.
- Build for KF6.

* Tue Jan 09 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.2-alt1
- Initial build for ALT.

