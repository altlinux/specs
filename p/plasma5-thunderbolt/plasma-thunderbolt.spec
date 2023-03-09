%define rname plasma-thunderbolt

%define sover 0
%define libkbolt libkbolt%sover

Name: plasma5-thunderbolt
Version: 5.27.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Plasma 5
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: bolt

Source: %rname-%version.tar
Patch1: alt-soversion.patch

# Automatically added by buildreq on Fri Feb 07 2020 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kwidgetsaddons-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms python-modules python2-base python3 python3-base qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-qml sh4
#BuildRequires: appstream extra-cmake-modules kf5-kcmutils-devel kf5-kconfigwidgets-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kded kf5-ki18n-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel libkf5plasmaquick libssl-devel python-modules-compiler python3-dev qt5-wayland-devel rpm-build-gir
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel qt5-wayland-devel
BuildRequires: kf5-kcmutils-devel kf5-kconfigwidgets-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel
BuildRequires: kf5-ki18n-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel

%description
This package contains a Plasma Sytem Settings module and a KDED module to
handle authorization of Thunderbolt devices connected to the computer. There's
also a shared library (libkbolt) that implements common interface between the
modules and the system-wide bolt daemon, which does the actual hard work of
talking to the kernel.

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

%package -n %libkbolt
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkbolt
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data kpackage
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K5plug/plasma/kcms/systemsettings/kcm_bolt.so
%_K5plug/kf5/kded/*bolt*.so
%_K5data/kpackage/kcms/kcm_bolt/
%_K5notif/*bolt*.notifyrc
%_K5xdgapp/*bolt*.desktop


#%files devel
#%_K5inc/plasma-thunderbolt_version.h
#%_K5inc/plasma-thunderbolt/
#%_K5link/lib*.so
#%_K5lib/cmake/plasma-thunderbolt
#%_K5archdata/mkspecs/modules/qt_plasma-thunderbolt.pri

%files -n %libkbolt
%_K5lib/libkbolt.so.%sover
%_K5lib/libkbolt.so.*

%changelog
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

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.3-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.2-alt1
- new version

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version

* Thu Feb 06 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.5-alt1
- initial build
