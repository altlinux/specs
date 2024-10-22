%define rname libkgapi

%define sover 6
%define libkpimgapidrive libkpim6gapidrive%sover
%define libkpimgapilatitude libkpim6gapilatitude%sover
%define libkpimgapicore libkpim6gapicore%sover
%define libkpimgapicalendar libkpim6gapicalendar%sover
%define libkpimgapiblogger libkpim6gapiblogger%sover
%define libkpimgapimaps libkpim6gapimaps%sover
%define libkpimgapipeople libkpim6gapipeople%sover
%define libkpimgapitasks libkpim6gapitasks%sover

Name: kde6-%rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Google services APIs
Url: http://www.kde.org
License: BSD-3-Clause and CC0-1.0 and LGPL-2.1-only and LGPL-3.0-only

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-tools-devel
BuildRequires: libsasl2-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-kwallet-devel kf6-ki18n-devel

%description
LibKGAPI is a C++ library that implements APIs for various Google services.

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
Requires: kf6-kcoreaddons-devel kf6-kcalendarcore-devel kf6-kcontacts-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpimgapilatitude
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpimgapilatitude
%name library

%package -n %libkpimgapidrive
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkpimgapidrive5 < %EVR
%description -n %libkpimgapidrive
%name library

%package -n %libkpimgapicore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpimgapicore
%name library

%package -n %libkpimgapicalendar
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpimgapicalendar
%name library

%package -n %libkpimgapiblogger
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpimgapiblogger
%name library

%package -n %libkpimgapimaps
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpimgapimaps
%name library

%package -n %libkpimgapipeople
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpimgapipeople
%name library

%package -n %libkpimgapitasks
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpimgapitasks
%name library


%prep
%setup -n %rname-%version
sed -i '1iadd_definitions(-std=gnu90)' src/saslplugin/CMakeLists.txt

%build
#    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
%K6build \
    #

%install
%K6install

# workaround against sasl plugins dir
for sffx in 3 4 5 6 ; do
    mkdir -p  %buildroot/%_libdir/sasl2-$sffx
    for f in %buildroot/%_libdir/sasl2/*.so* ; do
	fname=`basename "$f"`
	ln -s ../sasl2/"$fname" %buildroot/%_libdir/sasl2-$sffx/"$fname"
    done
done

%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_includedir/KPim6/KGAPI/
%_K6link/lib*.so
%_K6lib/cmake/K*GAPI/
#%_K6archdata/mkspecs/modules/qt_KGAPI*.pri

%files -n %libkpimgapidrive
%_K6lib/libKPim6GAPIDrive.so.*
%_libdir/sasl2*/*.so*
%files -n %libkpimgapilatitude
%_K6lib/libKPim6GAPILatitude.so.*
%files -n %libkpimgapicore
%_K6lib/libKPim6GAPICore.so.*
%files -n %libkpimgapicalendar
%_K6lib/libKPim6GAPICalendar.so.*
%files -n %libkpimgapiblogger
%_K6lib/libKPim6GAPIBlogger.so.*
%files -n %libkpimgapimaps
%_K6lib/libKPim6GAPIMaps.so.*
%files -n %libkpimgapipeople
%_K6lib/libKPim6GAPIPeople.so.*
%files -n %libkpimgapitasks
%_K6lib/libKPim6GAPITasks.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

