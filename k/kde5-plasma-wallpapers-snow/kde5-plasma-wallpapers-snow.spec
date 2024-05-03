%define _unpackaged_files_terminate_build 1

Name: kde5-plasma-wallpapers-snow
Version: 0.1.0
Release: alt1

Summary: Snowfall Live Wallpaper for KDE Plasma 5
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://store.kde.org/p/2104435/
Vcs: https://github.com/IvanSafonov/plasma-wallpaper-snow
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_kf5_data/plasma/wallpapers/
cp -r ./snow %buildroot%_kf5_data/plasma/wallpapers/org.kde.snow

%files
%_kf5_data/plasma/wallpapers/org.kde.snow

%changelog
* Thu May 02 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.1.0-alt1
- First build for ALT.
