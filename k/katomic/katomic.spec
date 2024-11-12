%define rname katomic

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Games/Strategy
Summary: Build complex atoms with a minimal amount of moves
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-katomic = %EVR
Obsoletes: kde5-katomic < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel  kf6-kdoctools-devel kf6-ki18n-devel kf6-knewstuff-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-kcrash-devel kf6-kcolorscheme-devel
BuildRequires: kde6-libkdegames-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data katomic kconf_update knsrcfiles
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/katomic
%_K6data/katomic/
%_K6icon/*/*/apps/katomic.*
%_K6xdgapp/org.kde.katomic.desktop
%_K6data/knsrcfiles/*katomic*.knsrc
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml

%changelog
* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build
