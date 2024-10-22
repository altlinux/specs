%define rname pimcommon

%define sover 6
%define libkpim6pimcommon libkpim6pimcommon%sover
%define libkpim6pimcommonakonadi libkpim6pimcommonakonadi%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: PIM common library
Url: http://www.kde.org
License: GPL-2.0-only AND LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-tools-devel
BuildRequires: libsasl2-devel xsltproc
BuildRequires: boost-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-purpose-devel kf6-kcmutils-devel kf6-ktexttemplate-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kldap-devel akonadi-search-devel grantleetheme-devel
BuildRequires: akonadi-devel akonadi-mime-devel akonadi-contacts-devel akonadi-notes-devel
BuildRequires: kimap-devel kmime-devel kpimtextedit-devel kde6-libkdepim-devel
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

%package -n %libkpim6pimcommon
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6pimcommon
%name library

%package -n %libkpim6pimcommonakonadi
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6pimcommonakonadi
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
%_includedir/KPim6/PimCommon*/
%_K6link/lib*.so
%_K6lib/cmake/K*PimCommon*/
%_K6plug/designer/*.so

%files -n %libkpim6pimcommon
%_K6lib/libKPim6PimCommon.so.%sover
%_K6lib/libKPim6PimCommon.so.*
%files -n %libkpim6pimcommonakonadi
%_K6lib/libKPim6PimCommonAkonadi.so.%sover
%_K6lib/libKPim6PimCommonAkonadi.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

