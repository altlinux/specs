%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%define rname plasma-mobile

%_K6if_ver_gteq %ubt_id M110
%def_enable dialer
%else
%def_disable dialer
%endif

Name: %rname
Version: 6.7.2
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
BuildRequires: libvulkan-devel libdrm-devel
BuildRequires: extra-cmake-modules qt6-base-devel qt6-wayland-devel qt6-svg-devel qt6-sensors-devel
BuildRequires: qcoro6-devel libudev-devel
BuildRequires: kf6-modemmanager-qt-devel ModemManager-devel kf6-networkmanager-qt-devel kf6-kcmutils-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdeclarative-devel kf6-ki18n-devel kf6-kio-devel kf6-knotifications-devel
BuildRequires: kf6-kpackage-devel kf6-kpeople-devel kf6-kitemmodels-devel kf6-kirigami-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: plasma-wayland-protocols
BuildRequires: plasma6-lib-devel kwin-devel plasma-workspace-devel plasma6-libkscreen-devel plasma6-kwayland-devel
BuildRequires: plasma6-activities-devel plasma6-layer-shell-qt-devel plasma6-kpipewire-devel
%if_enabled dialer
BuildRequires: libphonenumber-devel
%endif

%description
UI components for Plasma Phone.

%package -n plasma-settings-virtualkeyboard
Group: Graphical desktop/KDE
Summary: On-Screen Keyboard configuration
Requires: %name-core
Provides: kde5-plasma-settings-virtualkeyboard = 24
Obsoletes: kde5-plasma-settings-virtualkeyboard  < 24
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
Provides: kde5-plasma-settings-common = 24
Obsoletes: kde5-plasma-settings-common  < 24
%description common
%name common package

%prep
%setup -n %rname-%version
#%patch2 -p1
%if_disabled dialer
%patch3 -p1
sed -i 's|\(.*add_subdirectory.*dialer.*\)|#\1|' CMakeLists.txt
%endif

for f in po/*/*.po ; do
    fname=`basename "$f"`
    dir=`dirname "$f"`
    if [ "$fname" == "kcm_mobile_virtualkeyboard.po" ] ; then
	cp -ar "$f" "$dir/kcm_mobile_onscreenkeyboard.po"
    fi
done

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
%_K6data/plasma/quicksettings/*keyboard*/
%_datadir/metainfo/*keyboard*.xml

%files
%exclude %_K6data/plasma/quicksettings/*keyboard*/
%exclude %_datadir/metainfo/*keyboard*.xml
%_K6bin/*plasma*mobile*
%_K6exec/kauth/*helper
%_K6plug/plasma/applets/*.so
%_K6plug/kf6/kded/*mobile*.so
%_K6plug/plasma/kcms/systemsettings/kcm_*.so
#%_K6qml/org/kde/plasma/mm/
%_K6qml/org/kde/plasma/quicksetting/
%_K6qml/org/kde/plasma/mobileinitialstart
%_K6xdgapp/kcm_*.desktop
%_K6data/plasma/look-and-feel/org.kde.breeze.mobile/
%_K6data/plasma/quicksettings/*/
%_K6data/plasma/shells/org.kde.plasma.mobileshell/
%_K6data/plasma/mobileinitialstart/
%_K6data/plasma-mobile-device-presets/
%_K6notif/*.notifyrc
%if_disabled dialer
%exclude %_K6srv/plasma-applet-org.kde.plasma.phone.desktop
%endif
%_K6data/kwin/effects/mobiletaskswitcher/
%_K6data/kwin/scripts/convergentwindows/
%_K6data/plasma-mobile-apn-info/
%_K6data/plasma/layout-templates/org.kde.plasma.mobile.*/
%_K6dbus_sys_srv/*mobile*.service
%_K6dbus/system.d/*mobile*.conf
%_datadir/polkit-1/actions/*mobile*.policy
%_datadir/wayland-sessions/plasma-mobile.desktop
%_datadir/metainfo/*.xml
%_datadir/qlogging-categories6/*.*categories

#/usr/share/dbus-1/interfaces/org.kde.plasmashell.*.xml

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

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt2
- fix translations

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Mon Aug 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt2
- fix conflicts (closes: 51179)

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt2
- split virtualkeyboard settings into separate package

* Mon Jul 22 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- initial build
