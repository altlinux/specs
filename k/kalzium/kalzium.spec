%define rname kalzium

%def_disable avogadro
%def_disable facile

%define sover 5
%define libscience libscience%sover

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Education
Summary: Periodic system of the elements
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides:  kde5-kalzium = %EVR
Obsoletes: kde5-kalzium < %EVR

%if_enabled avogadro
Requires: avogadro
%endif
Requires: chemical-mime-data

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-scxml-devel qt6-5compat-devel
BuildRequires: eigen3 ocaml
BuildRequires: libopenbabel-devel llvm-devel openbabel
%if_enabled avogadro
BuildRequires: libopenbabel-devel openbabel avogadro-devel
%endif
%if_enabled facile
BuildRequires: facile
%endif
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-knewstuff-devel kf6-kplotting-devel
BuildRequires: kf6-karchive-devel kf6-ki18n-devel kf6-kunitconversion-devel kf6-ktextwidgets-devel

%description
Kalzium is an application which will show you some information about the
periodic system of the elements. Therefore you could use it as an
information database.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-kalzium-common = %EVR
Obsoletes: kde5-kalzium-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libscience
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libscience
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
%K6install_move data kalzium libkdeedu
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/kalzium
%_K6data/kalzium/
%_K6xdgapp/*kalzium*.desktop
%_K6cfg/*kalzium*
%_K6data/libkdeedu/data/*
%_K6icon/*/*/apps/kalzium.*
%_datadir/metainfo/*.xml

%files devel
%_K6inc/libkdeedu/*.h
%_K6link/lib*.so

%files -n %libscience
%_K6lib/libscience.so.%sover
%_K6lib/libscience.so.*


%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

