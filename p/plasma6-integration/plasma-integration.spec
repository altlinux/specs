%define rname plasma-integration

Name: plasma6-integration
Version: 6.7.2
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
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

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

