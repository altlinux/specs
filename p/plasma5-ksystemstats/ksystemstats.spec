%ifndef _unitdir_user
%define _unitdir_user %prefix/lib/systemd/user
%endif

%define rname ksystemstats

Name: plasma5-%rname
Version: 5.27.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 system statistics daemon
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-find-dbus-interface.patch

# Automatically added by buildreq on Wed Jul 07 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libctf-nobfd0 libgio-devel libglvnd-devel libgpg-error libnm-devel libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libudev-devel libxcbutil-keysyms pkg-config python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel rpm-build-python3 rpm-macros-python sh4 tzdata
#BuildRequires: appstream extra-cmake-modules kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-networkmanager-qt-devel libnl-devel libsensors3-devel plasma5-libksysguard-devel python-modules-compiler python3-dev python3-module-mpl_toolkits qt5-svg-devel qt5-wayland-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: libnl-devel libsensors3-devel
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-networkmanager-qt-devel
BuildRequires: plasma5-libksysguard-devel

%description
KSystemStats is a daemon that collects statistics about the running system.

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

%package -n libsystemstats
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libsystemstats
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/*stat*
%_K5plug/ksystemstats/
%_K5dbus_srv/*.service
%_unitdir_user/*.service

#%files devel
#%_K5inc/ksystemstats_version.h
#%_K5inc/ksystemstats/
#%_K5link/lib*.so
#%_K5lib/cmake/ksystemstats
#%_K5archdata/mkspecs/modules/qt_ksystemstats.pri

#%files -n libsystemstats
#%_K5lib/libksystemstats.so.*

%changelog
* Thu Mar 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.3-alt1
- new version

* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.2-alt1
- new version

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

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
- initial build
