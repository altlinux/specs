%define rname knotifications

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 desktop notifications

Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel
BuildRequires: libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel
BuildRequires: qt6-declarative-devel qt6-tools-devel
#BuildRequires: qt6-phonon-devel
#BuildRequires: qt6-speech-devel
#BuildRequires: libdbusmenu-qt6-devel
BuildRequires: libcanberra-devel
BuildRequires: kf6-kconfig-devel
#BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
#BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel
#BuildRequires: kf6-kiconthemes-devel kf6-kitemviews-devel kf6-kservice-devel kf6-kwidgetsaddons-devel
#BuildRequires: kf6-kwindowsystem-devel

%description
KNotification is used to notify the user of an event.
It covers feedback and persistent events.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6notifications
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6notifications
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KNotifications/
%_K6link/lib*.so
%_K6lib/cmake/KF6Notifications
#%_K6dbus_iface/*.xml

%files -n libkf6notifications
%_K6lib/libKF6Notifications.so.*
%_K6qml/org/kde/notification/


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

