%define rname kruler

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphics
Summary: Screen ruler
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-kruler = %EVR
Obsoletes: kde5-kruler < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kcolorscheme-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-ki18n-devel kf6-knotifications-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kruler
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kruler
%_K6icon/*/*/*/*kruler*.*
%_K6xdgapp/org.kde.kruler.desktop
%_K6data/kruler/
%_K6notif/kruler*
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

