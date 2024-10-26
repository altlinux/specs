%define rname libkomparediff2

%define sover 6
%define libkomparediff2 libkomparediff2_%sover

Name: kde6-%rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Library to compare files and strings
Url: http://www.kde.org
License: LGPL-2.0-or-later and GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
A shared library to compare files and strings using kde and GNU diff.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-libkomparediff2-common = %EVR
Obsoletes: kde5-libkomparediff2-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkomparediff2
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
Requires: /usr/bin/diff
Obsoletes: libkomparediff25 < %EVR
%description -n %libkomparediff2
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KompareDiff2/
%_K6link/lib*.so
%_K6lib/cmake/KompareDiff2/

%files -n %libkomparediff2
%_K6lib/libkomparediff2.so.%sover
%_K6lib/libkomparediff2.so.*


%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

