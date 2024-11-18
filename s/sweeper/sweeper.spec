%define rname sweeper

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: System Cleaner for KDE
Url: http://www.kde.org
License: LGPL-2.1-or-later

Provides:  kde5-sweeper = %EVR
Obsoletes: kde5-sweeper < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libssl-devel
BuildRequires: plasma6-activities-stats-devel
BuildRequires: kf6-kcrash-devel kf6-kdoctools-devel kf6-kio-devel kf6-ktextwidgets-devel

%description
System Cleaner.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/sweeper
%_K6xdgapp/org.kde.sweeper.desktop
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*sweeper*.xml

%changelog
* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

