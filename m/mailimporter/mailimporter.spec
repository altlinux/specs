%define rname mailimporter

%define sover 6
%define libkpim6mailimporter libkpim6mailimporter%sover
%define libkpim6mailimporterakonadi libkpim6mailimporterakonadi%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: %rname library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-tools-devel
BuildRequires: boost-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel 
BuildRequires: kf6-kdoctools-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel
BuildRequires: kimap-devel grantleetheme-devel kmime-devel kde6-libkdepim-devel
BuildRequires: akonadi-devel akonadi-mime-devel akonadi-contacts-devel akonadi-notes-devel
BuildRequires: pimcommon-devel kpimtextedit-devel

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpim6mailimporter
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6mailimporter
%name library

%package -n %libkpim6mailimporterakonadi
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6mailimporterakonadi
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
%_includedir/KPim6/MailImporter*/
%_K6link/lib*.so
%_K6lib/cmake/K*MailImporter*/

%files -n %libkpim6mailimporter
%_K6lib/libKPim6MailImporter.so.%sover
%_K6lib/libKPim6MailImporter.so.*

%files -n %libkpim6mailimporterakonadi
%_K6lib/libKPim6MailImporterAkonadi.so.%sover
%_K6lib/libKPim6MailImporterAkonadi.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

