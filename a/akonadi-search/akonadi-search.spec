%define rname akonadi-search

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Akonadi searching implementation
Url: http://www.kde.org
License: LGPL-2.1-or-later

Provides: kde5-akonadi-search = %EVR
Obsoletes: kde5-akonadi-search < %EVR
Requires: akonadi

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: boost-devel-headers libical-devel libxapian-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kcalendarcore-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-krunner-devel kf6-kpackage-devel kf6-kcmutils-devel kf6-kcontacts-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: akonadi-devel kmime-devel akonadi-mime-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-akonadi-search-common = %EVR
Obsoletes: kde5-akonadi-search-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6akonadisearchxapian
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6akonadisearchxapian
%name library

%package -n libkpim6akonadisearchcore
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6akonadisearchcore
%name library

%package -n libkpim6akonadisearchpim
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6akonadisearchpim
%name library

%package -n libkpim6akonadisearchdebug
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6akonadisearchdebug
%name library


%prep
%setup -n %rname-%version

# disable krunner by default
sed -i '/EnabledByDefault/s|true|false|' runner/plasma-krunner-pimcontacts.json*

%build
%K6build

%install
%K6install
%K6install_move data akonadi
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*
%_K6plug/pim6/akonadi/*.so
%_K6plug/kf6/krunner/*krunner*.so
%_K6plug/kf6/krunner/kcms/*krunner*.so
%_datadir/akonadi/agents/*.desktop

%files devel
%_includedir/KPim6/AkonadiSearch/
%_K6link/lib*.so
%_K6lib/cmake/K*AkonadiSearch/

%files -n libkpim6akonadisearchxapian
%_K6lib/libKPim6AkonadiSearchXapian.so.*
%files -n libkpim6akonadisearchcore
%_K6lib/libKPim6AkonadiSearchCore.so.*
%files -n libkpim6akonadisearchpim
%_K6lib/libKPim6AkonadiSearchPIM.so.*
%files -n libkpim6akonadisearchdebug
%_K6lib/libKPim6AkonadiSearchDebug.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

