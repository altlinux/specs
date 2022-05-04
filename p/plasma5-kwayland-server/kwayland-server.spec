%define rname kwayland-server

%define sover 5
%define libkwaylandserver libkwaylandserver%sover

Name: plasma5-%rname
Version: 5.24.5
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Qt-style API to interact with the wayland-server API
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Jul 28 2020 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libglvnd-devel libqt5-concurrent libqt5-core libqt5-gui libqt5-waylandclient libsasl2-3 libssl-devel libstdc++-devel libwayland-client-devel libwayland-server libwayland-server-devel pkg-config python-modules python2-base python3 python3-base python3-dev qt5-base-devel rpm-build-python3 sh4 wayland-devel xorg-proto-devel
#BuildRequires: appstream extra-cmake-modules git-core kde5-plasma-wayland-protocols kf5-kwayland-devel python3-module-mpl_toolkits qt5-wayland-devel wayland-protocols
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules kde5-plasma-wayland-protocols kf5-kwayland-devel python3-module-mpl_toolkits qt5-wayland-devel wayland-protocols

%description
KWayland is a Qt-style API to interact with the wayland-client and wayland-server API.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkwaylandserver
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkwaylandserver
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
mkdir -p %buildroot/KF5/
mv %buildroot/%_includedir/* %buildroot/KF5/
mkdir -p %buildroot/%_K5inc/
mv %buildroot/KF5/* %buildroot/%_K5inc/
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories5/*.*categories

%files devel
%_K5inc/kwaylandserver_version.h
%_K5inc/KWaylandServer/
%_K5link/lib*.so
%_K5lib/cmake/KWaylandServer/
#%_K5archdata/mkspecs/modules/qt_kwayland-server.pri

%files -n %libkwaylandserver
%_K5lib/libKWaylandServer.so.%sover
%_K5lib/libKWaylandServer.so.*

%changelog
* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- new version

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt1
- new version

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt1
- new version

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.4-alt1
- new version

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.4-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.3-alt1
- initial build
