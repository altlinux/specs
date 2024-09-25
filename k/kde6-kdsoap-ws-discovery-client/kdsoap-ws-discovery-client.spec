%define rname kdsoap-ws-discovery-client
%define sover 0
%define libkdsoapwsdiscoveryclient libkdsoapwsdiscoveryclient%sover

Name: kde6-%rname
Version: 0.3.0
Release: alt1
%K6init

Group: System/Libraries
Summary: WS-discovery client library
Url: https://www.kde.org/
Vcs: https://invent.kde.org/libraries/kdsoap-ws-discovery-client
License: GPL-3.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: boost-devel cmake qt6-base-devel
BuildRequires: extra-cmake-modules kde6-kdsoap-devel

%description
This package contains the main library implementing a client for the
Web Services Dynamic Discovery (WS-Discovery) protocol, used to discover
services on a local network.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
%description common
Common %name files

%package -n %libkdsoapwsdiscoveryclient
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkdsoapwsdiscoveryclient
%name library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libgcrypt-devel libqca-qt6-devel
%description devel
This package contains the development files for %name.


%prep
%setup -n %rname-%version

%build
%K6build \
    -DCMAKE_INSTALL_INCLUDEDIR=%_K6inc \
    -DBUILD_WITH_QT6:BOOL=ON \
    #

%install
%K6install
%find_lang --with-kde --all-name %name
rm -rf %buildroot/%_datadir/doc/* ||:

%files common -f %name.lang
%doc LICENSES/*

%files -n %libkdsoapwsdiscoveryclient
%_libdir/libKDSoapWSDiscoveryClient.so.%sover
%_libdir/libKDSoapWSDiscoveryClient.so.*

%files devel
%_K6lib/cmake/KDSoapWSDiscoveryClient/
%_K6inc/KDSoapWSDiscoveryClient/
%_K6link/lib*.so

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
