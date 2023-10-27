%define _unpackaged_files_terminate_build 1

Name: kde5-plasma-wallpapers-dynamic
Version: 4.4.0
Release: alt2
Summary: Dynamic wallpaper plugin for KDE Plasma
License: GPL-3.0-or-later and LGPL-3.0-or-later and MIT
Group: Graphical desktop/KDE
Url: https://github.com/zzag/plasma5-wallpapers-dynamic
Source: %name-%version.tar

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
BuildRequires: libheif-devel
BuildRequires: libexif-devel
BuildRequires: libavif-devel

%description
A wallpaper plugin for KDE Plasma that continuously updates
the desktop background based on the current time in your location.
More dynamic wallpapers can be found at
https://github.com/karmanyaahm/awesome-plasma5-dynamic-wallpapers

%package -n %name-devel
Summary: %summary
Group: Graphical desktop/KDE

%description -n %name-devel
A wallpaper plugin for KDE Plasma that continuously updates
the desktop background based on the current time in your location.
More dynamic wallpapers can be found at
https://github.com/karmanyaahm/awesome-plasma5-dynamic-wallpapers

%prep
%setup

%build
%K5cmake
%K5make

%install
%K5install
%find_lang --with-kde %name

%files -f %name.lang
%_bindir/kdynamicwallpaperbuilder
%_libdir/libkdynamicwallpaper.so.*
%_K5plug/kpackage/packagestructure/packagestructure_dynamicwallpaper.so
%_K5qml/com/github/zzag/plasma/wallpapers/dynamic
%_kf5_data/plasma/wallpapers/com.github.zzag.dynamic
%_datadir/wallpapers/Dynamic
%_datadir/locale/*/LC_MESSAGES/plasma_wallpaper_com.github.zzag.dynamic.mo
%_datadir/metainfo/com.github.zzag.dynamic.appdata.xml
%_datadir/bash-completion/completions/kdynamicwallpaperbuilder
%_datadir/fish/completions/kdynamicwallpaperbuilder.fish
%_datadir/zsh/site-functions/_kdynamicwallpaperbuilder
%_K5srv/plasma-wallpaper-com.github.zzag.dynamic.desktop
%doc LICENSES README.md

%files -n %name-devel
%_includedir/KDynamicWallpaper
%_K5link/libkdynamicwallpaper.so
%_libdir/cmake/KDynamicWallpaper

%changelog
* Thu Oct 26 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.4.0-alt2
- Fixed build with new rpm-build-kf5.

* Thu Oct 06 2022 Alexander Makeenkov <amakeenk@altlinux.org> 4.4.0-alt1
- Updated to version 4.4.0
- Spec:
  + Removed Packager tag
  + Fixed URL in description

* Sat May 14 2022 Alexander Makeenkov <amakeenk@altlinux.org> 4.3.1-alt1
- Updated to version 4.3.1

* Mon Dec 27 2021 Alexander Makeenkov <amakeenk@altlinux.org> 3.3.9-alt3
- Fix FTBFS: exclude .desktop file instead removing

* Fri Jul 16 2021 Alexander Makeenkov <amakeenk@altlinux.org> 3.3.9-alt2
- Fixed build: don't package service file

* Fri Jul 16 2021 Alexander Makeenkov <amakeenk@altlinux.org> 3.3.9-alt1
- Updated to version 3.3.9

* Sun Jan 10 2021 Alexander Makeenkov <amakeenk@altlinux.org> 3.3.6-alt1
- Updated to version 3.3.6

* Fri Aug 14 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.3.3-alt1
- Updated to version 3.3.3

* Fri May 01 2020 Alexander Makeenkov <amakeenk@altlinux.org> 2.7.1-alt1
- Initial build for ALT
