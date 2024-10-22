%define rname libkcddb

%define sover 5
%define libkcddb libkcddb6_%sover

Name: kde6-%rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE CDDB library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libmusicbrainz5-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdoctools-devel kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-kcmutils-devel

%description
KDE CDDB library.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-libkcddb-common = %EVR
Obsoletes: kde5-libkcddb-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkcddb
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkf5cddb5 < %EVR
%description -n %libkcddb
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_K6cfg/*kcddb*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KCddb*/
%_K6link/lib*.so
%_K6lib/cmake/KCddb*/
%_K6archdata/mkspecs/modules/qt_KCddb.pri

%files -n %libkcddb
%_K6lib/libKCddb6.so.%sover
%_K6lib/libKCddb6.so.*
%_K6plug/plasma/kcms/systemsettings_qwidgets/*cddb*.so
%_K6xdgapp/*cddb*.desktop


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

