%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: lomiri-music-app
Version: 3.3.0
Release: alt1

Summary: Music player for Lomiri Operating Environment
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/apps/lomiri-music-app

Source: %name-%version.tar

# sync with version 3.3.0-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Qml)

Requires: libmediascanner2
Requires: libqt5-qml
Requires: libqt5-quick
Requires: libqt5-quickparticles
Requires: libusermetrics
Requires: lomiri-thumbnailer
Requires: mpris-qt5-devel
Requires: qml(Lomiri.Components)
Requires: qml(Lomiri.Content)
Requires: qml(Lomiri.Layouts)
Requires: qml(Lomiri.PerformanceMetrics)
Requires: qml(QtMultimedia)

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Music (Player) App.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCLICK_MODE=OFF \
       -DINSTALL_TESTS=OFF \
       -DADD_MPRIS=ON
%cmake_build

%install
%cmake_install

rm -vf %buildroot%_datadir/lomiri-music-app/app/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/components/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/components/Delegates/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/components/Dialog/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/components/Flickables/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/components/HeadState/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/components/Helpers/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/components/ListItemActions/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/components/ViewButton/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/components/Walkthrough/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/graphics/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/logic/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/src/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/app/ui/CMakeLists.txt
rm -vf %buildroot%_datadir/lomiri-music-app/lomiri-music-app-migrate.py

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog LICENSE.txt NEWS README.md
%_bindir/lomiri-music-app
%_desktopdir/lomiri-music-app.desktop
%_datadir/lomiri-content-hub/peers/lomiri-music-app
%dir %_datadir/lomiri-music-app
%_datadir/lomiri-music-app/*
%_datadir/lomiri-url-dispatcher/urls/lomiri-music-app.url-dispatcher

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-music-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-music-app.mo

%changelog
* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus
