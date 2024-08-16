%define rname oxygen

%define sover 6
%define liboxygenstyle6 liboxygenstyle6_%sover
%define liboxygenstyleconfig6 liboxygenstyleconfig6_%sover
%define liboxygenstyle5 liboxygenstyle5_%sover
%define liboxygenstyleconfig5 liboxygenstyleconfig5_%sover

Name: plasma6-%rname
Version: 6.1.4
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma visual style
Url: http://www.kde.org
License: GPL-2.0-or-later

#Requires: icon-theme-oxygen

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-frameworkintegration-devel kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kitemviews-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kcmutils-devel kf6-frameworkintegration-devel kf6-kcolorscheme-devel kf6-kpackage-devel
BuildRequires: plasma6-lib-devel plasma6-kdecoration-devel plasma6-kwayland-devel
#
BuildRequires: rpm-build-kf5
BuildRequires: qt5-x11extras-devel qt5-declarative-devel
BuildRequires: kf5-frameworkintegration-devel kf5-kconfig-devel kf5-kwindowsystem-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kservice-devel kf5-kcompletion-devel

%description
Artwork, styles and assets for the Oxygen visual style for the Plasma Desktop.
%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-oxygen-common = 1:%version-%release
Obsoletes: plasma5-oxygen-common < 1:%version-%release
%description common
%name common package

%package -n %liboxygenstyle6
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %liboxygenstyle6
%name library

%package -n %liboxygenstyleconfig6
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %liboxygenstyleconfig6
%name library

%package -n %liboxygenstyle5
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %liboxygenstyle5
%name library

%package -n %liboxygenstyleconfig5
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %liboxygenstyleconfig5
%name library

%package -n plasma5-oxygen
Summary: KDE Plasma visual style
Group: Graphical desktop/KDE
Epoch: 1
Requires: %name-common >= %version-%release
%description -n plasma5-oxygen
Artwork, styles and assets for the Oxygen visual style for the Plasma Desktop.

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
    -DKDE_INSTALL_DATADIR=%_K5data \
    -DICON_INSTALL_DIR=%_iconsdir \
    -DBUILD_QT6:BOOL=OFF \
    -DBUILD_QT5:BOOL=ON \
    #

%install
%K5install
%K6install
%K6install_move data kstyle sounds plasma color-schemes
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/*6
%_K6plug/org.kde.kdecoration2*/*.so
%_K6plug/styles/oxygen*.so
%_K6plug/kstyle_config/*oxygen*.so
%_iconsdir/Oxygen_*/
%_iconsdir/*/*/apps/oxygen-settings.*
%_iconsdir/KDE_Classic/
%_K6xdgapp/*oxygen*.desktop
%_K6data/color-schemes/*
%_K6data/plasma/look-and-feel/org.kde.oxygen/
%_K6data/kstyle/themes/oxygen.themerc
%_datadir/metainfo/*oxygen*.xml

%files -n plasma5-oxygen
%_K5bin/*5
%_K5plug/styles/oxygen*.so

%files -n %liboxygenstyle6
%_K6lib/liboxygenstyle6.so.*
%_K6lib/liboxygenstyle6.so.%sover
%files -n %liboxygenstyleconfig6
%_K6lib/liboxygenstyleconfig6.so.*
%_K6lib/liboxygenstyleconfig6.so.%sover
%files -n %liboxygenstyle5
%_K6lib/liboxygenstyle5.so.*
%_K6lib/liboxygenstyle5.so.%sover
%files -n %liboxygenstyleconfig5
%_K6lib/liboxygenstyleconfig5.so.*
%_K6lib/liboxygenstyleconfig5.so.%sover



%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

