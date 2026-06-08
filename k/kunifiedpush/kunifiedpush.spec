%define rname kunifiedpush
%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif
%define service_name kunifiedpush-distributor

%define sover 1
%define libkunifiedpush libkunifiedpush%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: System/Libraries
Summary: UnifiedPush client
Url: http://www.kde.org
License: LGPL-2.0-or-later and BSD-3-Clause and BSD-2-Clause

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Sep 24 2025 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf6-kcodecs-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kwidgetsaddons-devel libctf-nobfd0 libdouble-conversion3 libglvnd-devel libgpg-error libimobiledevice-glue libp11-kit libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-opengl libqt6-pdf libqt6-qml libqt6-qmlmeta libqt6-qmlmodels libqt6-qmlworkerscript libqt6-quick libqt6-svg libqt6-test libqt6-waylandclient libqt6-waylandeglclienthwintegration libqt6-websockets libqt6-widgets libqt6-xml libsasl2-3 libssl-devel libstdc++-devel libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-setuptools qt6-base-devel qt6-declarative-devel rpm-build-file rpm-build-python3 rpm-macros-python sh5 tzdata vulkan-headers
#BuildRequires: appstream extra-cmake-modules glslang kf6-kcmutils-devel kf6-kcolorscheme-devel kf6-kconfigwidgets-devel kf6-ki18n-devel kf6-kservice-devel kf6-solid-devel libGLU-devel libvulkan-devel python-modules-compiler qt6-svg-devel qt6-wayland-devel qt6-webengine-devel qt6-websockets-devel tbb-devel
BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-wayland-devel qt6-websockets-devel
BuildRequires: kf6-kcmutils-devel kf6-kcolorscheme-devel kf6-kconfigwidgets-devel kf6-ki18n-devel kf6-kservice-devel kf6-solid-devel
BuildRequires: kf6-kcrash-devel

%description
UnifiedPush client library and service.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkunifiedpush
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkunifiedpush
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data kunifiedpush
#desktop-file-install --mode=0755 --dir %buildroot/%_K6xdgapp \
#    --set-key="X-DocPath" \
#    --set-value="kunifiedpush/index.html" \
#    %buildroot/%_K6xdgapp/org.kde.kunifiedpush.desktop

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc *LICENSE*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6xdgconf/KDE/*kunifiedpush*.conf
%_K6bin/*kunifiedpush*
%_K6plug/plasma/kcms/systemsettings/*push*.so
%_K6start/*kunifiedpush*.desktop
%_K6xdgapp/*push*.desktop
%_userunitdir/%service_name.service
%_userunitdir/graphical-session.target.wants/%service_name.service

%files devel
%_K6inc/KUnifiedPush/
%_K6link/lib*.so
%_K6lib/cmake/KUnifiedPush/

%files -n %libkunifiedpush
%_K6lib/libKUnifiedPush.so.%sover
%_K6lib/libKUnifiedPush.so.*

%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Wed Sep 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- initial build
