%define rname baloo-widgets

Name: %rname
Version: 24.08.1
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: Baloo Widgets
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libxapian-devel
BuildRequires: kf6-baloo-devel kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kfilemetadata-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-baloo-widgets-common = %EVR
Obsoletes: kde5-baloo-widgets-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6baloowidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkf5baloowidgets < %EVR
%description -n libkf6baloowidgets
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DBUILD_WITH_QT6:BOOL=ON \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6bin/baloo_filemetadata_temp_extractor
%_K6inc/BalooWidgets/
%_K6link/lib*.so
%_K6lib/cmake/KF6BalooWidgets/

%files -n libkf6baloowidgets
%dir %_K6plug/kf6/propertiesdialog/
%_K6lib/libKF6BalooWidgets.so.*
%_K6plug/kf6/kfileitemaction/*.so
%_K6plug/kf6/propertiesdialog/*.so


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

