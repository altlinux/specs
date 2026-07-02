%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname knighttime
%define service_name plasma-knighttimed

%define sover 0
%define libknighttime libknighttime%sover

Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE helpers for scheduling the dark-light cycle
Url: http://www.kde.org
License: GPL-3.0-only AND BSD-3-Clause AND MIT AND GPL-2.0-only AND LGPL-2.1-only AND CC0-1.0 AND LGPL-3.0-only

Source: %rname-%version.tar

# Automatically added by buildreq on Sat Nov 15 2025 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ git-core glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libdouble-conversion3 libglvnd-devel libgpg-error libp11-kit libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-pdf libqt6-positioning libqt6-qml libqt6-svg libqt6-waylandclient libqt6-waylandeglclienthwintegration libqt6-xml libsasl2-3 libssl-devel libstdc++-devel libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-setuptools qt6-base-devel qt6-declarative-devel qt6-positioning-devel qt6-tools rpm-build-file rpm-build-python3 sh5 tzdata vulkan-headers
#BuildRequires: appstream clang-tools extra-cmake-modules glslang kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kholidays-devel kf6-ki18n-devel libGLU-devel libvulkan-devel qt6-svg-devel qt6-tools-devel qt6-wayland-devel qt6-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: qt6-positioning-devel qt6-tools-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kholidays-devel kf6-ki18n-devel

%description
The KNightTime provides helpers for scheduling the dark-light cycle. It can be used to implement
features such as adjusting the screen color temperature based on time of day, etc.

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

%package -n %libknighttime
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libknighttime
%name library.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6libexecdir/*nighttime*
%_K6xdgapp/*nighttime*.desktop
%_K6dbus_srv/*NightTime*.service
%_userunitdir/%service_name.service

%files devel
%_K6inc/KNightTime/
%_K6link/lib*.so
%_K6lib/cmake/KNightTime/
%_K6dbus_iface/*NightTime*.xml

%files -n %libknighttime
%_K6lib/libKNightTime.so.*
%_K6lib/libKNightTime.so.%sover

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Sat Nov 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- initial build
