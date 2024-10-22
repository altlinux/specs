%define rname libkcompactdisc

%define sover 5
%define libkcompactdisc libkcompactdisc6_%sover

Name: kde6-%rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE Compact Disc library
Url: http://www.kde.org
License: GPL-2.0-or-later and LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libalsa-devel qt6-phonon-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-ki18n-devel

%description
Compact Disc library.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-libkcompactdisc-common = %EVR
Obsoletes: kde5-libkcompactdisc-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkcompactdisc
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkf5compactdisc5 < %EVR
%description -n %libkcompactdisc
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files devel
%_K6inc/KCompactDisc*/
%_K6link/lib*.so
%_K6lib/cmake/KCompactDisc*/
%_K6archdata/mkspecs/modules/qt_KCompactDisc.pri

%files -n %libkcompactdisc
%_K6lib/libKCompactDisc6.so.%sover
%_K6lib/libKCompactDisc6.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

