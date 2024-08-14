%define rname breeze

%define breezecommon_sover 6
%define libbreezecommon libbreezecommon%breezecommon_sover

Name: plasma6-%rname
Version: 6.1.2
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 visual style
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: icon-theme-breeze
Requires: %name-common >= %EVR
Conflicts: plasma5-breeze < 1:6

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-frameworkintegration-devel kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kitemviews-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kcmutils-devel  kf6-kpackage-devel kf6-kirigami-devel kf6-kcolorscheme-devel
BuildRequires: plasma6-kdecoration-devel
#
BuildRequires: rpm-build-kf5
BuildRequires: qt5-x11extras-devel qt5-declarative-devel
BuildRequires: kf5-frameworkintegration-devel kf5-kirigami-devel kf5-kconfig-devel kf5-kcodecs-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kconfigwidgets-devel kf5-kguiaddons-devel kf5-kiconthemes-devel

%description
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Conflicts: plasma5-breeze < 1:6
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kde-common
Conflicts: plasma5-breeze-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n plasma5-breeze
Group: Graphical desktop/KDE
Summary: KDE 5 visual style
Epoch: 1
Requires: %name-common >= %version-%release
%description -n plasma5-breeze
KDE 5 visual style.

%prep
%setup -n %rname-%version

%build
%define _K6buildsubdir BUILD6
%K6build \
    -DKDE_INSTALL_DATADIR=%_K6data \
    -DICON_INSTALL_DIR=%_iconsdir \
    -DBUILD_QT6:BOOL=ON \
    -DBUILD_QT5:BOOL=OFF \
    #
%K5build \
    -DKDE_INSTALL_DATADIR=%_K6data \
    -DICON_INSTALL_DIR=%_iconsdir \
    -DBUILD_QT6:BOOL=OFF \
    -DBUILD_QT5:BOOL=ON \
    #

%install
%K5install
%K6install
%K6install_move data kconf_update wallpapers

%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_bindir/*6
%_K6bin/*
%_K6plug/org.kde.kdecoration2/*.so
%_K6plug/styles/*.so
%_K6plug/kstyle_config/*.so
%_K6plug/org.kde.kdecoration2.kcm/*.so
%_K6xdgapp/*breeze*.desktop
%_K6data/QtCurve/
%_K6data/kstyle/themes/*
%_K6data/color-schemes/*
%_iconsdir/?reeze*/
%_iconsdir/hicolor/*/apps/breeze-settings.*
%_K6wall/*

%files -n plasma5-breeze
%_K5plug/styles/*.so

%files devel
%_libdir/cmake/Breeze/

%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

