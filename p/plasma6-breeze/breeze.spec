%define rname breeze

%define breezecommon_sover 6
%define libbreezecommon libbreezecommon%breezecommon_sover

Name: plasma6-%rname
Version: 6.7.2
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
Patch1: alt-defaults.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
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
%patch1 -p1

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
%K6install_move data kconf_update wallpapers

%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_bindir/*6
%_K6bin/*
%_K6plug/org.kde.kdecoration?/*.so
%_K6plug/styles/*.so
%_K6plug/kstyle_config/*.so
%_K6plug/org.kde.kdecoration?.kcm/*.so
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
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Mon May 18 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt2
- disable window outline by default

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

