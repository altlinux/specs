%define rname kcharselect

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Text tools
Summary: KDE Character Selector
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kcharselect = %EVR
Obsoletes: kde5-kcharselect < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kcolorscheme-devel
BuildRequires: kf6-ki18n-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-kbookmarks-devel
BuildRequires: kf6-kcrash-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kcharselect
%_K6xdgapp/org.kde.kcharselect.desktop
%_datadir/metainfo/*.xml


%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

