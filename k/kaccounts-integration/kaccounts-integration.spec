%define rname kaccounts-integration
%define sover 2
%define libkaccounts libkaccounts6_%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Framework for storing secrets and accounts
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: accounts-qt6-devel signon-devel
BuildRequires: qcoro6-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-sonnet-devel kf6-kdeclarative-devel kf6-kpackage-devel

%description
Accounts-SSO is the framework we are using to store secrets (tokens, passwords)
and for storing Accounts (small pieces of information containing a name,
a provider, etc).

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf6-filesystem
Provides: kde5-kaccounts-integration-common = %EVR
Obsoletes: kde5-kaccounts-integration-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkaccounts
Group: System/Libraries
Summary: %name library
Requires: %name-common
%ifarch %qt6_qtwebengine_arches
Requires: signon
%endif
Requires: accounts-qml-module
Obsoletes: libkaccounts2 < %EVR
%description -n %libkaccounts
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data kpackage
%find_lang %name --with-kde --all-name

mkdir -p %buildroot/%_K6plug/kaccounts/ui
mkdir -p %buildroot/%_K6plug/kaccounts/{ui,daemonplugins}

%files common -f %name.lang
%doc LICENSES/*
%dir %_K6plug/kaccounts/
%dir %_K6plug/kaccounts/daemonplugins/
%dir %_K6plug/kaccounts/ui/

%files devel
%_K6inc/KAccounts6/
%_K6link/lib*.so
%_K6lib/cmake/KAccounts6/

%files -n %libkaccounts
%_K6lib/libkaccounts6.so.%sover
%_K6lib/libkaccounts6.so.*
%_K6plug/plasma/kcms/systemsettings/*kaccounts*.so
%_K6xdgapp/*kaccounts*.desktop
%_K6plug/kf6/kded/*accounts*.so
%_K6plug/kaccounts/daemonplugins/*kaccounts*.so
%_K6qml/org/kde/kaccounts/
#%_K6data/kpackage/kcms/kcm_kaccounts/


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

