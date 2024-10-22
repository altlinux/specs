%define rname kaccounts-providers
%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Accounts Providers
Url: http://www.kde.org
License: LGPL-2.0-or-later

#BuildArch: noarch
#Requires: signon-ui
Provides: kde5-kaccounts-providers = %EVR
Obsoletes: kde5-kaccounts-providers < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: accounts-qt6-devel signon-devel intltool
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: qcoro6-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: kaccounts-integration-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdeclarative-devel kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-kpackage-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf6-filesystem
%description common
%name common package


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kpackage
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%config(noreplace) /etc/signon-ui/webkit-options.d/*.conf
%_K6plug/kaccounts/ui/*.so
%_datadir/accounts/providers/kde/
%_datadir/accounts/services/kde/
%_K6data/kpackage/genericqml/org.kde.kaccounts.*/
%_K6icon/hicolor/*/apps/kaccounts-*.*
#%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

