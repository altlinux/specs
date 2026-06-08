%define rname kmix

%define sover 6
%define libkmixcore libkmixcore%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Sound
Summary: KDE sound mixer
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kmix = %EVR
Obsoletes: kde5-kmix < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libalsa-devel libcanberra-devel libpulseaudio-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kpackage-devel
BuildRequires: kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel kf6-kstatusnotifieritem-devel

%description
A sound mixer applet for KDE.
It allows you to control the volumes of your
sound card from a KDE panel applet.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides:  kde5-kmix-common = %EVR
Obsoletes: kde5-kmix-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkmixcore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkmixcore
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DBUILD_DATAENGINE:BOOL=OFF \
    #

%install
%K6install
%K6install_move data kmix
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories?/*.*categories

%files
%_K6bin/*
%_K6start/*.desktop
%_K6data/kmix/
%_K6cfg/*kmix*.kcfg
%_K6data/kxmlgui?/kmix/
%_K6xdgapp/*kmix.desktop
%_K6notif/*kmix*.notifyrc
%_K6icon/*/*/actions/*kmix.*
%_datadir/metainfo/*.xml

%files devel
%_K6dbus_iface/*.xml

%files -n %libkmixcore
%_K6lib/libkmixcore.so.*
%_K6lib/libkmixcore.so.%sover

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

* Fri Dec 06 2024 Sergey V Turchin <zerg@altlinux.org> 24.11.90-alt1
- beta with KF6

* Mon Oct 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build
