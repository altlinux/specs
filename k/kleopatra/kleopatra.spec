%define rname kleopatra

%define core_sover 1
%define libkleopatraclientcore libkleopatraclientcore%core_sover
%define gui_sover 1
%define libkleopatraclientgui libkleopatraclientgui%gui_sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Certificate Manager for KDE
Url: http://www.kde.org
License: LGPL-2.1-or-later

Provides: kde5-kleopatra = %EVR
Obsoletes: kde5-kleopatra < %EVR
Requires: gnupg2 dirmngr pinentry-x11

Source: %rname-%version.tar
Patch1: alt-gpgme17.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules boost-devel qt6-declarative-devel
BuildRequires: libassuan-devel libgpgme-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-knotifications-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-sonnet-devel kf6-kitemmodels-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kcrash-devel kf6-kwallet-devel kf6-kio-devel kf6-kauth-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kconfig-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kmime-devel kde6-libkleo-devel
BuildRequires: kidentitymanagement-devel kmailtransport-devel kpimtextedit-devel akonadi-mime-devel akonadi-devel
BuildRequires: mimetreeparser-devel kmbox-devel

%description
%summary


%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-kleopatra-common = %EVR
Obsoletes: kde5-kleopatra-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkleopatraclientcore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkleopatraclientcore
%name library

%package -n %libkleopatraclientgui
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkleopatraclientgui
%name library

%prep
%setup -n %rname-%version
#%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data kleopatra kwatchgnupg kconf_update kio locale

mv %buildroot/%_datadir/mime/packages/application-vnd-kde{,6}-kleopatra.xml

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_datadir/mime/packages/*kleopatra*.xml

%files
%_K6bin/kleopatra
%_K6xdgapp/*kleopatra*.desktop
%_K6xdgapp/*kwatchgnupg*.desktop
%_K6data/kleopatra/
%_K6plug/pim6/kcms/kleopatra/kleopatra_config_gnupgsystem.so
%_K6icon/*/*/apps/*kleopatra.*
%_K6icon/*/*/apps/*kwatchgnupg.*
%_K6data/kio/servicemenus/*.desktop
#
%_K6bin/kwatchgnupg
%_K6data/kwatchgnupg/
#
%_datadir/metainfo/*.xml

%files -n %libkleopatraclientcore
%_K6lib/libkleopatraclientcore.so.%core_sover
%_K6lib/libkleopatraclientcore.so.*
%files -n %libkleopatraclientgui
%_K6lib/libkleopatraclientgui.so.%gui_sover
%_K6lib/libkleopatraclientgui.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

