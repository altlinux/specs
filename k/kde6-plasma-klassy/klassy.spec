%define nameS klassy

Name: kde6-plasma-klassy
Version: 6.4.0
Release: alt1

Summary: Klassy is a highly customizable binary Window Decoration, Application Style and Global Theme plugin for recent versions of the KDE Plasma desktop
License: MIT and BSD-3-Clause and CC0-1.0 and GPL-2.0-only and GPL-3.0-only
Group: Graphical desktop/KDE

Url: https://github.com/paulmcauley/klassy
Vcs: https://github.com/paulmcauley/klassy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules gcc-c++ qt6-base-devel kf6-kwindowsystem-devel
BuildRequires: kf6-frameworkintegration-devel kf6-kcmutils-devel qt6-svg-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcolorscheme-devel kf6-kconfig-devel kf6-kirigami-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel pkgconfig(Qt6Qml)
BuildRequires: plasma6-kdecoration-devel kf6-kwidgetsaddons-devel kf6-kconfigwidgets-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kde-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%K6cmake -DBUILD_QT5=OFF
%K6make

%install
%K6install

%files
%_bindir/%nameS-settings
%_libdir/qt6/plugins/*/*.so
%_libdir/qt6/plugins/org.kde.kdecoration?.kcm/klassydecoration/*/*.klpw
%_libdir/libklassycommon?.so.*
%_datadir/applications/*.desktop
%_datadir/color-schemes/*.colors
%_iconsdir/hicolor/scalable/apps/*.svgz
%_iconsdir/%nameS/*/*.svg
%_iconsdir/%nameS/index.theme
%_iconsdir/%nameS-dark/*/*.svg
%_iconsdir/%nameS-dark/index.theme
%_datadir/kstyle/themes/%nameS.themerc
%_datadir/plasma/*

%files common
%doc *.md LICENSES

%files devel
%_libdir/cmake/Klassy

%changelog
* Thu Jun 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 6.4.0-alt1
- 6.3.5 -> 6.4.0

* Fri May 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 6.3.5-alt1
- Initial build for ALT Linux.
