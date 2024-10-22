%define rname grantleetheme

%define sover 6
%define libkpim6grantleetheme libkpim6grantleetheme%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE6 %rname library
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-knewstuff-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: kf6-kguiaddons-devel kf6-kcolorscheme-devel kf6-ktexttemplate-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: grantlee5-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpim6grantleetheme
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6grantleetheme
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_includedir/KPim6/GrantleeTheme/
%_K6link/lib*.so
%_K6lib/cmake/K*GrantleeTheme/

%files -n %libkpim6grantleetheme
%_K6lib/libKPim6GrantleeTheme.so.%sover
%_K6lib/libKPim6GrantleeTheme.so.*
%_K6plug/kf6/ktexttemplate/kde_grantlee_plugin.so

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

