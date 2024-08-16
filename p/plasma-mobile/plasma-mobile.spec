%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%define rname plasma-mobile

%_K6if_ver_gteq %ubt_id M110
%def_enable dialer
%else
%def_disable dialer
%endif

Name: %rname
Version: 6.1.4
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: UI components for Plasma Phone
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-mobile = %EVR
Obsoletes: plasma5-mobile < %EVR

Requires: %name-core
Requires: plasma-settings-virtualkeyboard
Requires: plasma-nano
# qml(org.kde.pipewire)
Requires: plasma6-kpipewire
# qml(org.kde.kirigamiaddons.labs.mobileform)
Requires: kf6-kirigami-addons

Source: %rname-%version.tar
Patch2: alt-def-shell.patch
Patch3: alt-no-dialer.patch

BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules qt6-base-devel qt6-wayland-devel qt6-svg-devel qt6-sensors-devel
BuildRequires: qcoro6-devel libudev-devel
BuildRequires: kf6-modemmanager-qt-devel ModemManager-devel kf6-networkmanager-qt-devel kf6-kcmutils-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdeclarative-devel kf6-ki18n-devel kf6-kio-devel kf6-knotifications-devel
BuildRequires: kf6-kpackage-devel kf6-kpeople-devel kf6-kitemmodels-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: plasma6-lib-devel kwin-devel plasma-workspace-devel plasma6-libkscreen-devel plasma6-kwayland-devel
%if_enabled dialer
BuildRequires: libphonenumber-devel
%endif

%description
UI components for Plasma Phone.

%package -n plasma-settings-virtualkeyboard
Group: Graphical desktop/KDE
Summary: On-Screen Keyboard configuration
Requires: %name-core
Provides: kde5-plasma-settings-virtualkeyboard = %EVR
Obsoletes: kde5-plasma-settings-virtualkeyboard  < %EVR
%description -n plasma-settings-virtualkeyboard
On-Screen Keyboard configuration.

%package core
Summary: Core files needed for %rname
Group: Graphical desktop/KDE
Requires: %name-common
Requires: kf6-kirigami
Requires: kde-cli-tools
%description core
Core files needed for %rname

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-plasma-settings-common = %EVR
Obsoletes: kde5-plasma-settings-common  < %EVR
%description common
%name common package

%prep
%setup -n %rname-%version
#%patch2 -p1
%if_disabled dialer
%patch3 -p1
sed -i 's|\(.*add_subdirectory.*dialer.*\)|#\1|' CMakeLists.txt
%endif

%build
%K6build \
    -DLIBEXEC_INSTALL_DIR:PATH=%_K6exec \
    #

%install
%K6install
%K6install_move data kwin sounds wallpapers kpackage
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files core
%_K6qml/org/kde/plasma/private/mobileshell/

%files -n plasma-settings-virtualkeyboard
%_K6xdgapp/*keyboard*.desktop
%_datadir/metainfo/*keyboard*.xml
%_K6data/plasma/quicksettings/*keyboard*/
%_K6plug/plasma/kcms/systemsettings/*keyboard*.so

%files
%_K6bin/*plasma*mobile*
%_K6plug/plasma/applets/*.so
%_K6plug/plasma/kcms/systemsettings/*mobile*.so
%_K6plug/kf6/kded/*mobile*.so
%_K6plug/kwin/effects/plugins/*mobile*.so
%exclude %_K6plug/plasma/kcms/systemsettings/*keyboard*.so
%_K6plug/plasma/kcms/systemsettings/*cellular*.so
%_K6qml/org/kde/plasma/mm/
%_K6qml/org/kde/plasma/quicksetting/
%_K6qml/org/kde/plasma/mobileinitialstart
%_K6qml/org/kde/private/mobile/homescreen/halcyon/
%_K6xdgapp/*mobile*.desktop
%exclude %_K6xdgapp/*keyboard*.desktop
%_K6xdgapp/*cellular*.desktop
%_K6data/plasma/look-and-feel/org.kde.breeze.mobile/
%_K6data/plasma/plasmoids/*/
%_K6data/plasma/quicksettings/*/
%exclude %_K6data/plasma/quicksettings/*keyboard*/
%_K6data/plasma/shells/org.kde.plasma.mobileshell/
%_K6data/plasma/mobileinitialstart/
%_K6notif/*.notifyrc
%if_disabled dialer
%exclude %_K6srv/plasma-applet-org.kde.plasma.phone.desktop
%endif
%_K6data/kwin/effects/mobiletaskswitcher/
%_K6data/kwin/scripts/convergentwindows/
%_K6data/plasma-mobile-apn-info/
%_datadir/wayland-sessions/plasma-mobile.desktop
%_datadir/metainfo/*.xml
%exclude %_datadir/metainfo/*keyboard*.xml

#/usr/share/dbus-1/interfaces/org.kde.plasmashell.Mobile.xml

%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt2
- split virtualkeyboard settings into separate package

* Mon Jul 22 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- initial build
