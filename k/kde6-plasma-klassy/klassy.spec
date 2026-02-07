%define nameS klassy
%define soname 6

Name: kde6-plasma-klassy
Version: 6.5.2
Release: alt1
Epoch: 1

Summary: Klassy is a highly customizable plugin for KDE Plasma
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
Klassy is a highly customizable binary Window Decoration, Application Style and Global Theme
plugin for recent versions of the KDE Plasma desktop.

%package common
Summary: Klassy common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
Klassy common package.

%package devel
Group: Development/KDE and QT
Summary: Development files for Klassy
Requires: kde-common
Requires: libklassycommon%soname = %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use Klassy.

%package -n libklassycommon%soname
Group: System/Libraries
Summary: Klassy library
Requires: %name-common
%description -n libklassycommon%soname
Klassy library.

%prep
%setup

%build
%K6cmake -DBUILD_QT5=OFF
%K6make

%install
%K6install

%find_lang %nameS --with-kde --all-name

%files -f %nameS.lang
%_bindir/%nameS-settings
%_libdir/qt6/plugins/*/*.so
%_libdir/qt6/plugins/org.kde.kdecoration?.kcm/klassydecoration/*/*.klpw
%_datadir/applications/*.desktop
%_datadir/color-schemes/*.colors
%_iconsdir/hicolor/scalable/apps/*.svgz
%_iconsdir/%{nameS}*
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

%files -n libklassycommon%soname
%_K6lib/libklassycommon?.so.%soname
%_K6lib/libklassycommon?.so.%{soname}.*

%changelog
* Sun Feb 08 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:6.5.2-alt1
- 6.5.1 -> 6.5.2

* Sat Feb 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:6.5.1-alt1
- 6.5 -> 6.5.1

* Thu Feb 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:6.5-alt1
- 6.4 -> 6.5

* Sun Feb 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:6.4-alt1
- updated to git.2e76a993d4

* Thu Jun 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 6.4.0-alt1
- 6.3.5 -> 6.4.0

* Fri May 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 6.3.5-alt1
- Initial build for ALT Linux.
