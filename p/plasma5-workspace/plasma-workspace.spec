%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%ifndef _unitdir_user
%define _unitdir_user %prefix/lib/systemd/user
%endif

%define rname plasma-workspace

%define x11confdir %_sysconfdir/X11

%define kworkspace5_sover 5
%define libkworkspace5 libkworkspace5%kworkspace5_sover
%define plasma_geolocation_interface_sover 5
%define libplasma_geolocation_interface libplasma-geolocation-interface%plasma_geolocation_interface_sover
%define taskmanager_sover 6
%define libtaskmanager libtaskmanager%taskmanager_sover
%define weather_ion_sover 7
%define libweather_ion libweather_ion%weather_ion_sover
%define colorcorrect_sover 5
%define libcolorcorrect libcolorcorrect%colorcorrect_sover
%define notificationmanager_sover 1
%define libnotificationmanager libnotificationmanager%notificationmanager_sover
%define kfontinst_sover 5
%define libkfontinst libkfontinst%kfontinst_sover
%define kfontinstui_sover 5
%define libkfontinstui libkfontinstui%kfontinstui_sover
%define krdb_sover 5
%define libkrdb libkrdb%krdb_sover

%def_enable qalculate
%_K5if_ver_gteq %ubt_id M90
%def_enable appstream
%else
%def_disable appstream
%endif

Name: plasma5-workspace
Version: 5.26.4
Release: alt1
Epoch: 1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Plasma
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kf5-plasma-workspace = %EVR
Obsoletes: kf5-plasma-workspace < %EVR
Provides: plasma5-user-manager = %EVR
Obsoletes: plasma5-user-manager < %EVR

#Requires: kde5-kio-fuse
Requires: %name-qml
Requires: /usr/share/design/current xdg-user-dirs
Requires: iso-codes
Requires: xmessage
Requires: qt5-dbus qt5-tools qt5-quickcontrols qt5-virtualkeyboard dbus-tools-gui
Requires: kf5-kinit kf5-kconfig kf5-kded kf5-kglobalaccel kf5-kdeclarative
Requires: kf5-kwallet kf5-solid kf5-kimageformats kf5-kdbusaddons kf5-kio kf5-kio-extras
Requires: kf5-kquickcharts kf5-kirigami
Requires: plasma5-polkit-kde-agent plasma5-kwin plasma5-kactivitymanagerd
Requires: plasma5-kpipewire

Source: %rname-%version.tar
Source1: freememorynotifier.po
Source11: freememorynotifier.tar
Source2: libkicker-ru-add.po
Source3: plasma_lookandfeel_org.kde.lookandfeel-ru-add.po
Patch100: alt-startkde.patch
Patch101: alt-menu-add-tooltip.patch
Patch102: alt-def-wallpaper-image.patch
#
Patch104: alt-def-digital-clock.patch
Patch105: alt-lock-widgets.patch
Patch106: alt-digital-clock-date.patch
Patch107: alt-freespacenotifier.patch
Patch108: alt-def-background.patch
Patch109: alt-def-start-empty-session.patch
Patch110: alt-breeze-loginscreen-focus.patch
Patch111: alt-breeze-one-screen.patch
Patch112: alt-breeze-pw-renew.patch
Patch113: alt-breeze-autoupdate-username.patch
Patch114: alt-menu-search-results-add-genericname.patch
Patch115: alt-dbus-sessionchange.patch
#Patch116: alt-refresh-menu.patch
#
Patch118: alt-session-exclude.patch
Patch119: alt-freespace-thread-timer.patch
Patch120: alt-desktop-plasmashell.patch
Patch121: alt-freememorynotifier.patch
Patch122: alt-systemmonitor-ignoreconfig.patch
Patch123: alt-def-font.patch
Patch124: alt-filtering-widget-settings-upon-first-launch.patch
Patch125: alt-translate-keyboard-layouts.patch
Patch126: alt-add-using-the-altappstarter.patch
Patch127: alt-plasma-5.17-crash.patch
Patch128: alt-soname.patch
Patch129: alt-def-icons.patch
Patch130: alt-sddm-check-username.patch
Patch131: alt-kscreenlocker-theme-pam-support.patch
Patch132: alt-fix-virtualkeyboard.patch
Patch133: alt-dont-remove-desktop-actions.patch
Patch134: alt-zonetab.patch
Patch135: alt-fix-virtualkeyboard-size.patch
Patch136: alt-users-use-gost-yescrypt.patch
Patch137: alt-systemd-boot.patch

# Automatically added by buildreq on Sat Mar 21 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig glib2-devel glibc-devel-static kf5-attica-devel kf5-kdoctools-devel kf5-kjs-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcln-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libwayland-client libwayland-server libxcb-devel libxcbutil-keysyms libxcbutil-keysyms-devel libxkbfile-devel libxml2-devel pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-webkit-devel rpm-build-gir ruby ruby-stdlibs wayland-devel xml-common xml-utils xorg-fixesproto-devel xorg-kbproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules gcc-c++ iceauth kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel kf5-kpty-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkscreen-devel kf5-libksysguard-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libdbusmenu-qt5-devel libgps-devel libpam-devel libqalculate-devel libwayland-client-devel libwayland-server-devel libxapian-devel mkfontdir prison-devel python-module-google qt5-phonon-devel qt5-script-devel qt5-x11extras-devel rpm-build-ruby xmessage xprop xrdb xset xsetroot zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-base-devel-static qt5-phonon-devel qt5-script-devel qt5-svg-devel qt5-x11extras-devel qt5-wayland-devel
BuildRequires: libgps-devel libpam0-devel zlib-devel libpolkitqt5-qt5-devel
%if_enabled qalculate
BuildRequires: libqalculate-devel
%endif
%if_enabled appstream
BuildRequires: appstream-qt-devel
%endif
BuildRequires: libwayland-client-devel libwayland-server-devel libdrm-devel
BuildRequires: pipewire-libs-devel
BuildRequires: libxapian-devel libnm-devel
BuildRequires: libxcbutil-image-devel libxcbutil-devel
BuildRequires: iceauth xmessage xprop xrdb xset xsetroot
BuildRequires: kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel
BuildRequires: kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdesu-devel kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel
BuildRequires: kf5-kpackage-devel kf5-kparts-devel kf5-kpty-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-kxmlrpcclient-devel kf5-prison-devel
BuildRequires: kf5-networkmanager-qt-devel kf5-kpeople-devel kf5-kactivities-stats-devel
BuildRequires: kf5-kded kf5-kded-devel
BuildRequires: kde5-kholidays-devel kde5-plasma-wayland-protocols kde5-libkexiv2-devel
BuildRequires: plasma5-kscreenlocker-devel plasma5-breeze-devel plasma5-layer-shell-qt-devel
BuildRequires: plasma5-kpipewire-devel plasma5-kwin-devel plasma5-libkscreen-devel plasma5-libksysguard-devel
 
%description
KDE Plasma Workspace

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf5-filesystem
Provides: kf5-plasma-workspace-common = %EVR
Obsoletes: kf5-plasma-workspace-common < %EVR
Conflicts: plasma5-desktop-common < 5.20
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-plasma-workspace-devel = %EVR
Obsoletes: kf5-plasma-workspace-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %name-qml
Group: Graphical desktop/KDE
Summary: Base qml-components for plasma workspace
Requires: %name-common = %EVR
Requires: qml(QtGraphicalEffects)
Requires: qml(org.kde.plasma.core) qml(org.kde.kquickcontrols) qml(org.kde.kirigami) qml(org.kde.kwin)
%description -n %name-qml
Base qml-components for plasma workspace

%package -n sddm-theme-breeze
Group: Graphical desktop/KDE
Summary: SDDM breeze theme
Requires: libkf5plasmaquick
Requires: %name-common = %EVR
Requires: %name-qml = %EVR
Buildarch: noarch
%description -n sddm-theme-breeze
SDDM breeze theme

%package -n polkit-kde-plasma-workspace
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common
Provides: polkit-kde-kfontinst
%description -n polkit-kde-plasma-workspace
Common polkit files for %name

%package -n %libkworkspace5
Group: System/Libraries
Summary: %name library
Requires: %name-common
Provides: libkworkspace5 = %version-%release
Obsoletes: libkworkspace5 < %version-%release
%description -n %libkworkspace5
%name library

%package -n %libplasma_geolocation_interface
Group: System/Libraries
Summary: %name library
Requires: %name-common
Provides: libplasma_geolocation_interface = %version-%release
Obsoletes: libplasma_geolocation_interface < %version-%release
%description -n %libplasma_geolocation_interface
%name library

%package -n %libtaskmanager
Group: System/Libraries
Summary: %name library
Requires: %name-common
Provides: libtaskmanager = %version-%release
Obsoletes: libtaskmanager < %version-%release
%description -n %libtaskmanager
%name library

%package -n %libweather_ion
Group: System/Libraries
Summary: %name library
Requires: %name-common
Provides: libweather_ion = %version-%release
Obsoletes: libweather_ion < %version-%release
%description -n %libweather_ion
%name library

%package -n %libcolorcorrect
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libcolorcorrect
%name library

%package -n %libnotificationmanager
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libnotificationmanager
%name library

%package -n %libkfontinst
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkfontinst
%name library

%package -n %libkfontinstui
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkfontinstui
%name library

%package -n %libkrdb
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkrdb
%name library


%prep
%setup -n %rname-%version
%patch100 -p1 -b .startkde
%patch101 -p1
%patch102 -p1
#
%patch104 -p1
###%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
pushd lookandfeel/sddm-theme
%patch112 -p1
popd
%patch113 -p1
%patch114 -p1
%patch115 -p1
#%patch116 -p1
#
%patch118 -p1
%patch119 -p2
%patch120 -p1
%patch121 -p2
#%patch122 -p2
%patch123 -p1
#%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p2
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p2 -b .theme_pam
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p2
%patch136 -p1
%patch137 -p1

install -m 0644 %SOURCE1 po/ru/freememorynotifier.po
tar xf %SOURCE11 freememorynotifier/
msgcat --use-first po/ru/libkicker.po %SOURCE2 > po/ru/libkicker.po.tmp
cat po/ru/libkicker.po.tmp > po/ru/libkicker.po
rm -f po/ru/libkicker.po.tmp
msgcat --use-first po/ru/plasma_lookandfeel_org.kde.lookandfeel.po %SOURCE3 > po/ru/plasma_lookandfeel_org.kde.lookandfeel.po.tmp
cat po/ru/plasma_lookandfeel_org.kde.lookandfeel.po.tmp > po/ru/plasma_lookandfeel_org.kde.lookandfeel.po
rm -f po/ru/plasma_lookandfeel_org.kde.lookandfeel.po.tmp

# disable find PackageKitQt5
sed -i 's|PackageKitQt5|PackageKitQt5_UBUNTU_ONLY|' CMakeLists.txt

# disable krunners by default
for d in runners/*/*.desktop ; do
    sed -i 's|^X-KDE-PluginInfo-EnabledByDefault=.*$|X-KDE-PluginInfo-EnabledByDefault=false|' $d
done
for d in runners/*/*.json ; do
    sed -i '/EnabledByDefault/s|true|false|' $d
done
# enable some krunners by default
#for d in appstream services shell
#do
#    sed -i 's|^X-KDE-PluginInfo-EnabledByDefault=.*$|X-KDE-PluginInfo-EnabledByDefault=true|' runners/${d}/plasma-runner-${d}.desktop
#done
for d in appstream services shell
do
    sed -i '/EnabledByDefault/s|false|true|' runners/${d}/plasma-runner-${d}.json
done

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DKDE4_COMMON_PAM_SERVICE="kf5" \
    -DKDE_COMMON_PAM_SERVICE="kf5" \
    #

%install
%K5install
%K5install_move data kstyle solid kdevappwizard kpackage kglobalaccel
%K5install_move data desktop-directories doc kconf_update kio_desktop knsrcfiles
%K5install_move data kcontrol kdisplay kfontinst krunner konqsidebartng plasma/avatars locale
%K5install_move data plasma//nightcolor kio

# fix dbus service
sed -i 's|^Exec=.*|Exec=%_K5bin/krunner|' %buildroot/%_K5dbus_srv/org.kde.krunner.service

mkdir -p %buildroot/%_K5xdgconf/plasma-workspace/env/

mkdir -p %buildroot/%_bindir
ln -s `relative %_kf5_bin/startplasma-x11 %_bindir/startkde5` %buildroot/%_bindir/startkde5
ln -s startplasma-x11 %buildroot/%_kf5_bin/startkde5

# Add chksession support
mkdir -p %buildroot/%x11confdir/wmsession.d/
cat <<__EOF__ > %buildroot/%x11confdir/wmsession.d/01PLASMA
NAME=Plasma
DESC=Plasma by KDE
ICON=%_K5icon/hicolor/48x48/apps/kwin.png
EXEC=%_kf5_bin/startplasma-x11
SCRIPT:
exec %_kf5_bin/startplasma-x11
__EOF__


# Create menu session
mkdir -p %buildroot/%_menudir/
cat <<__EOF__ > %buildroot/%_menudir/kde5-session
?package(%name): needs=wm \
                        section="Session/Windowmanagers" \
			title="PLASMA" \
			longtitle="Plasma by KDE" \
			command="%_bindir/startplasma-x11" \
			icon="kwin.png"
__EOF__

# disable annoing autostart
mkdir -p %buildroot/%_K5start/
for n in tracker-extract tracker-miner-apps tracker-miner-fs tracker-miner-user-guides tracker-store ; do
    echo -e "[Desktop Entry]\nHidden=true" > %buildroot/%_K5start/$n.desktop
done
# disable annoing menus
mkdir -p %buildroot/%_kf5_xdgapp/
for n in gnome-mplayer mplayer gmplayer ; do
    echo -e "[Desktop Entry]\nHidden=true" > %buildroot/%_kf5_xdgapp/$n.desktop
done


%find_lang %name --with-kde --all-name


%files common -f %name.lang
%doc LICENSES/*
%dir %_K5xdgconf/plasma-workspace/
%dir %_K5xdgconf/plasma-workspace/env/
%dir %_K5data/desktop-directories/
%dir %_K5qml/org/kde/plasma/workspace/
%dir %_K5qml/org/kde/plasma/private/
%dir %_K5qml/org/kde/plasma/wallpapers/
%config(noreplace) %_K5xdgconf/*rc
%_datadir/qlogging-categories5/*.*categories
%_K5icon/hicolor/*/mimetypes/*.*
%_K5icon/hicolor/*/apps/*.*

%files
%config(noreplace) %x11confdir/wmsession.d/*PLASMA*
%_menudir/kde5-session
%dir %_K5plug/plasma/
%dir %_K5plug/plasma/*/
%dir %_K5plug/phonon_platform/
%_bindir/*
%_K5bin/*
%_K5exec/*
%_K5libexecdir/kauth/*
%_K5conf_bin/*
%_K5plug/plasma/*/*.so
%_K5plug/phonon_platform/*.so
%_K5plug/*.so
%_K5plug/kpackage/
%_K5plug/kf5/kded/*.so
%_K5plug/kf5/kio/*.so
%_K5plug/kf5/krunner/
%_K5plug/kf5/parts/*.so
%_K5plug/plasmacalendarplugins/
%_K5plug/plasma/kcms/systemsettings/
%_K5plug/plasma/kcms/systemsettings_qwidgets/
%_K5qml/org/kde/taskmanager/
%_K5qml/org/kde/holidayeventshelperplugin/
%_K5qml/org/kde/colorcorrect/
%_K5qml/org/kde/notificationmanager/
%_K5data/knsrcfiles/*.knsrc
%_K5data/plasma/
%dir %_K5data/plasma/look-and-feel/
%exclude %_K5data/plasma/look-and-feel/*
%_K5data/kglobalaccel/*.desktop
%_K5data/kio/servicemenus/*
%_K5data/kio_desktop/
%_K5data/kpackage/kcms/*/
%_K5data/krunner/
%_K5data/kstyle/
%_K5data/kfontinst/
%_K5data/konqsidebartng/
%_K5data/desktop-directories/*
%_K5data/solid/actions/*.desktop
%_K5xdgapp/*.desktop
%_K5start/*.desktop
%_K5notif/*.notifyrc
%_K5cfg/*.kcfg
%_K5srv/*.desktop
%_K5srvtyp/*.desktop
%_K5dbus_srv/*.service
%_K5dbus/system.d/*.conf
%_K5dbus_sys_srv/*.service
%_K5conf_up/*
%_datadir/xsessions/plasma.desktop
%_K5if_ver_gteq %ubt_id M90
%_datadir/wayland-sessions/plasmawayland.desktop
%endif
%_K5srv/ServiceMenus/*.desktop
%_K5xmlgui/*/
%_unitdir_user/*.service
%_unitdir_user/*.target

%files -n polkit-kde-plasma-workspace
%_datadir/polkit-1/actions/*fontinst*.policy
%_datadir/polkit-1/actions/*locale*.policy

%files -n %name-qml
%_K5qml/org/kde/plasma/
%_K5data/plasma/look-and-feel/*

%files -n sddm-theme-breeze
%_datadir/sddm/themes/breeze/

%files devel
%_K5inc/*
%_K5link/lib*.so
%_K5lib/cmake/KRunnerAppDBusInterface/
%_K5lib/cmake/KSMServerDBusInterface/
%_K5lib/cmake/Lib*/
%_K5dbus_iface/*.xml
#%_K5data/kdevappwizard/templates/*

%files -n %libkworkspace5
%_K5lib/libkworkspace5.so.*
%_K5lib/libkworkspace5.so.%kworkspace5_sover
%files -n %libplasma_geolocation_interface
%_K5lib/libplasma-geolocation-interface.so.*
%_K5lib/libplasma-geolocation-interface.so.%plasma_geolocation_interface_sover
%files -n %libtaskmanager
%_K5lib/libtaskmanager.so.*
%_K5lib/libtaskmanager.so.%taskmanager_sover
%files -n %libweather_ion
%_K5lib/libweather_ion.so.*
%_K5lib/libweather_ion.so.%weather_ion_sover
%files -n %libcolorcorrect
%_K5lib/libcolorcorrect.so.*
%_K5lib/libcolorcorrect.so.%colorcorrect_sover
%files -n %libnotificationmanager
%_K5lib/libnotificationmanager.so.*
%_K5lib/libnotificationmanager.so.%notificationmanager_sover
%files -n %libkfontinst
%_K5lib/libkfontinst.so.*
%_K5lib/libkfontinst.so.%kfontinst_sover
%files -n %libkfontinstui
%_K5lib/libkfontinstui.so.*
%_K5lib/libkfontinstui.so.%kfontinstui_sover
%files -n %libkrdb
%_K5lib/libkrdb.so.*
%_K5lib/libkrdb.so.%krdb_sover


%changelog
* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.4-alt1
- new version

* Thu Nov 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt2
- build with kexiv2

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.2-alt1
- new version

* Thu Oct 06 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.5-alt4
- temporary turn off systemd boot by default

* Fri Sep 09 2022 Oleg Solovyov <mcpain@altlinux.org> 1:5.25.5-alt3
- kscreenlocker passwordless changes:
  + Remove "Unlock" button after passwordless login
  + Hide passwordBox unless password requested
  + Restart fade timer on failed passwordless unlocks
  + Do not append error messages, start failedUnlock animation

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.5-alt2
- bump release

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.6-alt6
- bump release

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.5-alt1
- new version

* Tue Sep 06 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.4-alt4
- merge p10 changes

* Tue Sep 06 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.6-alt5
- move more qml for sddm-theme-breeze

* Thu Sep 01 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.4-alt3
- merge p10 changes

* Thu Sep 01 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.6-alt4
- enable freememorynotifier by default

* Fri Aug 26 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.4-alt2
- fix showing textfield with help to unlock session (thanx mcpin@alt)
- move more qml for sddm-theme-breeze

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.4-alt1
- new version

* Thu Aug 11 2022 Oleg Solovyov <mcpain@altlinux.org> 1:5.24.6-alt3
- freememorynotifier: show notifications from systemd-oomd

* Wed Jul 20 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.6-alt2
- disable free memory notifier by default

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.6-alt1
- new version

* Wed May 11 2022 Slava Aseev <ptrnine@altlinux.org> 1:5.24.5-alt2
- virtual keyboard fixes:
  + make virtual keyboard enable button act as a switch
  + prevent password field from being blocked by virtual keyboard
  + remove virtual keyboard flickering when minimizing

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.4-alt1
- new version

* Mon Mar 28 2022 Oleg Solovyov <mcpain@altlinux.org> 1:5.23.5-alt6
- Backport self-hiding GHNS buttons

* Wed Mar 09 2022 Oleg Solovyov <mcpain@altlinux.org> 1:5.23.5-alt5
- Show panel settings above panels

* Wed Feb 16 2022 Oleg Solovyov <mcpain@altlinux.org> 1:5.23.5-alt4
- fix launching kicker recent applications (Closes: #41912)

* Thu Jan 27 2022 Slava Aseev <ptrnine@altlinux.org> 1:5.23.5-alt3
- fix virtual keyboard size (closes: #40944)

* Tue Jan 11 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt2
- using zone1970.tab

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt1
- new version

* Thu Dec 30 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.4-alt8
- fix PATH variable

* Thu Dec 30 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.4-alt7
- enable appstream runner by default

* Fri Dec 17 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.4-alt6
- using no-break space for default custom date format of digital clock widget (closes: 38552)

* Mon Dec 06 2021 Oleg Solovyov <mcpain@altlinux.org> 1:5.23.4-alt5
- restore krunner in context menu (Closes: #41565)

* Fri Dec 03 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.4-alt4
- fix to set XDG variables against flatpak bug#41495 and same

* Fri Dec 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.23.4-alt3
- updated kscreenlocker-theme-pam patch

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.4-alt2
- reapply kscreenlocker-theme-pam patch

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.3-alt1
- new version

* Tue Nov 09 2021 Oleg Solovyov <mcpain@altlinux.org> 1:5.23.2-alt2
- fix build

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.2-alt1
- new version

* Wed Oct 13 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.5-alt5
- revert 5.22.5-alt3 changes

* Mon Sep 27 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.5-alt4
- fix default small icons size in systemsettings

* Mon Sep 06 2021 Oleg Solovyov <mcpain@altlinux.org> 1:5.22.5-alt3
- fix virtual keyboard in sddm and login screen

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.5-alt2
- enable services runner by default

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.3-alt1
- new version

* Wed Jul 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.22.2-alt2
- Updated and reapplied PAM support patch

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.2-alt1
- new version

* Tue Jun 29 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.5-alt2
- fix build requires

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.5-alt1
- new version

* Fri Apr 23 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.4-alt5
- clean requires

* Mon Apr 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.21.4-alt4
- Removed 'unlock' button. Now unlocking starts immediately instead of displaying the button.

* Fri Apr 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.21.4-alt3
- Fixed kscreenlocker theme to stop unexpectedly erasing password after grace period

* Thu Apr 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.21.4-alt2
- Adapted kscreenlocker theme to new interface with better PAM support

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.4-alt1
- new version

* Wed Mar 31 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.3-alt2
- package systemd targets

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.3-alt1
- new version

* Mon Jan 18 2021 Oleg Solovyov <mcpain@altlinux.org> 1:5.20.5-alt2
- sddm-theme: don't send login request with no username given

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.20.5-alt1
- new version

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.20.4-alt1
- new version

* Wed Nov 11 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.20.2-alt2
- update deafult digital clock custom date format

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.20.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.4-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.3-alt1
- new version

* Fri May 29 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.5-alt2
- update clock widget date default format

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.4-alt1
- new version

* Wed Apr 01 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.3-alt3
- turn off some krunner plugins by default

* Tue Mar 31 2020 Oleg Solovyov <mcpain@altlinux.org> 1:5.18.3-alt2
- fix crash when no firefox profiles exist

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.3-alt1
- new version

* Fri Mar 06 2020 Oleg Solovyov <mcpain@altlinux.org> 1:5.18.1-alt8
- fix firefox bookmarks runner

* Mon Mar 02 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.1-alt7
- fix start alt-app-starter from menu (Closes: 38166)

* Fri Feb 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.18.1-alt6
- applied upstream fix for configure button icons of some widgets

* Wed Feb 26 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.1-alt5
- don't force locking widgets

* Wed Feb 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.18.1-alt4
- updated fix for plasmashell crash

* Wed Feb 26 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.1-alt3
- fix requires

* Tue Feb 25 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.18.1-alt2
- fixed plasmashell crash related to widgets layout

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.1-alt1
- new version

* Thu Feb 13 2020 Oleg Solovyov <mcpain@altlinux.org> 1:5.17.5-alt4
- fix activity runner

* Wed Feb 05 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.17.5-alt3
- translate alt-app-starter menu entry

* Mon Jan 13 2020 Pavel Moseev <mars@altlinux.org> 1:5.17.5-alt2
- add using the alt-app-starter

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.17.5-alt1
- new version

* Fri Dec 20 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.4-alt2
- don't show empty brakets in menu search

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.4-alt1
- new version

* Wed Nov 20 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.3-alt4
- add generic names to main menu search results
- add main menu items tooltips

* Tue Nov 19 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.3-alt3
- fix disk activity monitor defaults

* Mon Nov 18 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.3-alt2
- fix requires

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.1-alt1
- new version

* Wed Oct 23 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.0-alt2
- create user data symlink

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.3-alt1
- new version

* Mon Jul 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.2-alt2
- rediff alt-systemmonitor-ignoreconfig.patch

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.2-alt1
- new version

* Fri Jun 21 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.1-alt3
- enable free memory notifications by default

* Fri Jun 21 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.1-alt2
- fix start plasma wayland session

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.1-alt1
- new version

* Mon Jun 17 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.15.5-alt4
- sddm-breeze-theme: translate keyboard layouts

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt3
- fix to setup startup environment variables

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.4-alt2
- fix digital clock defaults

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.4-alt1
- new version

* Tue Apr 09 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt7
- freememorynotifier: add tooltips, disable help button

* Mon Apr 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.12.8-alt6
- fix requires

* Thu Mar 28 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt5
- freememorynotifier: add translations

* Wed Mar 20 2019 Pavel Moseev <mars@altlinux.org> 1:5.12.8-alt4
- forbidden to disable the last checkbox in the widget settings
- filtering widget settings upon first launch

* Tue Mar 19 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt3
- added freememorynotifier translation template

* Mon Mar 11 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt2
- free space checking: restore notification

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.12.8-alt1
- new version

* Tue Feb 12 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.7-alt13
- memory notifier: fix timer

* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:5.12.7-alt12
- wayland session for p8 branch excluded

* Thu Jan 31 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:5.12.7-alt11
- startplasma and plasmacompositor fixed for wayland session

* Wed Jan 30 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.7-alt10
- memory notifier fixes:
  + disable notifications by default
  + re-create notification ASAP after closing the old one

* Mon Jan 28 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.7-alt9
- disable freememorynotifier autoload

* Fri Jan 18 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.7-alt8
- memory notifier fixes:
  + warn every time when the most-greedy process changes
  + build notification only once (would require less memory)
  + make notification persistent
  + hide notification when free memory is above threshold

* Thu Dec 27 2018 Pavel Moseev <mars@altlinux.org> 1:5.12.7-alt7
- fix general configuration widget - add function to check settings

* Tue Dec 25 2018 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.7-alt6
- fix warnings

* Tue Dec 25 2018 Pavel Moseev <mars@altlinux.org> 1:5.12.7-alt5
- fix general configuration widget - correctly set checked/unchecked state on load

* Wed Nov 28 2018 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.7-alt4
- implement freememorynotifier
- systemmonitor: add --ignoreconfig option

* Tue Nov 27 2018 Anton Midyukov <antohami@altlinux.org> 1:5.12.7-alt3
- new subpackage: sddm-theme-breeze, plasma5-workspace-qml

* Thu Oct 11 2018 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.7-alt2
- bookmarksrunner: fix showing firefox bookmarks

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.7-alt1
- new version

* Wed Aug 22 2018 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.6-alt5%ubt
- plasmashell: use KFreeSpaceJob
- notify user when filesystem freezes
- set timeout to 125 seconds

* Thu Aug 16 2018 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.6-alt4%ubt
- fix plasmashell freeze after losing connection to mounted remote fs

* Wed Aug 15 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.6-alt3%ubt
- fix requires

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.6-alt2%ubt
- fix version

* Tue Jul 03 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- update russian translation

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt2%ubt
- exclude krb5-ticket-watcher from saved session by default

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1%ubt
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2%ubt
- renamed kf5-plasma-workspace -> plasma5-workspace

* Mon Feb 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Mon Feb 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt2%ubt
- security fix: CVE-2018-6791

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- new version

* Mon Dec 11 2017 Oleg Solovyov <mcpain@altlinux.org> 5.11.3-alt3%ubt
- fix theme

* Mon Dec 04 2017 Oleg Solovyov <mcpain@altlinux.org> 5.11.3-alt2%ubt
- remove redundnant Password*.qml

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Wed Oct 04 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt2%ubt
- clear Ctrl+Alt+R binding

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Thu Aug 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt6%ubt
- fix system tray icon context menu (ALT#33763) (thanks darktemplar@alt)

* Tue Aug 08 2017 Oleg Solovyov <mcpain@altlinux.org> 5.10.4-alt5%ubt
- support for changing sessions from D-Bus

* Wed Aug 02 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt4%ubt
- require qt5-virtualkeyboard

* Wed Jul 26 2017 Oleg Solovyov <mcpain@altlinux.org> 5.10.4-alt3%ubt
- fix focus behavior on login screen

* Mon Jul 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt2%ubt
- fix dbus service

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Tue Jun 27 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt8%ubt
- fix package release

* Mon Jun 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt7%ubt
- update from 5.9 branch

* Fri Jun 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt6%ubt
- apply fix against KDE bugs 348390, 251222
- create ~/.local/share/kf5

* Tue Jun 13 2017 Oleg Solovyov <mcpain@altlinux.org> 5.9.5-alt5%ubt
- fix: unable to handle auth request

* Tue Jun 13 2017 Oleg Solovyov <mcpain@altlinux.org> 5.9.5-alt4%ubt
- fix autoupdate username

* Wed Jun 07 2017 Oleg Solovyov <mcpain@altlinux.org> 5.9.5-alt3%ubt
- new look for breeze theme

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt2%ubt
- feel last user name in sddm

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Mon Apr 03 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt5%ubt
- fix password renew with breeze sddm theme

* Fri Mar 31 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt4%ubt
- fix start sddm with breeze theme

* Fri Mar 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt3%ubt
- add password renew support for sddm theme

* Mon Mar 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt2%ubt
- clean build requires
- build with prison
- update from 5.9 branch

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Tue Feb 28 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2%ubt
- fix login background

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1%ubt
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt3.M80P.1
- build for M80P

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt4
- fix to upscale splash background on big screen

* Fri Oct 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt2.M80P.1
- build for M80P

* Fri Oct 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt3
- set user switch screen background

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1.M80P.1
- build for M80P

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt2
- set logout screen background

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt0.M80P.1
- build for M80P

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Thu Oct 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt2.M80P.1
- build for M80P

* Thu Oct 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt3
- fix plasma load

* Wed Oct 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1.M80P.1
- build for M80P

* Wed Oct 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt2
- fix plasma load

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Thu Oct 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt2
- fix plasma shell startup

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt2
- add upstream fix against KDEBUG#365621

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Wed Aug 03 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt2
- disable hide of free space notifier

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Tue Jul 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt2
- apply upstream fix against KDEBUG#364530

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt2
- don't bold clock font by default

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Thu Apr 07 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt2
- fix requires

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt2
- update requires

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Wed Feb 03 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt2
- fix startup splash progress

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt3
- don't lock widgets at first time
- don't save session by default
- set breeze default background

* Tue Jan 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt2
- fix XDG_*_DIRS variables for kstartupconfig5

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt4
- add compact date to digital clock

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Fri Nov 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt3
- fix krunner dbus service

* Tue Oct 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt2
- lock widgets at login

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt3
- add default plasma action to run konsole
- don't lock screen on resume by default
- set digital clock defaults

* Mon Sep 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt2
- set default desktop wallpaper

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Sep 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt2
- fix path to startkde in session file

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Fri Aug 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt5
- rebuild with new baloo

* Thu Aug 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt4
- disable screenlocker by default

* Fri Jul 31 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt3
- move dbus service to standard place

* Mon Jul 13 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt2
- change XDG data dirs order in startkde

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt2
- fix requires

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
