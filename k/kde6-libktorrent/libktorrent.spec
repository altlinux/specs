%define rname libktorrent

%define sover 6
%define libktorrent libktorrent6_%sover

Name: kde6-%rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: BitTorrent library for KDE
Url: http://ktorrent.org/
License: GPL-2.0-only

Provides: kde5-libktorrent = %EVR
Obsoletes: kde5-libktorrent < %EVR

Source: libktorrent-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: boost-devel doxygen extra-cmake-modules graphviz
BuildRequires: qt6-declarative-devel qt6-5compat-devel
BuildRequires: libgcrypt-devel libgmp-devel libqca-qt6-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel

%description
Library that allow using BitTorrent with KDE programs.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
Provides: kde5-libktorrent-common = %EVR
Obsoletes: kde5-libktorrent-common < %EVR
%description common
Common %name files

%package -n %libktorrent
Summary: KTorrent library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkf5torrent6 < %EVR
%description -n %libktorrent
KTorrent library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libgcrypt-devel libqca-qt6-devel
%description devel
This package contains the development files for %name.


%prep
%setup -qn libktorrent-%version

%build
%K6build \
    -DKDE_INSTALL_LOCALEDIR=%_K6i18n \
  #

%install
%K6install
%find_lang --with-kde --all-name %name

%files common -f %name.lang

%files -n %libktorrent
%doc LICENSES/*
%_libdir/libKTorrent6.so.%sover
%_libdir/libKTorrent6.so.*

%files devel
%_K6lib/cmake/KTorrent?/
%_K6inc/libktorrent/
%_K6link/lib*.so

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build
