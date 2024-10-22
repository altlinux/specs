%define rname kidentitymanagement

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Manage PIM identity
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kpimtextedit-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kirigami-addons-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel
BuildRequires: kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kf6-ktextaddons-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6identitymanagementcore
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6identitymanagementcore
%name library

%package -n libkpim6identitymanagementquick
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6identitymanagementquick
%name library

%package -n libkpim6identitymanagementwidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6identitymanagementwidgets
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_includedir/KPim6/KIdentityManagement*/
%_K6link/lib*.so
%_K6lib/cmake/K*IdentityManagement*/
%_K6dbus_iface/*.IdentityManager.xml

%files -n libkpim6identitymanagementcore
%_K6lib/libKPim6IdentityManagementCore.so.*
%files -n libkpim6identitymanagementquick
%_K6lib/libKPim6IdentityManagementQuick.so.*
%_K6qml/org/kde/kidentitymanagement/
%files -n libkpim6identitymanagementwidgets
%_K6lib/libKPim6IdentityManagementWidgets.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

