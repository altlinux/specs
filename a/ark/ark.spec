%define rname ark

%define sover 24
%define libkerfuffle libkerfuffle%sover

%def_disable libzip

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Archiving/Compression
Summary: KDE archivers frontend
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-ark = %EVR
Obsoletes: kde5-ark < %EVR

Requires: unrar p7zip unzip zip

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: bzlib-devel libarchive-devel liblzma-devel zlib-devel
%if_enabled libzip
BuildRequires: libzip-devel
%endif
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kitemmodels-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kfilemetadata-devel
BuildRequires: kf6-kglobalaccel-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kparts-devel kf6-kpty-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
Frontend to many archivers.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kde-common
Provides: kde5-ark-common = %EVR
Obsoletes: kde5-ark-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkerfuffle
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkerfuffle23 < %EVR
%description -n %libkerfuffle
%name library

%prep
%setup -n %rname-%version

%if_disabled libzip
sed -i '/^find_package.*LibZip/s|LibZip|LibZip_DISABLED|' CMakeLists.txt
%endif

%build
%K6build

%install
%K6install
%K6install_move data kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%dir %_K6plug/kf6/kfileitemaction/
%_datadir/qlogging-categories6/*.*categories

%files
%config(noreplace) %_K6xdgconf/*ark*
%_K6bin/ark
%_K6plug/kf6/parts/arkpart.so
%_K6plug/kf6/kio_dnd/extracthere.so
%_K6plug/kf6/kfileitemaction/*.so
%_K6xdgapp/*ark*.desktop
%_K6cfg/*ark*.kcfg
%_K6icon/hicolor/*/apps/ark.*
%_K6plug/kerfuffle/
%_K6conf_up/*ark*
%_datadir/metainfo/*.xml

#%files devel
#%_K6inc/ark_version.h
#%_K6inc/ark/
#%_K6link/lib*.so
#%_K6lib/cmake/ark

%files -n %libkerfuffle
%_K6lib/libkerfuffle.so.%sover
%_K6lib/libkerfuffle.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

