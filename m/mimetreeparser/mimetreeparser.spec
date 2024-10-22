%define rname mimetreeparser

%define sover 6
%define libkpim6mimetreeparsercore libkpim6mimetreeparsercore%sover
%define libkpim6mimetreeparserwidgets libkpim6mimetreeparserwidgets%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE6 %rname library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libGLU-devel libvulkan-devel
BuildRequires: kde6-libkleo-devel kf6-kcalendarcore-devel kf6-kcodecs-devel kf6-ki18n-devel kf6-kwidgetsaddons-devel
BuildRequires: kmbox-devel

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

%package -n %libkpim6mimetreeparsercore
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6mimetreeparsercore
%name library

%package -n %libkpim6mimetreeparserwidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6mimetreeparserwidgets
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
%_includedir/KPim6/MimeTreeParser*/
%_K6link/lib*.so
%_libdir/cmake/K*MimeTreeParser*/
%_K6archdata/mkspecs/modules/qt_*.pri

%files -n %libkpim6mimetreeparsercore
%_K6lib/libKPim6MimeTreeParserCore.so.%sover
%_K6lib/libKPim6MimeTreeParserCore.so.*
%_K6qml/org/kde/pim/mimetreeparser/
%files -n %libkpim6mimetreeparserwidgets
%_K6lib/libKPim6MimeTreeParserWidgets.so.%sover
%_K6lib/libKPim6MimeTreeParserWidgets.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

