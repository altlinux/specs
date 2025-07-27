%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: lomiri-gallery-app
Version: 3.1.1
Release: alt1

Summary: Gallery App for Lomiri Operating Environment
License: GPL-3.0-only and CC-3.0-BY-SA
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/apps/lomiri-gallery-app

Source: %name-%version.tar

# sync with version 3.1.1-1 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(libmediainfo)

Requires: lomiri-gallery-app-common

Requires: libqt5-quick
Requires: lomiri-thumbnailer
Requires: qml(Lomiri.Components)
Requires: qml(Lomiri.Components.Extras)
Requires: qml(Lomiri.Layouts)
Requires: qml(Lomiri.Content)
Requires: qqc2-suru-style

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Gallery App.

%package common
Summary: Gallery App for Lomiri Operating Environment (arch-indep files)
Group: Graphical desktop/Other
BuildArch: noarch

%description common
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides the arch-indep files of Lomiri's Gallery App.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCLICK_MODE=OFF \
       -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%find_lang %name

%files
%doc AUTHORS ChangeLog COPYING COPYING.CC-3.0-BY-SA NEWS README.md
%_bindir/lomiri-gallery-app

%files common -f %{name}.lang
%_desktopdir/lomiri-gallery-app.desktop
%_datadir/lomiri-content-hub/peers/lomiri-gallery-app
%dir %_datadir/lomiri-gallery-app
%_datadir/lomiri-gallery-app/*
%_datadir/lomiri-url-dispatcher/urls/lomiri-gallery-app.url-dispatcher
%_iconsdir/hicolor/128x128/apps/lomiri-gallery-app.png
%_iconsdir/hicolor/256x256/apps/lomiri-gallery-app.png
%_iconsdir/hicolor/64x64/apps/lomiri-gallery-app.png
%_iconsdir/hicolor/scalable/apps/lomiri-gallery-app.svg

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-gallery-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-gallery-app.mo

%changelog
* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
