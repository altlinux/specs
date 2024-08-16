%define rname milou

%define milou_sover 6
%define libmilou libmilou%milou_sover

Name: %rname
Version: 6.1.4
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma Search and Launch
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-milou = 1:%version-%release
Obsoletes: plasma5-milou < 1:%version-%release
Provides: plasma5-milou-common = 1:%version-%release
Obsoletes: plasma5-milou-common < 1:%version-%release

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdeclarative-devel kf6-ki18n-devel kf6-kpackage-devel
BuildRequires: kf6-krunner-devel kf6-kservice-devel kf6-kitemmodels-devel kf6-ksvg-devel
BuildRequires: plasma6-lib-devel

%description
Search and Launch.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6qml/org/kde/milou/
%_K6data/plasma/plasmoids/org.kde.milou/
%_datadir/metainfo/*.xml


%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

