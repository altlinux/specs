%define rname kstatusnotifieritem

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: Implementation of Status Notifier Items
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-tools-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: libfreetype-devel fontconfig-devel

%description
Implementation of Status Notifier Items.

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

%package -n libkf6statusnotifieritem
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6statusnotifieritem
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
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KStatusNotifierItem/
%_K6link/lib*.so
%_K6lib/cmake/KF6StatusNotifierItem
%_K6dbus_iface/*StatusNotifier*.xml

%files -n libkf6statusnotifieritem
%_K6lib/libKF6StatusNotifierItem.so.*


%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon Jun 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- initial build

