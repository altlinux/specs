%define rname kirigami-app-components

%define sover 6
%define libkirigamiaddonsstatefulapp libkirigamiaddonsstatefulapp%sover
%define libkirigamiapp libkirigamiapp%sover
%define libkirigamiactioncollection libkirigamiactioncollection%sover

Name: kf6-%rname
Version: 1.0.2
Release: alt1
%K6init

Group: System/Libraries
Summary: Full featured KDE application QML addon
License: BSD-3-Clause AND CC0-1.0 AND FSFAP AND LGPL-2.0-or-later AND LGPL-2.1-or-later
Url:  https://invent.kde.org/libraries/kirigami-addons


Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-tools-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-ki18n-devel kf6-kconfig-devel kf6-kirigami-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kguiaddons-devel kf6-kcolorscheme-devel kf6-kcrash-devel kf6-kiconthemes-devel

%description
This project contains Kirigami addons and modules necessary to do a full featured KDE application,
such as integration with configurable keyboard shortcuts and standard actions for About application About KDE, Donate etc.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
This package contains the development files for %name.

%package -n %libkirigamiactioncollection
Group: System/Libraries
Summary: %name library
#Requires: libqt6-quicklayouts libqt6-quickcontrols2 libqt6-quick
Requires: kf6-kirigami libkf6i18nqml libkf6coreaddons
%description -n %libkirigamiactioncollection
%name library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
#find_lang %name --with-kde --all-name

%files devel
%_K6inc/Kirigami/ActionCollection/
%_libdir/cmake/KF?KirigamiAppComponents/
%_K6link/lib*.so

%files -n %libkirigamiactioncollection
%doc LICENSES/*
%_K6qml/org/kde/kirigami/actioncollection/
%_K6lib/libKirigamiActionCollection.so.%sover
%_K6lib/libKirigamiActionCollection.so.*

%changelog
* Thu Sep 03 2026 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- initial build
