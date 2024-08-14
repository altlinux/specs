%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname kwayland

%define sover 6
%define libkwaylandclient libkwaylandclient%sover

Name: plasma6-%rname
Version: 6.1.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Workspace client wrapper for Wayland libraries
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-wayland-devel
BuildRequires: libwayland-client-devel libwayland-server-devel wayland-protocols plasma-wayland-protocols

%description
KWayland is a Qt-style API to interact with the wayland-client API.

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

%package -n %libkwaylandclient
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkwaylandclient
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
#find_lang %name --with-kde --all-name

%files common
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files -n %libkwaylandclient
%_K6lib/libKWaylandClient.so.%sover
%_K6lib/libKWaylandClient.so.*

%files devel
%_K6inc/KWayland/
%_K6link/lib*.so
%_K6lib/cmake/KWayland/
%_pkgconfigdir/*ayland*.pc

%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Tue Jul 02 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- initial build

