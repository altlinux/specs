%define rname kpeople

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 access to all contacts and aggregates them by person
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-declarative-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kitemviews-devel kf6-kservice-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kcontacts-devel kf6-kcodecs-devel

%description
KPeople offers unified access to our contacts from different sources, grouping
them by person while still exposing all the data.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6people
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6people
KF6 library

%package -n libkf6peoplebackend
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6peoplebackend
KF6 library

%package -n libkf6peoplewidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6peoplewidgets
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
#%_K6srvtyp/*.desktop

%files devel
%_K6inc/KPeople/
%_K6link/lib*.so
%_K6lib/cmake/KF6People/

%files -n libkf6people
%_K6lib/libKF6People.so.*
%files -n libkf6peoplebackend
%_K6lib/libKF6PeopleBackend.so.*
%_K6plug/kpeople/datasource/KPeopleVCard.so
%files -n libkf6peoplewidgets
%_K6qml/org/kde/people/
%_K6lib/libKF6PeopleWidgets.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

