%define rname kscreen

%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

Name: %rname
Version: 6.7.2
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Display Management software
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: xrandr iio-sensor-proxy
Requires: libkf6itemmodels
Requires: plasma6-libkscreen-utils plasma6-plasma5support
Provides: plasma5-kscreen = %EVR
Obsoletes: plasma5-kscreen < %EVR

Source: %rname-%version.tar
Source10: kcm_kscreen-ru-add.po
Source11: kscreen-ru-add.po
Patch1: alt-enable-per-screen-scaling.patch
Patch2: alt-improve-output-names.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-sensors-devel qt6-wayland-devel
BuildRequires: plasma-wayland-protocols
BuildRequires: libxcbutil-devel libXi-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kitemviews-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-ksvg-devel
BuildRequires: kf6-sonnet-devel kf6-kdeclarative-devel kf6-kpackage-devel kf6-kcmutils-devel kf6-kirigami-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: plasma6-layer-shell-qt-devel plasma6-libkscreen-devel plasma6-lib-devel
BuildRequires: plasma6-plasma5support plasma6-plasma5support-devel

%description
KCM and KDED modules for managing displays in KDE.

%prep
%setup -n %rname-%version
#%patch1 -p1
#%patch2 -p1

sed -i 's|^\(add_subdirectory.*tests.*\)|#\1|' CMakeLists.txt

msgcat --use-first %SOURCE10 po/ru/kcm_kscreen.po > po/ru/kcm_kscreen.po.tmp
cat po/ru/kcm_kscreen.po.tmp > po/ru/kcm_kscreen.po
rm -f po/ru/kcm_kscreen.po.tmp
msgcat --use-first %SOURCE11 po/ru/kscreen_common.po > po/ru/kscreen_common.po.tmp
cat po/ru/kscreen_common.po.tmp > po/ru/kscreen_common.po
rm -f po/ru/kscreen_common.po.tmp

%build
%K6build

%install
%K6install
%K6install_move data locale kpackage
%find_lang %name --all-name

%files -f %name.lang
%_datadir/qlogging-categories6/*.*categories
%_K6bin/*kscreen*
%_K6bin/*calibrator*
%_K6plug/plasma/kcms/systemsettings/*kscreen*.so
%_K6plug/kf6/kded/*kscreen*.so
%_K6plug/plasma/applets/*kscreen*.so
%_K6xdgapp/*kscreen*.desktop
#%_K6data/plasma/plasmoids/org.kde.kscreen/
%_K6data/kglobalaccel/*kscreen*.desktop
#%_K6data/kscreen/
%_userunitdir/*kscreen*.service
%_K6libexecdir/kscreen_osd_service
%_K6dbus_srv/*kscreen*.service
#%_datadir/metainfo/*.xml


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

