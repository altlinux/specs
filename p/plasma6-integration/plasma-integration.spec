%define rname plasma-integration

Name: plasma6-integration
Version: 6.1.5
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma integration of Qt applications
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: %name-common >= %EVR

Source: %rname-%version.tar
Patch1: alt-def-font.patch
Patch2: alt-singleclick.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-wayland-devel
BuildRequires: libxcb-devel libXres-devel libXcursor-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kstatusnotifieritem-devel
BuildRequires: plasma-wayland-protocols
BuildRequires: plasma6-kwayland-devel plasma6-breeze-devel
#
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-declarative-devel qt5-wayland-devel qt5-quickcontrols2-devel qt5-x11extras-devel qt5-base-devel-static
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kwayland-devel kf5-knotifications-devel kf5-kwindowsystem-devel kf5-kguiaddons-devel kf5-kxmlgui-devel


%description
Plasma Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

%package -n plasma5-integration
Summary: %{summary}
Group: Graphical desktop/KDE
Epoch: 1
Requires: %name-common >= %version-%release
%description -n plasma5-integration
Plasma Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-integration-common = 1:%version-%release
Obsoletes: plasma5-integration-common < 1:%version-%release
%description common
%name common package

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%define _K6buildsubdir BUILD6
%K6build \
    -DCMAKE_DISABLE_FIND_PACKAGE_FontNotoSans=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_FontNotoColorEmoji=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_FontHack=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_XDGDesktopPortalKDE=ON \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DBUILD_QT6:BOOL=ON \
    -DBUILD_QT5:BOOL=OFF \
    #
%K5build \
    -DCMAKE_DISABLE_FIND_PACKAGE_FontNotoSans=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_FontNotoColorEmoji=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_FontHack=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_XDGDesktopPortalKDE=ON \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DBUILD_QT6:BOOL=OFF \
    -DBUILD_QT5:BOOL=ON \
    #

%install
%K5install
%K6install
%find_lang %name --all-name
# cleanup
#rm -f %_K6data/kconf_update/fonts_* ||:

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6plug/platformthemes/KDEPlasmaPlatformTheme6.so

%files -n plasma5-integration
%_K5plug/platformthemes/KDEPlasmaPlatformTheme5.so

%changelog
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

