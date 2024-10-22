%define rname libkleo

%define sover 6
%define libkpim6libkleo libkpim6libkleo%sover

Name: kde6-%rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE6 %rname library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: boost-devel extra-cmake-modules qt6-declarative-devel
BuildRequires: libgpgme-devel libassuan-devel
BuildRequires: kf6-kcompletion-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-ki18n-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-sonnet-devel kf6-kcodecs-devel kf6-kitemmodels-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kpimtextedit-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-libkleo-common = %EVR
Obsoletes: kde5-libkleo-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpim6libkleo
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6libkleo
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data libkleopatra
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%config(noreplace) %_K6xdgconf/*rc
%_datadir/qlogging-categories6/*.*categories
%_K6data/libkleopatra/

%files devel
%_includedir/KPim6/Libkleo/
%_K6link/lib*.so
%_K6lib/cmake/K*Libkleo/

%files -n %libkpim6libkleo
%_K6lib/libKPim6Libkleo.so.%sover
%_K6lib/libKPim6Libkleo.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

