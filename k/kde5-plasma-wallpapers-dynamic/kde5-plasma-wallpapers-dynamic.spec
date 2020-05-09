%define _unpackaged_files_terminate_build 1

Name: kde5-plasma-wallpapers-dynamic
Version: 2.7.1
Release: alt1
Summary: Dynamic wallpaper plugin for KDE Plasma
License: GPL-3.0-or-later and LGPL-3.0-or-later and MIT
Group: Graphical desktop/KDE
Url: https://github.com/zzag/plasma5-wallpapers-dynamic
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-location-devel
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-plasma-framework-devel

%description
%summary.

%prep
%setup

%build
%K5cmake
%K5make

%install
%K5install

%files
%_K5plug/kpackage/packagestructure/packagestructure_dynamicwallpaper.so
%_K5qml/com/github/zzag/private/wallpaper
%_K5data/plasma/wallpapers/com.github.zzag.wallpaper
%_datadir/dynamicwallpapers
%_datadir/kservices5/plasma-wallpaper-com.github.zzag.wallpaper.desktop
%_datadir/locale/*/LC_MESSAGES/plasma_wallpaper_com.github.zzag.wallpaper.mo
%_datadir/metainfo/com.github.zzag.wallpaper.appdata.xml
%doc LICENSES README.md

%changelog
* Fri May 01 2020 Alexander Makeenkov <amakeenk@altlinux.org> 2.7.1-alt1
- Initial build for ALT
