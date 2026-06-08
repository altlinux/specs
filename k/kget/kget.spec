%define rname kget

%define sover 6
%define libkgetcore libkgetcore%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Networking/File transfer
Summary: Download Manager for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later and LGPL-2.1-or-later

Provides:  kde5-kget = %EVR
Obsoletes: kde5-kget < %EVR

Requires: kf6-kio

Source: %rname-%version.tar
Patch1: alt-dbus-service.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: boost-devel-headers libgpgme-devel libassuan-devel libmms-devel libqca-qt6-devel libsqlite3-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel
BuildRequires: kde6-libktorrent-devel

%description
KGet is a versatile and user-friendly download manager.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-kget-common = %EVR
Obsoletes: kde5-kget-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkgetcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
Obsoletes: libkgetcore5 < %EVR
%description -n %libkgetcore
KF6 library

%prep
%setup -n %rname-%version
%patch1 -p1
#sed -i '/^find_package(KF6Torrent/d' CMakeLists.txt

%build
%K6build \
    #

%install
%K6install
%K6install_move data kget khtml kwebkitpart dolphinpart kconf_update kio
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*
%_K6plug/kget/
%_K6plug/kget_kcms/
%_K6icon/*/*/apps/*kget.*
%_K6cfg/kget*
%_K6data/kget/
%_K6xdgapp/*kget*
%_K6notif/kget*
%_K6data/kio/servicemenus/kget_*.desktop
%_K6dbus_srv/*kget*
%_datadir/metainfo/*kget*.xml

#%files devel
#%_K6inc/kget
#%_K6link/lib*.so
#%_K6lib/cmake/KGet/
#%_K6dbus_iface/org.freedesktop.KGet.xml

%files -n %libkgetcore
%_K6lib/libkgetcore.so.*
%_K6lib/libkgetcore.so.%sover


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

