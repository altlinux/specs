%define _unpackaged_files_terminate_build 1

Name: kde-plasma-addon-wallpapers-dynamic
Version: 5.0.0
Release: alt1
Summary: Dynamic wallpaper plugin for KDE Plasma
License: BSD-3-Clause and CC-BY-SA-4.0 and CC0-1.0 and GPL-3.0-or-later and LGPL-3.0-or-later
Group: Graphical desktop/KDE
Url: https://github.com/zzag/plasma5-wallpapers-dynamic

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: libavif-devel
BuildRequires: libexif-devel
BuildRequires: libheif-devel
BuildRequires: plasma6-lib-devel
BuildRequires: qt6-positioning-devel

Provides: kde5-plasma-wallpapers-dynamic = %EVR
Obsoletes: kde5-plasma-wallpapers-dynamic < %EVR

%description
A wallpaper plugin for KDE Plasma that continuously updates
the desktop background based on the current time in your location.
More dynamic wallpapers can be found at
https://github.com/karmanyaahm/awesome-plasma5-dynamic-wallpapers

%package -n %name-devel
Summary: %summary
Group: Graphical desktop/KDE

Provides: kde5-plasma-wallpapers-dynamic-devel = %EVR
Obsoletes: kde5-plasma-wallpapers-dynamic-devel < %EVR

%description -n %name-devel
A wallpaper plugin for KDE Plasma that continuously updates
the desktop background based on the current time in your location.
More dynamic wallpapers can be found at
https://github.com/karmanyaahm/awesome-plasma5-dynamic-wallpapers

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install
%find_lang --with-kde %name

%files -f %name.lang
%_bindir/kdynamicwallpaperbuilder
%_libdir/libkdynamicwallpaper.so.*
%_K6qml/com/github/zzag
%_K6plug/kpackage/packagestructure/kdynamicwallpaper.so
%_datadir/plasma/wallpapers/com.github.zzag.dynamic
%_datadir/wallpapers/Dynamic
%_datadir/locale/*/LC_MESSAGES/plasma_wallpaper_com.github.zzag.dynamic.mo
%_datadir/metainfo/com.github.zzag.dynamic.appdata.xml
%_datadir/bash-completion/completions/kdynamicwallpaperbuilder
%_datadir/fish/completions/kdynamicwallpaperbuilder.fish
%_datadir/zsh/site-functions/_kdynamicwallpaperbuilder
%doc LICENSES README.md

%files -n %name-devel
%_includedir/KDynamicWallpaper
%_K6link/libkdynamicwallpaper.so
%_libdir/cmake/KDynamicWallpaper

%changelog
* Sun Sep 29 2024 Alexander Makeenkov <amakeenk@altlinux.org> 5.0.0-alt1
- Updated to version 5.0.0.
- Build for KF6.
- Fixed license.

* Sat Jan 20 2024 Alexander Makeenkov <amakeenk@altlinux.org> 4.4.1-alt1
- Updated to version 4.4.1.

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
