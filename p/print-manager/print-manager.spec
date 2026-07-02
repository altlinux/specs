%define rname print-manager

%def_disable installer

%define sover 6
%define libkcups libkcups%sover

Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: System/Configuration/Printing
Summary: Printer management for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-print-manager = 1:%version-%release
Obsoletes: kde5-print-manager < 1:%version-%release

Requires: cups
Requires: /usr/lib/cups/backend/smb /usr/bin/smbspool
#Requires: printer-drivers-X11
Requires: system-config-printer-lib
Requires: system-config-printer-udev
Requires: libkf6itemmodels kf6-kdeclarative kf6-kconfig

Source: %rname-%version.tar
Source10: add-ppdtranslations-ru.po
Patch1: alt-lib-sover.patch
Patch2: alt-queue-window.patch
Patch3: alt-print-opts-i18n.patch

# PackageKitQt6-for-system-config-printer
BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: /usr/bin/msgcat
BuildRequires: libvulkan-devel
BuildRequires: libcups-devel
%if_enabled installer
BuildRequires: packagekit-qt6-devel
%endif
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kpackage-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-kirigami-devel kf6-kitemmodels-devel
BuildRequires: kf6-kdeclarative kf6-kdeclarative-devel
BuildRequires: kf6-kconfig kf6-kconfig-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: plasma6-lib-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-print-manager-common = 1:%version-%release
Obsoletes: kde5-print-manager-common < 1:%version-%release
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkcups
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
Obsoletes: libkcupslib0.2 < 1:%version-%release
Obsoletes: libkcupslib6 < %EVR
%description -n %libkcups
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1
#%patch2 -p1
%patch3 -p1

tmp_file=`mktemp`
msgcat --use-first po/ru/print-manager.po %SOURCE10 >"$tmp_file"
cat "$tmp_file" >po/ru/print-manager.po
msgcat --use-first po/ru/plasma_applet_org.kde.plasma.printmanager.po %SOURCE10 >"$tmp_file"
cat "$tmp_file" >po/ru/plasma_applet_org.kde.plasma.printmanager.po
rm -f "$tmp_file"

%if_enabled installer
%else
sed -i '/find_package.*PackageKitQt6/s|PackageKitQt6|PackageKitQt6--for-system-config-printer-install|' CMakeLists.txt
%endif

%build
%K6build \
%if_enabled installer
    DSCP_PACKAGE_NAME=system-config-printer \
%else
    -DSCP_INSTALL:BOOL=OFF \
%endif
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/configure-printer
%_K6bin/plasma-print-queue
%_K6plug/plasma/kcms/systemsettings/*printer*.so
%_K6plug/kf6/kded/*print*.so
%_K6plug/plasma/applets/*print*.so
%_K6xdgapp/*rint*.desktop
%_K6qml/org/kde/plasma/printmanager/
%_K6notif/printmanager.notifyrc
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*print*.xml

%files -n %libkcups
%_K6lib/libkcups.so.%sover
%_K6lib/libkcups.so.*

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

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- initial build
