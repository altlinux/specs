%define pluginname com.github.zren.inactiveblur

Name: kde5-plasma-inactiveblur
Version: 5
Release: alt1
Summary: A wallpaper plugin for Plasma5
License: GPL-1
Group: Graphical desktop/KDE
Url: https://github.com/Zren/plasma-wallpapers/tree/master/inactiveblur
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch

%description
A wallpaper plugin for Plasma5 that blurs the wallpaper when theres an active window.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/kf5/plasma/wallpapers/%pluginname
install -m 0644 metadata.desktop %buildroot%_datadir/kf5/plasma/wallpapers/%pluginname
cp -pr contents %buildroot%_datadir/kf5/plasma/wallpapers/%pluginname

%files
%_datadir/kf5/plasma/wallpapers/%pluginname

%changelog
* Wed Mar 25 2020 Alexander Makeenkov <amakeenk@altlinux.org> 5-alt1
- Initial build for ALT
