%define rname kwalletmanager

Name: %rname
Version: 26.04.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Wallet Manager
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-kwalletmanager = %EVR
Obsoletes: kde5-kwalletmanager < %EVR

Source: %rname-%version.tar
Patch0: alt-fix-display-handbook.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
%summary.

%prep
%setup -n %rname-%version
%patch0 -p1
cp -ar po/ru/docs/kwalletmanager po/ru/docs/kwalletmanager5

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_bindir/kwalletmanager*
%_K6bin/kwalletmanager*
%_K6icon/*/*/*/*wallet*
%_K6exec/kauth/kcm_kwallet_helper*
%_K6plug/plasma/kcms/systemsettings_qwidgets/*kwallet*.so
%_datadir/dbus-1/services/*kwallet*.service
%_K6dbus_sys_srv/*kwallet*.service
%_K6dbus/system.d/*kwallet*.conf
%_K6xdgapp/*kwallet*.desktop
%_datadir/qlogging-categories6/*.*categories
%_datadir/polkit-1/actions/*kwallet5*.policy
%_datadir/metainfo/*.xml

%changelog
* Fri May 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Mon Sep 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Thu Jul 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Tue Jun 10 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Mon May 12 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Apr 21 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.0-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Tue Feb 18 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Jan 20 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Wed Nov 13 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Oct 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build
