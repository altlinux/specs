%define rname akonadi-import-wizard

%define sover 6
%define libkpimimportwizard libkpim6importwizard%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Akonadi Import Wizard
Url: http://www.kde.org
License: LGPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches
Provides: kde5-akonadi-import-wizard = %EVR
Obsoletes: kde5-akonadi-import-wizard < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: boost-devel libassuan-devel libdb4-devel libsasl2-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdoctools-devel kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kwallet-devel kf6-karchive-devel kf6-kiconthemes-devel kf6-ktexttemplate-devel
BuildRequires: kde6-libkleo-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel kf6-kcontacts-devel kidentitymanagement-devel
BuildRequires: kimap-devel kmailtransport-devel kmime-devel kpimtextedit-devel kde6-libkdepim-devel mailcommon-devel
BuildRequires: mailimporter-devel messagelib-devel pimcommon-devel


%description
Import Wizard allows to import emails, settings, addressbook and calendar data detected in
your user account to Akonadi.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-akonadi-import-wizard-common = %EVR
Obsoletes: kde5-akonadi-import-wizard-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpimimportwizard
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkpimimportwizard5 < %EVR
%description -n %libkpimimportwizard
%name library

%prep
%setup -n %rname-%version
sed -i '/DESTINATION/s/\${KDE_INSTALL_INCLUDEDIR}\/KPim\//${KDE_INSTALL_INCLUDEDIR_KF6}/' src/libimportwizard/CMakeLists.txt

%build
%K6build

%install
%K6install
%K6install_move data kconf_update importwizard
%find_lang %name --with-kde --all-name

%files common -f %name.lang

%files
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/*importwizard*
%_K6plug/pim6/importwizard/
%_K6data/*importwizard*/
%_K6xdgapp/*importwizard*.desktop
%_K6icon/*/*/apps/*import-wizard*

%files devel
%_includedir/KPim6/?mport?izard/
%_K6link/lib*.so
%_K6lib/cmake/K*ImportWizard/

%files -n %libkpimimportwizard
%_K6lib/libKPim6ImportWizard.so.%sover
%_K6lib/libKPim6ImportWizard.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

