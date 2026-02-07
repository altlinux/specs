%define _unpackaged_files_terminate_build 1

Name: kf6-qqc2-breeze-style
Version: 6.5.91
Release: alt1

Summary: Breeze inspired QQC2 Style
License: LGPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/plasma/qqc2-breeze-style

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)

BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kiconthemes-devel

Requires: kf6-kquickcharts

%description
This is a style for Qt Quick Controls (also known as QQC2 in Qt5)
which implements the KDE Visual Design Group's vision for Breeze
in pure Qt Quick and Kirigami.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains CMake files for
developing applications that use %name.

%prep
%setup

%build
%K6build

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README.md
%dir %_K6qml/org/kde/breeze/
%_K6qml/org/kde/breeze/*
%_K6plug/kf6/kirigami/platform/org.kde.breeze.so

%files devel
%dir %_libdir/cmake/QQC2BreezeStyle/
%_libdir/cmake/QQC2BreezeStyle/*

%changelog
* Sat Feb 07 2026 Nikolay Strelkov <snk@altlinux.org> 6.5.91-alt1
- Initial build for Sisyphus
