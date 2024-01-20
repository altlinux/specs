%define plugin_id a2n.blur

Name: kde5-plasma-active-blur
Version: 2.2
Release: alt1
Summary: kde plasma wallpaper plugin that blur the wallpaper when a window is active
License: GPL-3.0
Group: Graphical desktop/KDE
Url: https://github.com/bouteillerAlan/blurredwallpaper
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-kf5

%description
Blur the wallpaper if a windows is active.

%prep
%setup

%install
mkdir -p %buildroot%_kf5_data/plasma/wallpapers/%plugin_id
cp -pr contents metadata.json %buildroot%_kf5_data/plasma/wallpapers/%plugin_id

%files
%_kf5_data/plasma/wallpapers/%plugin_id

%changelog
* Tue Jan 09 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.2-alt1
- Initial build for ALT.

