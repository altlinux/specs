%define pluginname com.github.zren.inactiveblur

Name: kde5-plasma-inactiveblur
Version: 5
Release: alt2.gitf5c2783
Summary: A wallpaper plugin for Plasma5
License: GPL-1
Group: Graphical desktop/KDE
Url: https://github.com/Zren/plasma-wallpapers/tree/master/inactiveblur
Source: %name-%version.tar

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
* Sun Sep 04 2022 Alexander Makeenkov <amakeenk@altlinux.org> 5-alt2.gitf5c2783
- Updated to last upstream git (fixes for Plasma 5.25)
- Spec: Removed Packager tag

* Wed Mar 25 2020 Alexander Makeenkov <amakeenk@altlinux.org> 5-alt1
- Initial build for ALT
