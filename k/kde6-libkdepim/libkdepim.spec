%define rname libkdepim

%define sover 6
%define libkpim6libkdepim libkpim6libkdepim%sover
%define libkpim6libkdepimakonadi libkpim6libkdepimakonadi%sover

Name: kde6-%rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: PIM base library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-tools-devel-static
BuildRequires: libldap-devel libsasl2-devel
BuildRequires: akonadi-search-devel kf6-kcalendarcore-devel kf6-kcontacts-devel kldap-devel kmime-devel
BuildRequires: boost-devel akonadi-devel akonadi-mime-devel akonadi-contacts-devel akonadi-notes-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel kf6-kcmutils-devel

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

%package -n %libkpim6libkdepim
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6libkdepim
%name library

%package -n %libkpim6libkdepimakonadi
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6libkdepimakonadi
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kdepimwidgets
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
#%_K6data/kdepimwidgets/

%files devel
%_K6plug/designer/*.so
%_includedir/KPim6/Libkdepim/
%_K6link/lib*.so
%_K6lib/cmake/K*Libkdepim/
%_K6lib/cmake/*MailTransportDBusService/
%_K6dbus_iface/org.kde.*.service.xml

%files -n %libkpim6libkdepim
%_K6lib/libKPim6Libkdepim.so.%sover
%_K6lib/libKPim6Libkdepim.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

