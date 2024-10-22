%define rname incidenceeditor

%define sover 6
%define libkpim6incidenceeditor libkpim6incidenceeditor%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

ExcludeArch: %not_qt6_qtwebengine_arches

Group: System/Libraries
Summary: KDE6 %rname library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: boost-devel
BuildRequires: libldap-devel libsasl2-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel 
BuildRequires: kf6-kdoctools-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-ktexttemplate-devel
BuildRequires: kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel
BuildRequires: kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kde6-kdiagram-devel
BuildRequires: akonadi-calendar-devel calendarsupport-devel eventviews-devel kf6-kcalendarcore-devel kcalutils-devel
BuildRequires: kf6-kcontacts-devel kidentitymanagement-devel kldap-devel kmailtransport-devel
BuildRequires: kmime-devel kpimtextedit-devel kde6-libkdepim-devel 
BuildRequires: akonadi-devel akonadi-mime-devel akonadi-contacts-devel akonadi-notes-devel
BuildRequires: pimcommon-devel kimap-devel

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

%package -n %libkpim6incidenceeditor
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6incidenceeditor
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
%_includedir/KPim6/IncidenceEditor/
%_K6link/lib*.so
%_libdir/cmake/K*IncidenceEditor/

%files -n %libkpim6incidenceeditor
%_K6lib/libKPim6IncidenceEditor.so.%sover
%_K6lib/libKPim6IncidenceEditor.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

