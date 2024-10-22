%define rname kmime

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KMime Library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-tools-devel
BuildRequires: boost-devel-headers
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kf6-kcodecs-devel kf6-ki18n-devel

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6mime
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6mime
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_includedir/KPim6/KMime/
%_K6link/lib*.so
%_K6lib/cmake/K*Mime/
#%_K6archdata/mkspecs/modules/qt_KMime.pri

%files -n libkpim6mime
%_K6lib/libKPim6Mime.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

