%define rname mailcommon

%define sover 6
%define libkpim6mailcommon libkpim6mailcommon%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE6 %rname library
Url: http://www.kde.org
License: LGPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-tools-devel qt6-webengine-devel qt6-phonon-devel
BuildRequires: libgpgme-devel libassuan-devel libldap-devel libsasl2-devel xsltproc
BuildRequires: boost-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel 
BuildRequires: kf6-kdoctools-devel kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-syntax-highlighting-devel kf6-ktexttemplate-devel
BuildRequires: kmailtransport-devel kmime-devel kpimtextedit-devel kde6-libkdepim-devel mailimporter-devel
BuildRequires: messagelib-devel pimcommon-devel kde6-libkleo-devel
BuildRequires: akonadi-devel akonadi-mime-devel akonadi-contacts-devel akonadi-notes-devel
BuildRequires: kidentitymanagement-devel kimap-devel kldap-devel

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

%package -n %libkpim6mailcommon
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6mailcommon
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
%_K6plug/designer/*mailcommon*.so
%_includedir/KPim6/MailCommon/
%_K6link/lib*.so
%_libdir/cmake/K*MailCommon/

%files -n %libkpim6mailcommon
%_K6lib/libKPim6MailCommon.so.%sover
%_K6lib/libKPim6MailCommon.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

