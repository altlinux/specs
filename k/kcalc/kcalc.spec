%define rname kcalc

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Scientific Calculator
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-kcalc = %EVR
Obsoletes: kde5-kcalc < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libgmp-devel libmpfr-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-knotifications-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: kf6-kcrash-devel kf6-kcolorscheme-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kcalc kglobalaccel kconf_update
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kcalc
%_K6data/kglobalaccel/*kcalc*
%_K6xdgapp/*kcalc*
%_K6conf_up/*kcalc*
%_K6cfg/*kcalc*
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

