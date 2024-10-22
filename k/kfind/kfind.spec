%define rname kfind

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE utility to find files
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-kfind = %EVR
Obsoletes: kde5-kfind < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-5compat-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-karchive-devel
BuildRequires: kf6-kfilemetadata-devel kf6-kwidgetsaddons-devel kf6-ktextwidgets-devel kf6-ki18n-devel

%description
KDE utility to find files.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kfind
%_K6xdgapp/*kfind*.desktop
%_K6icon/*/*/apps/kfind.*
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

