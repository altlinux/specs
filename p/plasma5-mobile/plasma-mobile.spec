%define rname plasma-mobile
%def_disable dialer

Name: plasma5-mobile
Version: 5.26.5
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: UI components for Plasma Phone
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-phone-components = %EVR
Obsoletes: plasma5-phone-components < %EVR
Requires: plasma5-nano
# qml(org.kde.pipewire)
Requires: plasma5-kpipewire
# qml(org.kde.kirigamiaddons.labs.mobileform)
Requires: kf5-kirigami-addons

Source: %rname-%version.tar
Patch1: alt-startplasma.patch
Patch2: alt-def-shell.patch
Patch3: alt-no-dialer.patch

# Automatically added by buildreq on Fri Feb 21 2020 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gstreamer1.0-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-common kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-common kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libtelepathy-qt5-farstream0 libtelepathy-qt5-service0 libtelepathy-qt50 libwayland-client libxcbutil-keysyms pkg-config python-modules python2-base python3 python3-base qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-gir rpm-build-python3 rpm-build-qml sh4
#BuildRequires: appstream extra-cmake-modules gst-plugins1.0-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kpeople-devel kf5-kwayland-devel kf5-plasma-framework-devel libssl-devel python-modules-compiler python3-dev qt5-translations qt5-wayland-devel telepathy-qt5-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-wayland-devel qt5-svg-devel
BuildRequires: gst-plugins1.0-devel telepathy-qt5-devel
BuildRequires: kf5-modemmanager-qt-devel ModemManager-devel kf5-networkmanager-qt-devel kf5-kcmutils-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel
BuildRequires: kf5-kpackage-devel kf5-kpeople-devel kf5-kwayland-devel kf5-plasma-framework-devel
BuildRequires: plasma5-kwin-devel plasma5-workspace-devel
%if_enabled dialer
BuildRequires: phonenumber-devel
%endif

%description
UI components for Plasma Phone.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: plasma5-phone-components-common = %EVR
Obsoletes: plasma5-phone-components-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: plasma5-phone-components-devel = %EVR
Obsoletes: plasma5-phone-components-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libplasma-phone-components
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libplasma-phone-components
%name library


%prep
%setup -n %rname-%version
%patch1 -p1
#%patch2 -p1
%if_disabled dialer
%patch3 -p1
sed -i 's|\(.*add_subdirectory.*dialer.*\)|#\1|' CMakeLists.txt
%endif

%build
%K5build \
    -DLIBEXEC_INSTALL_DIR:PATH=%_K5exec \
    #

%install
%K5install
%K5install_move data kwin sounds wallpapers kpackage
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/startplasmamobile
%_K5plug/plasma/applets/*.so
%_K5plug/plasma/kcms/systemsettings/*mobile*.so
%_K5qml/org/kde/plasma/mm/
%_K5qml/org/kde/plasma/private/mobileshell/
%_K5qml/org/kde/plasma/quicksetting/
%_K5xdgapp/*mobile*.desktop
%_K5data/kpackage/kcms/kcm_mobileshell/
%_K5data/plasma/look-and-feel/org.kde.plasma.phone/
%_K5data/plasma/plasmoids/*/
%_K5data/plasma/quicksettings/*/
%_K5data/plasma/shells/org.kde.plasma.phoneshell/
%_K5notif/*.notifyrc
%_K5srv/plasma-applet-*.desktop
%exclude %_K5srv/plasma-applet-org.kde.plasma.phone.desktop
%_datadir/xsessions/plasma-mobile.desktop

%changelog
* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Tue Nov 01 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt2
- fix requires

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

* Fri Jul 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt2
- fix package

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- new version

* Mon May 31 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt2
- fix install xsession file

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

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Thu Mar 05 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt3
- update defaults

* Thu Mar 05 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt2
- update defaults

* Thu Feb 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- initial build
