%define rname kidletime

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 reporting of idle time of user and system
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Dec 26 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libcloog-isl4 libqt6-core libqt6-dbus libqt6-gui libqt6-widgets libqt6-x11extras libstdc++-devel libxcb-devel pkg-config python-base qt6-base-devel ruby ruby-stdlibs xorg-kbproto-devel xorg-scrnsaverproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel python-module-google  rpm-build-ruby
BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules 
BuildRequires: qt6-wayland-devel plasma-wayland-protocols wayland-protocols
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel
BuildRequires: libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel
BuildRequires: libXxf86vm-devel libxkbfile-devel

%description
KIdleTime is a singleton reporting information on idle time. It is useful not
only for finding out about the current idle time of the PC, but also for getting
notified upon idle time events, such as custom timeouts, or user activity.

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

%package -n libkf6idletime
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6idletime
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

%files devel
#%_K6inc/kidletime_version.h
%_K6inc/KIdleTime/
%_K6link/lib*.so
%_K6lib/cmake/KF6IdleTime

%files -n libkf6idletime
%_K6lib/libKF6IdleTime.so.*
%_K6plug/kf6/org.kde.kidletime.platforms/


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

