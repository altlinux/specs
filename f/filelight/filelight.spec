%define rname filelight

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Graphical disk usage information
Url: http://www.kde.org
License:  GPL-2.0-only or GPL-3.0-only

Provides: kde5-filelight = %EVR
Obsoletes: kde5-filelight < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-declarative-devel qt6-svg-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel  kf6-kdoctools kf6-kdoctools-devel kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel kf6-kpackage-devel kf6-kdeclarative-devel

%description
%summary.

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

%package -n libkf6filelight
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkf6filelight
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%config(noreplace) %_K6xdgconf/filelightrc
%_K6bin/filelight
%_K6xdgapp/org.kde.filelight.desktop
%_K6icon/*/*/*/*filelight.*
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

